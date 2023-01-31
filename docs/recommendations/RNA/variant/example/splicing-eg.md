---
parent: RNA
title: splicing
category: example
---

*	**one variant, several transcripts**
	*	NC_000023.11(NM_004006.2):r.[897u>g,832_960del]
	:	two different transcripts, r.897u>g and r.832_960del, derive from one variant (c.897T>G at the DNA level)
	:	alternative description LRG_199t1:r.[897u>g,832_960del]
*	**splice acceptor site**
	*	NC_000023.11(NM_004006.2):r.650_831del
	:	as a consequence of a variant destroying a splice acceptor site, the sequence from nucleotide r.650 to r.831 (exon 8) is deleted from the transcript
	*	NC_000023.11(NM_004006.2):r.650_712del
	:	as a consequence of a variant destroying a splice acceptor site, a new acceptor site in exon 8 (position 712 / 713) is activated and the sequence from nucleotide r.650 to r.712 is is deleted from the transcript
	*	NC_000023.11(NM_004006.2):r.649_650ins[650-52_650-2;c]
	:	as a consequence of a variant destroying a splice acceptor site (c.650-1G>C), a new acceptor site in intron 7 is activated and the intron 7 sequence from positions 650-52 to 650-1 is inserted in the transcript (NOTE: nucleotide 650-1 changed from g to c)
	:	alternative description LRG_199t1:r.649_650ins[650-52_650-2;c]
*	**splice donor site** (c.831+2T>A)
	*	NC_000023.11(NM_004006.2):r.650_831del
	:	as a consequence of a variant destroying the exon 8 splice donor site, the sequence from nucleotide r.650 to r.831 (exon 8) is deleted from the transcript
	*	NC_000023.11(NM_004006.2):r.778_831del
	:	as a consequence of a variant destroying the exon 8 donor acceptor site, a new donor site in exon 8 (position 777 / 778) is activated and the sequence from nucleotide r.778 to r.831 is deleted from the transcript
	*	NC_000023.11(NM_004006.2):r.831_832ins[ga;831+3_831+60]
	:	as a consequence of a variant destroying the exon 8 splice donor site, a new donor site in intron 8 (position 831+60 / 831+61) is activated and the intron 8 sequence from positions 831+1 to 831+60 is inserted in the transcript (NOTE: nucleotide 831+2 changed from u to a)
	:	alternative description LRG_199t1:r.831_832ins[ga;831+3_831+60]
*	**intron variant**
	*	NC_000023.11(NM_004006.2):r.649_650ins650-50_650-1
	:	as a consequence of an intron 7 variant (c.650-52_650-51del) a new stronger exon 8 splice acceptor site is created (position 650-51 / 650-50) and the intron 7 sequence from positions 650-50 to 650-1 is inserted in the transcript
	:	alternative description LRG_199t1:r.649_650ins650-50_650-1
	*	NC_000023.11(NM_004006.2):r.831_832ins831+1_831+67
	:	as a consequence of an intron 8 variant (c.831+71C>A) a new stronger exon 8 splice donor site is created (position 831+67 / 831+68) and the intron 8 sequence from positions 831+1 to 831+67 is inserted in the transcript
	:	alternative description LRG_199t1:r.831_832ins831+1_831+67	
	*	NC_000023.11(NM_004006.2):r.649_650ins650-1400_650-1268
	:	as a consequence of an intron 7 variant (c.650-1401T>G) a new exon is created and its sequence (positions 650-1400 to 650-1268) is inserted in the transcript
	:	alternative description LRG_199t1:r.649_650ins650-1400_650-1268	
*	**fusion transcript** (based on [_SVD-WG007_](/background/consultation/SVD-WG007/)) 
	*	NM_002354.2:r.-358_555::NM_000251.2:r.212\_\*279
	:	describes an EPCAM::MSH2 fusion transcript where nucleotides r.-358 to r.555 (EPCAM gene, reference transcript NM_002354.2) are spliced to nucleotides r.212 to r.\*279 (MSH2 gene, reference transcript NM_000251.2)
*	**uncertain** (RNA not analysed)
	*	NC_000023.11(NM_004006.2):r.(76a>c)
	:	RNA was not anaysed but a substitution of the “a” nucleotide at r.76 by a “c” is predicted
	*	NC_000023.11(NM_004006.2):r.?
	:	an effect on the RNA level is expected but it is not possible to give a reliable prediction of the consequences (RNA not analysed)
	*	NC_000023.11(NM_004006.2):r.spl
	:	RNA has not been analysed but it is very likely that splicing is affected
