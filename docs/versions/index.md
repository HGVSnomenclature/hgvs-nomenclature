# Versions

!!! info inline end "Version 21.0 is current"

    Read the [release notes for the current version](21.0).


The primary mission of HGVS Nomenclature is to facilitate reliable communication of sequence variants, which requires that the HGVS Nomenclature is stable. Nonetheless, modifications will be required from time to time in order to address new scientific needs, resolve inconsistencies, or clarify conventions.  A key goal of the [HVNC](/hvnc/) is to manage such changes in a way that balances the needs of progress and reliable data sharing, and to communicate the changes to the community clearly.

The HGVS Nomenclature uses concepts from [Semantic Versioning](https://semver.org/) to version releases. Each release version will consist of 3 numbers separated by dots in the format x.y.z with the following meanings:

- The "patch" version (z) is reserved for changes that fix or clarify intentions. This is akin to a bug fix.
- The "minor" version (y) will be used for new features that are consistent with prior versions but should not break them.  For example, adoption of a community proposal that added a new feature would trigger an increase in the minor version.
- The "major" version (x) will be used when changes are incompatible with existing conventions, and perhaps for other changes that are deemed to be significant. Major changes should be rare. Wherever possible, the HVNC will strive to ensure that backward incompatibilities result in obvious failures (e.g., falure to parse at all) rather than subtle errors that are difficult to catch.

!!! info "Beginning January 2024 with version 21.0.0, version numbers do not correspond to dates"

    Historically, HGVS used date-based versions (e.g., 20.05 in May 2020).  That practice has been discarded in factor of semantic versioning.  Because versions should increase monotonically, the major release of HGVS Nomenclature in January 2024 will have major version 21. **Beginning with version 21, users should not assume a correspondance between the major version and the year of release.**

## How should versions be used in practice?

The HVNC will provide guidance about effective use of version numbers in future releases.  For now, please use the following recommendations:

- Data providers (for example, databases, APIs, and manuscript authors) should state the version of HGVS Nomenclature that they use to communicate HGVS expressions.
- Data consumers (especially software tools) should state the maximum version of HGVS Nomenclature that they can receive.
- For the purposes of predicting compatibility between providers and consumers, it suffices to compare HGVS Nomenclature major and minor version numbers as a floating point number. (The patch version is reserved for clarifications and minor changes that would be reasonably expected to have incidental consequence (at most) to the interpretation of HGVS expressions.)
- Consider these cases:
      - `consumer_version < provider_version` (with same or different major versions): The most likely consequence is that the consumer will be missing features that are potentially used by the provider. The consumer may not be able to parse incoming data.
      - `consumer_version = provider_version`: This is the best case for reliable data exchange.
      - `consumer_version > provider_version`: If the major version numbers are equal, this is a supported and ideal mechanism for the evolution of HGVS Nomenclature in the community. However, if the consumer major version is greater than the provider major version, **caution should be exercised because the consumer is using a version of HGVS Nomenclature that has *known and intended* backward incompatibilities with earlier versions**.
