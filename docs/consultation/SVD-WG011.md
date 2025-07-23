# Nomenclature of positions upstream and downstream of transcripts

## Introduction
In the meeting of 7-10-2024, the committee decided that positions upstream and
downstream of a transcript may be addressed using the `c.` and `n.` coordinate
systems as long as these positions are within the boundaries of the reference
sequence. A notable advantage of this is the ability to address promoter and
regulatory regions relative to the transcript they act upon. The committee did,
however, not decide on the syntax used to address these positions.

## Considerations
The project leaders of the Variant Validator and Mutalyzer have discussed this
issue briefly and both agree that more clarification is needed before they can
proceed further. They have identified three candidates, a fourth was added
later:

1. Exonic numbering, i.e., relative to the start or end of the coding region.
  E.g., if the transcript starts at position `c.-100`, the first nucleotide
  upstream is addressed as `c.-101`. If the transcript ends at position
  `c.*100`, the first nucleotide downstream is addressed as `c.*101`.
2. Intronic numbering, i.e., relative to the start or end of the transcript.
  E.g., if the transcript starts at position `c.-100`, the first nucleotide
  upstream is addressed as `c.-100-1`. If the transcript ends at position
  `c.*100`, the first nucleotide downstream is addressed as `c.*100+1`.
3. Intronic numbering with additional annotation. This idea was
  [proposed](https://hgvs-nomenclature.org/stable/consultation/open-issues/#numbering-gene-flanking-nucleotides)
  with the intention to easily tell intronic and intergenic regions apart.
  E.g., if the transcript starts at position `c.-100`, the first nucleotide
  upstream is addressed as `c.-100-u1`. If the transcript ends at position
  `c.*100`, the first nucleotide downstream is addressed as `c.*100+d1`.
  Alternatively, the `u` and `d` could be replaced with one letter (an `i` for
  example) because the `+` and `-` already indicate whether a position is
  upstream or downstream.
4. Pure upstream and downstream numbering. E.g., the first nucleotide upstream
  is addressed as `c.u1`, the first nucleotide downstream is addressed as
  `c.d1`.

Some examples of the different options are given below. Potential
interpretation difficulties are highlighted in bold.
 
| Description                                                       | 1          | 2             | 3a         | 3b         | 4
|:--                                                                |:--         |:--            |:--         |:--         |:-- 
| 10 nucleotides before the transcription start site.               | **`-110`** | **`-100-10`** | `-100-u10` | `-100-i10` | `u10`
| 10 nucleotides after the transcription start site.                | **`-90`**  | `-90`         | `-90`      | `-90`      | `-90`
| 10 nucleotides before the end of an intron in the 5' UTR.         | `-50-10`   | **`-50-10`**  | `-50-10`   | `-50-10`   | `-50-10`
| 10 nucleotides after the start of an intron in the coding region. | `50+10`    | `50+10`       | `50+10`    | `50+10`    | `50+10`
| 10 nucleotides after the start of an intron in the 3' UTR.        | `*50+10`   | **`*50+10`**  | `*50+10`   | `*50+10`   | `*50+10`
| 10 nucleotides before the transcription end                       | **`*90`**  | `*90`         | `*90`      | `*90`      | `*90`
| 10 nucleotides after the transcription end                        | **`*110`** | **`*100+10`** | `*100+d10` | `*100+i10` | `d10`

Currently, the Variant Validator has no support for any of these options and
Mutalyzer supports option 1. Both project leaders endorse options 2 and 3 and
strongly advise against option 1. The project leader of Mutalyzer has expressed
a preference for option 3a and is open for options 3b and 4.

## Proposal
The different options were discussed in the meeting of 7-4-2025. The committee
seems largely in favour of option 4, because of its conciseness.

We therefore propose to replace the text under the heading "transcript
flanking" in the
[coding DNA numbering](https://hgvs-nomenclature.org/stable/background/numbering/#coding-dna-reference-sequences)
section with the following:

> Variants in nucleotides beyond the boundaries of a transcript, but within the
> boundaries of the reference sequence may be described using *upstream* (u) or
> *downstream* (d) positions relative to the annotated transcription start or
> end respectively.
>
> Examples:
> - `c.u10` denotes the position 10 nucleotides upstream of the annotated transcript.
> - `c.d10` denotes the position 10 nucleotides downstream of the annotated transcript.

Likewise, we propose to replace the text under the third bullet in the
[non-coding DNA numbering](https://hgvs-nomenclature.org/stable/background/numbering/#non-coding-dna-reference-sequences)
sections with the following:

> Nucleotides beyond the boundaries of a transcript, but within the
> boundaries of the reference sequence are numbered as for coding DNA
> reference sequences (see above), but proceeded by `n.` (instead of `c.`).

Additionally, we propose to modify the
[figure](https://hgvs-nomenclature.org/stable/background/numbering/#figure)
in which the different numbering systems are explained to reflect the changes
proposed above.

Finally, we propose to update the examples to reflect the changes proposed
above.

[Deletions extending beyond the transcribed region](https://hgvs-nomenclature.org/stable/recommendations/DNA/deletion/#examples):

Change the negative examples into positive ones.

> Genomic deletions extending 5' of a transcript can additionally be described
> like `NC_000023.11(NM_004006.2):c.(u?_-244)_(31+1_32-1)del` (`c.-244` is the
> first nucleotide of `NM_004006.2`). Deletions extending 3' of a transcript
> can be described like
> `NC_000023.11(NM_004006.2):c.(10086+1_10087-1)_(*2691_d?)del` (`c.*2691` is
> the last nucleotide of `NM_004006.2`).

[Deletions of genes](https://hgvs-nomenclature.org/stable/recommendations/DNA/deletion/#examples):

Add a gene deletion example.

> `NC_000023.11:g.31118229_33212557del` or
> `NC_000023.11(NM_004006.2):c.u1000_d1000del`: a deletion of the entire *DMD*
> gene, where the deletion starts 1000 nucleotides before the transcription
> start site and ends 1000 nucleotides after the end of the transcript.

[Duplications extending beyond the transcribed region](https://hgvs-nomenclature.org/stable/recommendations/DNA/duplication/#examples):

Change the negative examples into positive ones.

> Genomic duplications extending 5' of a transcript can additionally be
> described like `NC_000023.11(NM_004006.2):c.(u?_-244)_(31+1_32-1)dup`
> (`c.-244` is the first nucleotide of `NM_004006.2`). Duplications extending
> 3' of a transcript can be described like
> `NC_000023.11(NM_004006.2):c.(10086+1_10087-1)_(*2691_d?)dup` (`c.*2691` is
> the last nucleotide of `NM_004006.2`).

[Duplication of genes](https://hgvs-nomenclature.org/stable/recommendations/DNA/duplication/#examples)

Add a gene duplication example.

> `NC_000023.11:g.31118229_33212557dup` or
> `NC_000023.11(NM_004006.2):c.u1000_d1000dup`: a duplication of the entire
> *DMD* gene, including 1000 upstream and downstream nucleotides.

Remove the line:

> Describing the duplication based on a coding DNA reference sequence using
> `NC_000023.11(NM_004006.2):c.(-205839_-62966)_(*21568_*61692)dup` makes no
> sense."

[How should I describe a variant in the promoter region of a gene?](https://hgvs-nomenclature.org/stable/recommendations/DNA/substitution/#discussion)

Change the (already positive) example.

> [...] However, when using a genomic reference sequence, this variant can be
> described as `NC_000023.10(NM_004006.2):c.u128110C>T` or
> `NC_000023.10(NM_000109.4):c.u278C>T`. [...]
