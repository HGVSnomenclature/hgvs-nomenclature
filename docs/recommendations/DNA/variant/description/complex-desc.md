---
parent: DNA
title: complex (HGVS/ISCN)
category: description
---

Sequence changes can be very complex, involving a range of changes at one specific location. Complex changes, including translocations, are described using the recommendations of the accepted HGVS nomenclature **named extension ISCN**, based on the original proposal [_SVD-WG004 (ISCN<>HGVS)_](/bg-material/consultation/svd-wg004/)). The named ISCN extension has been developed in collaboration with [_Standing Committee on Human Cytogenomic Nomenclature (ISCN)_](/bg-material/consultation/ISCN/), covering the description of numerical and structural chromosomal changes detected using microscopic and cytogenetic techniques. It should be noted there is a basic difference between ISCN and HGVS: while ISCN describes the structure of the resulting chromosome(s), HGVS describes the **variant(s) detected**. It should be noted that the description of complex changes can become rather complicated and at some point, although literally correct, becomes effectively meaningless.<br>

The named ISCN extension has been introduced in 2016 and was modified last in May 2020.<br>

*	only aberrant findings, linked to defined chromosomal positions, are described
*	each rearranged chromosome is described in a separate line
*	X, Y, 1, 2, 3, ..., 21, 22
	:	changes affecting sex chromosomes (X then Y) are listed first, followed by those affecting autosomes (numbers from low to high)
	:	_**NOTE:**_	changed in ISCN2020. ISCN2016 had: _aberrations affecting autosomes are listed first (numbers from low to high), followed by those affecting sex chromosomes (X then Y)_
*	specific symbols
	*	pter, cen, qter
		:	the start of the chromosome is described as "**pter**", the end as "**qter**", the centromere as "**cen**"
		*	(pter)\_# and #\_(qter)
			:	for deletions extending from a known nucleotide position (#) to an unknown position in the direction of the telomere the format “(pter)\_#” or “#\_(qter)” is used.
		:	_**NOTE:**_	added in ISCN2020
	*	sup
		:	the presence of an additional sequence which is not attached to other chromosomal material (i.e. trisomy, marker or ring chromosome) is indicated by "**sup**" (supernumerary chromosome)
		:	_**NOTE:**_	the description of the supernumerary molecule is given using "[ ]sup"
		:	_**NOTE:**_	changed in ISCN2020. ISCN2016 had: _"add" for additional sequence_
	*	::
		:	a double colon (::) is used to designate break point junctions creating a ring chromosome.
		:	_**NOTE:**_	"::"" changed in ISCN2020. ISCN2016 had: _is used to designate break point junctions involving sequences from different chromosomes (translocation, transposition), chromothripsis break point junctions and junctions creating a ring chromosome_
		:	_**NOTE:**_	the "**::**" (double colon) is also used to designate the junction of fusion transcripts
*	chromosomal banding patterns are translated to genomic coordinates based the translation tables provided by NCBI ([_see Standards_](bg-material/standards/#ISCN))
*	in ISCN it is allowed to describe nucleotide positions using commas to indicate thousands and millions (e.g. “108,111,982”), in HGVS this is not allowed.
*	3'rule
	:	to determine the location of the break point, the general HGVS rule of maintaining the longest unchanged sequence applies (the 3' rule). Break point location is determined by the first break point encountered, i.e. from pter of the chromosome to be listed first
	*	pter to qter
		:	multiple breakpoints in one chromosome are listed in order of occurrence from pter to qter
	*	variant descriptions are always in the forward orientation (from pter to qter, the end of the chromosome), determined by the chromosomal origin of the intact centromere ("**cen**")
