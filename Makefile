.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:


deploy:
	mkdocs gh-deploy

serve:
	mkdocs serve
