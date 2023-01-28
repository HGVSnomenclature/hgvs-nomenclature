---
layout: default
title: Versioning
permalink: /versioning/
---

# {{ page.title }}

The recommendations for the description of sequence variants are designed to be _**stable**_, _**meaningful**_, _**memorable**_ and _**unequivocal**_. Still, every now and then modifications will be required to remove inconsistencies and/or to clarify confusing conventions. In addition, the recommendations may be extended to resolve cases that were hitherto not covered. HGVS nomenclature has version numbers to allow users to specify up to what point they follow the HGVS recommendations.

The version number is based on the date of the change and has the format: **HGVS nomenclature _Version 15.11_**, for the version accepted in 2015 ("**15**"), November ("**11**"). The current HGVS version number is shown in the top right corner of this web site ("_**Version xx.xx**_"). Note the version does not change when a typing error is corrected, an example added, an explanation clarified or a question answered. Outside the core HGVS recommendations, covered by the version number, the recommendations have "**named extensions**", i.e optional extensions for a specific use. Supporting named extensions is optional. A proper reference to the version of the HGVS nomenclature should mention the version number and the named extensions supported.


### The current version is HGVS nomenclature v20.05.

**<font color="red">NOTE:</font>** since proposals SVD-WG007 and SVD-WG008 have been accepted a **new version** of the HGVS nomenclature was released May 1, 2020.

For issues currently discussed see [_Open for Community Consultation_](/bg-material/consultation/) or [_Open Issues_](/recommendations/open-issues/).

* * *

## Version list

* * *

{:#version-list}

*	_**Version 20.05**_
	:	Accepted proposals include [_SVD-WG007_](/bg-material/consultation/svd-wg007/) and [_SVD-WG008_](/bg-material/consultation/svd-wg008/):
	*	SVD-WG008 (_Reference Sequences_)
		:	specifies requirements for acceptable Reference Sequences  
	*	SVD-WG007 (_RNA fusion_)
		:	specifies how to describe RNA fusion transcripts   

*	_**Version 19.01**_
	:	Accepted proposals include [_SVD-WG005_](/bg-material/consultation/svd-wg005/) and [_SVD-WG006_](/bg-material/consultation/svd-wg006/):
	*	SVD-WG006 (_circular DNA_)
		:	allows descriptions like o.16000_100del  
	*	SVD-WG005 (_gom/lom_)
		:	allows descriptions of changes in general methylation status like g.123_456|lom  

*	_**Named extension ISCN**_
	:	Proposal [_SVD-WG004_](/bg-material/consultation/svd-wg004/) (ISCN<>HGVS) has been accepted a "named extension ISCN"

*	_**Version 15.11**_
	:	Accepted proposals include [_SVD-WG001_](/bg-material/consultation/svd-wg001/) and [_SVD-WG002_](/bg-material/consultation/svd-wg002/):
	*	SVD-WG001 (_No change_)
		:	allows descriptions like g.11890634G=, c.123G=, r.123g= and p.(Arg41=).
	*	SVD-WG002 (_n. reference sequence_)
		:	allows descriptions like NR_028379.1:n.345A>G.  
	:	HGVS nomenclature _**version 15.11**_ is described in Den Dunnen et al. (2016) [HGVS recommendations for the description of sequence variants: 2016 update. Hum.Mutat. 25: 37: 564-569](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf){:target="\_blank"}. The most significant changes between version 15.11 and version 1.0 are [_described below_](#v1511). 

*	_**Version 2.121101**_
	:	**Variants affecting translation termination**  -  variants that replace the translation termination codon but do not encounter a new stop in the new reading frame are described as "p.*321Argext*?". Frame shift variants with the same effect are described as "p.Ile321Argfs*?" ([_see Protein descriptions_](/recommendations/protein/variant/extension))

*	_**Version 2.120831**_
	:	**Protein description in parentheses**  -  parentheses in protein variant descriptions can be omitted when there is sufficient experimental evidence
	:	**Variants affecting translation initiation**  -  at protein level, variants that generate a new upstream translation initiation codons are described using the format "p.Met1ext-5" ([_see Protein extensions_](/recommendations/protein/variant/extension)).

*	**Version 1**
	:	The 2000 publication of Den Dunnen JT and Antonarakis SE [_Mutation nomenclature extensions and suggestions to describe complex mutations: a discussion. Hum.Mutat. 15:7-12_](http://www3.interscience.wiley.com/cgi-bin/fulltext/68503056/PDFSTART)) contain a more formal set of recommendations an are considered as version 1.

*	**Version 0**
	:	On the page "[_History regarding the description of sequence variants_](/history/)" we give an overview of all publications on the description of sequence variants. These papers can be considered as pre-versions of the first recommendations, a version 0.

* * *
<a name ="v1511"></a>
### Changes/additions going from the 2000 to 2016 recommendations 

*   _**Reference sequence**_
	:	for diagnostic applications, the recommendation is to use a [Locus Reference Genomic sequence](http://www.lrg-sequence.org/){:target="\_blank"} (LRG, [Dalgleish et al. 2010](http://genomemedicine.com/content/2/4/24){:target="\_blank"}) as the reference sequence for variant descriptions. Prefixes for new reference sequence types have been added (e.g. **m.** and **n.**, as well as indicators to specify different transcript variants (**t1**) and protein isoforms (**p1**) annotated in the reference sequence ([_see Reference Sequences_](/bg-material/refseq#DNAc))
*	_**Definitions**_
	:	the basic types of variants were defined more strictly. In addition variant types have been prioritized ([_see General recommendations_](/recommendations/general))
*   _**Pre-existing standards**_
	:	pre-existing standards from the IUPAC and IUBMB for the description of nucleotides and amino acids are now used throughout the recommendations. These include letter codes to describe incompletely specified residues at both DNA and protein level ([see _Standards_](/bg-material/standards#aacode)). Description of the translation termination (stop) codon at the protein/amino acid level <font color="#FF0000">changed from "X" to "Ter" / "*"</font> since "X" in the _IUPAC-IUB_ nomenclature means an "_unspecified_" or "_unknown_" amino acid.
*   _**Incorporate ISCN standards**_
	:	recommendations were made to describe changes with uncertain break points (i.e. not sequenced), obtained using technologies like FISH, arrays and MLPA. Furthermore, where possible, HGVS incorporated established ISCN standards in the recommendations, include the use of "**/**" (forward slash) to describe somatic variants and "**//**" for chimerism ([_see General recommendations_](/recommendations/general)). 
*   _**Simplification**_
	:	in HGVS version 1.0 some symbols were used for more then one purpose leading to undesired confusion. These inconsistencies were removed.
*   _**Prediction / experimental proof**_
	:	to clarify a variant described at the protein level is a prediction, without experimental evidence, the recommendation was added to describe the predicted consequence in parentheses, like p.(Arg12Gly). 
*   _**Repeated sequences**_
	:	recommendations were made to describe variability in repeated sequences (mono-, di-, tri- residue stretches, etc. [_see Repeated sequences_](/recommendations/DNA/variant/repeated)).
