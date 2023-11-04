# HGVS Nomenclature Grammar

The HGVS Nomenclature is fundamentally a computational language, but it has historically been written using human-interpreted descriptions rather than using a precise [formal grammar](https://en.wikipedia.org/wiki/Formal_grammar). While migrating from human descriptions to a formal grammar would increase formal precision, it would be disruptive to the community. Instead, the [HVNC](../hvnc.md) has chosen to selectively adopt principles and presentation of computational grammars in order to improve the precision of definitions while preserving human readability. We have chosen a common variation of the [Extended Backus-Naur Form (EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to define variant syntax.

We recognize that most users of HGVS will not want to concern themselves with the pedagogy of formal grammars and that most discussions of the topic are dense. This primer describes the most essential concepts for EBNF as used by the HGVS Nomenclature, presented slightly informally to make them accessible to a broad audience.

## Basics

- A grammar specifies the valid syntax for a string of characters. A _symbol_ is a grammatical classification that aids parsing.
- There are two kinds of symbols: a _literal symbol_ represents verbatim text, and a _non-terminal symbol_ represents a named concept like "an integer sequence position". [more](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols)
- Literal symbols are specified in double quotes. For example, `"A"`` means that an "A" character is accepted as input (and nothing else).
- A "pipe" (`|`) separates alternatives. For example `"A" | "B"` accepts a single "A" or "B" character (and nothing else).
- Symbols (of either type) may be concatenated. For example, `digit digit` matches a two-digit number. (Note: HGVS Nomenclature uses a common variant of EBNF in which concatenation is implied by adjacent symbols. Other EBNF variants require a comma between concatenated symbols.)
- A _production rule_ defines a non-terminal symbol as a pattern of other symbols. For example, `digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"` says that `digit` is made of "0" or "1" or "2", etc. Similarly, `two_digit_dumber = digit digit` defines a two_digit_number non-terminal symbol as being composed of two adjacent digits.
- _Modfiers_ are used to indicate cardinality: `*` indicates zero or more of the preceeding rule or symbol; `+` indicates one or more; and `?` denotes zero or one (i.e., optional). For example, `number = digit+` recognizes any sequence of digits without sign or decimal point.
- Parenthesis may be used to group a subexpression. For example, `"A" ( "B" | "C" )` accepts "AB" or "AC", and nothing else.

Putting this all together, a rule to match NCBI [RefSeq accessions](https://support.nlm.nih.gov/knowledgebase/article/KA-03437/) might be written as `refseq_accession = letter letter "_" digit+ "." digit+`, which would accept accessions like "NM_000551.3" and "NC_000012.12". Note that, as defined here, `refseq_accession` would also accept invalid or unlikely accessions such as "QQ_012.3333333333333333"; this example highlights the distinction between syntactic and semantic validity.

## Grammar Elements

For consistency and brevity, commonly used grammar elements are listed here.

- `aa_position = aa position`
- `aa_position_range = aa_position "_" aa_position`
- `position = number`

### Literals

- `"Ter"`: The 3-letter amino acid termination codon; written as `"*"` when using 1-letter amino acid codes.

### Primitives

(in alphabetical order)

- `aa` = any 3 or 1 letter amino acid
- `accession = letter ( letter | digit | "_" | "." )+`
- `digit = [0-9]` # any single digit
- `letter = [A-Za-z]` # not actually EBNF; indicates any upper or lower case letter
- `number = digit+`

### General Elements

- `coordinate_type` = `"c"`, `"g"`, `"m"`, `"n"`, `"o"`, `"p"`, or `"r"`
- `position_point` = the zero-width insertion point in a sequence, specified as two adjacent sequence positions in a `position_range`
- `position_range` = two positions, separated by underscore (`"_"`)
- `position` = any position
- `c_position` = a simple integer position (e.g., `22`) or an intronic position defined relative to a integer position (e.g., `22-3`)
- `sequence_identifer` = a valid sequence identifier (a.k.a. accession); see [reference sequences](../background/refseq.md) `alternate_nucleotide` = single nucleotide of the variant sequence at this position `reference_nucleotide` = single nucleotide of the reference sequence at this position
