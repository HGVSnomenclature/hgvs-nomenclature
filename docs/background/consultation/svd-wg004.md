---
layout: default-md
title: SVD-WG004
category: SVD-WG
---

## Community Consultation

* * *

### NOTE

The proposal below is the original proposal as published first on November 10, 2015. The proposal is **not updated** and does not include changes made after acceptance of the proposal. To see the current recommendations please check [_Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/). 

* * *

### Proposal SVD-WG004 (ISCN<>HGVS)

*	Status: <font color="red">closed</font>
	:	proposal SVD-WG004 opened for **Community Consultation** on November 10 (2015) and closed on Jan.15 (2016). Although no objections were received, because SVD-WG004 covers variants that may become rather complex to describe and will be difficult to implement, the SVD-WG decided to accepted the proposal only as a [_**named extension**_](/versioning). 

The proposal suggests to extend the HGVS recommendations to allow description of complex variants incl. those covered so far by the **ISCN** (e.g. transpositions, translocations, chromothripsis, marker chromosomes, etc.). In addition it includes suggestions to harmonise the HGVS and ISCN recommendations, removing discrepancies as much as possible.

* * *

#### HGVS <> ISCN

The current HGVS recommendations [(_see Recommendations_)](/recommendations/general) do not cover translocations. One small example is given [(_see DNA sequence variants_)](http://www.hgvs.org/mutnomen/recs-DNA.html#tra) but this is insufficient to properly describe such changes when detected. The SVD-WG has received the request to extend the HGVS recommendations to include the description of translocations.

Historically the description of translocations is the responsibility of the [_ISCN committee_](/bg-material/consultation/ISCN). The ISCN recommendations cover the description of numerical and structural chromosomal changes detected using microscopic/cytogenetic techniques, while the HGVS recommendations cover the description of changes at the nucleotide level detected using sequencing. Given the increased use of sequencing technologies to characterize chromosomal abnormalities the ISCN committee and the HGVS/HVP/HUGO Sequence Variant Description Working Group (SVD-WG) have thoroughly checked and discussed the recommendations of both committees. The committees decided to design one format that, wherever possible, leaves existing standards intact but that also draws a clear border between ISCN and HGVS. Discussions concentrated around earlier proposals for the description of translocations, e.g. as presented at the [HGVS/ASHG meeting in Boston](http://onlinelibrary.wiley.com/doi/10.1002/humu.22516/abstract) [(_see presentation_)](http://www.hgvs.org/mutnomen/SVtrans_HGVS2013_PT.pdf), and a paper from [Ordulu et al. (2014)](http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf) reporting sequencing results of structural chromosome rearrangements.

* * *

#### Proposal

The committees propose that as soon as nucleotide positions are used in the description of rearrangements, HGVS nomenclature is followed and descriptions are split in a ISCN and a HGVS part.

##### the basics

*	only aberrant findings are described
*	both the ISCN-like description of chromosome aberrations and the HGVS-like nucleotide variant descriptions must be included for full clarity and information
*	the ISCN-like portion of the description appears first and can be modeled on the short or long form ISCN description of structural rearrangements
*	the ISCN-like portion of the description begins with "**seq**" to indicate that the aberration was identified by sequence-based technology.  The description must include the genome build in square brackets after "**seq[..]**".
*	the combined nomenclature uses the existing HGVS standards [(_see HGVS website_)](http://www.HGVS.org/varnomen/) for the HGVS-like portion, along with additional recommendations outlined below

##### HGVS additions

*	1, 2, 3, ..., 21, 22, X, Y
:	aberrations affecting autosomes are listed first (numbers from low to high), followed by those affecting sex chromosomes (X then Y)
*	3'rule
:	to determine the location of the break point, the general HGVS rule of maintaining the longest unchanged sequence applies (the 3' rule). Break point location is determined by the first break point encountered, i.e. from pter of the chromosome with the lowest number
*	pter to qter
:	multiple breakpoints in one chromosome are listed in order of occurrence from pter to qter
	*	variant descriptions are always in the forward orientation (from pter to qter, the end of the chromosome), determined by the chromosomal origin of the intact centromere ("**cen**")
	*	inverted sequences are described using "**inv**"
*	pter, cen, qter
:	the start of the chromosome is described as "**pter**", the end as "**qter**", the centromere as "**cen**"
:	_**NOTE:**_	since the genomic reference sequence contains N's at the start/end of the chromosome (telomeres) the use of specific nucleotide positions is undesirable
:	_**NOTE:**_	the use of "**cen**" helps to recognize the derivative chromosome
*	"add"
:	the presence of an additional sequence (marker/ring chromosome) is indicated by "**add**"
:	_**NOTE:**_	the description of the addional molecule is given using "[ ]add"
:	_**NOTE:**_	"ext" is not available since it is already used to describe protein extension variants
*	"**::**" (double colon)
:	"::" (double colon) is used to designate break point junctions involving sequences from different chromosomes (translocation, transposition), chromothripsis break point junctions and junctions creating a ring chromosome
:	_**NOTE:**_	non-template sequences ("inserts") at these imperfect break points are described using the format "**::sequence::**" (e.g. ::AAGTAC:: )

* * *

#### Examples

Note the format: **<font color="red">the variant is first described using ISCN nomenclature, next using HGVS</font>**.

*	translocations
	*	balanced
		*	between short arms chromosomes 2 and 11
		:	seq[GRCh37] t(2;11)(p25.1;p15.2)
		:	g.[chr2:pter\_8247756::chr11:15825273\_cen\_qter] and g.[chr11:pter\_15825272::chr2:8247757\_cen\_qter]
		*	between long arms chromosomes 2 and 11, with 5 bp deletion of chr11 sequence
		:	seq[GRCh37] t(2;11)(q31.1;q22.3)
		:	g.[chr2:pter\_cen\_174500098::chr11:108111987\_qter] and g.[chr11:pter\_cen\_108111981::chr2:174500099\_qter]
		:	_**NOTE:**_	coupling chr11:108111981 to 108111987 implies nucleotides 108111982\_108111986 are deleted
		*	between short arm chromosome 3 and long arm chromosomes 14, with insertion of non-templated sequence at the break point on the derivative chromosome 3
		:	seq[GRCh37] t(3;14)(14qter->14q12::3p22.2->3qter;14pter->14q12::3p22.2->3pter)
		:	g.[chr14:pter\_cen\_29745313::chr3:pter\_36969141inv] and g.[chr14:29745314\_qterinv::CATTTGTTCAAATTTAGTTCAAATGA::chr3:36969142\_cen\_qter]
		*	between homologous chromosomes (based on [Ordulu et al. example](http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf))
		:	seq[GRCh37]
		:	t(9;9)(9qter->9q22.33::9p21.2->9qter;9pter->9q22.33::9p21.2->9pter)
		:	g.[chr9:102425452\_qterinv::chr9:26393002\_cen\_qter] and g.[chr9:pter\_cen\_102425451::chr9:26393001pterinv]
	*	unbalanced
		*	derivative chromosome 2, translocation between short arms chromosomes 2 and 11
		:	seq[GRCh37] der(2)t(2;11)(p25.1;p15.2)
		:	g.chr2:pter\_8247756delinschr11:pter\_15825266
		*	derivative chromosome 3, translocation between long arms chromosomes 3 and 8, with an estimated nucleotide range for the break point on chromosome 8 (based on Uncertain Break point Localization example from [Ordulu et al.](http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf))
		:	seq[GRCh37] der(3)(3pter->3q25.32::8q24.21->8qter)
		:	g.chr3:158573187\_qterdelinschr8:(128534000\_128546000)\_qter
		*	derivative chromosome 5, translocation between short arm chromosome 5 and long arm chromosome 10 with homology at the break point (chr5 29658440\_29658442 and chr10 67539995\_67539997, based on Homology examples in [Ordulu et al.](http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf))
		:	 seq[GRCh37] der(5)t(5;10)(p13.3;q21.3)
		:	g.chr5:pter\_29658442delinschr10:67539995\_qterinv
*	inversion, pericentric
	*	with substitution at break point
	:	seq[GRCh37] inv(6)(pter->p25.3::q16.1->p25.3::q16.1->qter)
	:	chr6:g.[776788\_93191545inv;93191546T>C]
	*	de novo with 275bp deletion and 1bp insertion at break points
	:	seq[GRCh37] inv(2)(pter->p22.3::q31.1->p22.3::q31.1->qter)dn
	:	chr2:g.[32310435\_32310710del;32310711\_171827243inv;insG]
	:	_**NOTE:**_	the HGVS description does not include the de novo occurence of the variant
*	deletion
	*	within a chromosome (based on [Ordulu 2014. Fig.1D]((http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf))
	:	seq[GRCh37] del(X)(q21.31q22.2)
	:	chrX:g.89555676\_100352080del
	*	ring chromosome derived from chromosome 22
	:	seq[GRCh37] r(22)(p11.2q13.1)
	:	chr22:g.pter\_10000000del::40000000\_qterdel
	:	_**NOTE:**_	"::" is used to indicate the join instead of ";" to describe two not connected deletions
*	insertion
	*	duplication  (tandem)
		*	within a chromosome, orientation identical relative to original sequence (based on Ordulu et al. Fig 5)
		:	seq[GRCh37] dup(8)(q24.21q24.21)
		:	chr8:g.128746677\_128749160dup
		*	within a chromosome, orientation reversed relative to original sequence
		:	seq[GRCh37] dup(8)(q24.21q24.21)
		:	chr8:g.128746677\_128749160dupinv
	*	insertion
		*	inserted sequence reversed in orientation relative to chromosome sequence containing centromere
		:	seq[GRCh37] der(4)ins(4;X)(q28.3;q22.2q21.31)
		:	g.chr4:134850793\_134850794inschrX:89555676\_100352080inv
	*	transposition
		*	balanced  (deletion + insertion elsewhere)
			*	(balanced intrachromosomal) inserted sequence same orientation as chromosome sequence containing centromere (based on [Ordulu et al. Fig.1C](http://ac.els-cdn.com/S0002929714001724/1-s2.0-S0002929714001724-main.pdf))
			:	seq[GRCh37] ins(4;X)(q28.3;q21.31q22.2)
			:	g.[chr4:134850793\_134850794inschrX:89555676\_100352080] and chrX:g.[89555676\_100352080del]
			*	(balanced intrachromosomal) inserted sequence reversed in orientation relative to chromosome sequence containing centromere
			:	seq[GRCh37] ins(4;X)(q28.3;q22.2q21.31)
			:	g.[chr4:134850793\_134850794inschrX:89555676\_100352080inv] and chrX:g.[89555676\_100352080del]
		*	unbalanced  (copy inserted elsewhere)
			:	describe as insertion
*	additional chromosome
	*	supernumerary ring chromosome derived from chromosome 22
	:	seq[GRCh37] +r(22)(p11.2q13.1)
	:	chr22:g.[pter\_10000000del::40000000\_qterdel]add
	*	uniparental disomy, additional copy of maternal chromosome 14 
	:	seq[GRCh37] 46,XY,upd(14)mat
	:	chr14:g.[pter\_cen\_qter]add
	:	_**NOTE:**_	the HGVS description does not include the maternal origin of the chromosome
