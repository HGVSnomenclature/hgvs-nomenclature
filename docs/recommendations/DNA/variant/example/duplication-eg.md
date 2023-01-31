---
parent: DNA
title: duplication
category: example
---

*	one nucleotide
	*	NM_004006.2:c.20dup (NC_000023.10:g.33229410dup)
	:	the duplication of a T at position c.20 in the sequence AGAAGTAGAGG to AGAAGT**<font color="red">T</font>**AGAGG
	:	**NOTE**: it is **not** allowed to describe the variant as c.19_20insT ([_see prioritisation_](/recommendations/general/))
	:	**NOTE**: the recommendation is not to describe the variant as NM_004006.2:c.20dupT, i.e. describe the duplicated nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. NM_004006.2:c.20dupG).
	*	NM_004006.2:c.5697dup (3'rule)
	:	a duplication of the A at position c.5697 in the sequence ATTG**<font color="red">AAAAAAAA</font>**TTAG to ATTG**<font color="red">AAAAAAAAA</font>**TTAG, i.e. the last A of the 8 nucleotide A-stretch running from position c.5690 to c.5697.
	:	**NOTE**: the 3'rule has been applied here stating that **"for all descriptions the most 3’ position possible is arbitrarily assigned to have been changed"** ([_see General_Recommendations_](/general/).
	*	NC_000023.11:g.32343183dup (3'rule)
	:	a duplication of the T at position g.32343183 in the sequence CTAA**<font color="red">TTTTTTTT</font>**CAAT to CTAA**<font color="red">TTTTTTTTT</font>**CAAT, i.e. the last T of the 8 nucleotide T-stretch running from position g.32343176 to g.32343183.
	:	**NOTE**: the T nucleotide in NC_000023.11:g.32343183 corresponds to the A nucleotide in NM_004006.2:c.5690, a transcript annotated on the minus strand of the X-chromosome. However, applying the 3'rule, the deletion of this nucleotide based on a coding DNA reference sequence (transcript level) should be described as NM_004006.2:c.5697dup (not as NM_004006.2:c.5690dup).
*	several nucleotides
	*	NM_004006.2:c.20_23dup (NC_000023.11:g.33211290_33211293dup)
	:	a duplication from position c.20 to c.23 in the sequence AGAAGTAGAGG to AGAAGTAGA**<font color="red">TAGA</font>**GG
	:	**NOTE**: the recommendation is not to describe the variant as c.20_23dupTAGA, i.e. describe the duplicated nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. c.20_23dupTGGA).
	*	NC_000023.11(NM_004006.2):c.260_264+48dup (NC_000023.11:g.32844735_32844787dup)
	:	a duplication of nucleotides c.260 to c.264+48 (coding DNA reference sequence), crossing an exon/intron border
*	exon/intron/exon
	*	exon/exon
		*	NC_000023.11(NM_004006.2):c.3921dup
		:	the duplication of the T nucleotide at the exon/exon border in the sequence ..GA**<font color="red">T</font>** gta..//..cag TCA.. changing to ..GA**<font color="red">TT</font>** gta..//..cag TCA..
		:	**NOTE** : according to an exception of the 3'rule the variant (NC_000023.11:g.32441180dup) is **not described** as c.3922dup since this would shift the position of the variant to the next exon (c. 3922 linking to g.32441180) ([_see exception in Numbering_](/background/numbering/#DNAc) and [_see Q&A_](/recommendations/DNA/variant/deletion/#6del))
	*	exon/intron
		*	NC_000023.11(NM_004006.2):c.1704+1dup
		:	the duplication of the G nucleotide at the exon/intron border in the sequence GAACAG**<font color="red">g</font>**t.../..agTGCCTT changing to GAACAG**<font color="red">gg</font>**t.../..agTGCCTT (not c.1704dup)
		:	**NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1704dup
	*	intron/exon
		*	NC_000023.11(NM_004006.2):c.1813dup
		:	the duplication of the G nucleotide at the intron/exon border in the sequence CTGGCCgt.../..ag**<font color="red">G</font>**TTTTA changing to CTGGCCgt.../..ag**<font color="red">GG</font>**TTTTA (not c.1813-1dup)
		:	**NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1813dup
*	exons
	*	NC_000023.11(NM_004006.2):c.4072-1234_5155-246dup
		:	a duplication of nucleotides c.4072-1234 to c.5155-246 duplicating exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene.
		: 	**NOTE** : the format c.4072-1234_5155-246dupXXXXX, with XXXXX indicating the size of the duplication, **should not** be used
		: 	**NOTE** : the description NM_004006.2:c.4072-1234_5155-246dup is not correct, the reference sequence NM_004006.2 is a coding DNA reference sequence which **does not include** the intron sequences involved
	*	NC_000023.11(NM_004006.2):c.720_991dup
		:	a duplication of nucleotides c.720 to c.991 starting in exon 8 (position c.720) and ending in exon 10 (position c.991) of the DMD-gene.
	*	NC_000023.11(NM_004006.2):c.(4071+1_4072-1)\_(5154+1_5155-1)dup
		:	a duplication of exon 30 (starting at position c.4072) to exon 36 (ending at position c.5145) of the human DMD-gene. The duplication break point has **not been sequenced**. Exons 29 (ending at c.4071) and 37 (starting at nucleotide c.5146) have been tested an shown to be **not duplicated**. The duplication therefore starts in intron 29 (position c.4071+1 to c.4072-1) and ends in intron 36 (position c.5145+1 to c.5156-1).
		:	**NOTE** : this description is part of [_proposal SVD-WG003 (undecided)_](/background/consultation/SVD-WG003).
		:	**NOTE** : previously, the suggestion was made to describe such duplications using the format c.4072-?\_5154+?dup. However, since c.4072-? indicates "**to an unknown postion 5' of c.4072**" and c.5154+? "**to an unknown postion 3' of c.5154**" this description is not correct when it is known that exons 29 and 37 are involved.
	*	NC_000001.11(NM_206933.2):c.[675-542_1211-703dup;1211-703_1211-704insGTAAA]
		:	a duplication of the sequence from nucleotide position c.75-542 to 1211-703, followed by the insertion of the sequence "GTAAA".
		:	**NOTE** : the variant is not described using "dupins", a format not used in HGVS nomenclature 
	*	NC_000023.11:g.(32381076_32382698)\_(32430031_32456357)[3]  (NC_000023.11(NM_004006.2)c.(4071+1_4072-1)\_(5154+1_5155-1)[3])
		:	three copies of the sequence from exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene were detected (break points not sequenced).
	*	duplications extending beyond the transcribed region
	:	following current recommendations (see [_Numbering_](/background/numbering)) it is not allowed to describe variants in nucleotides beyond the boundaries of a reference sequence. Consequently, duplications extending 5' of a transcript **can not** be described like NC_000023.11(NM_004006.2):c.(?\_-244)\_(31+1_32-1)dup (c.-244 is the first nucleotide of NM_004006.2). Duplications extending 3' of a transcript **can not** be described like NC_000023.11(NM_004006.2):c.(10086+1_10087-1)\_(\*2691\_?)dup (c.\*2691 is the last nucleotide of NM_004006.2). Such duplications can only be described using **genomic coordinates**. The HGVS nomenclature committee (SVD-WG) is discussing whether a c. based format should be proposed.
*	gene
	*	NC_000023.11:g.(31060227_31100351)\_(33274278_33417151)dup
	:	a duplication of the entire DMD gene based on a SNP-array analysis where the maximum size of the duplication lies between SNPs rs396303 and rs7887548 (nucleotides 31060227 and 33417151) and the minimum size between SNPs rs808178 and rs7887103 (nucleotides 31100351 and 33274278). Describing the duplication based on a coding DNA reference sequence using NC_000023.11(NM_004006.2):c.(-205839\_-62966)\_(\*21568\_\*61692)dup makes no sense.
	:	**NOTE**: the array analysis detects an extra copy of the sequences and it has to be determined whether it is a duplication. When it is not sure the variant is a duplication the variant should be described as an insertion, g.?\_?insNC_000023.11:(31060227_31100351)\_(33274278_33417151)
	*	NC_000023.11:g.(?\_31120496)\_(33339477\_?)dup
	:	a duplication of the entire DMD gene based on a MLPA assay where nucleotides g.31120496 and g.33339477 are the center of the probes for the resp. last and first (brain promoter) exons.
	:	**NOTE**: the MLPA analysis detects an extra copy of the sequences and it has to be determined whether it is a duplication. When it is not sure the variant is a duplication the variant should be described as an insertion, g.?\_?insNC_000023.11:(?\_31120496)\_(33339477\_?)
*	chromosome
	*	NC_000023.11:g.pter_qtersup
	:	a duplication of the entire X-chromosome ("sup" = [_supernumary chromosome_](/recommendations/DNA/variant/complex/))
	:	**NOTE**: when, e.g. based on next-generation sequencing, only "an additional copy of all X-chromosome sequences" are detected the variant should be described as NC_000023.11:g.pter_qter[2]
*	NC_000023.11:g.33344590_33344592=/dup
:	a mosaic case where from position g.33344590 to g.33344592 besides the normal sequence also chromosomes are found containing a duplication of this sequence
*	NC_000023.11:g.33344590_33344592=//dup
:	a chimeric case, i.e. the sample is a mix of cells containing g.33344590_33344592= and g.33344590_33344592dup
