---
parent: RNA
title: alleles
category: example
---

For more examples [_see DNA alleles_](/recommendations/DNA/variant/alleles/).

*	**variants on one allele**
	*	LRG\_199t1:r.[76a>u;103del]
	:	one transcript contains two different changes, r.76a>u and r.103del. The variants are found **in cis**.
	*	LRG\_199t1:r.[(578c>u;1339a>g;1680del)]
	:	one transcript contains three different predicted changes, r.(578c>u), r.(1339a>g) and r.(1680del). The variants are found **in cis**.
*	**variants on two alleles**
	*	LRG\_199t1:r.[76a>u];[103del]
	:	the two transcript alleles each contain a different change, r.76a>u and r.103del. A **heterozygous** case (compound heterozygote, e.g. in a recessive disease). The variants are found **in trans**.
	*	NM\_004006.2:r.[76a>u];[76a>u]
	:	both transcript alleles contain the same variant, r.76a>u. A **homozygous** case (e.g. in a recessive disease).
	:	_**NOTE**_: LRG\_199t1:r.76a>u(;)(76a>u) indicates analysis detects one variant (r.76a>u), suggesting both transcript alleles contain this variant, but it can not be excluded the other allele is deleted or not expressed.
	*	LRG_199t1:r.[76a>u];[76=]
	:	one transcript allele contains a variant, r.76a>u, the other transcript allele contains at position r.76 the reference sequence, r.76= (is **wild-type**).
	:	_**NOTE**_: the description r.[76a>u];[=], containing r.76a>u and r.=, is different since it indicates the entire coding RNA reference sequence was analysed and the only variant identified was r.76a>u (on one allele).
	*	NM\_004006.2:r.[76a>u];[?]
	:	one transcript allele contains a variant, r.76a>u, while a variant in the other transcript allele is expected but not yet identified (r.?) (e.g. in individuals affected by a recessive disease).
*	**alleles not certain**
	*	NM\_004006.2:r.76a>u(;)103del
	:	two variants are found in a transcript, r.76a>u and r.103del, but it is not known whether they derive from the same or from different transcript alleles (chromosomes).
	:	_**NOTE**_: when it is not known on which allele a variant is, allele brackets should not be used
*	**one allele, two transcripts**
	*	LRG\_199t1:r.[897u>g,832_960del]
	:	two different transcripts, r.897u>g and r.832_960del, derive from one variant (LRG_199t1:c.897T>G at the DNA level)
