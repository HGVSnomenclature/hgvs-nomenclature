# repeated sequences

## Definition

Repeated sequence: a sequence where, compared to a reference sequence, a segment of **one or more** nucleotides (the repeat unit) is present several times, one after the other.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml rna.repeated
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- reference sequences accepted are r. (coding and non-coding RNA).
- repeated sequences include both small (mono-, di-, tri-, etc., nucleotide) and larger (kilobase-sized) repeats.
- the format based on **repeat position** is preferred, descriptions of the repeat sequence quickly become too lengthy.
  - **NOTE**: while r.123cug[23] describes a repeat of 23 "cug" units, r.123_125[23] describes a tri-nucleotide repeat of 23 units which **could be interrupted** with other units (e.g. a rare "cua"). The description r.123cug[23] can thus only be used when the repeat was sequenced.
- the format r.-125\_-123cug[4], should not be used; it contains redundant information ("-125\_-123" and "cug").
- for **composite repeats** the basic format can be used, successively listing each different repeat unit; r.456_465[4]466_489[9]490_499[3].

## Examples

- r.-124\_-123[14] (alternatively r.-124ug[14]): a repeated di-nucleotide sequence, with the first unit located from position r.-124 to r.-123, is present in 14 copies.: **NOTE**: when the repeat is variable in the population and the reference sequence has 15 units, the description r.-123ug[14] is preferred over r.-97\_-96del: **NOTE**: when the repeat is variable in the population and the reference sequence has 15 units, the description r.-123ug[17] is preferred over r.-99\_-96dup
- r.-124\_-123[14];[18] (alternatively r.-124ug[14];[18]): a repeated di-nucleotide sequence, with the first unit located from position r.-124 to r.-123, is present in 14 copies on one allele and 18 copies on the other allele
- FMR1 GGC-repeat: in literature the Fragile-X tri-nucleotide repeat is known as the CGG-repeat. Hoever, based on a coding RNA reference sequence (GenBank NM_002024.5) and applying the **3'rule**, the repeat has on the RNA level to be described as a "ggc"-repeat see [Recommendations](../general.md).
  - r.-128\_-126[79]: an extended repeat of exactly 79 units: **NOTE** : r.-128ggc[79] can only be used when the repeat has been sequenced, excluding it is interrupted by one or more "gga"-triplets
  - r.-128\_-126[(600\_800)]: the repeated tri-nucleotide sequence, starting at position c.-128, has an estimated size of between 600 to 800 copies.: **NOTE**: the repeat can be pure or a mix of "ggc" and "gga" triplets.
- HD AGC-repeat: based on the HTT (huntingtin) coding DNA reference sequence (GenBank NM_002111.6), applying the **3'rule**, the Huntington's Disease tri-nucleotide repeat is described as an AGC (not CAG) repeat.
  - c.53AGC[19]: **NOTE**: the coding RNA reference sequence (NM_002111.6) contains an allele of 21 "agc" repeats: **NOTE**: on protein level the reference allele contains 21 Gln's, described as p.Gln[21] (alternatively p.Q[21]). The difference derives from the fact that the "agc" repeat is interrupted by a "aac"-triplet ("caa" coding) at position 20.
  - r.53_55[31]: the coding RNA reference sequence (NM_002111.6) contains a tri-nucleotide allele of 32 repeats (agc-19, aac, agc, cgc, cac, cgc-7, cuc-2) encoding 21 Gln and 11 Pro-residues.

## Discussion

---
