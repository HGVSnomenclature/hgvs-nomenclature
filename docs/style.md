
# Style conventions used in this documentation

This page explains the style conventions used in HGVS Nomenclature for both readers and authors.

The HGVS Nomenclature is written using [Markdown](https://en.wikipedia.org/wiki/Markdown).  If
you're unfamiliar with Markdown, please read [Introduction to
Markdown](https://www.writethedocs.org/guide/writing/markdown/).  This page documents conventions
used to apply Markdown to the HGVS Nomenclature.  Contributors should follow the styles outlined
below. Inline HTML is discouraged except when necessary, and underlining should never be used.

## Imperative terms

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC
2119](https://datatracker.ietf.org/doc/html/rfc2119).  The salient features of that document are
excerpted below with minor editing.

1. MUST   This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute
   requirement of the specification.

2. MUST NOT   This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute
   prohibition of the specification.

3. SHOULD   This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in
   particular circumstances to ignore a particular item, but the full implications must be
   understood and carefully weighed before choosing a different course.

4. SHOULD NOT   This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons
   in particular circumstances when the particular behavior is acceptable or even useful, but the
   full implications should be understood and the case carefully weighed before implementing any
   behavior described with this label.

5. MAY   This word, or the adjective "OPTIONAL", mean that an item is truly optional. An
   implementation which does not include a particular option MUST be prepared to interoperate with
   another implementation which does include the option, though perhaps with reduced functionality.
   In the same vein an implementation which does include a particular option MUST be prepared to
   interoperate with another implementation which does not include the option (except, of course,
   for the feature the option provides.)

6. Imperatives of the type defined in this memo must be used with care and sparingly.  In
   particular, they MUST only be used where it is actually required for interoperation or to limit
   behavior which has potential for causing harm (e.g., limiting retransmisssions)  For example,
   they must not be used to try to impose a particular method on implementors where the method is
   not required for interoperability.

## Style Examples

{{ read_csv('style-examples.csv', escapechar='\') }}

## HGVS Expression Grammar

A formal description of HGVS Nomenclature Expressions are written using [Extended Backus-Naur Form
(EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). EBNF is commonly used to
define a computational language simply and concisely.  HGVS Nomenclature uses a common variation of
EBNF in which concatenation does not use commas and instead relies on implicit concatenation of
adjacent symbols.

```markdown

## Syntax

- `type "." "[" posedit1 ";" posedit2 "]"` (variants in *cis*)
- `type "." "[" posedit1 "]" ";" "[" posedit2 "]"` (variants in *trans*)
- `type "." "[" posedit1 "(;)" posedit2 "]"` (phase unknown or uncertain)

where

- `type` is the reference sequence type
- `posedit1` and `posedit2` are the positions and changes 

## Examples

- `NC_000001.11:g.[123G>A;345del]`
- `NC_000001.11:g.[123G>A];[345del]`
- `NC_000001.11:g.[123G>A(;)345del]`
```

which renders like this:

## Syntax

- `type "." "[" posedit1 ";" posedit2 "]"` (variants in *cis*)
- `type "." "[" posedit1 "]" ";" "[" posedit2 "]"` (variants in *trans*)
- `type "." "[" posedit1 "(;)" posedit2 "]"` (phase unknown or uncertain)

where

- `type` is the reference sequence type
- `posedit1` and `posedit2` are the positions and changes 

## Examples

- `NC_000001.11:g.[123G>A;345del]`
- `NC_000001.11:g.[123G>A];[345del]`
- `NC_000001.11:g.[123G>A(;)345del]`

