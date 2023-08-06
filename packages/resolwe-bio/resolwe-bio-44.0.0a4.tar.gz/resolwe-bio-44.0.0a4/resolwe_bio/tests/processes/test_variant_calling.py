from os.path import join
from pathlib import Path

from resolwe.flow.models import Data
from resolwe.test import tag_process

from resolwe_bio.utils.filter import filter_html, filter_vcf_variable
from resolwe_bio.utils.test import BioProcessTestCase, skipUnlessLargeFiles


class VariantCallingTestCase(BioProcessTestCase):
    @tag_process("vc-chemut")
    def test_variant_calling_chemut(self):
        with self.preparation_stage():
            inputs = {
                "src": "chemut_genome.fasta.gz",
                "species": "Dictyostelium discoideum",
                "build": "dd-05-2009",
            }
            ref_seq = self.run_process("upload-fasta-nucl", inputs)
            bwa_index = self.run_process("bwa-index", {"ref_seq": ref_seq.id})

            inputs = {"src1": ["AX4_mate1.fq.gz"], "src2": ["AX4_mate2.fq.gz"]}

            parental_reads = self.run_process("upload-fastq-paired", inputs)

            inputs = {"src1": ["CM_mate1.fq.gz"], "src2": ["CM_mate2.fq.gz"]}

            mut_reads = self.run_process("upload-fastq-paired", inputs)

            inputs = {"genome": bwa_index.id, "reads": parental_reads.id}
            align_parental = self.run_process("alignment-bwa-mem", inputs)

            inputs = {"genome": bwa_index.id, "reads": mut_reads.id}
            align_mut = self.run_process("alignment-bwa-mem", inputs)

        inputs = {
            "genome": ref_seq.id,
            "parental_strains": [align_parental.id],
            "mutant_strains": [align_mut.id],
            "reads_info": {
                "PL": "Illumina",
                "LB": "x",
                "CN": "def",
                "DT": "2014-08-05",
            },
            "Varc_param": {"stand_emit_conf": 10, "stand_call_conf": 30},
        }

        variants = self.run_process("vc-chemut", inputs)
        self.assertFields(variants, "build", "dd-05-2009")
        self.assertFields(variants, "species", "Dictyostelium discoideum")

    @tag_process("filtering-chemut")
    def test_filtering_chemut(self):
        with self.preparation_stage():
            vcf_input = {
                "src": "variant_calling_filtering.vcf.gz",
                "species": "Dictyostelium discoideum",
                "build": "dd-05-2009",
            }
            variants = self.run_process("upload-variants-vcf", vcf_input)

        inputs = {
            "variants": variants.pk,
            "analysis_type": "snv",
            "parental_strain": "AX4",
            "mutant_strain": "mutant",
            "read_depth": 5,
        }

        filtered_variants = self.run_process("filtering-chemut", inputs)
        self.assertFile(
            filtered_variants,
            "vcf",
            "variant_calling_filtered_variants.vcf.gz",
            compression="gzip",
        )
        self.assertFields(filtered_variants, "build", "dd-05-2009")
        self.assertFields(filtered_variants, "species", "Dictyostelium discoideum")

    @skipUnlessLargeFiles("56GSID_10k_mate1_RG.bam")
    @tag_process("vc-realign-recalibrate")
    def test_vc_preprocess_bam(self):
        with self.preparation_stage():
            bam_input = {
                "src": join("large", "56GSID_10k_mate1_RG.bam"),
                "species": "Homo sapiens",
                "build": "b37",
            }
            bam = self.run_process("upload-bam", bam_input)
            inputs = {
                "src": "hs_b37_chr2_small.fasta.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            genome = self.run_process("upload-fasta-nucl", inputs)
            vcf_input = {
                "src": "1000G_phase1.indels.b37_chr2_small.vcf.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            indels = self.run_process("upload-variants-vcf", vcf_input)
            dbsnp_input = {
                "src": "dbsnp_138.b37.chr2_small.vcf.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            dbsnp = self.run_process("upload-variants-vcf", dbsnp_input)

        inputs = {
            "alignment": bam.id,
            "genome": genome.id,
            "known_indels": [indels.id],
            "known_vars": [dbsnp.id],
        }

        variants = self.run_process("vc-realign-recalibrate", inputs)
        self.assertFields(variants, "build", "b37")
        self.assertFields(variants, "species", "Homo sapiens")

    @skipUnlessLargeFiles("56GSID_10k_mate1_RG.bam")
    @tag_process("picard-pcrmetrics")
    def test_collecttargetedpcrmetrics(self):
        with self.preparation_stage():
            bam_input = {
                "src": join("large", "56GSID_10k_mate1_RG.bam"),
                "species": "Homo sapiens",
                "build": "b37",
            }
            bam = self.run_process("upload-bam", bam_input)
            master_file = self.prepare_amplicon_master_file()

            inputs = {
                "src": "hs_b37_chr2_small.fasta.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            genome = self.run_process("upload-fasta-nucl", inputs)

        inputs = {
            "alignment": bam.id,
            "master_file": master_file.id,
            "genome": genome.id,
        }

        pcrmetrics = self.run_process("picard-pcrmetrics", inputs)
        self.assertFile(pcrmetrics, "target_coverage", "picard.perTargetCov.txt")

    @skipUnlessLargeFiles("56GSID_10k.realigned.bqsrCal.bam")
    @tag_process("vc-gatk-hc", "vc-gatk4-hc")
    def test_gatk_haplotypecaller(self):
        with self.preparation_stage():
            input_folder = Path("haplotypecaller") / "input"
            output_folder = Path("haplotypecaller") / "output"
            alignment = self.run_process(
                "upload-bam",
                {
                    "src": Path("large") / "56GSID_10k.realigned.bqsrCal.bam",
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )

            inputs = {
                "src": "hs_b37_chr2_small.fasta.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            genome = self.run_process("upload-fasta-nucl", inputs)

            master_file = self.prepare_amplicon_master_file()
            bed_file = self.run_process(
                "upload-bed",
                {
                    "src": input_folder / "56G_masterfile_test_merged_targets_5col.bed",
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )

            dbsnp_input = {
                "src": "dbsnp_138.b37.chr2_small.vcf.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            dbsnp = self.run_process("upload-variants-vcf", dbsnp_input)

        gatk3_vars = self.run_process(
            "vc-gatk-hc",
            {
                "alignment": alignment.id,
                "intervals": master_file.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
            },
        )
        self.assertFile(
            gatk3_vars,
            "vcf",
            output_folder / "56GSID_10k.gatkHC.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )
        self.assertFields(gatk3_vars, "build", "b37")
        self.assertFields(gatk3_vars, "species", "Homo sapiens")

        gatk4_vars = self.run_process(
            "vc-gatk4-hc",
            {
                "alignment": alignment.id,
                "intervals": master_file.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
            },
        )
        self.assertFile(
            gatk4_vars,
            "vcf",
            output_folder / "56GSID_10k.gatkHC4.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )
        self.assertFields(gatk4_vars, "build", "b37")
        self.assertFields(gatk4_vars, "species", "Homo sapiens")

        # This chunk checks that user is specifying only master file or bed
        # file, but not both. Once we remove the dependence on master file,
        # this test will be obsolete.
        gatk3_incol = self.run_process(
            "vc-gatk-hc",
            {
                "alignment": alignment.id,
                "intervals": master_file.id,
                "intervals_bed": bed_file.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
            },
            Data.STATUS_ERROR,
        )
        self.assertEqual(
            gatk3_incol.process_error[0],
            "You have specified intervals and intervals_bed, whereas only one is permitted.",
        )

        gatk3_bed = self.run_process(
            "vc-gatk-hc",
            {
                "alignment": alignment.id,
                "intervals_bed": bed_file.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
            },
        )
        self.assertFile(
            gatk3_bed,
            "vcf",
            output_folder / "56GSID_10k.gatkHC.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )

        gatk4_bed = self.run_process(
            "vc-gatk4-hc",
            {
                "alignment": alignment.id,
                "intervals_bed": bed_file.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
            },
        )

        self.assertFile(
            gatk4_bed,
            "vcf",
            output_folder / "56GSID_10k.gatkHC4.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )

        # Test specifically for HaplotypeCaller with RNA-seq data
        gatk_rnaseq = self.run_process(
            "vc-gatk4-hc",
            {
                "alignment": alignment.id,
                "genome": genome.id,
                "dbsnp": dbsnp.id,
                "mbq": 10,
                "advanced": {
                    "soft_clipped": True,
                    "java_gc_threads": 3,
                    "max_heap_size": 7,
                },
            },
        )
        self.assertFields(gatk_rnaseq, "build", "b37")
        self.assertFields(gatk_rnaseq, "species", "Homo sapiens")
        self.assertFile(
            gatk_rnaseq,
            "vcf",
            output_folder / "56GSID_10k.rna-seq.gatkHC.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )

    @skipUnlessLargeFiles("56GSID_10k.realigned.bqsrCal.bam")
    @tag_process("lofreq")
    def test_lofreq(self):
        with self.preparation_stage():
            alignment = self.run_process(
                "upload-bam",
                {
                    "src": join("large", "56GSID_10k.realigned.bqsrCal.bam"),
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )

            inputs = {
                "src": "hs_b37_chr2_small.fasta.gz",
                "species": "Homo sapiens",
                "build": "b37",
            }
            genome = self.run_process("upload-fasta-nucl", inputs)

            master_file = self.prepare_amplicon_master_file()

        inputs = {
            "alignment": alignment.id,
            "intervals": master_file.id,
            "genome": genome.id,
        }

        lofreq_vars = self.run_process("lofreq", inputs)
        self.assertFile(
            lofreq_vars,
            "vcf",
            "56GSID_10k.lf.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )
        self.assertFields(lofreq_vars, "build", "b37")
        self.assertFields(lofreq_vars, "species", "Homo sapiens")

    @tag_process("snpeff-legacy", "snpeff")
    def test_snpeff(self):
        with self.preparation_stage():
            input_folder = Path("snpeff") / "input"
            output_folder = Path("snpeff") / "output"
            variants_lf = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "56GSID_10k.lf.vcf",
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )
            variants_gatk = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "56GSID_10k0.gatkHC.vcf",
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )
            dbsnp = self.run_process(
                "upload-variants-vcf",
                {
                    "src": "dbsnp_138.b37.chr2_small.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "b37",
                },
            )
            variants_rna = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "filtered_snpeff.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "GRCh38",
                },
            )
            dbsnp_rna = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "dbsnp.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "GRCh37",
                },
            )
            genes = self.run_process(
                "upload-geneset",
                {
                    "src": input_folder / "set_of_genes.txt",
                    "source": "ENSEMBL",
                    "species": "Homo sapiens",
                },
            )

        final_var_lf = self.run_process(
            "snpeff-legacy",
            {
                "variants": variants_lf.id,
                "known_vars_annot": [dbsnp.id],
                "var_source": "lofreq",
            },
        )
        self.assertFile(final_var_lf, "annotation", "56GSID.lf.finalvars.txt")
        self.assertRegex(final_var_lf.process_warning[0], r"Inconsistency for entry .*")

        final_var_gatk = self.run_process(
            "snpeff-legacy",
            {
                "variants": variants_gatk.id,
                "known_vars_annot": [dbsnp.id],
                "var_source": "gatk_hc",
            },
        )
        self.assertFile(
            final_var_gatk, "annotation", output_folder / "56GSID.gatk.finalvars.txt"
        )

        snpeff = self.run_process(
            "snpeff",
            {
                "variants": variants_rna.id,
                "database": "GRCh38.99",
                "dbsnp": dbsnp_rna.id,
            },
            Data.STATUS_ERROR,
        )
        self.assertEqual(
            snpeff.process_error[0],
            "Genome build for the DBSNP file and used database "
            "should be the same. DBSNP file is based on "
            "GRCh37, while snpEff database is based on "
            "GRCh38.",
        )

        snpeff_filtering = self.run_process(
            "snpeff",
            {
                "variants": variants_rna.id,
                "database": "GRCh38.99",
                "filtering_options": "( REF = 'A' )",
                "extract_fields": [
                    "CHROM",
                    "POS",
                    "REF",
                    "ALT",
                    "ANN[*].GENE",
                    "ANN[*].HGVS_P",
                ],
                "advanced": {"one_per_line": True},
            },
        )
        self.assertFile(
            snpeff_filtering,
            "vcf_extracted",
            output_folder / "extracted_variants.vcf.gz",
            compression="gzip",
            file_filter=filter_vcf_variable,
        )
        self.assertFile(
            snpeff_filtering,
            "vcf",
            output_folder / "filtered_variants.vcf.gz",
            compression="gzip",
            file_filter=filter_vcf_variable,
        )

        snpeff_filtering = self.run_process(
            "snpeff",
            {
                "variants": variants_rna.id,
                "database": "GRCh38.99",
                "filtering_options": "ANN[*].EFFECT has 'missense_variant'",
                "sets": [genes.id],
                "extract_fields": [
                    "CHROM",
                    "POS",
                    "ID",
                    "REF",
                    "ALT",
                    "QUAL",
                    "ANN[*].GENE",
                    "ANN[*].HGVS_P",
                ],
            },
        )
        self.assertFile(
            snpeff_filtering,
            "vcf_extracted",
            output_folder / "variants_set.vcf.gz",
            compression="gzip",
            file_filter=filter_vcf_variable,
        )

    @tag_process("gatk-refine-variants")
    def test_gatk_refinement(self):
        input_folder = Path("variant_refinement") / "input"
        output_folder = Path("variant_refinement") / "output"
        with self.preparation_stage():
            ref_seq = self.run_process(
                "upload-fasta-nucl",
                {
                    "src": input_folder / "chrX_1_28000.fa.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )
            variants_main = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "snp.recalibrated_chrX_28000.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )
            vcf_pop = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "chrX_28000.renamed.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )

        gatk_cgp = self.run_process(
            "gatk-refine-variants",
            {
                "vcf": variants_main.id,
                "ref_seq": ref_seq.id,
                "vcf_pop": vcf_pop.id,
            },
        )
        self.assertFile(
            gatk_cgp,
            "vcf",
            output_folder / "variants.refined.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )

    @tag_process("ensembl-vep")
    def test_ensembl_vep(self):
        input_folder = Path("ensembl-vep") / "input"
        output_folder = Path("ensembl-vep") / "output"
        with self.preparation_stage():
            vcf = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "snp.recalibrated_chrX_28000.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "GRCh38",
                },
            )
            cache = self.run_process(
                "upload-vep-cache",
                {
                    "cache_file": input_folder / "cache_homo_sapiens_X.tar.gz",
                    "species": "Homo sapiens",
                    "build": "GRCh38",
                    "release": "103",
                },
            )
            ref_seq = self.run_process(
                "upload-fasta-nucl",
                {
                    "src": input_folder / "chrX_1_28000.fa.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )
        vep = self.run_process(
            "ensembl-vep",
            {
                "vcf": vcf.id,
                "cache": cache.id,
                "ref_seq": ref_seq.id,
            },
        )
        self.assertFile(
            vep,
            "vcf",
            output_folder / "snp_annotated.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )
        self.assertFile(vep, "tbi", output_folder / "snp_annotated.vcf.gz.tbi")
        self.assertFile(
            vep,
            "summary",
            output_folder / "snp_annotated.vcf_summary.html",
            file_filter=filter_html,
        )
        self.assertEqual(
            vep.process_warning,
            [
                "The current version of Ensembl-VEP is 104. "
                "It is recommended that cache version is also 104."
            ],
        )

    @tag_process("variants-to-table")
    def test_variants_to_table(self):
        input_folder = Path("variants_to_table") / "input"
        output_folder = Path("variants_to_table") / "output"
        with self.preparation_stage():
            vcf = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "refined_variants.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "GRCh38",
                },
            )
        variants = self.run_process(
            "variants-to-table",
            {
                "vcf": vcf.id,
                "vcf_fields": ["CHROM", "POS", "ALT"],
                "advanced_options": {
                    "gf_fields": ["GT", "GQ"],
                    "split_alleles": False,
                },
            },
        )
        self.assertFile(variants, "tsv", output_folder / "variants_to_table.tsv")

    @tag_process("gatk-variant-filtration")
    def test_variant_filtration(self):
        input_folder = Path("variant_filtration") / "input"
        output_folder = Path("variant_filtration") / "output"
        with self.preparation_stage():
            ref_seq = self.run_process(
                "upload-fasta-nucl",
                {
                    "src": input_folder / "chr1_19000.fasta.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )
            vcf = self.run_process(
                "upload-variants-vcf",
                {
                    "src": input_folder / "chr1_19000.vcf.gz",
                    "species": "Homo sapiens",
                    "build": "custom_build",
                },
            )

        filtering = self.run_process(
            "gatk-variant-filtration",
            {
                "vcf": vcf.id,
                "ref_seq": ref_seq.id,
                "filter_expressions": ["FS > 30.0", "QD < 2.0", "DP > 20"],
                "filter_name": ["FS", "QD", "DP"],
                "advanced": {
                    "window": 35,
                    "java_gc_threads": 3,
                    "max_heap_size": 8,
                },
            },
        )
        self.assertFile(
            filtering,
            "vcf",
            output_folder / "filtered_variants.vcf.gz",
            file_filter=filter_vcf_variable,
            compression="gzip",
        )

        filtering_error = {
            "vcf": vcf.id,
            "ref_seq": ref_seq.id,
            "filter_expressions": ["QD < 2.0", "DP > 20"],
            "filter_name": ["FS", "QD", "DP"],
        }

        filtering = self.run_process(
            "gatk-variant-filtration", filtering_error, Data.STATUS_ERROR
        )
        error_msg = [
            ("The number of filter expressions and filter names is not the same.")
        ]
        self.assertEqual(filtering.process_error, error_msg)
