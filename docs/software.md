# Software

This page lists general purpose open source software that manipulates HGVS
expressions. Our intention is to help the community find software that aids in
the adoption of HGVS Nomenclature. The entries below are provided by the
authors; the entries are not validated or endorsed by the HVNC. Software packages are listed
alphabetically.  See [Listing Definitions](#listing-definitions) for an
explanation of terms. See the [submission requirements and
instructions](#submissions) for information about submitting to this list.


```sh exec="true"
bin/make-software-table docs/software/*.yml
```

## Listing Definitions

- **Software Type**: One of:
    - Library: Software component that is used by developers when building applications
    - API (e.g., REST): Software that exposes an internet-visible programming interface that is language-independent
    - Web UI: Software used with a browser window and generally intended for broader audiences

- **License**: Only open access web services and open-source software with
  licenses approved by the [Open Source Initiative](https://opensource.org) will
  be listed. In addition, [well-recognized
  licenses](https://opensource.org/licenses/?categories=popular-strong-community)
  will be preferred.

- **Functionality**: Software is annotated as performing one or more of the following functions:
    - backtranslation: Can the software infer possible transcript variants from observed protein consequences?
    - conversion: Does the software convert to/from HGVS and other formats (e.g., VCF, SPDI, VRS)
    - extraction: Is the software able to generate a description from a reference and observed sequence?
    - liftover: Does the software support mapping variants between aligned genomic sequences?
    - normalization: Does the software normalize variants (e.g., 3' shift) and rewrite (e.g., `ins` → `dup`)
    - parsing: Does the software parse variant descriptions into a object model usable by the client?
    - transcription: Does the software support mapping variants between genome and transcript variants?
    - translation: Does the software infer protein consequences from transcript variants?
    - validation: Does the software provide syntactic validation (i.e., the correct form) and semantic validation (i.e., the parsed structure makes sense)?

## Submissions

### Requirements

The software must:

- Be *primarily* concerned with provided the functionality listed above.
  Software that merely accepts or emits HGVS variant descriptions as part of their
  operation (e.g., variant annotation) do not meet this criterion.
- Meet the license requirements above. Commercial software, including hybrid
  open-source/commercial software, will not be included.
- Have a publication in PubMed. This requirement is intended to create a bar
  that implies review by peers.

### Instructions

To submit a software entry:

- Fork the [hgvs-nomenclature repo](https://github.com/HGVSnomenclature/hgvs-nomenclature/)
- Create a new entry in the docs/software/ directory using an existing entry as a template
- Build the documentation locally (see
  [README.md](https://github.com/HGVSnomenclature/hgvs-nomenclature/blob/main/README.md))
  to ensure that your software entry appears as intended
- Submit a pull request
