# Duplication

<!-- ## Definition -->

Duplication: a sequence change where, compared to a reference sequence, a copy of one or more nucleotides is inserted **directly 3'** of the original copy of that sequence.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.dup
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- `positions_duplicated` should contain **two different positions**, e.g., `123_126`, not `123_123`.
- the `positions_duplicated` should be listed from **5' to 3'**, e.g., `123_126`, not `126_123`.
- by definition, duplication may only be used when the additional copy is **directly 3'-flanking** of the original copy (a "tandem duplication").
    - when a variant can be described as a duplication, it **must** be described as a duplication and not as e.g., an insertion (see [Prioritization](../general.md)).
    - when there is no evidence that the extra copy of a sequence detected is in tandem (directly 3'-flanking the original copy), the change can not be described as a duplication, it should be described as **an insertion** (see [Insertion](insertion.md)).
    - **inverted duplications** are described as an insertion (`r.234_235ins123_234inv`), not as a duplication (see [Inversion](inversion.md)).
- for all descriptions, the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
    - the 3'rule also applies for changes in single residue stretches and tandem repeats.
    - **NOTE**: the exception to the 3'rule for duplications around exon/exon junctions (see [Duplications](../DNA/duplication.md)) does not apply when describing variants based on an RNA reference sequence.

## Examples

- **`r.7dup` (one nucleotide)**<br>
  the duplication of a `u` at position `r.7` in the sequence `acuuacu`<code class="ins">u</code>`gcc`.<br>
  **NOTE**: it is **not** allowed to describe the variant as <code class="invalid">r.6_7insu</code> (see [prioritisation](../general.md)).

- **`r.6_8dup` (several nucleotides)**<br>
  a duplication from position `r.6` to `r.8` in the sequence `acaauugc`<code class="ins">ugc</code>`c`.<br>
  **NOTE**: the recommendation is not to describe the variant as <code class="invalid">r.6_8dupugc</code>, i.e., describe the deleted nucleotide sequence.

## Discussion

!!! note "Why do we not describe a duplication as an insertion?"

    Although duplications are basically a special type of insertion, there are several reasons why the recommendation is to describe duplications separately.

    - the description is simple and shorter;
    - it is clear and prevents confusion regarding the position when an insertion is incorrectly reported, like <code class="invalid">c.22insG</code>;
    - insertion more or less means "coming from elsewhere".
      Mechanistically, a duplication is most likely caused by a local event, DNA polymerase slippage, duplicating a local sequence.

!!! note "How should I describe the change `aucg`<code class="spot1">aucgaucgaucg</code><code class="spot2">a</code>`ggguccc` to `aucg`<code class="spot1">aucgaucgaucg</code><code class="spot2">a</code><code class="ins">aucgaucgaucg</code>`ggguccc`? The fact that the inserted sequence (<code class="ins">aucgaucgaucg</code>) is present in the original sequence, suggests it derives from a duplicative event."

    The variant should be described as an insertion; `r.17_18ins5_16`.
    A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem).
    Note that the description given still makes it clear that the sequence inserted between `r.17` and `r.18` is probably derived from nearby, i.e. positions `r.5` to `r.16`, and thus likely derived from a duplicative event.
