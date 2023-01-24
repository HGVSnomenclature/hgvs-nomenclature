---
parent: Protein
title: alleles
category: example
---

For more examples [_see DNA alleles_](/recommendations/DNA/variant/alleles/).

*	**variants on one allele**
	*	NP\_003997.1:p.[Ser68Arg;Asn594del]
	:	a protein allele contains two different variants, p.Ser68Arg and p.Asn594del (the variants are found **in cis**)
	*	NP\_003997.1:p.[(Ser68Arg;Asn594del)]
	:	a protein allele contains two different **predicted** variants, p.(Ser68Arg) and p.(Asn594del) (the variants are found **in cis**)
	:	_**NOTE**_: the parentheses are placed **inside** of the allele brackets, the description p.([Ser68Arg;Asn594del]) is not correct
*	**variants on different alleles**
	*	**homozygous**
		*	NP\_003997.1:p.[Ser68Arg];[Ser68Arg]
		:	two protein alleles contain the same variant, p.Ser68Arg (the variants are found **in trans**, e.g. in a recessive disease)
		*	NP\_003997.1:p.[(Ser68Arg)];[(Ser68Arg)]
		:	two protein alleles contain the same variant with a **predicted** consequence p.(Ser68Arg)
		:	_**NOTE**_: the parentheses are placed **inside** of the allele brackets, the description p.([Ser68Arg];[Ser68Arg]) is not correct
		*	NP\_003997.1:p.(Ser68Arg)(;)(Ser68Arg)
		:	a possible homozygous case where one protein allele contains predicted variant p.(Ser68Arg), but where it can not be excluded the other allele is deleted
	*	**heterozygous**
		*	NP\_003997.1:p.[Ser68Arg];[Asn594del]
		:	two protein alleles each contain a different variant, p.Ser68Arg and p.Asn594del (compound heterozygote, e.g. in a recessive disease, the variants are found **in trans**)
		*	NP\_003997.1:p.[(Ser68Arg)];[?]
		:	one protein allele contains a variant, with predicted consequence p.(Ser68Arg), while a variant for the other protein allele is expected but not yet identified (p.(?)) (e.g. in individuals affected by a recessive disease).
		*	NP\_003997.1:p.[Ser68Arg];[Ser68=]
		:	one protein allele contains a variant, p.Ser68Arg, the other allele contains at this position the reference sequence, Ser68= (is **wild-type**).
		:	_**NOTE**_: for other variant types the format is p.[Ser68del];[Ser68=], p.[Ser68\_Arg70dup];[Ser68\_Arg70=], p.[Ser68\_Ala74insSerGln];[Ser68\_Ala74=], etc. (based on [_Proposal SVD-WG001_](http://varnomen.hgvs.org/bg-material/consultation/svd-wg001/)).
		:	_**NOTE**_: using p.[=] would mean the entire NP_003997.1 protein reference sequence was tested and found not changed
	*	**allele unknown**
		*	NP\_003997.1:p.(Ser68Arg)(;)(Asn594del)
		:	two predicted protein variants are found, p.(Ser68Arg) and p.(Asn594del), but it is not known whether they are on the same or on different alleles (chromosomes).
		:	_**NOTE**_: when it is not known on which allele a variant is, allele brackets are not used
		*	NP\_003997.2:p.[(Asn158Asp)(;)(Asn158Ile)]^[(Asn158Val)]
		:	for the variants NM\_004006.3:c.472A>G and c.473A>T it is not known whether they are on the same or on different alleles (chromosomes). The predicted consequence when the variants are on different alleles is p.(Asn158Asp)(;)(Asn158Ile), when the variants are on the same allele (i.e. c.472_473delinsGT) the predicted consequence is p.(Asn158Val). To discriminate between the two possibilities square brackets need to be used.
*	**one allele encoding two proteins**
	*	NP\_003997.1:p.[Lys31Asn,Val25\_Lys31del]
		:	two different proteins, p.Lys31Asn and p.Val25\_Lys31del, derive from a variant on one allele (c.93G>T at the DNA level with r.[83g>u,73\_93del] at the RNA level).
