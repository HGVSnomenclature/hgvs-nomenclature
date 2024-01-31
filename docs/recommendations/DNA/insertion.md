# Insertion

<!-- ## Definition -->

Insertion: a sequence change where, compared to the reference sequence, one or more nucleotides are inserted **and** where the insertion is not a copy of a sequence immediately 5'.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml dna.ins
```

## Notes

- the "positions flanking" should contain **two flanking nucleotides**, e.g., 123 and 124, but not 123 and 125.
    - † = see [Uncertain](../uncertain.md); when the position and/or the sequence of an inserted sequence has not been defined, a description may have a format like `g.(100_150)insN[25]`.
    - the "positions_flanking" should be listed from 5' to 3', e.g., `123_124`, not `124_123`.
- tandem duplications are described as a duplication (`g.123_456`<code class="spot1">dup</code>), not an insertion (<code class="invalid">g.456_457ins123_456</code>, see [Prioritization](../general.md)).
    - **inverted duplications** are described as insertion (`g.234_235ins123_234inv`), not as a duplication (see [Inversion](inversion.md)).
- two variants separated by one or more nucleotides should be described individually and **not** as a "delins".<br>
  **exception**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins".<br>
  **NOTE**: the SVD-WG has prepared a proposal to modify this recommendation (see [SVD-WG010](../../consultation/SVD-WG010.md)).
  The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant**.
- for all descriptions, the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- the **"inserted_sequence"** can be given as the nucleotides inserted (e.g., `insAGC`) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g., `c.849_850ins858_895`) or another reference (e.g., `NC_000002.11:g.47643464_47643465ins[NC_000022.10:g.35788169_35788352]`).
  When the inserted sequence is not present in the reference genome it should be submitted to a database (e.g., [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/)) and the accession.version number obtained to refer to it.
    - † = see [Uncertain](../uncertain.md); when the position and/or the sequence of an inserted sequence has not been defined, a description may have a format like `g.(100_150)insN[25]`.

## Examples

- simple insertions
    - **`NC_000023.10:g.32867861_32867862insT` (`NM_004006.2:c.169_170insA`)**<br>
    the insertion of a `T` nucleotide between nucleotides `g.32867861` and `g.32867862`.

    - **`NC_000023.10:g.32862923_32862924insCCT` (`LRG_199t1:c.240_241insAGG`)**<br>
    the insertion of nucleotides `CCT` between nucleotides `g.32862923` and `g.32862924`.

    - **`NM_004006.2:c.849_850ins858_895`**<br>
    the insertion of a copy of nucleotides `c.858` to `c.895` between nucleotides `c.849` and `c.850`.

    - **`NC_000002.11:g.47643464_47643465ins[NC_000022.10:g.35788169_35788352]`**<br>
    the insertion of nucleotides `g.35788169` to `g.35788352` as found in `NC_000022.10` between nucloetides `g.47643464` and `g.47643465`.

- complex insertions
    - **`NM_004006.2:c.419_420ins[T;401_419]`**<br>
    the insertion of `T` followed by a copy of the sequence from `c.401` to `c.419` (a duplication not directly flanking the original sequence).

    - **`LRG_199t1:c.419_420ins[T;450_470;AGGG]`**<br>
    the insertion of `T` followed by a copy of the sequence from `c.450` to `c.470`, followed by `AGGG`.

    - **`NC_000006.11:g.10791926_10791927ins[NC_000004.11:g.106370094_106370420;A[26]]`**<br>
    the insertion of a copy of an Alu-repeat sequence (from chromosome 4 nucleotides `g.106370094` to `g.106370420`), and a stretch of 26 `A` nucleotides, between nucleotides `g.10791926` and `g.10791927` on chromosome 6.

- insertion of inverted duplicated copies
    - **`NM_004006.2:c.849_850ins850_900inv`**<br>
    a copy of nucleotides `c.850` to `c.900` is inserted, in inverted orientation, 5' of the original sequence, between nucleotides `c.849` and `c.850`.

    - **`NM_004006.2:c.900_901ins850_900inv`**<br>
    a copy of nucleotides `c.850` to `c.900` is inserted, in inverted orientation, 3' of the original sequence, between nucleotides `c.900` and `c.901`.

    - **`LRG_199t1:c.940_941ins[885_940inv;A;851_883inv]`**<br>
    an inverted copy of nucleotides `c.851` to `c.940`, with a `G>A` substitution of nucleotide `c.884`, is inserted directly 3' of the original sequence.

    - **`NM_004006.2:c.940_941ins[903_940inv;851_885inv]`**<br>
    an inverted copy of nucleotides `c.851` to `c.940`, with a deletion from nucleotides `c.886` to `c.902`, is inserted directly 3' of the original sequence.

- incomplete descriptions, preferably use exact descriptions only
    - **`NM_004006.2:c.(222_226)insG`**<br>
    the insertion of a `G` at an unknown position in the sequence encoding amino acid 75.

    - **`NC_000004.11:g.(3076562_3076732)insN[12]`**<br>
    the insertion of 12 nucleotides (not specified) at an unknown position between nucleotides `g.3076562` and `g.3076732` (exon 1 of the _HTT_ gene containing the Gln/Pro repeat region).

    - **`NC_000023.10:g.32717298_32717299insN` (`NM_004006.2:c.761_762insN`) **<br>
    the insertion of one not specified nucleotide (`N`) between positions `g.32717298` and `g.32717299`.

    - **`NM_004006.2:c.761_762insNNNNN` (alternatively `NM_004006.1:c.761_762insN[5]`)**<br>
    the insertion of 5 not specified nucleotides (`NNNNN`) between positions `c.761` and `c.762`.

    - **`NC_000023.10:g.32717298_32717299insN[100]`**<br>
    the insertion of 100 nucleotides (not specified) between positions `g.32717298` and `g.32717299`.

    - **`NC_000023.10:g.32717298_32717299insN[(80_120)]`**<br>
    the insertion of 80 to 120 nucleotides between positions `g.32717298` and `g.32717299`.

    - **`NC_000023.10:g.32717298_32717299insN[?]`**<br>
    the insertion of an unknown number of nucleotides between positions `g.32717298` and `g.32717299`.

    - **`NC_000006.11:g.8897754_8897755ins[N[543];8897743_8897754]`**<br>
    the insertion of an undefined sequence of 543 nucleotides (`N[543]`), and a 12 nucleotide target site duplication (`g.8897743` to `g.8897754`), between nucleotides `g.8897754` and `g.8897755` on chromosome 6.

- other
    - **`g.?_?ins[NC_000023.10:g.(12345_23456)_(34567_45678)]`**<br>
    the insertion of a sequence from the X-chromosome (`NC_000023.10`), maximally involving nucleotides `12345_45678` but certainly nucleotides `23456_34567`, at an unknown position (`g.?_?`) in the genome (see [Uncertain](../uncertain.md)).

## Discussion

!!! note "Can I describe a variant as <code class="invalid">g.123insG</code>?"

    No, since the description is not unequivocal it is not allowed.
    What does the description mean, the insertion of a `G` **at** position `g.123` or the insertion of a `G` **after** position `g.123`?

    The situation becomes even more complex when, using a coding DNA reference sequence, a "-" character is used; e.g., <code class="invalid">c.-14insG</code> or <code class="invalid">c.456-13insG</code>.
    In the description <code class="invalid">c.456-13insG</code>, when the insertion is **after** intronic nucleotide `c.456-13`, is this position `c.456-12` or `c.456-14`?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format <code class="invalid">g.123ˆ124insG</code> or <code class="invalid">g.123ˆ124G</code>.
    The recommendations try to restrict the number of different characters used to a minimum.
    Since a character was already used to indicate a range (the *underscore*) a new character was not required.

!!! note "How should I describe the change `ATCG`<code class="spot1">ATCGATCGATCG</code><code class="spot2">A</code>`GGGTCCC` to `ATCG`<code class="spot1">ATCGATCGATCG</code><code class="spot2">A</code><code class="ins">ATCGATCGATCG</code>`GGGTCCC`? The fact that the inserted sequence (<code class="ins">ATCGATCGATCG</code>) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; `g.17_18ins5_16`.
    A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem).
    Note that the description given still makes it clear that the sequence inserted between `g.17` and `g.18` is probably derived from nearby, i.e. positions `g.5` to `g.16`, and thus likely derived from a duplicative event.

!!! note "A variant in the _CDKN2A_ gene, duplicating the first 24 nucleotides of the coding DNA reference sequence, has been described as <code class="invalid">c.23ins24</code>. My interpretation is it should be described as `c.1_24dup`, is this correct?"

    Since the sequence in that region is <span class="sequence">cagc<code class="spot1">ATGGAGCC</code>GGCGGCGGGGAGCAGC<code class="spot1">ATGGAGCC</code>TTCG</span> the correct decription is `c.9_32dup` (`p.(Ala4_Pro11dup)`). `c.1_24dup` seems correct but neglects the **3'rule** (3' shift possible for the highlighted region). `c.23ins24` is not correct since the position of the insertion is not described properly and because ins"24" does not define the sequence inserted.
