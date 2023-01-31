---
parent: DNA
title: alleles
category: example
---

*	**variants on one allele**
	*	NM_004006.2:c.[2376G>C;3103del]
	:	one allele (chromosome) of a gene contains two different changes, c.2376G>C and c.3103del. The variants are found **in cis**.
	*	NC_000023.10:g.[30683643A>G;33038273T>G]
	:	one allele (X-chromosome) contains two different variants in two different genes, g.30683643A>G in the GK gene and g.33038273T>G in the DMD gene.
	*	NC_000003.12:g.63912687AGC[(50_60)]
	:	one allele (chromosome 3) contains a repeated AGC tri-nucleotide sequence, starting at position g.6391268, containing 50 to 60 AGC copies
	*	NC_000003.12:g.63912687AGC[(60_?)]
	:	one allele (chromosome 3) contains a repeated AGC tri-nucleotide sequence, starting at position g.6391268, containing 60 or more AGC copies
*	**variants on two alleles**
	*	NM_004006.2:c.[2376G>C];[3103del]
	:	the two alleles (chromosomes) of a gene each contain a different change, c.2376G>C and c.3103del. The variants are found **in trans**. A **heterozygous** case (compound heterozygote, e.g. in a recessive disease).
	:	**NOTE**: do not use c.[2376G>C;3103=];[2376=;3103del], the indication "not changed" is used only when one variant was identified (like LRG_199t1:c.[2376G>C];[2376=])
	*	NM_004006.2:c.[2376G>C];[2376G>C]
	:	both alleles (chromosomes) of a gene contain the same variant, c.2376G>C. A **homozygous** case (e.g. in a recessive disease).
	:	**NOTE**: it is not allowed to shorten this to c.2376[G>C];[G>C] or even c.2376G>C[];[]
	*	NM_004006.2:c.[296T>G;476T>C;1083A>C];[296T>G;1083A>C]
	:	a sample contains variants c.296T>G and c.1083A>C on both alleles (chromosomes) and variant c.476C>T on only one allele.
	*	NM_004006.2:c.[2376G>C];[2376=]
	:	one allele (chromosome) of a gene contains a variant, c.2376G>C, the other allele (chromosome) contains the reference sequence, c.2376= (is **wild-type**).
	:	**NOTE**: the description c.[2376G>C];[=], containing c.2376G>C and c.=, is different since it indicates the entire coding DNA reference sequence was analysed and the only variant identified was c.2376G>C (on one allele).
	:	**NOTE**: for other variant types the format is c.[2376del];[2376=], c.[2376_2399dup];[2376_2399=], c.[2376_2377insGT];[2376_2377=], etc. For more examples see [_Proposal SVD-WG001_](http://varnomen.hgvs.org/background/consultation/SVD-WG001/).
	*	NM_004006.2:c.[2376G>C];[?]
	:	one allele (chromosomes) of a gene contains a variant, c.2376G>C, while a variant for the other allele is expected but not yet identified (c.?) (e.g. in individuals affected by a recessive disease).
*	**alleles not certain**
	*	NM_004006.2:c.2376G>C(;)3103del
	:	two variants in a gene, c.2376G>C and c.3103del, but it is not known whether they are on the same or on different alleles (chromosomes).
	:	**NOTE**: in the latest publication of the recommendations ([Den Dunnen et al. (2016)](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf)) the example given is not correct. Allele brackets should not be used when it is not known whether variants are on one allele or not.
	*	NM_004006.2:c.2376G>C(;)(2376G>C)
	:	analysis detects one variant (c.2376G>C), suggesting both alleles (chromosomes) contain this variants, but it can not be excluded the other allele is deleted
	*	NM_004006.2:c.[296T>G;476T>C];[476T>C]\(;)1083A>C
	:	a sample contains a homozygous variant (c.476T>C) and two heterozygous variants (c.296T>G and c.1083G>C) for which it is not known on which allele (chromosome) they are (although at least one, in the example c.296T>G, is on the same allele as c.476T>C).
	*	NM_004006.2:c.[296T>G];[476T>C]\(;)1083G>C(;)1406del
	:	a sample contains heterozygous variants on different alleles (c.296T>G and c.476T>C) and two additional heterozygous variants (c.1083G>C and c.1406del) for which it is not known on which allele (chromosome) they are.
