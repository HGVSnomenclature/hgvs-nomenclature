# Duplication

<!-- ## Definition -->

Duplication: a sequence change where, compared to a reference sequence, a copy of one or more nucleotides are inserted **directly 3'** of the original copy of that sequence.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml dna.dup
```

## Notes

- "positions_duplicated" should contain **two different positions**, e.g. 123_126 not 123_123.
- the "positions_duplicated" should be listed from **5' to 3'**, e.g. 123_126 not 126_123.
- by definition, duplication may only be used when the additional copy is **directly 3'-flanking** of the original copy (a "tandem duplication").
    - when a variant can be described as a duplication it **must** be described as a duplication and not as e.g. an insertion (see _Prioritization_](../general.md)
    - when there is no evidence that the extra copy of a sequence detected is in tandem (directly 3'-flanking the original copy), the change can not be described as a duplication, it should be described as **an insertion** (see [Insertion](insertion.md) and [proposal SVD-WG003](../../consultation/SVD-WG003.md)).
    - **inverted duplications** are described as insertion (g.234_235ins123_234inv), not as a duplication (see [Inversion](inversion.md))
- when more than one additional copies are inserted directly 3' of the original copy the change is indicated using the format for [Repeated sequences](repeated.md), like [3] (triplication), [4] (quadruplication), etc.
- two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
        - exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins" : **NOTE:** the SVD-WG has prepared a proposal to modify this recommendation (see [SVD-WG010](../../consultation/SVD-WG010.md)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant**
- for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
    - **exception**: duplications around exon/exon junctions when identical nucleotides flank the junction (see [Numbering](../../background/numbering.md#DNAc)); : when ..GAT gta..//..cag TCA.. changes to ..GATT gta..//..cag TCA.., based on a coding DNA reference sequence the variant is described as `LRG_199t1:c.3921dup` (NC_000023.10:g.32459297dup) and **not as** c.3922dup (which would translate to g.32456507dup)
- † = see [Uncertain](../uncertain.md); when the postion and/or the sequence of a duplication has not been defined

## Examples

- one nucleotide
    - NM_004006.2:c.20dup (NC_000023.10:g.33229410dup): the duplication of a T at position c.20 in the sequence AGAAGTAGAGG to AGAAGT<code class="spot1">T</code>AGAGG: **NOTE**: it is **not** allowed to describe the variant as c.19_20insT (see [prioritisation](../general.md)): **NOTE**: the recommendation is not to describe the variant as NM_004006.2:c.20dupT, i.e. describe the duplicated nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. NM_004006.2:c.20dupG).
    - NM_004006.2:c.5697dup (3'rule): a duplication of the A at position c.5697 in the sequence ATTG<code class="spot1">AAAAAAAA</code>TTAG to ATTG<code class="spot1">AAAAAAAAA</code>TTAG, i.e. the last A of the 8 nucleotide A-stretch running from position c.5690 to c.5697.: **NOTE**: the 3'rule has been applied here stating that **"for all descriptions the most 3' position possible is arbitrarily assigned to have been changed"** (see [General_Recommendations](../general.md).
    - NC_000023.11:g.32343183dup (3'rule): a duplication of the T at position g.32343183 in the sequence CTAA<code class="spot1">TTTTTTTT</code>CAAT to CTAA<code class="spot1">TTTTTTTTT</code>CAAT, i.e. the last T of the 8 nucleotide T-stretch running from position g.32343176 to g.32343183.: **NOTE**: the T nucleotide in NC_000023.11:g.32343183 corresponds to the A nucleotide in NM_004006.2:c.5690, a transcript annotated on the minus strand of the X-chromosome. However, applying the 3'rule, the deletion of this nucleotide based on a coding DNA reference sequence (transcript level) should be described as NM_004006.2:c.5697dup (not as NM_004006.2:c.5690dup).
- several nucleotides
    - NM_004006.2:c.20_23dup (NC_000023.11:g.33211290_33211293dup): a duplication from position c.20 to c.23 in the sequence AGAAGTAGAGG to AGAAGTAGA<code class="spot1">TAGA</code>GG: **NOTE**: the recommendation is not to describe the variant as c.20_23dupTAGA, i.e. describe the duplicated nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increases (e.g. c.20_23dupTGGA).
    - NC_000023.11(NM_004006.2):c.260_264+48dup (NC_000023.11:g.32844735_32844787dup): a duplication of nucleotides c.260 to c.264+48 (coding DNA reference sequence), crossing an exon/intron border
- exon/intron/exon
    - exon/exon
        - NC_000023.11(NM_004006.2):c.3921dup: the duplication of the T nucleotide at the exon/exon border in the sequence ..GA<code class="spot1">T</code> gta..//..cag TCA.. changing to ..GA<code class="spot1">TT</code> gta..//..cag TCA..: **NOTE** : according to an exception of the 3'rule the variant (NC_000023.11:g.32441180dup) is **not described** as c.3922dup since this would shift the position of the variant to the next exon (c. 3922 linking to g.32441180) (see [exception in Numbering](../../background/numbering.md#DNAc) and see [Q&A](deletion.md#6del))
    - exon/intron
        - NC_000023.11(NM_004006.2):c.1704+1dup: the duplication of the G nucleotide at the exon/intron border in the sequence GAACAG<code class="spot1">g</code>t.../..agTGCCTT changing to GAACAG<code class="spot1">gg</code>t.../..agTGCCTT (not c.1704dup): **NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1704dup
    - intron/exon
        - NC_000023.11(NM_004006.2):c.1813dup: the duplication of the G nucleotide at the intron/exon border in the sequence CTGGCCgt.../..ag<code class="spot1">G</code>TTTTA changing to CTGGCCgt.../..ag<code class="spot1">GG</code>TTTTA (not c.1813-1dup): **NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or r.1813dup
- exons
    - `NC_000023.11(NM_004006.2):c.4072-1234_5155-246dup`: a duplication of nucleotides c.4072-1234 to c.5155-246 duplicating exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene.: **NOTE** : the format c.4072-1234_5155-246dupXXXXX, with XXXXX indicating the size of the duplication, **should not** be used: **NOTE** : the description NM_004006.2:c.4072-1234_5155-246dup is not correct, the reference sequence NM_004006.2 is a coding DNA reference sequence which **does not include** the intron sequences involved
    - `NC_000023.11(NM_004006.2):c.720_991dup`: a duplication of nucleotides c.720 to c.991 starting in exon 8 (position c.720) and ending in exon 10 (position c.991) of the DMD-gene.
    - `NC_000023.11(NM_004006.2):c.(4071+1_4072-1)_(5154+1_5155-1)dup`: a duplication of exon 30 (starting at position c.4072) to exon 36 (ending at position c.5145) of the human DMD-gene. The duplication break point has **not been sequenced**. Exons 29 (ending at c.4071) and 37 (starting at nucleotide c.5146) have been tested an shown to be **not duplicated**. The duplication therefore starts in intron 29 (position c.4071+1 to c.4072-1) and ends in intron 36 (position c.5145+1 to c.5156-1).: **NOTE** : this description is part of [proposal SVD-WG003 (undecided)](../../consultation/SVD-WG003.md).: **NOTE** : previously, the suggestion was made to describe such duplications using the format `c.4072-?_5154+?dup`. However, since c.4072-? indicates "**to an unknown postion 5' of c.4072**" and c.5154+? "**to an unknown postion 3' of c.5154**" this description is not correct when it is known that exons 29 and 37 are involved.
    - `NC_000001.11(NM_206933.2):c.[675-542_1211-703dup;1211-703_1211-704insGTAAA]`: a duplication of the sequence from nucleotide position c.75-542 to 1211-703, followed by the insertion of the sequence "GTAAA".: **NOTE** : the variant is not described using "dupins", a format not used in HGVS nomenclature
    - `NC_000023.11:g.(32381076_32382698)_(32430031_32456357)[3]` (`NC_000023.11(NM_004006.2):c.(4071+1_4072-1)_(5154+1_5155-1)[3]`): three copies of the sequence from exon 30 (starting at position c.4072) to exon 36 (ending at position c.5154) of the DMD-gene were detected (break points not sequenced).
    - duplications extending beyond the transcribed region: following current recommendations (see [Numbering](../../background/numbering.md)) it is not allowed to describe variants in nucleotides beyond the boundaries of a reference sequence. Consequently, duplications extending 5' of a transcript **can not** be described like NC_000023.11(NM_004006.2):c.(?\_-244)\_(31+1_32-1)dup (c.-244 is the first nucleotide of NM_004006.2). Duplications extending 3' of a transcript **can not** be described like `NC_000023.11(NM_004006.2):c.(10086+1_10087-1)_(*2691_?)dup` (`c.*2691` is the last nucleotide of NM_004006.2). Such duplications can only be described using **genomic coordinates**. The HGVS nomenclature committee (SVD-WG) is discussing whether a c. based format should be proposed.
- gene
    - `NC_000023.11:g.(31060227_31100351)_(33274278_33417151)dup`: a duplication of the entire DMD gene based on a SNP-array analysis where the maximum size of the duplication lies between SNPs rs396303 and rs7887548 (nucleotides 31060227 and 33417151) and the minimum size between SNPs rs808178 and rs7887103 (nucleotides 31100351 and 33274278). Describing the duplication based on a coding DNA reference sequence using `NC_000023.11(NM_004006.2):c.(-205839_-62966)_(*21568_*61692)dup` makes no sense.: **NOTE**: the array analysis detects an extra copy of the sequences and it has to be determined whether it is a duplication. When it is not sure the variant is a duplication the variant should be described as an insertion, `g.?_?ins[NC_000023.11:g.(31060227_31100351)_(33274278_33417151)]`
    - `NC_000023.11:g.(?_31120496)_(33339477_?)dup`: a duplication of the entire DMD gene based on a MLPA assay where nucleotides g.31120496 and g.33339477 are the center of the probes for the resp. last and first (brain promoter) exons.: **NOTE**: the MLPA analysis detects an extra copy of the sequences and it has to be determined whether it is a duplication. When it is not sure the variant is a duplication the variant should be described as an insertion, `g.?_?ins[NC_000023.11:g.(?_31120496)_(33339477_?)]`
- chromosome
    - `NC_000023.11:g.pter_qtersup`: a duplication of the entire X-chromosome ("sup" = [supernumary chromosome](complex.md)): **NOTE**: when, e.g. based on next-generation sequencing, only "an additional copy of all X-chromosome sequences" are detected the variant should be described as NC_000023.11:g.pter_qter[2]
- `NC_000023.11:g.33344590_33344592=/dup` : a mosaic case where from position g.33344590 to g.33344592 besides the normal sequence also chromosomes are found containing a duplication of this sequence
- `NC_000023.11:g.33344590_33344592=//dup` : a chimeric case, i.e. the sample is a mix of cells containing g.33344590_33344592= and g.33344590_33344592dup

## Discussion

!!! note "Why do we not describe a duplication as an insertion?"

    Although duplications are basically a special type of insertion, there are several reasons why the recommendation is to describe duplications separately

    - the description is simple and shorter
    - it is clear and prevents confusion regarding the position when an insertion is incorrectly reported like "22insG"
    - it prevents hypothetical discussions regarding the site of the insertion; in the case of a duplication including an intron/exon border (e.g. c.123-8_137dup) is the "insertion" in the intron or in the exon?
    - insertion more or less means "coming from elsewhere". Mechanistically, a duplication is most likely caused by a local event, DNA polymerase slippage, duplicating a local sequence.

!!! note "Can I use g.123dup6 to describe a 6 nucleotide duplication?"

    No, a duplication of more than one nucleotide should give the position of the first and last nucleotide duplicated, separated using the range symbol ("_", underscore), e.g. g.123_128dup. Note also that from the description "g.123dup6" it is not clear whether the duplication starts **at** position g.123 (so g.123_128dup) or **after** position 123 (so g.124_129dup).<a id="123dup"></a>

!!! note "In the example above, **c.3921dup**, should the description based on a coding DNA reference sequence not be c.3922dup?"

    Strictly speaking you are right. However, for cases like this an exception was made to prevent that when c.3922dup is translated back to a genomic position one would end up at the wrong nucleotide, in the wrong exon (NC_000023.10:g.32456507dup in stead of NC_000023.10:g.32459297dup).

!!! note "How should I describe the change ATCG**ATCGATCGATCG**AGGGTCCC to ATCG**ATCGATCGATCG**A<code class="spot1">ATCGATCGATCG</code>GGGTCCC? The fact that the inserted sequence (ATCGATCGATCG) is present in the original sequence suggests it derives from a duplicative event"

    The variant should be described as an insertion; g.17_18ins5_16. A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem). Note that the description given still makes it clear that the sequence inserted between g.17 and g.18 is probably derived from nearby, i.e. position g.5 to g.16, and thus likely derived from a duplicative event.
