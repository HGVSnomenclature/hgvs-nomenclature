# Software

This page lists general purpose open source software that manipulates HGVS
expressions. Our intention is to help the community find software that aids in
the adoption of HGVS Nomenclature. The entries below are provided by the
authors; the entries are not validated or endorsed by the HVNC. Tools are listed
alphabetically.  See the [submission requirements and instructions](#submission)
for information about submitting to this list.


!!! note "Under Construction"

    This page is being developed. See discussion at [https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions/56](https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions/56)

    TODO:

    - update links for docs, issues, home
    - reconsider how to list functionality (and what functionality)
    - allow types to be multi-select (e.g., rust library with a python interface and an API)


## Software

```sh exec="true"
bin/make-software-table docs/software/*.yml
```

## Listing Details

- **Software Type**: One of:
    - Library: Software component that is used by developers when building other tools
    - API (e.g., REST): Software that exposes an internet-visible programming interface that is language-independent
    - Web UI: Software used with a browser window and generally intended for broader audiences

- **License**: Only open-source tools with licenses approved by the [Open Source
  Initiative](https://opensource.org) will be listed. In addition,
  [well-recognized
  licenses](https://opensource.org/licenses/?categories=popular-strong-community)
  will be preferred.

- **Functionality**: Software is annotated as performing one or more of the following functions:
    - conversion: Does the software convert to/from HGVS and other formats (e.g., VCF, SPDI, VRS)
    - liftover: Does the software provide *direct* liftover between aligned genomic sequences?
    - normalization: Does the software normalize variants (e.g., 3' shift) and rewrite (e.g., `ins` → `dup`)
    - parsing: Does the software parse HGVS expressions into a usable structure for analysis?
    - projection: Does the software project variants from one sequence to another?
    - translation: Does the software infer protein consequences from transcript variants?
    - validation: Does the software provide syntactic validation (i.e., the correct form) and semantic validation (i.e., the parsed structure makes sense)?

## Submissions

To submit a software entry, fork the [hgvs-nomenclature repo](https://gituhub.com/HGVSnomenclature/hgvs-nomenclature/) and create a new entry in the docs/software/ directory using entry.yml-template.  You should build the documentation yourself to ensure that your software entry appears as intended.
