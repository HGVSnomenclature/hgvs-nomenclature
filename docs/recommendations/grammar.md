# Grammar

A grammar is concerned with creating rules for processing a sequence of characters. The HGVS Nomenclature grammar is defined using [Extended Backus-Naur Form (EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). EBNF is commonly used to define a computational language simply and concisely. HGVS Nomenclature uses a common variation of EBNF in which concatenation does not use commas and instead relies on implicit concatenation of adjacent symbols.

Here are the most essential concepts for EBNF as used by the HGVS Nomenclature, presented slightly informally to make them accessible to a broad audience.

- Literal characters ("symhols") are specified in double quotes. For example, `"A"`` means that an "A" character is accepted as input (and nothing else).
- A "pipe" (`|`) separates alternatives. For example `"A" | "B"` accepts a single "A" or "B" character (and nothing else).
- A "production rule" is a name for a pattern of characters, often with a particular meaning. For example, `digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"` says that the _symbol_ `digit` is made of "0" or "1" or "2", etc.
- A sequence of rule names and/or symbols may be concatenated. For example, the rule `two_digit_number = digit digit` accepts exactly two digits.
- Modfiers are used to indicate cardinality: `*` indicates zero or more of the preceeding rule or symbol; `+` indicates one or more; and `?` denotes zero or one (i.e., optional). For example, `number = digit+` recognizes any sequence of digits without sign or decimal point.
- Parenthesis may be used to group a subexpression. For example, `"A" ( "B" | "C" )` accepts "AB" or "AC", and nothing else.

Putting this all together, a rule to match NCBI RefSeq accessions might be written as `letter letter "_" digit+ "." digit+`, which would accept accessions like "NM_000551.3" and "NC_000012.12".

## Grammar Elements

For consistency and brevity, commonly used grammar elements are listed here.

### Primitives

(in alphabetical order)

- `digit = [0-9]` # any single digit
- `letter = [A-Za-z]` # not actually EBNF; indicates any upper or lower case letter
- `number = digit+`

### General Elements

- `coordinate_type = "c" | "g" | "m" | "n" | "o" | "p" | "r"`
- `sequence_identifer = letter ( letter | digit | "_" | "." )+`
- `position` = any position
- `position_range` = two positions, separated by underscore (`"_"`)
- `insertion_position` = a `position_range` that specifies the insertion point in a sequence as two adjacent bases
