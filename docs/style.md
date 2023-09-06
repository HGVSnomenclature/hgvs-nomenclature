# Style conventions used in this documentation

The HGVS Nomenclature is written using [Markdown](https://en.wikipedia.org/wiki/Markdown).  If you're unfamiliar with Markdown, please read [Introduction to Markdown](https://www.writethedocs.org/guide/writing/markdown/).  This page documents conventions used to apply Markdown to the HGVS Nomenclature.  Contributors should follow the styles outlined below. Inline HTML is discouraged except when necessary, and underlining should never be used.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC
2119](https://datatracker.ietf.org/doc/html/rfc2119).

## Style Examples

{{ read_csv('style-examples.csv') }}

## Syntax blocks

Syntax blocks are used to convey the representation of a variant.  In keeping with historical presentation, we use an informal representation of the syntax rather than a formal computational grammar.


```markdown
## Syntax

- `TYPE.[POSEDIT1;POSEDIT2]` (one allele)
- `TYPE.[POSEDIT1];[POSEDIT2]` (two alleles)

where

- `TYPE` is the reference sequence type
- `POSEDIT1` and `POSEDIT2` are the positions and changes 

## Examples

- `NC_000001.11:g.[123G>A;345del]`
- `NC_000001.11:g.[123G>A];[345del]`
```

which renders like this:

![Example of formatting for syntax descriptions in the HGVS Nomenclature. (Taken from DNA Alleles.)](syntax-example.png)