---
parent: RNA
title: deletion
category: example
---

*	one nucleotide
	*	LRG_199t1:r.10del
	:	a deletion of the U at position r.10 in the reference sequence LRG_199t1
*	several nucleotides
	*	NM_004006.2:r.6_8del
	:	a deletion of nucleotides r.6 to r.8 in the reference sequence NM_004006.2
	:	**NOTE**: it is allowed to describe the variant as r.6_8deluug
	*	LRG_2t1:r.1034_1036del
	:	a deletion of nucleotides r.1034 to r.1036 ("uug") in the reference sequence LRG_2t1
	:	**NOTE**: since the 3'rule has to be applied the variant, crossing the intron between nucleotides r.1035 and r.1036, is **not** described as r.1033_1035del (deletion "guu")
	*	LRG_199t1:r.(4072_5145del)
	:	the predicted deletion of exon 30 (starting at position r.4072) to exon 36 (ending at position r.5145) of the DMD-gene; RNA has **not been analysed**
*	LRG_199t1:r.=/6_8del
	:	a mosaic case where from position r.6 to r.8 besides the normal sequence also transcripts are found containing a deletion of this sequence
	: **NOTE**:	for the predicted consequences of a variant the description is LRG_199t1:r.(=/6_8del)
	
