# deletion

## Definition

Deletion: a sequence change where, compared to a reference sequence, one or more nucleotides are not present (deleted).

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml rna.deletion
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- The `coordinate_type` must be one of r. (coding and non-coding RNA).
- the "position(s)\_deleted" should contain **two different positions**, e.g. 123_126 but not 123_123.
- the "position(s)\_deleted" should be listed from **5' to 3'**, e.g. 123_126 but not 126_123.
- for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
  - the 3'rule also applies for changes in single residue stretches and tandem repeats (nucleotide or amino acid). **NOTE:** the exception to the 3'rule for deletions around exon/exon junctions see [Deletions](../DNA/deletion.md) does not apply when describing variants based on a RNA reference sequence.
- see [Uncertain](../uncertain.md); when the postion and/or the sequence of a deletion has not been defined, a description may have a format like `r.(100_150)delN[15]`.

## Examples

- one nucleotide
  - `LRG_199t1:r.10del`: a deletion of the U at position r.10 in the reference sequence LRG_199t1
- several nucleotides
  - `NM_004006.2:r.6_8del`: a deletion of nucleotides r.6 to r.8 in the reference sequence NM_004006.2. **NOTE**: it is allowed to describe the variant as <code class="invalid">r.6_8deluug</code>.
  - `LRG_2t1:r.1034_1036del`: a deletion of nucleotides r.1034 to r.1036 ("uug") in the reference sequence LRG_2t1. **NOTE**: since the 3'rule has to be applied the variant, crossing the intron between nucleotides r.1035 and r.1036, is **not** described as <code class="invalid">r.1033_1035del</code> (deletion "guu").
  - `LRG_199t1:r.(4072_5145del)`: the predicted deletion of exon 30 (starting at position r.4072) to exon 36 (ending at position r.5145) of the DMD-gene; RNA has **not been analysed**
- `LRG_199t1:r.=/6_8del`: a mosaic case where from position r.6 to r.8 besides the normal sequence also transcripts are found containing a deletion of this sequence. **NOTE**: for the predicted consequences of a variant the description is `LRG_199t1:r.(6_8del)`.

## Discussion

!!! note "Can I use <code class="invalid">r.123del6</code> to describe a 6 nucleotide deletion?"

    No, a deletion of more than one residue should mention the first and last residue deleted, separated using the range symbol ("_", underscore), e.g. `r.123_128del` and not <code class="invalid">r.123del6</code>.

!!! note "Is the description of a deletion of exon 17 as <code class="invalid">r.EX17del</code> still allowed?"

    A description like <code class="invalid">r.EX17del</code> has never been allowed. Descriptions should be specific and indicate the nucleotides affected by the change.
