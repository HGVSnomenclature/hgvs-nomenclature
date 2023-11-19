# Software

!!! note "Under Construction"

    This page is being developed. See discussion at [https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions/56](https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions/56)


This page lists general purpose open source software that manipulates HGVS expressions. Our intention is to help the community find software that aids in the adoption of HGVS Nomenclature. The entries below are provided by the authors; the entries are not validated or endorsed by the HVNC. Tools are listed alphabetically.

## Submissions

To submit a software entry, fork the [hgvs-nomenclature repo](https://gituhub.com/HGVSnomenclature/hgvs-nomenclature/) and create a new entry in the docs/software/ directory using entry.yml-template.  You should build the documentation yourself to ensure that your software entry appears as intended.

## Listing Details

- **Software Type**: One of:
    - Library: Software component that is used by developers when building other tools
    - API (e.g., REST): Software that exposes an internet-visible programming interface that is language-independent
    - Web UI: Software used with a browser window and generally intended for broader audiences

- **License**: Only open-source tools with [well-recognized OSI-approved licenses](https://opensource.org/licenses/?categories=popular-strong-community) will be listed.

- **Functionality**: Any software that manipulates general HGVS expressions may be listed. Here, "manipulates" means that the software must do one or more of the following: 1) parse, 2) generate, 3) validate, or 4) project or translate, and "general" means that the software must perform these operations on a significant subset of variants across transcripts and variant types (insertions, deletions, etc). Given that many packages read or write HGVS expressions, that functionality alone is not sufficient to be listed here.

## Software

```sh exec="true"
bin/make-software-table docs/software/*.yml
```
