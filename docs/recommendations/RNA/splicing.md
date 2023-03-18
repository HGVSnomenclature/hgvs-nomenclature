# splicing

## Definition

Splicing: a sequence change where, compared to a reference sequence, the normal RNA splicing pattern is altered.

## Description

Variants affecting RNA splicing result in either a [_deletion_](../deletion/) or [_insertion_](../insertion/) on the RNA level and should be described as such.

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* a "," (comma) is used to separate different transcripts/proteins derived from one allele; r.[123a>u,122_154del]
## Examples

* **one variant, several transcripts**
    * NC\_000023.11(NM\_004006.2):r.[897u>g,832_960del]: two different transcripts, r.897u>g and r.832_960del, derive from one variant (c.897T>G at the DNA level): alternative description LRG\_199t1:r.[897u>g,832_960del]
* **splice acceptor site**
    * NC\_000023.11(NM\_004006.2):r.650\_831del: as a consequence of a variant destroying a splice acceptor site, the sequence from nucleotide r.650 to r.831 (exon 8) is deleted from the transcript
    * NC\_000023.11(NM\_004006.2):r.650\_712del: as a consequence of a variant destroying a splice acceptor site, a new acceptor site in exon 8 (position 712 / 713) is activated and the sequence from nucleotide r.650 to r.712 is is deleted from the transcript
    * NC\_000023.11(NM\_004006.2):r.649\_650ins[650-52\_650-2;c]: as a consequence of a variant destroying a splice acceptor site (c.650-1G>C), a new acceptor site in intron 7 is activated and the intron 7 sequence from positions 650-52 to 650-1 is inserted in the transcript (NOTE: nucleotide 650-1 changed from g to c): alternative description LRG\_199t1:r.649\_650ins[650-52\_650-2;c]
* **splice donor site** (c.831+2T>A)
    * NC\_000023.11(NM\_004006.2):r.650\_831del: as a consequence of a variant destroying the exon 8 splice donor site, the sequence from nucleotide r.650 to r.831 (exon 8) is deleted from the transcript
    * NC\_000023.11(NM\_004006.2):r.778\_831del: as a consequence of a variant destroying the exon 8 donor acceptor site, a new donor site in exon 8 (position 777 / 778) is activated and the sequence from nucleotide r.778 to r.831 is deleted from the transcript
    * NC\_000023.11(NM\_004006.2):r.831\_832ins[ga;831+3\_831+60]: as a consequence of a variant destroying the exon 8 splice donor site, a new donor site in intron 8 (position 831+60 / 831+61) is activated and the intron 8 sequence from positions 831+1 to 831+60 is inserted in the transcript (NOTE: nucleotide 831+2 changed from u to a): alternative description LRG\_199t1:r.831\_832ins[ga;831+3\_831+60]
* **intron variant**
    * NC\_000023.11(NM\_004006.2):r.649\_650ins650-50\_650-1: as a consequence of an intron 7 variant (c.650-52_650-51del) a new stronger exon 8 splice acceptor site is created (position 650-51 / 650-50) and the intron 7 sequence from positions 650-50 to 650-1 is inserted in the transcript: alternative description LRG\_199t1:r.649\_650ins650-50\_650-1
    * NC\_000023.11(NM\_004006.2):r.831\_832ins831+1\_831+67: as a consequence of an intron 8 variant (c.831+71C>A) a new stronger exon 8 splice donor site is created (position 831+67 / 831+68) and the intron 8 sequence from positions 831+1 to 831+67 is inserted in the transcript: alternative description LRG\_199t1:r.831\_832ins831+1\_831+67    
    * NC\_000023.11(NM\_004006.2):r.649\_650ins650-1400\_650-1268: as a consequence of an intron 7 variant (c.650-1401T>G) a new exon is created and its sequence (positions 650-1400 to 650-1268) is inserted in the transcript: alternative description LRG\_199t1:r.649\_650ins650-1400\_650-1268    
* **fusion transcript** (based on [_SVD-WG007_](../../../consultation/SVD-WG007/)) 
    * NM\_002354.2:r.-358\_555::NM\_000251.2:r.212\_\*279: describes an EPCAM::MSH2 fusion transcript where nucleotides r.-358 to r.555 (EPCAM gene, reference transcript NM\_002354.2) are spliced to nucleotides r.212 to r.\*279 (MSH2 gene, reference transcript NM\_000251.2)
* **uncertain** (RNA not analysed)
    * NC\_000023.11(NM\_004006.2):r.(76a>c): RNA was not anaysed but a substitution of the "a" nucleotide at r.76 by a "c" is predicted
    * NC\_000023.11(NM\_004006.2):r.?: an effect on the RNA level is expected but it is not possible to give a reliable prediction of the consequences (RNA not analysed)
    * NC\_000023.11(NM\_004006.2):r.spl: RNA has not been analysed but it is very likely that splicing is affected
## Discussion

!!! note "A variant changes the +1 intron sequence (GT to AT). Although I did not analyse RNA, I am quite sure that normal splicing is affected. How can I best indicate this?"

    HGVS recommends to use the format "<b>r.spl</b>" to indicate that RNA was not analysed but splicing is most probably affected. In general the format is used for variants changing the +1, +2, -2 and -1 position of an intron, i.e. affecting the GT splice donor and AG splice acceptor site (excl. GT to GC and GC to GT variants). "<b>r.(spl?)</b>" is frequently used to indicate normal splicing might be affected as a consequence of variants in the first or last nucleotide of an exon, the +3 to +5 intron position (splice donor site) and variants generating a new AG-dinucleotide close to the normal splice acceptor site (AG). See [Uncertain](https://varnomen.HGVS.org/recommendations/uncertain/).

!!! note "How can I best describe the predicted consequences at the protein level of a variant that most probably affects splicing?"

    The best format seems to use "p.?", meaning "I do not know what to expect at the protein level".
