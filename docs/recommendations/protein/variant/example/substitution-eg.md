---
parent: Protein
title: substitution
category: example
---

*	**missense**
	* 	LRG\_199p1:p.Trp24Cys
	: 	amino acid Trp24 is changed to a Cys
	* 	NP\_003997.1:p.(Trp24Cys)
	: 	amino acid Trp24is predicted to change to a Cys (no experimental proof, e.g. based on DNA level data)
*	**nonsense**
	*	LRG\_199p1:p.Trp24Ter (p.Trp24\*)
    	:	amino acid Trp24 is changed to a stop codon (Ter, \*)<br>
        :	_**NOTE:**_	this change is **not** described as a deletion of the C-terminal end of the protein (i.e. p.Trp24\_Met36853del)
*	**silent**  (no change)
	* 	NP\_003997.1:p.Cys188=
	:	amino acid Cys188 is not changed (DNA level change ..TGC.. to ..TGT..)
	:	_**NOTE:**_	the description p.= means the **entire** protein coding region was analysed and no variant was found that changes (or is predicted to change) the protein sequence.
* 	**translation initiation codon**  
	*	no protein
	:	LRG\_199p1:p.0
	:	as a consequence of a variant in the translation initiation codon no protein is produced
	:	_**NOTE:**_	LRG\_199p1:p.0? can be used when you predict that no protein is produced. Do not use descriptions like "p.Met1Thr", this is for sure **not** the consequence of the effect on protein translation
	*	unknown
	:	LRG\_199p1:p.Met1?
    	:	the consequence, at the protein level, of a variant affecting the translation initiation codon can not be predicted (i.e. is unknown)
	*	**new translation initiation site**
		*	**<u>downstream</u>**  -  NP\_003997.1:p.Leu2\_Met124del (deletion)
		:	a variant in the translation initiation codon causes the activation of a downstream translation initiation site (Met) resulting in deletion of the first 123 amino acids (Met-1 to Val-123) of the protein.<br>
        	:	_**NOTE:**_	the 3' rule applies.
		*	**<u>upstream</u>**  -  p.Met1_Leu2insArgSerThrVal (insertion)
		:	a variant in the translation initiation codon (Met1) changes it to a Valine (Val) and activates an upstream translation initiation site at position -4, replacing amino acid Met1 with MetArgSerThrVal. Applying the 3' rule the variant is described as an insertion.
		:	_**NOTE:**_	this variant is not described as an extension
		*	**<u>new</u>**  -  p.Met1ext-5 (extension)
		:	a variant in the 5’ UTR activates a new in-frame upstream translation initiation site starting with amino acid Met-5 ([_see Extension_](/recommendations/protein/variant/extension))
*	translation termination codon _(stop codon, **no-stop change**)_
	:	[_see Extension_](/recommendations/protein/variant/extension)
*	splicing
	*	NP\_003997.1:p.?
	:	the predicted consequence of variant NM\_004006.2c.2622G>C is a silent change (p.(Lys874=)). Since it affects the last nucleotide of the exon it can not be excluded the variant affects splicing, having unknown consequences.
	:	_**NOTE:**_	when others have reported the same variant, and were able to analyse RNA, you could consider to give the consequences they observed as the predicted consequences for the variant, e.g. r.[(2603\_2622del,2622g>c)] p.[(Ser868Argfs\*2,Ser868=)]
*	uncertain
	*	NP\_003997.1:p.(Gly56Ala^Ser^Cys)
	:	amino acid Gly56 is changed to an Ala, Ser or Cys ([_see Uncertain_](/recommendations/uncertain/))
*	mosaic
	*	LRG\_199p1:p.Trp24=/Cys
	:	a mosaic case where at amino acid position 24 besides the normal amino acid (a Trp, described as “=”) also protein is found containing a Cys (Trp24Cys)
	:	_**NOTE:**_	irrespective of the frequency in which each amino acid was found, the reference is always described first
	:	_**NOTE:**_	for the predicted consequences of a variant the description is LRG_199t1:p.(Trp24=/Cys)
