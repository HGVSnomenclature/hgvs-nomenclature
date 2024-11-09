# Adjoined Transcripts

<!-- ## Definition -->

Adjoined Transcript: a transcript (RNA molecule) composed of adjoined RNA from two or more contributing transcripts.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.adjoined_transcript
```

## Notes
- Adjoined transcripts are a product of chimeric transcript gene fusions.
- The adjoined transcript syntax proposed in [Community Proposal SVD WG007](../../consultation/SVD-WG007.md) and adopted
  here has the following limitations:
  - This syntax is for two-partner adjoined transcripts only.
  - This syntax is for RNA sequence only (no use of coding / non-coding DNA reference sequences).
- This syntax REQUIRES the use of a range (not a single position) for `five_prime_range` / `three_prime_range`.
- When the adjoined transcript junction but not the entire transcript is analyzed, the outer range bounds SHOULD be
  specified with `?`, e.g. `NM_152263.2:r.?_775::NM_002609.3:r.1580_?`
- All adjoined transcripts are described using the same format, irrespective of whether they derive
  from inter-chromosomal or intra-chromosomal DNA rearrangements (translocation, deletion, inversion)
  or other mechanisms (trans-splicing).
