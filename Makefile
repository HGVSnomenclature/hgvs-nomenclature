.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

SHELL:=/bin/bash -eu -o pipefail

serve:
	mkdocs serve
