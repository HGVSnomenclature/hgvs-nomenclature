---
parent: Protein
title: duplication
category: description
---

Format:  **"prefix""amino\_acid(s)+position(s)\_duplicated""dup"**,  e.g. p.(Cys76\_Glu79dup)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acid(s)+position(s)\_duplicated"**  =  amino acid with position or range (first amino acid with position to last amino acid with position) duplicated  =  Cys76\_Glu79<br>
**"dup"**  =  type of change is a duplication =  dup

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727\_Ser783dup).
*	the "amino\_acids+positions\_duplicated" should contain **two different** positions, i.e. Cys76\_Glu79, not Cys76\_Cys76.
	*	the "positions\_duplicated" should be listed from **5' to 3'**, i.e. Cys76\_Glu79, not Glu79\_Cys76.
*	by definition, duplication may only be used when the additional copy is **directly C-terminal** of the original copy (a "tandem duplication").
	*	when the extra copy is, at the protein level, not in tandem (directly C-terminal), the change should be described as **insertion** ([_see Insertion_](/recommendations/protein/variant/insertion/)).
	*	duplications extending the amino acid sequence at the C-terminal end with one or more amino acids are described as [_Extension_](/recommendations/protein/variant/extension)
*	for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (_**3'rule**_)
*	duplications at the DNA or RNA level, **starting N-terminal of and including** the translation termination (stop) codon usually have no (predicted) effect on the protein level.
*	duplications at DNA or RNA level
	*	which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant.
	*	**encoding a translation stop codon** in the duplicated sequence are at the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
	*	encoding an open reading frame which **after** the duplicated sequence shift to another reading frame are described as a frame shift.
