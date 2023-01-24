---
parent: DNA
title: complex (HGVS/ISCN)
category: example
---

**The description of translocations has changed**<br>
In the original proposal (SVD-WG004) **one identical derivative chromosome** would receive **two different descriptions**, depending on whether it was identified in a balanced or an unbalanced case. In a balanced case the description would use a "::" format joining the breakpoints, while in an unbalanced case the description would use a "delins" format. HGVS recommendations try to avoid such conflicts wherever possible. HGVS therefore recommends to describe translocations exclusively using a "delins" format. 

*	**translocations**
	*	**balanced**
		*	t(2;11)(p25.1;p15.2)
		:	_(involving short arms chromosomes 2 and 11)_
			*	NC\_000002.12:g.pter\_8247756delins[NC\_000011.10:g.pter\_15825272]
			:	**NC\_000011.10:g.pter\_5825272delins[NC\_000002.12:g.pter\_8247756]**
			:	_**NOTE:**_	corrected for NC\_000002.12::g.pter\_8247756::NC\_000011.10:g.15825273\_cen\_qter and NC\_000011.10:g.pter\_15825272::NC\_000002.12:g.8247757\_cen\_qter in ISCN2016
			*	ISCN
			:	chr2:g.pter\_8,247,756::chr11:g.15,825,273\_cen\_qter (der11) and chr11:g.pter\_15,825,272::chr2:g.8,247,757\_cen\_qter (der2)
		*	t(2;11)(q31.1;q22.3)
		:	_(involving long arms chromosomes 2 and 11, with 5 bp deletion of chr11 sequence)_
			*	NC\_000002.12:g.17450009\_qterdelins[NC\_000011.10:g.108111987\_qter]
			:	**NC\_000011.10:g.108111982\_qterdelins[NC\_000002.12:g.17450009\_qter**
			*	ISCN
			:	chr2:g.pter\_cen\_174500098::chr11:g.108111987\_qter (der2) and chr11:g.pter\_cen\_108111981::chr2:g.174500099\_qter (der11)
			:	_**NOTE:**_	coupling chr11:108111981 to 108111987 implies nucleotides 108111982\_108111986 are deleted
		*	t(3;14)(14qter->14q12::3p22.2->3qter;14pter->14q12::3p22.2->3pter)
		:	_(between short arm chromosome 3 and long arm chromosomes 14, with an inserted sequence at the break point on the derivative chromosome 3)_
			*	NC\_000003.12:g.pter\_36969141delins[CATTTGTTCAAATTTAGTTCAAATGA;NC\_000014.9:g.29745314\_qterinv]
			:	**NC\_000014.9:g.29745314\_qterdelins[NC\_000003.12:g.36969141\_pterinv]**
			*	ISCN
			:	chr14:g.pter\_cen\_29,745,313::chr3:g.pter\_36,969,141inv (der14) and chr14:g.29,745,314\_qterinv::CATTTGTTCAAATTTAGTTCAAATGA::chr3:g.36,969,142\_cen\_qter (der3)
		*	NC\_000009.12:g.pter\_26393001delins102425452\_qterinv
		:	**NC\_000009.12:g.102425452\_qterdelinspter\_26393001inv**
		:	for ISCN t(9;9)(9qter->9q22.33::9p21.2->9qter;9pter->9q22.33::9p21.2->9pter)
		:	_(between homologous chromosomes, based on [Ordulu et al. example](https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4){:target="\_blank"})_	
	*	**unbalanced**
		*	NC\_000002.12:g.pter\_8247756delins[NC\_000011.10:g.pter\_15825266]
		:	for ISCN der(2)t(2;11)(p25.1;p15.2)
		:	_(derivative chromosome 2, translocation between short arms chromosomes 2 and 11)_
		*	NC\_000003.12:g.158573187\_qterdelins[NC\_000008.11:g.(128534000\_128546000)\_qter]
		:	for ISCN der(3)(3pter->3q25.32::8q24.21->8qter)
		:	_(derivative chromosome 3, translocation between long arms chromosomes 3 and 8, with an estimated nucleotide range for the break point on chromosome 8, based on uncertain break point localization example from [Ordulu et al. example](https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4){:target="\_blank"})_
		*	NC\_000005.10:g.29658442delins[NC\_000010.11:g.67539995\_qterinv]
		:	for ISCN der(5)t(5;10)(p13.3;q21.3)
		:	_(derivative chromosome 5, translocation between short arm chromosome 5 and long arm chromosome 10 with homology at the break point (chr5 29658440\_29658442 and chr10 67539995\_67539997), based on Homology examples in [Ordulu et al. example](https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4){:target="\_blank"})_
*	**inversion, pericentric**
	*	NC\_000006.12:g.[776788\_93191545inv;93191546T>C]
	:	for ISCN inv(6)(pter->p25.3::q16.1->p25.3::q16.1->qter)
	:	_(with substitution at break point)_
	*	NC\_000002.12:g.[32310435\_32310710del;32310711\_171827243inv;insG]
	:	for ISCN inv(2)(pter->p22.3::q31.1->p22.3::q31.1->qter)dn
	:	_(de novo, with 275 bp deletion and 1 bp insertion at break points)_
	:	_**NOTE:**_	the HGVS description does not include the de novo occurrence of the variant
*	**deletion**
	*	NC_000023.11:g.(86200001\_103700000)del
	:	for ISCN del(X)(q21.31q22.2)
	:	_(within a chromosome, breakpoint not sequenced)_
	*	NC\_000022.11:g.pter\_(12200001\_14700000)del::(37600001\_410000000)\_qterdel
	:	for ISCN r(22)(p11.1q13.1)
	:	_(ring chromosome derived from chromosome 22, breakpoint not sequenced)_
	:	_**NOTE:**_	"::" is used to indicate the join instead of ";" to describe two not connected deletions
*	**insertion**
	*	**duplication**  (tandem)
		*	NC\_000008.11:g.(127300001\_131500000)\_(131500001\_136400000)dup
		:	for ISCN dup(8)(q24.21q24.22)
		:	_(within a chromosome, breakpoint not sequenced)_
		*	NC\_000008.11:g.(131500001\_136400000)ins[(127300001\_131500000)\_(131500001\_136400000)inv]
		:	for ISCN dup(8)(q24.22q24.21)
		:	_(within a chromosome, orientation reversed relative to original sequence, breakpoint not sequenced)_
	*	**insertion**
		*	NC\_000004.12:g.134850793\_134850794ins[NC\_000023.11:g.89555676\_100352080inv]
		:	for ISCN der(4)ins(4;X)(q28.3;q22.2q21.31)
		:	_(inserted sequence reversed in orientation relative to chromosome sequence containing centromere)_
	*	**transposition**
		*	**balanced**  (deletion + insertion elsewhere)
			*	HGVS NC\_000004.12:g.134850793\_134850794ins[NC\_000023.11:g.89555676\_100352080] and NC\_000023.11:g.89555676\_100352080del
			:	for ISCN ins(4;X)(q28.3;q21.31q22.2)
			:	_(balanced intrachromosomal, inserted sequence same orientation as chromosome sequence containing centromere, based on [Ordulu et al. Fig.1C](https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4){:target="\_blank"})_
			*	NC\_000004.12:g.134850793\_134850794ins[NC\_000023.11:g.89555676\_100352080inv] and NC\_000023.11:g.89555676\_100352080del
			:	for ISCN ins(4;X)(q28.3;q22.2q21.31)
			:	_(balanced intrachromosomal, inserted sequence reversed in orientation relative to chromosome sequence containing centromere)_
		*	**unbalanced**  (copy inserted elsewhere)
		:	describe as insertion
*	**supernumerary chromosome**
	*	NC\_000022.11:g.[pter\_(12200001\_14700000)del::(37600001\_410000000)\_qterdel]sup
	:	for ISCN +r(22)(p11.1q13.1)
	:	_(supernumerary ring chromosome derived from chromosome 22, breakpoint not sequenced)_
	:	_**NOTE:**_	changed in ISCN2020. ISCN2016 had: “add” for additional sequence
