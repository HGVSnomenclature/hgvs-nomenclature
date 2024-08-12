#!/usr/bin/env python
"""generate all release note files in docs/versions/ from GitHub release notes API
"""

from datetime import datetime, timedelta
import itertools
import logging
import pathlib
import re

import jinja2
from requests_cache import CachedSession


repo_owner = "HGVSNomenclature"
repo_name = "hgvs-nomenclature"
out_dir = pathlib.Path("docs/versions")


_logger = logging.getLogger(__name__)

# cache github to prevent rate limit errors
requests_session = CachedSession('/tmp/github_cache', expire_after=timedelta(minutes=10))


def fetch_github_releases(repo_owner, repo_name):
    # return list of releases with x.y.z semver tags

    semver_pattern = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
    response = requests_session.get(url)
    response.raise_for_status()
    releases = []
    for r in response.json():
        m = semver_pattern.match(r["tag_name"])
        if m:
            version_t = tuple(map(int, r["tag_name"].split(".")))
            releases.append({
                "body": re.sub(r'^#', '##', r["body"], flags=re.MULTILINE),
                "published_at": datetime.fromisoformat(r["published_at"].rstrip("Z")),
                "version_t": version_t,
                "version_xy": ".".join(r["tag_name"].split(".")[:2]),
                "version": r["tag_name"],
            })
    return releases


def group_releases_by_major_minor(releases):
    sorted_releases = sorted(releases, key=lambda r: r["version_t"], reverse=True)
    grouped_releases_i = itertools.groupby(sorted_releases, key=lambda r: r["version_xy"])
    return {tag: list(releases) for tag, releases in grouped_releases_i}


def create_markdown_files(grouped_releases, output_dir):
    template = _get_release_file_template()
    for version_xy, releases in grouped_releases.items():
        page_content = template.render(
            version_xy=version_xy, releases=releases
        )
        # mkdocs renderer renders '^* # blah' as as bulleted headline :-/ (github is fine)
        page_content = page_content.replace('* #', '* Closed #')
        out_fn = output_dir / f"{version_xy}.md"
        with out_fn.open("w") as f:
            f.write(page_content)
            _logger.info(f"Wrote {out_fn}")

def _get_release_file_template():
    return jinja2.Template(
        """
# {{version_xy}} Series

{%if version_xy == '21.0' %}
!!! note "We need your help"

    Version 21.0.0 is the first significant update in HGVS Nomenclature in almost four years.
    While we have resolved many errors during this work, it is possible that new errors were introduced. If you find an issue, please [contact us](../index.md#contact-us).
{% endif %}

{% for release in releases %}
## {{ release["version"] }} ({{release["published_at"].date()}})

{{ release["body"] }}

{% endfor %}

{%if version_xy == '21.0' %}
## 21.0.0 (2024-01-13)

### Major Changes

- **Our preferred name is "HGVS Nomenclature".**
  The many previous names (e.g., HGVS guidelines, HGVS recommendations, VarNomen, Mutnomen) created confusion and are obsolete.
- **The URL is now stable.**
  To foster stable URLs and better serve the community, HGVS Nomenclature now has a dedicated domain name, [hgvs-nomenclature.org](https://hgvs-nomenclature.org/).
  The previous pages are now archived at [archive.hgvs-nomenclature.org](https://archive.hgvs-nomenclature.org/).
  The old site, [varnomen.hgvs.org](https://varnomen.hgvs.org/) forwards users to the corresponding page on the new site.
- **Documentation management was improved.**
  Pages from the old documentation were migrated to a new system that should make it easier to maintain HGVS Nomenclature and support multiple device sizes (phones, tablets, laptops).
  The intention during migration was to retain the intention of the original text, while modernizing the management of HGVS Nomenclature and cleaning up the presentation.
- **Adopted Semantic Versioning and defined how versions should interoperate.**
  HGVS Nomenclature will now use Semantic Versioning, which should make it easier for users to track new features in HGVS Nomenclature.
  Beginning with this release, historical versions will also be available adjacent to newer versions.
  See [Versions](index.md) for details.
- **HGVS Nomenclature is now part of HUGO.**
  HGVS Nomenclature is overseen by the [Human Variant Nomenclature Committee](../hvnc.md), a subcommittee of the [Human Genome Organization (HUGO)](https://www.hugo-international.org/).
- **Updated channels to communicate with the HVNC and contribute ideas.**
  We have introduced two new mechanisms to contact the HVNC: there is now an email list to discuss HGVS nomenclature, and we have formalized the process by which may submit ideas.
  See [Contact Us](../index.md#contact-us) for details.
  The Facebook group and older email address (which was read only by the committee chair) are now obsolete.

### New features

In version 21.0.0, most changes to the HGVS Nomenclature were operational, but some new features were introduced:

- **Developed a formal grammar for HGVS Nomenclature syntax.**
  HGVS Nomenclature previously used human-readable descriptions of the syntax of variants.
  These descriptions were not usable by computers and sometimes conflicted.
  We have started to introduce the use of formal grammars to represent variant syntax.
  See [Grammar Elements](../recommendations/grammar.md) for details.
- **Summarized all syntax in a single table.**
  As a by-product of migrating to a formal grammar, we have also generated a summary of all HGVS syntax on a single page by variant type.
  See [HGVS Syntax Summary](../recommendations/summary.md).
- **Added a list of software that manipulates HGVS variant descriptions.**
  See [Software](../software.md).
- **Updated recommendations for gene fusion syntax.**
  We have aligned definitions of terms used in the characterization of gene fusions and DNA rearrangements with the VICC Gene Fusion Specification, the HUGO Gene Nomenclature Committee, and the ISCN Nomenclature Committee.
  This has resulted in the revision of the term _fusion transcript_ to _adjoined transcript_ in relevant sections of the nomenclature and glossary.
  We have also updated our recommendations for users to consult the [VICC Gene Fusion Specification nomenclature](https://fusions.cancervariants.org/en/latest/nomenclature.html) for exon-based representations of adjoined transcripts.
{% endif %}
    """
    )

def main(config=None, *args, **kwargs):
    releases = fetch_github_releases(repo_owner, repo_name)
    _logger.info(f"Fetched {len(releases)} releases from {repo_owner}/{repo_name}")

    grouped_releases = group_releases_by_major_minor(releases)
    _logger.info(f"Grouped into {len(grouped_releases)} major.minor releases")

    create_markdown_files(grouped_releases, out_dir)


if __name__ == "__main__":
    import coloredlogs

    coloredlogs.install(level="INFO")

    main()
