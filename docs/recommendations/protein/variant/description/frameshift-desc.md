---
parent: Protein
title: frame shift
category: description
---

Format:   **"prefix""amino_acid"position"new_amino_acid""fs""Ter""position_termination_site"**,  e.g. p.(Arg123LysfsTer34)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acid"**  =  first amino acid changed  =  Arg<br>
**"position"**  =  position  =  123<br>
**"new_amino_acid"**  =  new amino acid  =  Lys<br>
**"fs"**  =  type of change is a frame shift  =  fs<br>
**"Ter"**  =  termination codon  =  Ter / \*<br>
**"position_termination_site"**  =  position new termination site  =  34

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg123LysfsTer34).
*	for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (_**3'rule**_)
*	frame shifts are a special type of amino acid **deletion/insertion** which, by definition, do not include the deletion from the site of the change to the C-terminal end of the protein (translation termination (stop) codon), like "Arg123\_Leu833del", nor the amino acid sequence inserted.
	*	the description of a frame shift starts with the **first new** amino acid, this might not be first codon affected by the variant at the DNA level
	*	the position of the translation termination (stop) codon in the new reading frame is calculated **starting** at the first amino acid changed by the frame shift (codon 1), and **ending** at the first stop codon encountered (Ter# or \*#)<br>
		*	_**NOTE**_: the number of amino acids in the new C-terminal sequence is "#-1" amino acids<br>
		*	_**NOTE**_: the shortest frame shift variant possible contains "fsTer2"; variants which introduce an **immediate** translation termination (stop) codon are described as nonsense variant, e.g. p.Tyr4Ter (or PTyr4*) not p.Tyr4TerfsTer1 ([_see Substitution_](/recommendations/protein/variant/substitution/)).
	*	frame shifts can also be described using a **short format**; p.Arg123fs i.e. indicating the first amino acid changed, its position and "fs" without further detail.
*	the (predicted) amino acid changes of additional variants on the same allele (in cis) downstream of the frame shift are not described unless they change the amino acid sequence or length of the shifted reading frame (i.e. introduce an amino acid substitution, an earlier translational termination (stop) codon or affect the termination codon of the shifted frame). 	
*	deletions starting 5’ of and including the translation termination (stop) codon are described as **frame shift**
*	inserted sequences at DNA or RNA level
	*	extending the amino acid sequence at the C-terminal end with one or more amino acids are described as [_Extension_](/recommendations/protein/variant/extension/)
	*	containing a **translation stop codon** in the inserted sequence are described as an insertion, not as a deletion-insertion removing the entire C-terminal amino acid sequence
	*	encoding an open reading frame but after the DNA insertion shifting to another reading are described as a **frame shift**
