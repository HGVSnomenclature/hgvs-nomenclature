.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

SHELL:=/bin/bash -eu -o pipefail

default:
	@echo "No $@ target. See README.md"

setup:
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -U setuptools pip uv; \
	uv pip install -r requirements.txt; \
	pre-commit install

	######################################################################
	## You must `source venv/bin/activate` to activate this environment ##
	######################################################################

update-release-notes:
	python simple_hooks/generate_release_notes.py

build serve: %:
	mkdocs $@

sitemap.xml: site/sitemap.xml
	cp $< $@

site/sitemap.xml: build;
