.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

SHELL:=/bin/bash -O globstar
PATH:=${PWD}/bin:${PATH}

deploy:
	mkdocs gh-deploy

serve:
	mkdocs serve


remigrate:
	make copy
	make prune
	make rename1
	make adapt
	make rename2
	make overlay
	make misc-governance
	#make rel-links
	# prettier -w docs/**/*.md    # messes up 

copy:
	rm -fr docs && cp -a ../VarNomen docs

prune:
	rm -fr docs/{.git,.gitignore,404.html,CNAME,contact.html,history-1996.html,README.md,_config.yml,_includes,_layouts,css,fonts,index.html,js,tmp,_recommendations/index.html,_bg-material/index.html}

# rename1 is required before adaptation because of file path inspection
rename1:
	mv docs/_bg-material docs/background
	mv docs/_recommendations docs/recommendations

adapt:
	adapt-varnomen-pages docs/**/*.md
	@cd docs/recommendations; \
	for d in DNA RNA protein; do \
		rm -fv $$d/index.{html,md}; \
		mv -v $$d/variant/*.md $$d/; \
		rm -fr $$d/variant; \
	done

# rename2 depends on changes made during adaptation
rename2:
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

	mv docs/HVNC.md docs/governance.md
	perl -i -p0e 's%# HVNC%# Governance%' docs/governance.md
	perl -i -p0e 's%/HVNC/%/governance/%g' docs/**/*.md

	mv docs/recent.md docs/news.md
	perl -i -p0e 's%### Recent Additions%# News%' docs/news.md

overlay:
	# overlay manually edited files from previous commit 
	git checkout HEAD -- docs/{.pages,images,index.md,stylesheets,background/.pages,recommendations/.pages,consultation/.pages}

misc-governance:
	perl -i -p0 \
		-e 's%### Task%### Misson%;' \
		-e 's%The task of the HVNC%The mission of the HVNC%;' \
		-e 's%(Reece.+201)4%$${1}3%;' \
		-e 's%Human Genom %Human Variome %' docs/governance.md

rel-links:
	./bin/abs-links-to-rel-links docs/**/*.md

check-links:
	mkdocs build
	./bin/check-relative-links site/**/*.html
	