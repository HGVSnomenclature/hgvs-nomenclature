# Repeated Sequences

<!-- ## Definition -->

Repeated sequence: a sequence where, compared to a reference sequence, a segment of **one or more** nucleotides (the repeat unit) is present several times, one after the other.

## Syntax

**NOTE**: a Community Consultation proposal is being prepared which will suggest to allow only the format where the **entire range** of the repeated sequence is indicated; so `r.123_191cag[23]`, **not** `r.123cag[23]`.

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.rpt
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- repeated sequences include both small (mono-, di-, tri-, etc., nucleotide) and larger (kilobase-sized) repeats.
- the format based on **repeat position** is preferred, descriptions of the repeat sequence quickly become too lengthy.<br>
  **NOTE**: while `r.123cug[23]` describes a repeat of 23 `cug` units, `r.123_125[23]` describes a tri-nucleotide repeat of 23 units which **could be interrupted** with other units (e.g., a rare `cua`).
  The description `r.123cug[23]` can thus only be used when the repeat was sequenced.
- the format <code class="invalid">r.-125_-123cug[4]</code> should not be used; it contains redundant information (`-125_-123` and `cug`).
- for **composite repeats**, the basic format can be used, successively listing each different repeat unit; <code class="invalid">r.456_465[4]466_489[9]490_499[3]</code>.

## Examples

- **`r.-124_-123[14]` (alternatively `r.-124ug[14]`)**<br>
  a repeated di-nucleotide sequence, with the first unit located from position `r.-124` to `r.-123`, is present in 14 copies.<br>
  **NOTE**: when the repeat is variable in the population and the reference sequence has 15 units, the description `r.-123ug[14]` is preferred over `r.-97_-96del`.<br>
  **NOTE**: when the repeat is variable in the population and the reference sequence has 15 units, the description `r.-123ug[17]` is preferred over `r.-99_-96dup`.

- **`r.-124_-123[14];[18]` (alternatively `r.-124ug[14];[18]`)**<br>
  a repeated di-nucleotide sequence, with the first unit located from position `r.-124` to `r.-123`, is present in 14 copies on one allele and 18 copies on the other allele.

- _FMR1_ `GGC`-repeat: in literature, the Fragile-X tri-nucleotide repeat is known as the `CGG`-repeat.
  Hoever, based on a coding RNA reference sequence (GenBank `NM_002024.5`) and applying the **3'rule**, on the RNA level, the repeat has to be described as a `ggc`-repeat (see [Recommendations](../general.md)).
    - **`r.-128_-126[79]`**<br>
      an extended repeat of exactly 79 units.<br>
      **NOTE**: `r.-128ggc[79]` can only be used when the repeat has been sequenced, excluding it is interrupted by one or more `gga`-triplets.

    - **`r.-128_-126[(600_800)]`**<br>
      the repeated tri-nucleotide sequence, starting at position `c.-128`, has an estimated size of between 600 and 800 copies.<br>
      **NOTE**: the repeat can be pure or a mix of `ggc` and `gga` triplets.

- HD `AGC`-repeat: based on the _HTT_ (huntingtin) coding DNA reference sequence (GenBank `NM_002111.6`), applying the **3'rule**, on the RNA level, the Huntington's Disease tri-nucleotide repeat is described as an `agc` (not `cag`) repeat.
    - **`r.53agc[19]`**<br>
      **NOTE**: the coding RNA reference sequence (`NM_002111.6`) contains an allele of 21 `agc` repeats.<br>
      **NOTE**: on protein level, the reference allele contains 21 `Gln`s, described as `p.Gln[21]` (alternatively `p.Q[21]`).
      The difference derives from the fact that the `agc` repeat is interrupted by a `aac`-triplet (`caa` coding) at position 20.

    - **`r.53_55[31]`**<br>
      the coding RNA reference sequence (`NM_002111.6`) contains a tri-nucleotide allele of 32 repeats (`agc`-19, `aac`, `agc`, `cgc`, `cac`, `cgc`-7, `cuc`-2) encoding 21 `Gln` and 11 `Pro`-residues.
