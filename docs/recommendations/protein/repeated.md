# repeated sequences

## Definition

Repeated sequence: a sequence where, compared to a reference sequence, a segment of **one or more** amino acids (the repeat unit) is present several times, one after the other..

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml aa.rpt
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- repeated sequences include both small (mono-, di-, tri-, etc., amino acid) and larger repeats.

## Examples

- `p.Ala2[10]`: a repeated amino acid sequence, with the first Ala-residue located at position 2 is present in 10 copies.: **NOTE**: when the repeat is variable in the population and the reference sequence has 10 units, the description `p.Ala2[9]` is preferred over `p.Ala11del.`: **NOTE**: when the repeat is variable in the population and the reference sequence has 10 units, the description `p.Ala2[12]` is preferred over `p.Ala10_Ala11dup.`
- `p.Ala2[10];[11]`: a repeated amino acid sequence, with the first Ala-residue located at position 2, is present in 10 copies on one allele and 11 copies on the other allele.
- `p.Gln18[23]`: a repeated amino acid sequence, with the first Gln-residue located at position 18 is present in 23 copies (HD Gln-repeat based on the HTT (huntingtin) protein reference sequence (GenBank NP_002102.4)): **NOTE**: the protein reference sequence (GenBank NP_002102.4) contains an allele of 23 Gln copies (encoded by 22 "cag" and 1 "caa" codons).
  - `p.(Gln18)[(70_80)]`: the predicted Gln amnio acid repeat, starting at position 18, has an estimated size of between 70 to 80 copiess.: **NOTE**: the repeat can encoded by a mix of different coding triplets ("cag", "caa").
