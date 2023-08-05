#!/bin/bash -e

. /var/cache/build/packages-manual/common.sh

# Install R packages.
# Install renv which is a pre-requisite to installing all other packages in next chunk.
Rscript --slave --no-save --no-restore-history -e "install.packages('renv', repos = 'https://cloud.r-project.org')"

sed -e 's/^#.*$//g' -e '/^$/d' /var/cache/build/packages-r.txt | \
    Rscript --slave --no-save --no-restore-history \
        -e "renv::install(readLines('stdin'), repos='https://cloud.r-project.org')"

# XXX: This is unverifiable and thus may compromise the whole image.
# XXX: Use notary (https://github.com/ropenscilabs/notary) when ready.
Rscript --slave --no-save --no-restore-history -e " \
  install.packages('http://hartleys.github.io/QoRTs/QoRTs_STABLE.tar.gz', repos=NULL, type='source') \
"
