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
	make varnomen-overlay
	make varnomen-adapt
	# prettier -w docs/**/*.md    # messes up 

varnomen-copy:
	rm -fr docs && cp -a ../VarNomen docs

varnomen-prune:
	rm -fr docs/{.git,.gitignore,404.html,CNAME,contact.html,history-1996.html,README.md,_config.yml,_includes,_layouts,css,fonts,index.html,js,tmp}

varnomen-rename:
	mv docs/_bg-material docs/background
	mv docs/_recommendations docs/recommendations

	mv docs/background/consultation docs/
	mv docs/background/consultation.md docs/consultation/index.md
	cd docs/consultation; for p in svd-wg*.md; do np=$${p%.md}; mv $$p $${np^^}.md;done
	perl -i -p0e 's%/background/consultation/%/consultation/%g' docs/**/*.md

	mv docs/history.md docs/background/
	perl -i -p0e 's%/history/%/background/history/%g' docs/**/*.md
	
	mv docs/versioning.md docs/background/
	perl -i -p0e 's%/versioning/%/background/versioning/%g' docs/**/*.md

	mv docs/recommendations/open-issues.md docs/consultation/
	perl -i -p0e 's%/recommendations/open-issues/%/consultation/open-issues/%g' docs/**/*.md

varnomen-adapt:
	adapt-varnomen-pages docs/**/*.md
	@cd docs/recommendations; \
	for d in DNA RNA protein; do \
		rm -fv $$d/index.{html,md}; \
		mv -v $$d/variant/*.md $$d/; \
		rm -fr $$d/variant; \
	done

varnomen-overlay:
	git checkout HEAD -- docs/{.pages,images,index.md,stylesheets,background/.pages,recommendations/.pages,migration-plan.md}
