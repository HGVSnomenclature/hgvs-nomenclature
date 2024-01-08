# Splicing

<!-- ## Definition -->

Splicing: a sequence change where, compared to a reference sequence, the normal RNA splicing pattern is altered.

## Syntax

Variants affecting RNA splicing result in either a [deletion](deletion.md) or [insertion](insertion.md) on the RNA level and should be described as such. Recommendations on representing adjoined transcripts formed by gene fusions are discussed in the Notes and Examples below.

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- a "," (comma) is used to separate different transcripts/proteins derived from one allele; `r.[123a>u,122_154del]`
- HGVS recommends following the [HGNC guidelines](https://www.genenames.org/about/guidelines/) and the [VICC Gene Fusion Specification](https://fusions.cancervariants.org/en/latest) nomenclature to describe products of gene fusions

    - The HGNC recommendations include using a `GENESYMBOL1::GENESYMBOL2` syntax for gene-level fusion descriptions, and `GENESYMBOL1-GENESYMBOL2` syntax for read-through transcripts
    - The VICC nomenclature extends the HGNC recommendations to include a terminology, information model, and nomenclature for gene-level and exon-level representation, with components for disambiguating regulatory fusions from chimeric transcript fusions
    - HGVS also recommends the use of adjoined transcripts (see examples) for precise and unambiguous characterization of chimeric transcripts at the sequence level

## Examples

- **one variant, several transcripts**
    - `NC_000023.11(NM_004006.2):r.[897u>g,832_960del]`<br>
      two different transcripts, `r.897u>g` and `r.832_960del`, derive from one variant (`c.897T>G` at the DNA level)<br>
      alternative description `LRG_199t1:r.[897u>g,832_960del]`
- **splice acceptor site**
    - `NC_000023.11(NM_004006.2):r.650_831del`<br>
      as a consequence of a variant destroying a splice acceptor site, the sequence from nucleotide `r.650` to `r.831` (exon 8) is deleted from the transcript
    - `NC_000023.11(NM_004006.2):r.650_712del`<br>
      as a consequence of a variant destroying a splice acceptor site, a new acceptor site in exon 8 (position 712 / 713) is activated and the sequence from nucleotide `r.650` to `r.712` is deleted from the transcript
    - `NC_000023.11(NM_004006.2):r.649_650ins[650-52_650-2;c]`<br>
      as a consequence of a variant destroying a splice acceptor site (`c.650-1G>C`), a new acceptor site in intron 7 is activated and the intron 7 sequence from positions 650-52 to 650-1 is inserted in the transcript (NOTE: nucleotide 650-1 changed from g to c)<br>
      alternative description `LRG_199t1:r.649_650ins[650-52_650-2;c]`
- **splice donor site** (`c.831+2T>A`)
    - `NC_000023.11(NM_004006.2):r.650_831del`<br>
      as a consequence of a variant destroying the exon 8 splice donor site, the sequence from nucleotide `r.650` to `r.831` (exon 8) is deleted from the transcript
    - `NC_000023.11(NM_004006.2):r.778_831del`<br>
      as a consequence of a variant destroying the exon 8 donor acceptor site, a new donor site in exon 8 (position 777 / 778) is activated and the sequence from nucleotide `r.778` to `r.831` is deleted from the transcript
    - `NC_000023.11(NM_004006.2):r.831_832ins[ga;831+3_831+60]`<br>
      as a consequence of a variant destroying the exon 8 splice donor site, a new donor site in intron 8 (position 831+60 / 831+61) is activated and the intron 8 sequence from positions 831+1 to 831+60 is inserted in the transcript (NOTE: nucleotide 831+2 changed from u to a)<br>
      alternative description `LRG_199t1:r.831_832ins[ga;831+3_831+60]`
- **intron variant**
    - `NC_000023.11(NM_004006.2):r.649_650ins650-50_650-1`<br>
      as a consequence of an intron 7 variant (`c.650-52_650-51del`) a new stronger exon 8 splice acceptor site is created (position 650-51 / 650-50) and the intron 7 sequence from positions 650-50 to 650-1 is inserted in the transcript<br>
      alternative description `LRG_199t1:r.649_650ins650-50_650-1`
    - `NC_000023.11(NM_004006.2):r.831_832ins831+1_831+67`<br>
      as a consequence of an intron 8 variant (`c.831+71C>A`) a new stronger exon 8 splice donor site is created (position 831+67 / 831+68) and the intron 8 sequence from positions 831+1 to 831+67 is inserted in the transcript<br>
      alternative description `LRG_199t1:r.831_832ins831+1_831+67`
    - `NC_000023.11(NM_004006.2):r.649_650ins650-1400_650-1268`<br>
      as a consequence of an intron 7 variant (`c.650-1401T>G`) a new exon is created and its sequence (positions 650-1400 to 650-1268) is inserted in the transcript<br>
      alternative description `LRG_199t1:r.649_650ins650-1400_650-1268`
- **fusion transcript** (based on [SVD-WG007](../../consultation/SVD-WG007.md))
    - `NM_002354.2:r.-358_555::NM_000251.2:r.212_*279`<br>
      describes an `EPCAM::MSH2` fusion transcript where nucleotides `r.-358` to `r.555` (EPCAM gene, reference transcript NM_002354.2) are spliced to nucleotides `r.212` to `r.*279` (MSH2 gene, reference transcript NM_000251.2)
- **uncertain** (RNA not analysed)
    - `NC_000023.11(NM_004006.2):r.(76a>c)`<br>
      RNA was not analysed but a substitution of the "a" nucleotide at `r.76` by a "c" is predicted
    - `NC_000023.11(NM_004006.2):r.?`<br>
      an effect on the RNA level is expected, but it is not possible to give a reliable prediction of the consequences (RNA not analysed)
    - `NC_000023.11(NM_004006.2):r.spl`<br>
      RNA has not been analysed, but it is very likely that splicing is affected

## Discussion

!!! note "A variant changes the +1 intron sequence (GT to AT). Although I did not analyse RNA, I am quite sure that normal splicing is affected. How can I best indicate this?"

    HGVS recommends to use the format `r.spl` to indicate that RNA was not analysed but splicing is most probably affected. In general the format is used for variants changing the +1, +2, -2 and -1 position of an intron, i.e. affecting the GT splice donor and AG splice acceptor site (excl. GT to GC and GC to GT variants). `r.(spl?)` is frequently used to indicate normal splicing might be affected as a consequence of variants in the first or last nucleotide of an exon, the +3 to +5 intron position (splice donor site) and variants generating a new AG-dinucleotide close to the normal splice acceptor site (AG). See [Uncertain](../uncertain.md).

!!! note "How can I best describe the predicted consequences at the protein level of a variant that most probably affects splicing?"

    The best format seems to use `p.?`, meaning "I do not know what to expect at the protein level".
