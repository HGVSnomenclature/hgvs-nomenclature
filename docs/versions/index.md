# Versions

The primary mission of HGVS Nomenclature is to facilitate reliable communication of sequence variants, which requires that the HGVS Nomenclature is stable. Nonetheless, modifications will be required from time to time in order to address new scientific needs, resolve inconsistencies, or clarify conventions.  A key goal of the [HVNC](/hvnc/) is to manage such changes in a way that balances the needs of progress and reliable data sharing, and to communicate the changes to the community clearly.

The HGVS Nomenclature uses concepts from [Semantic Versioning](https://semver.org/) to version releases. Each release version will consist of 3 numbers separated by dots in the format x.y.z with the following meanings:

- The "patch" version (z) is reserved for changes that fix or clarify intentions. This is akin to a bug fix.
- The "minor" version (y) will be used for new features that are consistent with prior versions but should not break them.  For example, adoption of a community proposal that added a new feature would trigger an increase in the minor version.
- The "major" version (x) will be used when changes are incompatible with existing conventions, and perhaps for other changes that are deemed to be significant. Major changes should be rare.

!!! Important

    Historically, HGVS used date-based versions (e.g., 20.05 in May 2020).  That practice has been discarded in factor of semantic versioning.  Because versions should increase monotonically, the major release of HGVS Nomenclature in January 2024 will have major version 21.

    **Beginning with version 21, users should not assume a correspondance between the major version and the year of release.**
