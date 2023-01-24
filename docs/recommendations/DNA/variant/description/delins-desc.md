---
parent: DNA
title: deletion-insertion
category: description
---

Format:   **"prefix""position(s)\_deleted""delins""inserted_sequence"**,  e.g. g.123\_127delinsAG

**"prefix"**  =  reference sequence used  =  g.<br>
**"position(s)\_deleted"**  =  position nucleotide or range of nucleotides deleted  =  123\_127<br>
**"delins"**  =  type of change is a deletion-insertion  =  delins<br>
**"inserted\_sequence"**  =  description inserted sequence  =  AG<br>

---

### Note

*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
*	by definition, when **one** nucleotide is replaced by **one** other nucleotide the change is a [_substitution_](/recommendations/DNA/variant/substitution/).
*	changes involving two or more consecutive nucleotides are described as deletion/insertion (delins) variants
*	two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
	:	**_NOTE:_**	this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position (e.g. c.235\_237delinsTAT (p.Lys79Tyr) versus c.[235A>T;237G>T] (p.[Lys79*;Lys79Asn]).
	:	_**<font color="#FF0000">NOTE:</font>**_ the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/bg-material/consultation/svd-wg010/)). The new proposal is: **two variants that are separated by fewer than two intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
*	**conversions**, a sequence change where a **range of nucleotides** are replaced by a sequence from elsewhere in the genome, are described as a "delins". The previous format "con" is no longer used (see [_Community Consultation SVD-WG009_](/bg-material/consultation/svd-wg009/))
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
