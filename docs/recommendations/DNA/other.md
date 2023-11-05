# Other

<!-- ## Definition -->

No change: a sequence was analysed but no variant was detected. Mosaic: the occurrence in one individual of two or more cell populations, derived from a single zygote, with different sequences. Chimeric: the occurrence in one individual of two or more cell populations, derived from different zygotes, with different sequences.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml dna.other
```

## Notes

- see [SVD-WG001 (no change)](../../consultation/SVD-WG001.md) for the original proposal

## Examples

- no change

  - one nucleotide
    - NC_000023.11:g.32867908=: a screen was performed showing nucleotide g.32867908 was a "G" as in the genomic reference sequence (the nucleotide was not changed)
    - LRG_199t1:c.123=: a screen was performed showing nucleotide c.123 was a "C" as in the coding DNA reference sequence (the nucleotide was not changed): **NOTE:** the description c.123C>C is not allowed
  - several nucleotides
    - NC_000023.11:g.32867908_32867923=: a screen was performed showing nucleotides g.32867908 to g.32867923 were as in the genomic reference sequence (the nucleotides were not changed)
    - LRG_199t1:c.123_145=: a screen was performed showing nucleotides c.123 to c.145 were as in the coding DNA reference sequence (the nucleotides were not changed)
    - NM_004006.2:c.[123=;456=;789=]: a screen was performed showing nucleotides c.123, c.456 and c.789 (all on the same allele) were identical to the coding DNA reference (the nucleotides were not changed)

- methylation : descriptions based on Community Consultation [proposal SVD-WG005](../../consultation/SVD-WG005.md) _ NC_000011.10:g.1999904_1999946\|gom: the sequence from position g.1999904 to g.1999946 showed a gain of methylation ("\|gom") _ NC_000011.10:g.1999904_1999946\|lom: the sequence from position g.1999904 to g.1999946 showed a loss of methylation ("\|lom") \* NC_000011.10:g.1999904_1999946\|met=: the sequence from position g.1999904 to g.1999946 showed normal methylation ("\|met=")

- mosaicism
  - LRG_199t1:c.85=/T>C: a mosaic case where at position 85 besides the normal sequence (a T, described as "=") also chromosomes are found containing a C (c.85T>C): **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first
- chimerism
  - NM_004006.2:c.85=//T>C: a chimeric case, i.e. the sample is a mix of cells containing c.85= and c.85T>C.: **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first

## Discussion
