---
parent: Protein
title: insertion
category: description
---

Format: **"prefix""amino_acids+positions_flanking""ins""inserted_sequence"**,  e.g. p.(Lys23\_Leu24insArgSerGln)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acids+positions_flanking"**  =  amino acids with position flanking insertion site  =  Lys23\_Leu24<br>
**"ins"**  =  type of change is an insertion  =  ins<br> 
**"inserted_sequence"**  =  inserted sequence  =  ArgSerGln

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727\_Ser728insTrpCys).
*	the "amino\_acids+positions\_flanking" should contain **two flanking residues**, e.g. Lys23 and Leu24, not two non-flanking residues (Lys23 and Asn25).
	*	an insertion can not be described using **one** amino acid position, like p.Lys23insAsp.
*	for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (_**3'rule**_).
*	duplicating insertions should be described as duplications ([_see Duplication_](/recommendations/DNA/variant/duplication/)), not as insertion.
*	when the inserted amino acid sequence is large the insertion may be described by its length only, e.g. p.Lys2\_Leu3insX[34]
:	_**NOTE:**_	the inserted amino acid sequence can be derived from the description od the variant at DNA or RNA level.
*	insertions extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as [_Extension_](/recommendations/protein/variant/extension).	
*	insertions at DNA or RNA level
	*	which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant.
	*	**encoding a translation stop codon** in the inserted sequence are at the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
	*	encoding an open reading frame which **after** the inserted sequence shift to another reading frame are described as a [_**frame shift**_](/recommendations/protein/variant/frameshift/)
