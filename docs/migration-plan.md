# Migration Plan

This is a temporary page that collects the current plan and status for making these pages official.
This page will be removed after cutting over (Phase 4 below) to the new site.

## Current state

- The [HGVSnomenclature/HVNC](https://github.com/HGVSnomenclature/HVNC) repo contains discussions
  and the process proposal
- The [HGVSnomenclature/VarNomen](https://github.com/HGVSnomenclature/VarNomen) repo contains the
  current web pages
- The [hgvs-nomenclature/hgvs-nomenclature](https://github.com/hgvs-nomenclature/hgvs-nomenclature)
  contains the migrated website that is built automatically by Read the Docs and appears at
  hgvs-nomenclature.org

## Desired state / expected outcomes

- Standardize name as "HGVS nomenclature" with the corresponding [slug](https://patterns.dataincubator.org/book/url-slug.html) "hgvs-nomenclature".
- A single repo containing 1) current discussions, 2) historical varnomen pages, and 3) new web
  pages as markdown.
- The repo will be named hgvs-nomenclature
- Web pages available at hgvs-nomenclature.org and hosted at Read the Docs.
- varnomen.hgvs.org forwards to hgvs-nomenclature.org.

## Migration Plan

### Phase 1: Consolidate above repos into single repo

- Johan grants Reece owner access to the organization. (see below)
- Reece archives the VarNomen pages so that they are available for historical purposes, but not
  writeable. NO UPDATES TO VARNOMEN AFTER THIS TIME.
- Reece imports the (now archived) VarNomen web pages as-is into the HVNC repo in order to preserve
  historical pages in the new repo.  (HGVSnomenclature/HVNC will be the
  base of our work because it has the current discussions, which are not easily moved.)
- Reece migrates the
  [17-migrate-web-site-to-markdown-and-mkdocs](https://github.com/hgvs-nomenclature/hgvs-nomenclature.github.io/tree/17-migrate-web-site-to-markdown-and-mkdocs)
  branch with the new pages
- Reece arranges for read the docs updates from this branch.
- Reece removes the temporary hgvs-nomenclature/hgvs-nomenclature repo (which is no longer needed).
- Reece renames the HGVC repo to hgvs-nomenclature.

### Phase 2: Migrate existing pages

- Reece finishes the migrating VarNomen pages and submits a PR.
- We merge the PR. The goal for this PR is only to achieve parity with the original website content.
- At this point, the new pages will be at hgvs-nomenclature.org (but essentially unknown to the
  world) and the old pages will still appear at varnomen.hgvs.org.

### Phase 3: Updating the website

- We undertake whatever additional edits we desire before releasing.

### Phase 4: Cutover to new site

- Create a forwarding page at varnomen.hgvs.org announcing the new site. Visitors to
  varnomen.hgvs.org will be automatically redirected by the web page (after a short announcement).
- Someone (Johan? Reece?) asks hgvs.org admins to permanently redirect varnomen.hgvs.org.

### Later

- Consider reformatting/restructuring goals for the website.
- Propose and discuss versioning changes.

## Granting access to the HGVSnomenclature org (for Johan)

- Go to https://github.com/orgs/HGVSnomenclature/people, click "Invite member", type "reece" (my username).
- You should have an option to select my role in the organization. Choose Owner.
- Note: I think I'm going to need to handle some DNS validation, which I think requires owner permissions. (That's why I made the similarly-named hgvs-nomenclature organization to test web pages.)
- I'm happy to help with admin going forward, or we can downgrade my permissions later.
- Details instructions are at https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
If needed, we can zoom to do this together.