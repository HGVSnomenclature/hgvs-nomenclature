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


_logger = logging.getLogger("mkdocs.plugins.hooks")

# cache github to prevent rate limit errors
requests_session = CachedSession(
    "/tmp/github_cache", expire_after=timedelta(minutes=10)
)


def fetch_github_releases(repo_owner, repo_name):
    # return list of releases with x.y.z semver tags
    def dos2unix(s: str) -> str:
        return s.replace("\r\n", "\n").replace("\r", "\n")

    semver_pattern = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
    response = requests_session.get(url)
    response.raise_for_status()
    releases = []
    for r in response.json():
        m = semver_pattern.match(r["tag_name"])
        if m:
            version_t = tuple(map(int, r["tag_name"].split(".")))
            releases.append(
                {
                    "body": re.sub(
                        r"^#", "##", dos2unix(r["body"]), flags=re.MULTILINE
                    ),
                    "published_at": datetime.fromisoformat(
                        r["published_at"].rstrip("Z")
                    ),
                    "version_t": version_t,
                    "version_xy": ".".join(r["tag_name"].split(".")[:2]),
                    "version": r["tag_name"],
                }
            )
    return releases


def group_releases_by_major_minor(releases):
    sorted_releases = sorted(releases, key=lambda r: r["version_t"], reverse=True)
    grouped_releases_i = itertools.groupby(
        sorted_releases, key=lambda r: r["version_xy"]
    )
    return {tag: list(releases) for tag, releases in grouped_releases_i}


def create_markdown_files(grouped_releases, output_dir):
    template = _get_release_file_template()
    for version_xy, releases in grouped_releases.items():
        new_content = template.render(version_xy=version_xy, releases=releases)
        # mkdocs renderer renders '^* # blah' as as bulleted headline :-/ (github is fine)
        new_content = new_content.replace("* #", "* Closed #")

        out_fn = output_dir / f"{version_xy}.md"
        if out_fn.exists():
            current_content = out_fn.open("r", encoding="utf-8").read()
            if current_content == new_content:
                _logger.info(f"{out_fn}: Unchanged")
                return
        with out_fn.open("w", encoding="utf-8") as f:
            f.write(new_content)
            _logger.info(f"{out_fn}: Created/updated")


def _get_release_file_template():
    template_str = """
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
    """.strip()
    template = jinja2.Template(template_str)
    return template


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
