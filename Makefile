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
	make varnomen-copy
	make varnomen-prune
	make varnomen-rename
	make varnomen-adapt
	# prettier -w docs/**/*.md    # messes up 

varnomen-copy:
	rm -fr docs && cp -a ../VarNomen docs
	git checkout HEAD -- docs/{.pages,images,index.md,stylesheets}

varnomen-prune:
	rm -fr docs/{.gitignore,404.html,CNAME,README.md,_config.yml,_includes,_layouts,css,fonts,index.html,js,tmp}

varnomen-rename:
	mv docs/_bg-material docs/background
	mv docs/_recommendations docs/recommendations
	@cd docs/background/consultation; \
	for p in svd-wg*.md; do np=$${p%.md}; mv $$p $${np^^}.md;done

varnomen-adapt:
	adapt-varnomen-pages docs/**/*.md
	@cd docs/recommendations; \
	for d in DNA RNA protein; do \
		rm -v $$d/index.html; \
		mv -v $$d/variant/*.md $$d/; \
		rm -fr $$d/variant; \
	done


