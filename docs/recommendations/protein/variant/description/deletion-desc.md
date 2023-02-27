---
parent: Protein
title: deletion
category: description
---

Format:  **"prefix""amino_acid(s)+position(s)\_deleted""del"**,  e.g. p.(Cys76\_Glu79del)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acid(s)+position(s)\_deleted"**  =  amino acid with position or range (first amino acid with position to last amino acids with position) deleted  =  Cys76\_Glu79<br>
**"del"**  =  type of change is a deletion =  del

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727\_Ser783del).
*	the "amino\_acids+positions\_deleted" should contain **two different** positions, i.e. Cys76\_Glu79, not Cys76\_Cys76.
	*	the "positions\_deleted" should be listed from **5' to 3'**, i.e. Cys76\_Glu79, not Glu79\_Cys76.
*	for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (_**3'rule**_).
*	in theory, a **nonsense** variant can be considered as a deletion removing the C-terminal end of the protein (e.g. p.Trp26\_Arg1623del). By definition, nonsense variants are described as an amino acid substitution (p.Trp26Ter or p.Trp26* [_see Substitution_](/recommendations/protein/variant/substitution)) replacing the first amino acid affected by a translation termination (stop) codon.
*	variants extending the amino acid sequence at the C-terminal end with one or more amino acids, are described as [_Extension_](/recommendations/protein/variant/extension).
*	deletions at the DNA or RNA level
	*	which introduce an **immediate** translation termination (stop) codon are described as nonsense variant.
	*	**starting N-terminal of and including** the translation termination (stop) codon are described as [_Frame shift_](/recommendations/protein/variant/frameshift).	
