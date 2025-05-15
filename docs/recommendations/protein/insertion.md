# Insertion

<!-- ## Definition -->

Insertion: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to the reference sequence, one or more amino acids are inserted, which is not a frameshift and where the insertion is not a copy of a sequence immediately N-terminal (5').

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.ins
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg727_Ser728insTrpCys)`.
- the "positions_flanking" should contain **two flanking residues**, e.g., `Lys23_Leu24`, not two non-flanking residues (`Lys23_Asn25`).
    - an insertion can not be described using **one** amino acid position, like <code class="invalid">p.Lys23insAsp</code>.
- for all descriptions, the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- duplicating insertions should be described as duplications (see [Duplication](../DNA/duplication.md)), not as an insertion.
- when the inserted amino acid sequence is large, the insertion may be described by its length, e.g., `p.Lys2_Leu3insXaa[34]` (open reading frame insertion) or `p.Lys2_Leu3insTer12` (translation stop in inserted sequence).<br>
  **NOTE**: the inserted amino acid sequence can be derived from the description of the variant on the DNA or RNA level.
- insertions extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as an [Extension](extension.md).
- insertions on DNA or RNA level that
    - introduce an **immediate** translation termination (stop) codon on the protein level, are described as a nonsense variant.
    - **encode a translation stop codon** in the inserted sequence are on the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    - encode an open reading frame which **after** the inserted sequence shifts to another reading frame, are described as a [frameshift](frameshift.md).

## Examples

- **`p.His4_Gln5insAla`**<br>
  the insertion of amino acid <code class="ins">Ala</code> between amino acids `His4` and `Gln5`, changing `MetLysGlyHisGlnGlnCys` to `MetLysGlyHis`<code class="ins">Ala</code>`GlnGlnCys`.

- **`p.Lys2_Gly3insGlnSerLys`**<br>
  the insertion of amino acids <code class="ins">GlnSerLys</code> between amino acids `Lys2` and `Gly3`, changing `MetLysGlyHisGlnGlnCys` to `MetLys`<code class="ins">GlnSerLys</code>`GlyHisGlnGlnCys`.

- **`p.(Met3_His4insGlyTer)`**<br>
  the predicted consequence on the protein level of an insertion on the DNA level (`c.9_10insGGGTAG`), is the insertion of `GlyTer` (alternatively `Gly*`).<br>
  **NOTE**: this is not described as `p.(Met3_Ile3418delinsGly)`, a deletion-insertion replacing the entire C-terminal protein coding sequence downstream of `Met3` with a `Gly`.

- **`NP_004371.2:p.(Pro46_Asn47insSerSerTer)`**<br>
  the predicted consequence on the protein level resulting from DNA variant `NM_004380.2:c.138_139insTCATCATGAGCTCCC`, is the insertion of `SerSerTer` between amino acids `Pro46` and `Asn47` (alternatively `SerSer*`).<br>
  **NOTE**: the insertion is not described as <code class="invalid">insSerSerTerAlaPro</code>; amino acids after the translation termination codon are not listed.

- **`p.Arg78_Gly79insXaa[23]`**<br>
  the in-frame insertion of a 23 amino acid sequence between amino acids `Arg78` and `Gly79`.<br>
  **NOTE**: it must be possible to deduce the 23 inserted amino acids from the description given on the DNA or RNA level.

- **`NP_060250.2:p.Gln746_Lys747ins*63`**<br>
  the in-frame insertion of a 62 amino acid sequence ending at a stop codon at position `*63` between amino acids `Gln746` and `Lys747`.<br>
  **NOTE**: it must be possible to deduce the inserted amino acid sequence from the description given on the DNA or RNA level.

- incomplete descriptions (preferably use exact descriptions only)
    - **`NP_003997.1:p.(Ser332_Ser333insXaa)`**<br>
      the insertion of an unknown amino acid (`insXaa`) between amino acids `Ser332` and `Ser333`.<br>
      **NOTE**: the IUPAC code for an unknown amino acid is `X` (see [Standards](../../background/standards.md)).
      Note that in the past, `X` has been used to indicate a translation termination codon.
      Therefore, we recommend the use of the three-letter amino acid code only, `Xaa`.

    - **`NP_003997.1:p.(Val582_Asn583insXaa[5])` (alternatively `NP_003997.1:p.(Val582_Asn583insXaaXaaXaaXaaXaa)`)**<br>
      the insertion of 5 unknown amino acids (`insXaa[5]`) between amino acids `Val582` and `Asn583`.

## Discussion

!!! note "Can I describe a variant as <code class="invalid">p.His4insAla</code>?"

    No, since the description is not unequivocal it is not allowed.
    What does the description mean, the insertion of a `Ala` **at** position 4 or the insertion of a `Ala` **after** position 4?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format <code class="invalid">p.His4Gln5insAla</code> or <code class="invalid">p.123ˆ124Ala</code>.
    The recommendations try to restrict the number of different characters used to a minimum.
    Since a character was already used to indicate a range (the *underscore*), a new character was not required.

!!! note "How should I describe the change `MetArgThr`<code class="spot1">GlySerSer</code>`HisGlnTrpPhe` to `MetArgThr`<code class="spot1">GlySerSer</code>`His`<code class="ins">GlySerSer</code>`GlnTrpPhe`? The fact that the inserted sequence (<code class="ins">GlySerSer</code>) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; `p.His7_Gln8insGly4_Ser6`.
    A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem).
    Note that the description given still makes it clear that the sequence inserted between `p.His7` and `p.Gln8` is probably derived from nearby, i.e. position `p.Gly4` to `p.Ser6`, and thus likely derived from a duplicative event.
