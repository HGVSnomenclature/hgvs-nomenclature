---
layout: default-md
title: SVD-WG007
category: SVD-WG
---

## Community Consultation

### Proposal SVD-WG007 (RNA fusion)

*	Status: <font color="red">accepted</font>
	:	proposal SVD-WG007 opened for **Community Consultation** on April 10 (2019), and closed June 30 (2019). 

Based on the proposal the [RNA Deletion-insertion page](http://varnomen.hgvs.org/recommendations/RNA/variant/delins/) has been updated (April 2020).

* * *

The proposal suggests to extend the HGVS recommendations with a format to decribe RNA fusion transcripts

*	RNA fusion transcripts are described following the format to describe a fusion between two DNA molecules (translocations), i.e. using **"::"**.

* * *

#### Examples

*	translocation fusion:  NM\_152263.2:r.-115\_775::NM\_002609.3:r.1580\_\*1924
	:	a TPM3::PDGFRB fusion transcript where nucleotides r.-115 to r.775 (reference transcript NM\_152263.2, TPM3 gene) are coupled to nucleotides r.1580 to r.\*1924 (reference transcript NM\_002609.3, PDGFRB gene)
*	deletion fusion:  NM\_002354.2:r.-358_555::NM\_000251.2:r.212\_\*279
	:	EPCAM::MSH2 fusion transcript where nucleotides r.-358 to r.555 (reference transcript NM\_002354.2, EPCAM gene) are coupled to nucleotides r.212 to r.\*279 (reference transcript NM\_000251.2, MSH2 gene)
*	NOTES
	*	::aggcucccuugg::
	:	a format like "**::aggcucccuugg::**" is used to indicate the insertion of a 12 nucletoide sequence (aggcucccuugg) between two fusion transcripts
	*	NM\_152263.2:r.?\_775::NM\_002609.3:r.1580\_?
	:	when only the break point and not the entire transcript has been analysed the format NM\_152263.2:r.?\_775::NM\_002609.3:r.1580\_? should be used

* * *

#### NOTE

All fusion transcripts are described using the same format irrepsective of whether they derive from inter-chromosomal or intra-chromosomal rearrangements (translocation, deletion, inversion).
