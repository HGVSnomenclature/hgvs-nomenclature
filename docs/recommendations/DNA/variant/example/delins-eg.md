---
parent: DNA
title: deletion-insertion
category: example
---

*	NC\_000023.11:g.32386323delinsGA
	:	a deletion of nucleotide g.32386323 (a T, not described), replaced by nucleotides GA, changing ..CAGC<font color="red">T</font>CTTT.. to ..CAGC<font color="red">GA</font>CTTT.. The variant corresponds to LRG\_199t1:c.4661delinsTC based on a coding DNA reference sequence.
	:	_**NOTE**_: the recommendation is not to describe the variant as NC\_000023.11:g.32386323delTinsGA, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NC\_000023.11:g.32386323delCinsGA).
*	NM\_004006.2:c.6775\_6777delinsC 
	:	a deletion of nucleotides c.6775 to c.6777 (GAG, not described), replaced by a C nucleotide, changing ..GGAA<font color="red">GAG</font>TTGC.. to ..GGAA<font color="red">C</font>TTGC..
	:	_**NOTE**_: the recommendation is not to describe the variant as NM\_004006.2:c.6775\_6777delGAGinsC, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NM\_004006.2:c.6775\_6777delGTGinsC ).
*	LRG\_199t1:c.145\_147delinsTGG (p.Arg49Trp)
	:	a deletion replacing nucleotides c.145 to c.147 (CGC, not described) with TGG
*	LRG\_199t1:c.9002\_9009delinsTTT
	:	a deletion of nucleotides c.9002 to c.9009, replaced by nucleotides TTT
	:	_**NOTE**_:	two variants separated by one nucleotide, together affecting one amino acid, should be described as a “delins”, so the description c.[145C>T;147C>G] is not correct
*	LRG\_199t1:c.850\_901delinsTTCCTCGATGCCTG
	:	a deletion of nuceotides c.850 to c.901, replaced by TTCCTCGATGCCTG
	:	_**NOTE**_:	parts of the inserted sequence "align" with the reference sequence, giving an alternative description like c.[850\_869del;874\_881del;887\_897del;901\_902insG]. The **"delins" format is recommended**: it is simpler and prevents software tools making incorrect predictions for the consequences at protein level. 
*	NC\_000002.12:g.pter\_8247756delins\[NC\_000011.10:g.pter\_15825266\]
	:	nucleotides g.pter to g.8247756 of chromosome 2 are deleted and replaced by nucleotides g.pter to g.1582566 of chromosome 11: the derivative chromosome 2 from an unbalanced translocation between the short arms of chromosomes 2 and 11 (ISCN der(2)t(2;11)(p25.1;p15.2)). Example copied from [_Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/).
	:	_**NOTE**_:	balanced translocations ([_see Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/)) are described as two complementary "delins" variants.
*	NC\_000022.10:g.42522624\_42522669delins42536337\_42536382
	:	conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides g.42522624 to g.42522669 with those of the 3' flanking CYP2D7P1 gene, nucleotides g.42536337 to g.42536382 from the same genomic reference sequence (NC\_000022.10)
*	NC\_000012.11:g.6128892\_6128954delins[NC\_000022.10:g.17179029\_17179091]
	:	conversion replacing nucleotides g.6128892 to g.6128954 of the VWF gene (NM\_000552.3:c.3675-45\_3692) on chromosome 12 with nucleotides g.17179029 to g.17179091 of the VWFP1 pseudogene on chromosome 22
*	NM\_000797.3:c.812\_829delins908\_925
	:	conversion replacing nucleotides c.812 to c.829 of the DRD4 gene with nucleotides c.908 to c.925 from the same reference sequence
*	NM\_004006.2:c.812\_829delinsN[12]
	:	nucleotides c.812 to c.829 have been deleted and replaced by 12 unknown nucleotides (N[12])
