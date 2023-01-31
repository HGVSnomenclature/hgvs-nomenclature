.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

SHELL:=/bin/bash -O globstar
PATH:=${PWD}/bin:${PATH}

deploy:
	mkdocs gh-deploy

serve:
	mkdocs serve


varnomen-remigrate:
	rm -fr docs/*
	make varnomen-copy
	make varnomen-adapt
	make varnomen-rename
	cp -a ../../biocommons/biocommons.github.io/docs/stylesheets docs/
	git checkout e2a6f26 -- docs/images docs/index.md
	# prettier -w docs/**/*.md    # messes up 

varnomen-copy:
	cd ../VarNomen; \
	cp -a _bg-material ../hgvs-nomenclature.github.io/docs/background; \
	cp -a _recommendations ../hgvs-nomenclature.github.io/docs/recommendations; \
	cp -a HVNC.md recent.md assets history.md versioning.md ../hgvs-nomenclature.github.io/docs/

varnomen-adapt:
	adapt-varnomen-pages docs/**/*.md

varnomen-rename:
	cd docs/background/consultation; \
	for p in svd-wg*.md; do np=$${p%.md}; mv -v $$p $${np^^}.md;done
