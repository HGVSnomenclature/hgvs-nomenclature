# insertion

## Definition

Insertion: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to the reference sequence, one or more amino acids are inserted, which is not a frame shift and where the insertion is not a copy of a sequence immediately N-terminal (5') 

## Description

Format: **"prefix""amino_acids+positions_flanking""ins""inserted_sequence"**,  e.g. p.(Lys23\_Leu24insArgSerGln)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acids+positions_flanking"**  =  amino acids with position flanking insertion site  =  Lys23\_Leu24<br>
**"ins"**  =  type of change is an insertion  =  ins<br> 
**"inserted_sequence"**  =  inserted sequence  =  ArgSerGln

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* **prefix** reference sequence accepted is "p." (protein).
* predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727\_Ser728insTrpCys).
* the "amino\_acids+positions\_flanking" should contain **two flanking residues**, e.g. Lys23 and Leu24, not two non-flanking residues (Lys23 and Asn25).
    * an insertion can not be described using **one** amino acid position, like p.Lys23insAsp.
* for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
* duplicating insertions should be described as duplications ([_see Duplication_](/recommendations/DNA/variant/duplication/)), not as insertion.
* when the inserted amino acid sequence is large the insertion may be described by its length, e.g. p.Lys2\_Leu3insX[34] (open reading frame insertion) or p.Lys2\_Leu3insTer12 (translation stop in inserted sequence).
:    **NOTE:**    the inserted amino acid sequence can be derived from the description od the variant at DNA or RNA level.
* insertions extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as [_Extension_](/recommendations/protein/variant/extension).    
* insertions at DNA or RNA level
    * which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant.
    * **encoding a translation stop codon** in the inserted sequence are at the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    * encoding an open reading frame which **after** the inserted sequence shift to another reading frame are described as a [**frame shift**](/recommendations/protein/variant/frameshift/)
## Examples

* p.His4\_Gln5insAla: the insertion of amino acid <font color="red">Ala</font> between amino acids His4 and Gln5 changing MetLysGlyHisGlnGlnCys to MetLysGlyHis**<font color="red">Ala</font>**GlnGlnCys
* p.Lys2\_Gly3insGlnSerLys: the insertion of amino acids <font color="red">GlnSerLys</font> between amino acids Lys2 and Gly3 changing MetLysGlyHisGlnGlnCys to MetLys**<font color="red">GlnSerLys</font>**GlyHisGlnGlnCys
* p.(Met3\_His4insGlyTer): the predicted consequence at the protein level of an insertion at the DNA level (c.9\_10insGGGTAG) is the insertion of GlyTer (alternatively Gly\*): **NOTE**: this is not described as p.(Met3\_Ile3418delinsGly), a deletion-insertion replacing the entire C-terminal protein coding sequence downstream of Met3 with a Gly)
* NP\_004371.2:p.(Pro46_Asn47insSerSerTer): the predicted consequence at the protein level resulting from DNA variant NM\_004380.2:c.138\_139insTCATCATGAGCTCCC is te insertion of "SerSerTer" between amino acids Pro46 and Asn47 (alternatively SerSer\*).: **NOTE:** the insertion is not described as "insSerSerTerAlaPro", amino acids after the translation termination codon are not listed
* p.Arg78\_Gly79insX[23]: the in-frame insertion of a 23 amino acid sequence between amino acids Arg78 and Gly79: **NOTE:** it must be possible to deduce the 23 inserted amino acids from the description given at DNA or RNA level
* NP\_060250.2:p.Gln746\_Lys747ins\*63: the in-frame insertion of a 62 amino acid sequence ending at a stop codon at position \*63 between amino acids Gln746 and Lys747: **NOTE:** it must be possible to deduce the inserted amino acid sequence from the description given at DNA or RNA level
* incomplete descriptions (preferably use exact descriptions only)
    * NP\_003997.1:p.(Ser332\_Ser333insX[1]): the insertion of an unknown amino acid ('insX[1]') between amino acids Ser332 and Ser333: **NOTE**: the IUPAC code for an unknown amino acid is 'X' ([_see Standards_](/background/standards/)). Note that in the past 'X' has been used to indicate a translation termination codon.
    * NP\_003997.1:p.(Val582\_Asn583insX[5]) (alternatively NP_003997.1:p.(Val582_Asn583insXXXXX)): the insertion of 5 unknown amino acids (insX[5]) between amino acids Val582 and Asn583
## Discussion

!!! note "Can I describe a variant as p.His4insAla?"

    No, since the description is not unequivocal it is not allowed. What does the description mean, the insertion of a Ala <b>at</b> position 4 or the insertion of a Ala <b>after</b> position 4?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format p.His4Gln5insAla or p.123ˆ124Ala. The recommendations try to restrict the number of different characters used to a minimum. Since a character was already used to indicate a range (the <i>underscore</i>) a new character was not required.

!!! note "How should I describe the change "MetArgThr<b>GlySerSer</b>HisGlnTrpPhe" to "MetArgThr<b>GlySerSer</b>His<b>GlySerSer</b>GlnTrpPhe"?  The fact that the inserted sequence (GlySerSer) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; p.His7_Gln8insGly4_Ser6. A description using "dup" is not correct since, by definition, a duplication should be <b>directly 3'-flanking of the original copy</b> (in tandem). Note that the description given still makes it clear that the sequence inserted between p.His7 and pGln8 is probably derived from nearby, i.e. position p.Gly4 to p.Ser6, and thus likely derived from a duplicative event.
