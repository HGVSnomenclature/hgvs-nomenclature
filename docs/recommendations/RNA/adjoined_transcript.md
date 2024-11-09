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
    - This syntax is for RNA sequence only (no use of coding (`c.`) / non-coding DNA (`n.`) reference sequences).
    - Linker sequences are specified using [General Recommendations](../general.md) for RNA sequence character codes, e.g. `aggcucccuugg`
- This syntax REQUIRES the use of a range (not a single position) for `five_prime_range` / `three_prime_range`.
- When the adjoined transcript junction but not the entire transcript is analyzed, the outer range bounds SHOULD be
  specified with `?`, e.g. `NM_152263.2:r.?_775::NM_002609.3:r.1580_?`
- All adjoined transcripts are described using the same format, irrespective of whether they derive
  from inter-chromosomal or intra-chromosomal DNA rearrangements (translocation, deletion, inversion)
  or other mechanisms (trans-splicing).

## Examples

- **translocation-derived adjoined transcript**<br>
    `NM_152263.2:r.-115_775::NM_002609.3:r.1580_*1924` describes an adjoined transcript from a `TPM3::PDGFRB` gene fusion, where nucleotides `r.-115` to `r.775` (reference transcript `NM_152263.2`, _TPM3_ gene) are coupled to nucleotides `r.1580` to `r.*1924` (reference transcript `NM_002609.3`, _PDGFRB_ gene).

- **deletion-derived adjoined transcripts**
    - **`NM_002354.2:r.-358_555::NM_000251.2:r.212_*279`**<br>
        describes an adjoined transcript from an `EPCAM::MSH2` gene fusion, where nucleotides `r.-358` to `r.555` (reference transcript `NM_002354.2`, _EPCAM_ gene) are coupled to nucleotides `r.212` to `r.*279` (reference transcript `NM_000251.2`, _MSH2_ gene).

    - **`NM_002354.2:r.?_555::guaugauuuuuuaataa::NM_000251.2:r.212_?`**<br>
        describes an adjoined transcript from an `EPCAM::MSH2` gene fusion, where only the fusion break point has been characterised, showing the insertion of a 17 nucleotide sequence (`guaugauuuuuuaataa`) between two adjoined transcripts.
