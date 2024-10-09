# Style conventions used in this documentation

This page explains the style conventions used in HGVS Nomenclature for both readers and authors.

## For Readers

### Imperative terms

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).
The salient features of that document are excerpted below with minor editing.

1. **MUST**<br>
   This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.

2. **MUST NOT**<br>
   This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.

3. **SHOULD**<br>
   This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.

4. **SHOULD NOT**<br>
   This phrase, or the phrase "NOT RECOMMENDED", mean that there may exist valid reasons in particular circumstances when the particular behavior is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behavior described with this label.

5. **MAY**<br>
   This word, or the adjective "OPTIONAL", mean that an item is truly optional.
   An implementation which does not include a particular option MUST be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality.
   In the same vein, an implementation which does include a particular option MUST be prepared to interoperate with another implementation which does not include the option (except, of course, for the feature the option provides.)

6. Imperatives of the type defined in this memo must be used with care and sparingly.
   In particular, they MUST only be used where it is actually required for interoperation or to limit behavior which has potential for causing harm (e.g., limiting retransmissions).
   For example, they must not be used to try to impose a particular method on implementors where the method is not required for interoperability.

## For Authors

This section is relevant only for those who are contributing to the documentation.

### Documentation Source

The HGVS Nomenclature is written using [Markdown](https://en.wikipedia.org/wiki/Markdown). If you're unfamiliar with Markdown, please read [Introduction to Markdown](https://www.writethedocs.org/guide/writing/markdown/). Markdown is converted to HTML using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

### Setting up

See https://github.com/HGVSNomenclature/hgvs-nomenclature/ for instructions on setting up mkdocs to make it easier to review your contributions.

### Style Examples

Contributors should follow the styles outlined below.
Inline HTML is discouraged except when necessary, and underlining should never be used.

{{ read_csv('style-examples.csv', escapechar='\\') }}

### Syntax Blocks

Syntax blocks are formatted by ./bin/pull-syntax from data in syntax.yaml.
See any recommendation page for an example.
