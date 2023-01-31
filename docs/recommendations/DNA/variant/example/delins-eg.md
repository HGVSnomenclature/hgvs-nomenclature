---
parent: DNA
title: deletion-insertion
category: example
---

*	NC_000023.11:g.32386323delinsGA
	:	a deletion of nucleotide g.32386323 (a T, not described), replaced by nucleotides GA, changing ..CAGC<font color="red">T</font>CTTT.. to ..CAGC<font color="red">GA</font>CTTT.. The variant corresponds to LRG_199t1:c.4661delinsTC based on a coding DNA reference sequence.
	:	**NOTE**: the recommendation is not to describe the variant as NC_000023.11:g.32386323delTinsGA, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NC_000023.11:g.32386323delCinsGA).
*	NM_004006.2:c.6775_6777delinsC 
	:	a deletion of nucleotides c.6775 to c.6777 (GAG, not described), replaced by a C nucleotide, changing ..GGAA<font color="red">GAG</font>TTGC.. to ..GGAA<font color="red">C</font>TTGC..
	:	**NOTE**: the recommendation is not to describe the variant as NM_004006.2:c.6775_6777delGAGinsC, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NM_004006.2:c.6775_6777delGTGinsC ).
*	LRG_199t1:c.145_147delinsTGG (p.Arg49Trp)
	:	a deletion replacing nucleotides c.145 to c.147 (CGC, not described) with TGG
*	LRG_199t1:c.9002_9009delinsTTT
	:	a deletion of nucleotides c.9002 to c.9009, replaced by nucleotides TTT
	:	**NOTE**:	two variants separated by one nucleotide, together affecting one amino acid, should be described as a “delins”, so the description c.[145C>T;147C>G] is not correct
*	LRG_199t1:c.850_901delinsTTCCTCGATGCCTG
	:	a deletion of nuceotides c.850 to c.901, replaced by TTCCTCGATGCCTG
	:	**NOTE**:	parts of the inserted sequence "align" with the reference sequence, giving an alternative description like c.[850_869del;874_881del;887_897del;901_902insG]. The **"delins" format is recommended**: it is simpler and prevents software tools making incorrect predictions for the consequences at protein level. 
*	NC_000002.12:g.pter_8247756delins\[NC_000011.10:g.pter_15825266\]
	:	nucleotides g.pter to g.8247756 of chromosome 2 are deleted and replaced by nucleotides g.pter to g.1582566 of chromosome 11: the derivative chromosome 2 from an unbalanced translocation between the short arms of chromosomes 2 and 11 (ISCN der(2)t(2;11)(p25.1;p15.2)). Example copied from [_Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/).
	:	**NOTE**:	balanced translocations ([_see Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/)) are described as two complementary "delins" variants.
*	NC_000022.10:g.42522624_42522669delins42536337_42536382
	:	conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides g.42522624 to g.42522669 with those of the 3' flanking CYP2D7P1 gene, nucleotides g.42536337 to g.42536382 from the same genomic reference sequence (NC_000022.10)
*	NC_000012.11:g.6128892_6128954delins[NC_000022.10:g.17179029_17179091]
	:	conversion replacing nucleotides g.6128892 to g.6128954 of the VWF gene (NM_000552.3:c.3675-45_3692) on chromosome 12 with nucleotides g.17179029 to g.17179091 of the VWFP1 pseudogene on chromosome 22
*	NM_000797.3:c.812_829delins908_925
	:	conversion replacing nucleotides c.812 to c.829 of the DRD4 gene with nucleotides c.908 to c.925 from the same reference sequence
*	NM_004006.2:c.812_829delinsN[12]
	:	nucleotides c.812 to c.829 have been deleted and replaced by 12 unknown nucleotides (N[12])
