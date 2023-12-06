# Insertion

<!-- ## Definition -->

Insertion: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to the reference sequence, one or more amino acids are inserted, which is not a frameshift and where the insertion is not a copy of a sequence immediately N-terminal (5')

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.ins
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. `p.(Arg727_Ser728insTrpCys)`.
- the "amino_acids+positions_flanking" should contain **two flanking residues**, e.g. Lys23 and Leu24, not two non-flanking residues (Lys23 and Asn25).
    - an insertion can not be described using **one** amino acid position, like `p.Lys23insAsp`.
- for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- duplicating insertions should be described as duplications (see [Duplication](../DNA/duplication.md)), not as insertion.
- when the inserted amino acid sequence is large the insertion may be described by its length, e.g. `p.Lys2_Leu3insX[34]` (open reading frame insertion) or `p.Lys2_Leu3insTer12` (translation stop in inserted sequence). : **NOTE:** the inserted amino acid sequence can be derived from the description od the variant at DNA or RNA level.
- insertions extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as [Extension](extension.md).
- insertions at DNA or RNA level
    - which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant.
    - **encoding a translation stop codon** in the inserted sequence are at the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    - encoding an open reading frame which **after** the inserted sequence shift to another reading frame are described as a [frameshift](frameshift.md)

## Examples

- `p.(Met3_His4insGlyTer)`: the predicted consequence on the protein level of an insertion at the DNA level (c.9_10insGGGTAG) is the insertion of GlyTer (alternatively Gly\*): **NOTE**: this is not described as `p.(Met3_Ile3418delinsGly),` a deletion-insertion replacing the entire C-terminal protein coding sequence downstream of Met3 with a Gly)
- `NP_004371.2:p.(Pro46_Asn47insSerSerTer)`: the predicted consequence on the protein level resulting from DNA variant `NM_004380.2:c.138_139insTCATCATGAGCTCCC` is the insertion of "SerSerTer" between amino acids Pro46 and Asn47 (alternatively SerSer\*).: **NOTE:** the insertion is not described as "insSerSerTerAlaPro", amino acids after the translation termination codon are not listed
- incomplete descriptions (preferably use exact descriptions only)
    - `NP_003997.1:p.(Ser332_Ser333insX[1])`: the insertion of an unknown amino acid ('insX[1]') between amino acids Ser332 and Ser333: **NOTE**: the IUPAC code for an unknown amino acid is 'X' (see [Standards](../../background/standards.md)). Note that in the past 'X' has been used to indicate a translation termination codon.
    - `NP_003997.1:p.(Val582_Asn583insX[5])` (alternatively `NP_003997.1:p.(Val582_Asn583insXXXXX))`: the insertion of 5 unknown amino acids (insX[5]) between amino acids Val582 and Asn583

## Discussion

!!! note "Can I describe a variant as `p.His4insAla`?"

    No, since the description is not unequivocal it is not allowed. What does the description mean, the insertion of a Ala **at** position 4 or the insertion of a Ala **after** position 4?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format `p.His4Gln5insAla` or `p.123ˆ124Ala`. The recommendations try to restrict the number of different characters used to a minimum. Since a character was already used to indicate a range (the *underscore*) a new character was not required.

!!! note "How should I describe the change "MetArgThr**GlySerSer**HisGlnTrpPhe" to "MetArgThr**GlySerSer**His**GlySerSer**GlnTrpPhe"? The fact that the inserted sequence (GlySerSer) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; `p.His7_Gln8insGly4_Ser6`. A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem). Note that the description given still makes it clear that the sequence inserted between `p.His7` and `p.Gln8` is probably derived from nearby, i.e. position `p.Gly4` to `p.Ser6`, and thus likely derived from a duplicative event.
