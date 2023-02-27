---
parent: DNA
title: deletion
category: example
---

*	one nucleotide
	*	NC\_000023.11:g.33344591del
	:	a deletion of the T at position g.33344591 in the sequence TGTG**<font color="red">A</font>**TTCT to TGTG**<font color="red">_</font>**TTCT
	:	_**NOTE**_: the recommendation is not to describe the variant as NC\_000023.11:g.33344591delT, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. NC\_000023.11:g.33344591delG).
	*	NM\_004006.2:c.5697del (3'rule)
	:	a deletion of the A at position c.5697 in the sequence ATTG**<font color="red">AAAAAAAA</font>**TTAG to ATTG**<font color="red">AAAA_AAA</font>**TTAG, i.e. the last A of the 8 nucleotide A-stretch running from position c.5690 to c.5697.
	:	_**NOTE**_: the 3'rule has been applied here stating that _**"for all descriptions the most 3’ position possible is arbitrarily assigned to have been changed"**_ ([_see General_Recommendations_](/general/).
	*	NC\_000023.11:g.32343183del (3'rule)
	:	a deletion of the T at position g.32343183 in the sequence CTAA**<font color="red">TTTTTTTT</font>**CAAT to CTAA**<font color="red">TTTT_TTT</font>**CAAT, i.e. the last T of the 8 nucleotide T-stretch running from position g.32343176 to g.32343183.
	:	_**NOTE**_: the T nucleotide in NC\_000023.11:g.32343183 corresponds to the A nucleotide in NM\_004006.2:c.5690, a transcript annotated on the minus strand of the X-chromosome. However, applying the 3'rule, the deletion of this nucleotide based on a coding DNA reference sequence (transcript level) should be described as NM\_004006.2:c.5697del (not as NM\_004006.2:c.5690del).
*	several nucleotides
	*	NC\_000023.11:g.33344590\_33344592del
	:	a deletion of nucleotides g.33344590 to g.33344592 in the sequence GTGT**<font color="red">GAT</font>**TCTG to GTGT**<font color="red">___</font>**TCTG
	:	_**NOTE**_: the recommendation is not to describe the variant as NC\_000023.11:g.33344590\_33344592delGAT, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. NC\_000023.11:g.33344590\_33344592delTTA).
	*	NC\_000023.11(NM\_004006.2):c.183\_186+48del
	:	a deletion of nucleotides c.183 to c.186+48 (coding DNA reference sequence), crossing an exon/intron border
*	exon/intron/exon
	*	exon/exon
		*	LRG\_199t1:c.3921del
		:	the deletion of the T nucleotide at the exon/exon border in the sequence ..GA**<font color="red">T</font>** gta..//..cag TCA.. changing to ..GA**<font color="red">_</font>** gta..//..cag TCA..
		:	_**NOTE**_ : according to an exception of the 3'rule the variant (NC\_000023.10:g.32459297del) is **not described** as c.3922del since this would shift the position of the variant to the next exon (c. 3922 linking to g.32456507) ([_see exception in Numbering_](/bg-material/numbering/#DNAc) and [_see Q&A_](/recommendations/DNA/variant/deletion/#6del))
	*	exon/intron
		*	LRG\_199t1:c.1704+1del
		:	the deletion of the G nucleotide at the exon/intron border in the sequence GAACAG**<font color="red">g</font>**t.../..agTGCCTT changing to GAACAG**<font color="red">_</font>**t.../..agTGCCTT (not c.1704del)
		:	_**NOTE**_: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1704del
	*	intron/exon
		*	LRG\_199t1:c.1813del
		:	the deletion of the G nucleotide at the intron/exon border in the sequence CTGGCCgt.../..ag**<font color="red">G</font>**TTTTA changing to CTGGCCgt.../..ag**<font color="red">_</font>**TTTTA (not c.1813-1del)
		:	_**NOTE**_: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1813del	
*	exons 
	*	NC\_000023.11(NM\_004006.2):c.4072-1234\_5155-246del
	:	a deletion of nucleotides c.4072-1234 to c.5155-246 removing exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene.
	:	_**NOTE**_ : c.4072-1234\_5155-246delXXXXX, the size of the deletion (XXXXX) **should not** be described
	*	break point not sequenced
	:	recommended is to describe the deletion detected as precise as possible, [_see Uncertain_](varnomen.hgvs.org/recommendations/uncertain/) for examples. In practice, most people use the so-called **"exon-based description"**, a general description which does not contain specific information regarding the exact nucleotide positions tested.
		*	general, "exon-based" description<br>
		:	NC\_000023.11(NM\_004006.2):c.(4071+1\_4072-1)\_(5154+1\_5155-1)del
		:	a deletion of exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene. The deletion break point has **not been sequenced**. Exons 29 (ending at c.4071) and 37 (starting at nucleotide c.5155) have been tested and shown to be **not deleted**. The deletion therefore starts in intron 29 (position c.4071+1 to c.4072-1) and ends in intron 36 (position c.5154+1 to c.5155-1).
		:	_**NOTE**_ : previously, the suggestion was made to describe such deletions using the format NC\_000023.11(NM\_004006.2):c.4072-?\_5154+?del. However, since c.4072-? indicates "**to an unknown postion 5' of c.4072**" and c.5154+? "**to an unknown postion 3' of c.5154**" this description is not correct when it is known that exons 29 and 37 are present. See also [_SVD-WG003 (undecided)_](/bg-material/consultation/svd-wg003).
		*	specific description
		:	NC\_000023.11(NM\_004006.2):c.(3996\_4196)\_(5090\_5284)del
		:	**probe-based** description of a deletion, identified by MLPA, of exon 30 (deleted position tested c.4196) to exon 36 (deleted position tested c.5090) of the DMD-gene. The deletion break point has **not been sequenced**. Exons 29 (position tested c.3996) and 37 (position tested c.5284) are **not deleted**.
	*	deletions extending beyond the transcribed region
	:	following current recommendations (see [_Numbering_](/bg-material/numbering)) it is not allowed to describe variants in nucleotides beyond the boundaries of a reference sequence. Consequently, deletions extending 5' of a transcript **can not** be described like NC\_000023.11(NM\_004006.2):c.(?\_-244)\_(31+1\_32-1)del (c.-244 is the first nucleotide of NM\_004006.2). Deletions extending 3' of a transcript **can not** be described like NC\_000023.11(NM\_004006.2):c.(10086+1\_10087-1)\_(\*2691\_?)del (c.\*2691 is the last nucleotide of NM\_004006.2). Such deletions can only be described using **genomic coordinates**. The HGVS nomenclature committee (SVD-WG) is discussing whether a c. based format should be proposed.
*	gene
	*	NC\_000023.11:g.(31060227\_31100351)\_(33274278\_33417151)del
	:	a deletion of the entire DMD gene based on a SNP-array analysis where the maximum size of the deletion lies between SNPs rs396303 and rs7887548 (nucleotides 31060227 and 33417151) and the minimum size between SNPs rs808178 and rs7887103 (nucleotides 31100351 and 33274278).
	*	NC\_000023.11:g.(?\_31120496)\_(33339477\_?)del
	:	a deletion of the entire DMD gene based on a MLPA assay where the nucleotide positions g.31120496 and g.33339477 are defined by the first nucleotide of the probe 3’ of the ligation site for the resp. the last and first exons tested.
*	NC\_000023.11:g.33344590\_33344592=/del
:	a mosaic case where from position g.33344590 to g.33344592 besides the normal sequence also chromosomes are found containing a deletion of this sequence
*	NC\_000023.11:g.33344590\_33344592=//del
:	a chimeric case, i.e. the sample is a mix of cells containing g.33344590\_33344592= and g.33344590\_33344592del
