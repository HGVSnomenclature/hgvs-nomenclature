.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

SHELL:=/bin/bash -eu -o pipefail

build serve: %:
	mkdocs $@

sitemap.xml: site/sitemap.xml
	cp $< $@

site/sitemap.xml: build;
