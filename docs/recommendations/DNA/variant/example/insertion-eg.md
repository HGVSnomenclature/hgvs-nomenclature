---
parent: DNA
title: insertion
category: example
---

*	simple insertions
	*	NC\_000023.10:g.32867861\_32867862insT  (NM\_004006.2:c.169\_170insA)
	:	the insertion of an T nucleotide between nucleotides g.32867861 and g.32867862 
	*	NC\_000023.10:g.32862923\_32862924insCCT (LRG\_199t1:c.240\_241insAGG)
	:	the insertion of nucleotides CCT between nucleotides g.32862923 and g.32862924
	*	NM\_004006.2:c.849\_850ins858\_895
	:	the insertion of a copy of nucleotids c.858 to c.895 between nuclotides c.849 and c.850
	*	NC\_000002.11:g.47643464\_47643465ins[NC\_000022.10:g.35788169\_35788352]
	:	the insertion of nucleotides g.35788169 and g.35788352 as found in NC\_000022.10 between nucloetides g.47643464 and g.47643465
*	complex insertions
	*	NM\_004006.2:c.419\_420ins[T;401\_419]
	:	the insertion of T followed by a copy of the sequence from c.401 to c.419 (a duplication not directly flanking the original sequence)
	*	LRG\_199t1:c.419\_420ins[T;450\_470;AGGG]
	:	the insertion of T followed by a copy of the sequence from c.450 to c.470, followed by AGGG
	*	NC\_000006.11:g.10791926\_10791927ins[NC\_000004.11:g.106370094\_106370420;A[26]]
	:	the insertion of a copy of an Alu-repeat sequence (from chromosome 4 nucleotides g.106370094 to g.106370420), and a stretch of 26 A nucleotides, between nucleotides g.10791926 and g.10791927 on chromosome 6. 
*	insertion of inverted duplicated copies
	*	NM\_004006.2:c.849\_850ins850\_900inv
	:	a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 5' of the original sequence, between nucleotide c.849 and c.850
	*	NM\_004006.2:c.900\_901ins850\_900inv
	:	a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 3' of the original sequence, between nucleotide c.900 and c.901
	*	LRG_199t1:c.940\_941ins[885\_940inv;A;851\_883inv]
	:	an inverted copy of nucleotides c.851 to c.940, with a G>A substitution of nucleotide c.884, is inserted directly 3' of the original sequence
	*	NM\_004006.2:c.940\_941ins[903\_940inv;851\_885inv]
	:	an inverted copy of nucleotides c.851 to c.940, with a deletion from nucleotides c.886 to c.902, is inserted directly 3' of the original sequence
*	incomplete descriptions, preferably use exact descriptions only
	*	NM\_004006.2:c.(222\_226)insG
	:	the insertion of a G at an unknown position in the sequence encoding amino acid 75
	*	NC\_000004.11:g.(3076562\_3076732)insN[12]
	:	the insertion of 12 nucleotides (not specified) at an unknown position between nucleotides g.3076562 and g.3076732 (exon 1 of the HTT gene containing the Gln/Pro repeat region)
	*	NC\_000023.10:g.32717298\_32717299insN  (NM\_004006.2:c.761\_762insN) 
	:	the insertion of one not specified nucleotide (N) between position g.32717298 and g.32717299
	*	NM\_004006.2:c.761\_762insNNNNN (alternatively NM\_004006.1:c.761\_762insN[5])
	:	the insertion of 5 not specified nucleotides (NNNNN) between position c.761 and c.762
	*	NC\_000023.10:g.32717298\_32717299insN[100]
	:	the insertion of 100 nucleotides (not specified) between position g.32717298 and g.32717299
	*	NC\_000023.10:g.32717298\_32717299insN[(80_120)]
	:	the insertion of 80 to 120 nucleotides between position g.32717298 and g.32717299
	*	NC\_000023.10:g.32717298\_32717299insN[?]
	:	the insertion of an unknown number of nucleotides between position g.32717298 and g.32717299
	*	NC\_000006.11:g.8897754\_8897755ins[N[543];8897743\_8897754]
	:	the insertion of an undefined sequence of 543 nucleotides (N[543]), and a 12 nucleotide target site duplication (g.8897743 to g.8897754), between nucleotides g.8897754 and g.8897755 on chromosome 6. 
*	g.?\_?ins[NC\_000023.10:(12345\_23456)\_(34567\_45678)]
	:	the insertion of a sequence from the X-chromosome (NC\_000023.10), maximally involving nucleotides 12345\_45678 but certainly nucleotides 23456\_34567, at an unknown position (g.?\_?) in the genome ([_see Uncertain_](/recommendations/uncertain))
