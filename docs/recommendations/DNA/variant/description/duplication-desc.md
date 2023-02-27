---
parent: DNA
title: duplication
category: description
---

Format:   **"prefix""position(s)_duplicated""dup"**,  e.g. g.123_345dup

**"prefix"**  =  reference sequence used  =  g.<br>
**"position(s)\_duplicated"**  =  position nucleotide or range of nucleotides duplicated  =  123_345<br>
**"dup"**  =  type of change is a duplication  =  dup <sup>1</sup>

---

### Note

*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
*	"positions\_duplicated" should contain **two different positions**, e.g. 123\_126 not 123\_123.
*	the "positions\_duplicated" should be listed from **5' to 3'**, e.g. 123\_126 not 126\_123.
*	by definition, duplication may only be used when the additional copy is _**directly 3'-flanking**_ of the original copy (a "tandem duplication").
	*	when a variant can be described as a duplication it **must** be desribed as a duplication and not as e.g. an insertion (see _Prioritization_](/recommendations/general/) 
	*	when there is no evidence that the extra copy of a sequence detected is in tandem (directly 3'-flanking the original copy), the change can not be described as a duplication, it should be described as **an insertion** (see [_Insertion_](/recommendations/DNA/variant/insertion/) and [_proposal SVD-WG003_](/bg-material/consultation/svd-wg003/)).
	*	**inverted duplications** are described as insertion (g.234\_235ins123\_234inv), not as a duplication ([_see Inversion_](/recommendations/DNA/variant/inversion))
*	when more then one additional copies are inserted directly 3' of the original copy the change is indicated using the format for [_Repeated sequences_](/recommendations/DNA/variant/repeated/), like [3] (triplication), [4] (quadruplication), etc.
*	two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:	_**<font color="#FF0000">NOTE:</font>**_ the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/bg-material/consultation/svd-wg010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
	*	**exception**
	:	duplications around exon/exon junctions when identical nucleotides flank the junction ([_see Numbering_](/bg-material/numbering/#DNAc)); 
		:	when ..GAT gta..//..cag TCA.. changes to ..GATT gta..//..cag TCA.., based on a coding DNA reference sequence the variant is described as LRG\_199t1:c.3921dup (NC\_000023.10:g.32459297dup) and **not as** c.3922dup (which would translate to g.32456507dup)
*	<sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of a duplication has not been defined
