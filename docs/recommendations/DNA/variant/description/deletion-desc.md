---
parent: DNA
title: deletion
category: description
---

Format:  **"prefix""position(s)\_deleted""del"**,  e.g. g.123\_127del

**"prefix"**  =  reference sequence used  =  g.<br>
**"position(s)\_deleted"**  =  position nucleotide or range of nucleotides deleted  =  123\_127<br>
**"del"**  =  type of change is a deletion =  del <sup>1</sup> 

---

### Note

*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
*	"position(s)\_deleted" should contain **two different positions**, e.g. 123\_126 not 123\_123.
*	the "position(s)\_deleted" should be listed from **5' to 3'**, e.g. 123\_126 not 126\_123.
	*	**exception**
	:	when a circular genomic reference sequnce is used ("o." and "m." prefix) nucleotide positions may be listed from 3’ to 5’ when the deletion includes both the last and first nucleotides of the reference sequence
*	two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:	_**<font color="#FF0000">NOTE:</font>**_ the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/bg-material/consultation/svd-wg010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
	*	**exception**
	:	deletions around exon/exon junctions when identical nucleotides flank the junction ([_see Numbering_](/bg-material/numbering/#DNAc));  
		:	when ..GAT gta..//..cag TCA.. changes to ..GA\_ gta..//..cag TCA.., based on a coding DNA reference sequence the variant is described as LRG\_199t1:c.3921del (NC\_000023.10:g.32459297del) and **not as** c.3922del (which would translate to g.32456507del)
*	<sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of a deletion has not been defined, a description may have a format like g.(100\_150)del(15)
