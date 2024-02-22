# Insertion

<!-- ## Definition -->

Insertion: a sequence change where, compared to the reference sequence, one or more nucleotides are inserted **and** where the insertion is not a copy of a sequence immediately 5'.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.ins
```

## Notes

- `positions flanking` should contain **two flanking nucleotides**, e.g., `123_124`, not `123_125`.
- the `positions_flanking` should be listed from **5' to 3'**, e.g., `123_124`, not `124_123`.
- tandem duplications are described as a duplication (`r.123_456`<code class="spot1">dup</code>), not an insertion (<code class="invalid">r.456_457ins123_456</code>, see [Prioritization](../general.md)).
  - **inverted duplications** are described as an insertion (`r.234_235ins123_234inv`), not as a duplication (see [Inversion](inversion.md)).
- for all descriptions, the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- the **"inserted_sequence"** can be given as the nucleotides inserted (e.g., `insagc`) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g., `r.849_850ins858_895`) or another reference (see Examples).
  When the inserted sequence is not present in a reference sequence, it should be submitted to a database (e.g., [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/)); the accession.version number obtained can then be used to describe the variant, like `r.123_124ins[L37425.1:r.23_361]`.
- † = see [Uncertain](../uncertain.md); when the position and/or the sequence of an inserted sequence has not been defined, a description may have a format like `r.(100_150)insn[25]`.

## Examples

- **`LRG_199t1:r.426_427insa`**<br>
  the insertion of an `a` nucleotide between nucleotides `r.426` and `r.427`.

- **`LRG_199t1:r.756_757insuacu`**<br>
  the insertion of nucleotides `uacu` between nucleotides `r.756` and `r.757`.

- **`NM_004006.2:r.(222_226)insg` (`p.Asn75fs`)**<br>
  the insertion of a `g` at an unknown position in the sequence encoding amino acid 75.

- **`NM_004006.2:r.549_550insn`**<br>
  the insertion of one not specified nucleotide (`n`) between positions `r.549` and `r.550`.

- **`NM_004006.2:r.761_762insnnnnn` (alternatively `r.761_762insn[5]`)**<br>
  the insertion of 5 not specified nucleotides (`nnnnn`) between positions `r.761` and `r.762`.

- **`LRG_199t1:r.1149_1150insn[100]`**<br>
  the insertion of 100 not specified nucleotides between positions `r.1149` and `r.1150`.

- <code class="invalid">NG_012232.1(NM_004006.2):r.2949_2950ins[2950-30_2950-12;2950-4_2950-1]</code><br>
  the insertion of intronic nucleotides `r.2950-30` to `r.2950-12` and `r.2950-4` to `r.2950-1` between nucleotides `r.2949` and `r.2950` (caused by the deletion `NC_000023.10(NM_004006.2):c.2950-11_2950-5del`).
  Alternative description <code class="invalid">r.2949_2950ins[2950-30_2950-12;uuag]</code>.<br>
  **NOTE**: for more examples of variants affecting splicing, see [Splicing](splicing.md).

## Discussion

!!! note "Can I describe a variant as <code class="invalid">r.123insg</code>?"

    No, since the description is not unequivocal, it is not allowed.
    What does the description mean, the insertion of a `g` **at** position `r.123` or the insertion of a `g` **after** position `r.123`?

    The situation becomes even more complex when, using a coding RNA reference sequence, a "-" character is used; e.g., <code class="invalid">r.-14insG</code>.
    When the insertion is **after** nucleotide `r.-14`, is this position `r.-13` or `r.-15`?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format <code class="invalid">r.123ˆ124insu</code> or <code class="invalid">r.123ˆ124u</code>.
    The recommendations try to restrict the number of different characters used to a minimum.
    Since a character was already used to indicate a range (the *underscore*), a new character was not required.

!!! note "How should I describe the change `aucg`<code class="spot1">aucgaucgaucg</code><code class="spot2">a</code>`ggguccc` to `aucg`<code class="spot1">aucgaucgaucg</code><code class="spot2">a</code><code class="ins">aucgaucgaucg</code>`ggguccc`? The fact that the inserted sequence (<code class="ins">aucgaucgaucg</code>) is present in the original sequence, suggests it derives from a duplicative event."

    The variant should be described as an insertion; `r.17_18ins5_16`.
    A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem).
    Note that the description given still makes it clear that the sequence inserted between `r.17` and `r.18` is probably derived from nearby, i.e. positions `r.5` to `r.16`, and thus likely derived from a duplicative event.
