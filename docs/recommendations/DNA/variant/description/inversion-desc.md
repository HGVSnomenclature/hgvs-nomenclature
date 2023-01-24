---
parent: DNA
title: inversion
category: description
---

Format:   **"prefix""positions\_inverted""inv"**,  e.g. g.123_345inv

**"prefix"**  =  reference sequence used  =  g.<br>
**"positions\_inverted"**  =  range of nucleotides inverted  =  123_345<br>
**"inv"**  =  type of change is an inversion  =  inv

---

### Note

*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
*	by definition, the region inverted ("positions\_inverted") contains **more then one nucleotide**. The description g.234inv is therefore not allowed; a one nucleotide inversion should be described as a [_substitution_](/recommendations/DNA/variant/substitution/)
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
	*	the 3'rule applies to ALL descriptions (genome, gene, transcript and protein) of a given variant
*	**inverted duplications** are described as an insertion using the format g.234\_235ins123\_234inv, not as g.123\_456dupinv ([_see Q&A_](#dupinv))
*	two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:	_**<font color="#FF0000">NOTE:</font>**_ the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/bg-material/consultation/svd-wg010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
*	inversions are not used on protein level. Depending on the (predicted) consequences of an inversion on protein level, changes are usually described as either a **delins** or a **frame shift**.
