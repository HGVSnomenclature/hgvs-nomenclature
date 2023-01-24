---
parent: Protein
title: deletion-insertion
category: description
---

Format:   **"prefix""amino_acid(s)+position(s)\_deleted""delins""inserted\_sequence"**,  e.g. p.(Arg123\_Lys127delinsSerAsp)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino\_acid(s)+position(s)\_deleted"**  =  position amino acid or range of amino acids deleted  =  Arg123\_Lys127<br>
**"delins"**  =  type of change is a deletion-insertion  =  delins<br>
**"inserted_sequence"**  =  description inserted sequence  =  SerAsp<br>

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg123_Lys127delinsSerAsp).
*	by definition, when **one** amino acid is replaced with **one** other amino acid, the change is a [_substitution_](/recommendations/protein/variant/substitution/), not a deletion-insertion.
*	changes involving two or more consecutive amino acids are described as a deletion/insertion variant (delins) (see [_Substitution_](/recommendations/protein/variant/substitution/).
	*	_**NOTE**_:	this does not mean that at the DNA or RNA level the variant is described as a "delins" variant as well; on DNA level other rules may apply.
	*	the description p.Arg76\_Cys77delinsSerTrp is correct, the description p.[Arg76Ser;Cys77Trp] is not correct.
	*	two variants separated by one or more amino acids should be described individually and not as a “delins”.
*	for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (_**3'rule**_).
*	when the inserted amino acid sequence is large the insertion may be described by its length only, e.g. p.Arg456_Leu488delins(54)
	*	_**NOTE**_:	the inserted amino acid sequence can be derived from the description od the variant at DNA or RNA level.
*	deletion/insertion variants extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as [_Extension_](/recommendations/protein/variant/extension).
*	deletion-insertion variants at the DNA or RNA level.
	*	which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant, e.g. p.Tyr4Ter (or p.Tyr4*) not p.Cys5\_Ser6delinsTerGluAsp.
	*	**encoding a translation stop codon** in the inserted sequence are described as deletion-insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
	*	encoding an open reading frame which **after** the inserted sequence shift to another reading frame are described as a [_**frame shift**_](/recommendations/protein/variant/frameshift/).
	*	**starting N-terminal (5') of and including** the translation termination (stop) codon are described as [_**frame shift**_](/recommendations/protein/variant/frameshift).
*	fusion proteins represent a special case of deletion-insertion variant. The fusion break point is described using **"::"**
	:	**_NOTE:_**	to avoid confusion, HGVS recommends to follow the [HGNC guidelines](https://www.genenames.org/about/guidelines/){:target="\_blank"} to describe products of gene translocations or fusions (format GENESYMBOL1::GENESYMBOL2) and readthrough transcripts (format GENESYMBOL1-GENESYMBOL2)
