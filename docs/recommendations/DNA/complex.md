# Complex (HGVS/ISCN)

<!-- ## Definition -->

Complex: a sequence change where, compared to a reference sequence, a range of changes occur that can not be described as one of the basic variant types (substitution, deletion, duplication, insertion, inversion, deletion-insertion, or repeated sequence).

## Description

Sequence changes can be very complex, involving a range of changes at one specific location.
Complex changes, including translocations, are described using the recommendations of the accepted HGVS nomenclature **named extension ISCN**, based on the original proposal [SVD-WG004 (ISCN<>HGVS)](../../consultation/SVD-WG004.md).
The named ISCN extension has been developed in collaboration with [Standing Committee on Human Cytogenomic Nomenclature (ISCN)](../../consultation/ISCN.md), covering the description of numerical and structural chromosomal changes detected using microscopic and cytogenetic techniques.
It should be noted there is a basic difference between ISCN and HGVS: while ISCN describes the structure of the resulting chromosome(s), HGVS describes the **variant(s) detected**. Note also the description of complex changes can become rather complicated and at some point, although literally correct, become effectively meaningless.

The named ISCN extension has been introduced in 2016 and was modified last in 2025 based on the [ISCN 2024 recommendations](https://karger.com/books/book/6011/ISCN-2024An-International-System-for-Human).

- only aberrant findings, linked to defined chromosomal positions, are described.

- each rearranged chromosome is described in a separate line.

- **`X`, `Y`, `1`, `2`, `3`, ..., `21`, `22`**<br>
  changes affecting sex chromosomes (X then Y) are listed first, followed by those affecting autosomes (numbers from low to high).<br>

- specific symbols
    - **`pter`, `cen`, `qter`**<br>
      the start of the chromosome is described as `pter`, the end as `qter`, and the centromere as `cen`.
        - **`(pter)_#` and `#_(qter)`**<br>
          for deletions extending from a known nucleotide position (`#`) to an unknown position in the direction of the telomere the format `(pter)_#` or `#_(qter)` is used.<br>
          **NOTE**: added in ISCN2020.
        - **`(cen)`**<br>
          for deletions extending from a known nucleotide position (`#`) to an unknown position in the direction of the centromere the format `(cen)` is used.<br>

    - **`sup`**<br>
      the presence of an additional sequence which is not attached to other chromosomal material (i.e. trisomy, marker or ring chromosome) is indicated by `sup` (supernumerary chromosome).<br>
      **NOTE**: changed in ISCN2020. ISCN2016 had: _"add" for additional sequence_.

    - **`::`**<br>
      a double colon is used to designate breakpoint junctions i.e. in creating a ring chromosome.<br>
      **NOTE**: `::` changed in ISCN2020.
      ISCN2016 had: _is used to designate breakpoint junctions involving sequences from different chromosomes (translocation, transposition), chromothripsis breakpoint junctions and junctions creating a ring chromosome_.<br>
      **NOTE**: `::` is in HGVS nomenclature also used to designate adjoined transcripts.

- chromosomal banding patterns are translated to genomic coordinates based the translation tables provided by NCBI (see [Standards](../../background/standards.md#ISCN)).

- in ISCN, it is allowed to describe nucleotide positions using commas to indicate thousands and millions (e.g., "108,111,982"). In HGVS, this is not allowed.

- when the chromosome structure associated with a gain is not known (e.g. insertional location), gains can be described using the copy number in square brackets ("**[ ]**") with "[2]" indicationg one additional copy, "[3]" indicating two additional copies, etc.

- to indicate the sex chromosome complement, the HGVS allele format can be used, adding NC_000023.11:g.[pter_qter=] for the presence of a normal X-chromosome and NC_000024.10:g.[pter_qter=] for the presence of a normal Y-chromosome. For variants in the pseudoautosomal regions where there is uncertainty whether the X or Y chromosome is involved the caret ("^") should be used between the two possible variants.

- **3'rule**<br>
  to determine the location of the breakpoint, the general HGVS rule of maintaining the longest unchanged sequence applies (the 3' rule). Breakpoint location is determined by the first breakpoint encountered, i.e. `pter` of the chromosome is to be listed first.
    - **pter to qter**<br>
      multiple variants in one chromosome are listed in order of occurrence from `pter` to `qter`.
    - variant descriptions are always in the forward orientation (from `pter` to `qter`, the end of the chromosome), determined by the chromosomal origin of the intact centromere (`cen`).

## Examples
<a id="examples"></a>

**The description of translocations has changed.**<br>
In the original proposal (SVD-WG004), **one identical derivative chromosome** would receive **two different descriptions**, depending on whether it was identified in a balanced or an unbalanced case.
In a balanced case, the description would use a "::" format joining the breakpoints, while in an unbalanced case, the description would use a "delins" format.
HGVS recommendations try to avoid such conflicts wherever possible.
HGVS, therefore, recommends to describe translocations exclusively using a "delins" format.

- **Aneuploidy**
    - **`seq (X)x1`**<br>
      **`NC_000023.11:g.pter_qterdel^NC_000024.10:g.pter_qterdel`**<br>
          Sequencing revealed a single X chromosome, and no other sex chromosomes were present in this individual. As with the ISCN abbreviated microarray nomenclature, the specific genome build is not necessary when describing an aneuploidy. The HGVS nomenclature describes the deletion of an X or (**`"^"`**) Y chromosome, as the missing chromosome is unknown.

    - **`seq (13)x3`**<br>
      **`NC_000013.11:g.(pter)_(qter)[2]`**<br>
          Sequencing data shows a gain of chromosome 13 using the abbreviate microarray format. No structural information was detected regarding if the extra copy of the trisomy was associated with a Robertsonian translocation or any other type of structural rearrangement. The HGVS nomenclature indicates that, compared to the reference sequence, there is one additional copy of all chromosome 13 sequences detected (**`“[2]”`**).
          **NOTE**:  **`"dup"`** or **`"sup"`** are not used in this circumstance because the nature of the abnormality is not known.<br>

    - **`47,XY,+13.seq (13)×3`**<br>
      **`NC_000013.11:g.pter_qtersup`**<br>
          Conventional karyotype analysis and sequencing data show a gain of chromosome 13 associated with trisomy 13. The HGVS nomenclature indicates there is one additional copy of chromosome 13 (**`"sup"`**) compared to the reference sequence. ISCN and HGVS strings both indicate that the additional copy number is associated with a supernumerary chromosome 13, confirmed by the karyotype.

    - **`seq[GRCh38] 18p11.32p11.21(158,684_14,853,925)×4`** or **`seq (18p)×4`**<br>
      **`NC_000018.10:g.(pter_158684)_(14853925_?)[3]`**<br>
          Sequencing data shows four copies of the short arm of chromosome 18. No structural information was determined, and it is unknown if the additional copies of 18p are associated with an abnormal chromosome (e.g., supernumerary isochromosome 18p) or present in tandem. The ISCN short microarray format or abbreviated microarray format can be used to describe the variant. HGVS nomenclature describes this finding as the detection of two additional copies (**`"[3]"`**) of all chromosome 18 sequences detected between positions g.158684 and g.14853925.<br>
          **NOTE**: **`"dup"`** or **`"sup"`** are not used in this circumstance because the nature of the abnormality is not known.

    - **`seq (X)x3`**<br>
      **`NC_000023.11:g.[(pter)_(qter)[2]];[pter_qter=]`**<br>
          Sequencing data shows three copies of the X chromosome using the abbreviated microarray format. There are no copies of the Y chromosome indicated, suggesting this individual’s sex chromosome composition is XXX. HGVS nomenclature indicates that, compared to the reference sequence, there is one additional copy of all chromosome X sequences detected (**`"[2]"`**). The “Allele” format used indicates that also one normal copy of an X-chromosome was detected, for a total of three chromosome X.<br>
          **NOTE**: **`"sup"`** is not used in this circumstance because the nature of the abnormality is not known.
      
    - **`47,XXX.seq (X)×3`**<br>
      **`NC_000023.11:g.[pter_qter=];[pter_qter=];[pter_qtersup]`**<br>
          Conventional karyotype analysis and sequencing data shows three copies of the X chromosome, associated with an 47,XXX karyotype. HGVS nomenclature indicates that three chromosome X sequences were detected, two normal (**`"="`**) and one additional copy [**`"sup"`**].

    - **`seq (X)×2,(Y)×1`**<br>
      **`[NC_000023.11:g.(pter)_(qter)[2]];[NC_000024.10:g.pter_qter=]`**<br>
          Sequencing data shows two copies of all X chromosome sequences, and one copy of all Y chromosome sequences. The copy number state of both the X and Y are explicitly stated using abbreviated microarray format to clarify the sex chromosome complement of this individual. HGVS nomenclature indicates that one additional copy of all X chromosome sequences was detected (**`"[2]"`**) with one copy of all chromosome Y sequences (NC_000024.10:g.pter_qter=).<br>
          **NOTE**: **`"sup"`** is not used in this circumstance because the nature of the chromosome X abnormality is not known.

    - **`seq (X)×1,(Y)×2`**<br>
      **`[NC_000023.11:g.pter_qter=];[NC_000024.11:g.(pter)_(qter)[2]]`**<br>
          Sequencing data shows one copy of all X chromosome sequences, and two copies of all Y chromosome sequences. The copy number state of both X and Y are stated using abbreviated microarray format to clarify the sex chromosome complement of this individual. HGVS nomenclature indicates that a normal copy of all chromosome X sequences was detected (NC_000023.11:g.pter_qter=) and an extra copy of all Y chromosome sequences (**`"[2]"`**).<br>
          **NOTE**: **`"sup"`** is not used in this circumstance because the nature of the chromosome Y abnormality is not known.

    - **`seq (X)×1[0.6]`**<br>
      **`NC_000023.11:g.[pter_qter=];[pter_qter=/del]`**<br>
          Sequencing data shows mosaicism for monosomy X in 60% of the DNA sample using abbreviated microarray format. The normal state is implied to be XX in this individual. HGVS nomenclature indicates there is a normal chromosome X copy (**`"="`**) and a copy with a mosaic loss of the entire X chromosome (**`"=/del"`**) detected. In HGVS nomenclature the mosaicism percentage is not indicated.


- **Sequence-based nomenclature for description of large structural variation/copy number variation**
    - **deletion**
        - **`seq[GRCh38] del(10)(p15.3)dn`**<br>
          **`NC_000010.11:g.(pter)_2944337del`**<br>
          The ISCN short karyotype format describes a de novo terminal deletion of the short arm of chromosome 10 with a breakpoint in 10p15.3. The short karyotype format is used to indicate that no additional structural variation was associated with this terminal deletion. The breakpoints for the deletion are indicated in the HGVS portion of the nomenclature. The deletion includes the start of chromosome 10 (pter) to nucleotide 2,944,337. In this case, since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.

        - **`seq[GRCh38] 10p15.3(46,696_1,737,263)×1dn`**<br>
          **`NC_000010.11:g.(pter_46696)_(1737263_?)del`**<br>
          The ISCN short microarray format describes a de novo terminal deletion of the short arm of chromosome 10 with a breakpoint in 10p15.3 using a relative copy-number detection methodology (e.g., targeted short-read NGS sequencing) where the neither the precise breakpoint nor structural information were determined. The deletion involves the region 46,696 to 1,737,263 and the uncertainty range is not specified. This deletion is likely terminal, but the nomenclature describes only the region of the chromosome that was assayed for copy number, similar to array nomenclature. HGVS nomenclature indicates that the deletion is likely terminal, with the use of **`"pter"`** for the 5′ breakpoint, and the use of a question mark (**`"?"`**) for the undefined 3′ breakpoint.

        - **`seq[GRCh38] 10p15.3(46696_1737263×13067438×2)dn`**<br>
          **`NC_000010.11:g.(pter_46696)_(1737263_3067438)del`**<br>
          The ISCN extended microarray format describes a de novo terminal deletion of the short arm of chromosome 10 with a breakpoint in 10p15.3 using a relative copy-number detection methodology from a targeted capture assay (e.g., exome sequencing), where neither the precise breakpoint nor structural information was detected. The deletion involves the most distal targeted region assayed (46,696) and is likely a terminal deletion. The uncertainty region for the proximal breakpoint corresponds to the region between the end of the deleted region (1,737,263) and the next neighboring region assayed that demonstrated normal copy number (3,967,438).<br>
          **NOTE**: delimiting commas are not used in the extended microarray format. Since the ISCN and HGVS strings indicate similar information, either ISCN or HGVS nomenclature can be used.

        - **`seq[GRCh38] 22q11.21(18,891,533_21,111,169)×1pat`**<br>
          **`NC_000022.10:g.(?_18891533)_(21111169_?)del`**<br>
          The ISCN short microarray format describes a paternally inherited interstitial deletion within 22q11.2, consistent with the recurrent 22q11.2 deletion syndrome (LCR-A to LCR-D). The precise deletion breakpoint was not detected and the uncertainty region is not determined due to limitations of the assay. Since the ISCN and HGVS strings indicate similar information, either ISCN or HGVS nomenclature can be used.

        - **`seq[GRCh38] 22q11.21(18164049×2,18891533_21111169×1,22556921×2)pat`**<br>
          **`NC_000022.10:g.(18164049_18891533)_(21111169_22556921)del`**<br>
          The ISCN extended microarray format describes a paternally inherited interstitial deletion within 22q11.2, consistent with the recurrent 22q11.2 deletion syndrome (LCR-A to LCR-D). The precise breakpoint was not detected as the breakpoints appear to fall within repetitive regions of the genome. The uncertainty region for the proximal breakpoint corresponds to segmental duplication regions between 18,164,049 and 18,891,533, with the distal breakpoint between 21,111,169 and 22,556,921.
          **NOTE**: delimiting commas are not used in the extended microarray format. Since the ISCN and HGVS strings indicate similar information, either ISCN or HGVS nomenclature can be used.

        - **`seq[GRCh38] X,del(X)(q21.31q22.1)`**<br>
          **`NC_000023.11:g.89555676_100352080del`**<br>
          The ISCN short karyotype format describes a heterozygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 in an XX individual. The normal X is indicated in the ISCN portion to clarify the sex chromosome complement. The use of the short karyotype format indicates the deletion is interstitial and is not associated with any other structural rearrangements. The HGVS portion of the joint nomenclature indicates that the deletion includes the segment from nucleotide 89,555,676 to nucleotide 100,352,080, with nucleotides 89,555,675 to 100,352,081 now joined. Since both the breakpoint and structural information is known for this deletion, both the ISCN and HGVS strings are required.

        - **`seq[GRCh38] Xq21.31q22.1(91,435,563_100,342,090)×1`**<br>
          **`NC_000023.11:g.[pter_qter=];[(?_91435563)_(100342090_?)del]`**<br>
          The ISCN short microarray format describes a heterozygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 where the neither the precise breakpoint nor related structural information was detected. The minimal deletion includes the segment from nucleotide 91,435,563 to nucleotide 100,342,090, and the uncertainty region is not defined. This deletion is inferred to be present in an XX individual. The HGVS description indicates that the extent of the deleted region is not known with the use of question marks **`"(?)"`**. In order to indicate deletion was seen in the heterozygous state in an XX individual, the normal sex chromosome is indicated by using the “Allele” format (**`"[pter_qter=]"`**).

        - **`seq[GRCh38] Xq21.31q22.1(88753400×2,91435563_100342090×1,100402866×2)`**<br>
          **`NC_000023.11:g.[pter_qter=];[(88754300_91435563)_(100342090_100402866)del]`**<br>
          The ISCN extended microarray format describes a heterozygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 in an XX individual, where neither the precise breakpoint nor related structural information was detected. The minimal deletion includes the segment from nucleotide 91,435,563 to nucleotide 100,342,090. The extended microarray format indicates the neighboring proximal and distal targeted regions that show normal copy number (two copies). As the extended microarray format indicates the normal copy is two for the X chromosome, and there is no indication of the presence of a Y, this individual can be inferred to have two X chromosomes, one with a deletion. The HGVS string indicates that there is an interstitial deletion of the X chromosome with the 5′ end breakpoints between 88,754,300 and 91,435,563 and the 3′ end breakpoints between 100,342,090 and 100,402,866. In order to indicate deletion was seen in the heterozygous state in an XX individual, the normal sex chromosome is indicated by using the “Allele” format (**`"[pter_qter="]`**).

        - **`seq[GRCh38] Y,del(X)(q21.31q22.1)`**<br>
          **`NC_000023.11:g.89555676_100352080del`**<br>
          The ISNC short karyotype format describes a hemizygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 in an XY individual. The use of the karyotype format indicates that the deletion is interstitial and is not associated with any other structural rearrangements. The HGVS portion of the nomenclature indicates that the deletion includes the segment from nucleotide 89,555,676 to nucleotide 100,352,080, with nucleotides 89,555,675 to 100,352,081 now joined. Since both the breakpoint and structural information is known for this deletion, both the ISCN and HGVS strings are required.

        - **`seq[GRCh38] (Y)×1,Xq21.31q22.1(91,435,563_100,342,090)×0`**<br>
          **`[NC_000023.11:g.(?_91435563)_(100342090_?)del];[NC_000024.10:g.pter_qter=]`**<br>
          The ISCN short format describes a hemizygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 where neither the precise breakpoint nor related structural information was detected. The minimal deletion includes the segment from nucleotide 91,435,563 to nucleotide 100,342,090, and the uncertainty region is not defined. This deletion of the X chromosome is found in an XY individual, as indicated by the presence of one copy of the Y chromosome. This is to distinguish that this deletion was not found in the homozygous state in an XX individual, nor was found to be present on the single X chromosome in an 45,X individual. The HGVS string indicates that there is a chromosome X copy with a deletion of an unknown extent using question marks **`"(?)"`** and the presence of one copy of a normal Y chromosome using the “Allele” format (**`"[pter_qter="]`**).

        - **`seq[GRCh38] (Y)×1,Xq21.31q22.1(88753400×1,91435563_100342090×0,100402866×1)`**<br>
          **`[NC_000023.11:g.(88753400_91435563)_(100342090_100402866)del];[NC_000024.10:g.pter_qter=]`**<br>
          The ISCN extended microarray format describes a hemizygous interstitial deletion within the long arm of chromosome X from band Xq21.31 to q22.1 in an XY individual, where neither the precise breakpoint nor related structural information was detected. The deletion includes the segment from nucleotide 91,435,563 to nucleotide 100,342,090. The extended microarray format indicates the neighboring proximal (88,753,400) and distal (100,342,090) targeted regions that show normal copy number (1 copy). The nomenclature indicates that there is only one X chromosome in this individual, and the indication of the Y copy number clarifies that this finding is in the context of an XY individual. The HGVS string indicates that there is an interstitial deletion of the X chromosome with the 5‘ end breakpoints between 88,754,300 and 91,435,563 and the 3‘ end breakpoints between 100,342,090 and 100,402,866. In order to indicate the zygosity of the deletion, the “Allele” format is used.

        - **`seq[GRCh38] del(X)(q21.31q22.1),del(X)(q21.31q22.1)`**<br>
          **`NC_000023.11:g.[89555676_100352080del];[89555676_100352080del]`**<br>
          The ISCN short karyotype format portion of the nomenclature indicates that an XX individual has identical (homozygous) deletions involving both X chromosomes. The karyotype format indicates that no additional structural rearrangements were associated with the interstitial deletions. Alternatively, the ISCN portion could be written: seq[GRCh38] del(X)(q21.31q22.1)x2. The HGVS portion of the nomenclature indicate that identical interstitial deletions within the long arms of both X chromosomes from band Xq21.31 to band Xq22.1 involving the region from nucleotide 89,555,676 to nucleotide 100,352,080. In the HGVS portion each allele is described between square brackets (**`"[89555676_100352080del]"`**), separated by a semicolon (**`";"`**) to indicate the variants are in trans. Since both the breakpoint and structural information is known for these deletions, both the ISCN and HGVS strings are required.

       - **`seq[GRCh38] Xq21.31q22.1(88753400×2,91435563_100342090×0,100402866×2)`**<br>
         **`NC_000023.11:g.[(88753400_91435563)_(100342090_100402866)del];[(88753400_91435563)_(100342090_100402866)del]`**<br>
         The ISCN extended microarray format describes an interstitial homozygous deletion within the long arm of chromosome X from band Xq21.31 to q22.1, where neither the precise breakpoint nor structural information was detected. The homozygous deletion includes the segment from nucleotide 91,435,563 to nucleotide 100,342,090. The extended microarray format indicates the neighboring proximal and distal targeted regions show normal copy number (2 copies), indicating this homozygous deletion was observed in an XX individual. HGVS nomenclature describes each allele between square brackets (**`"[ ]"`**), separated by a semicolon (**`";"`**) to indicate the variants are in trans. Since the ISCN and HGVS strings indicate similar information, either ISCN or HGVS nomenclature can be used.

       - **`seq[GRCh38] del(X)(q21.31q22.1),del(X)(q21.31q22.1)`**<br>
         **`NC_000023.11:g.[89555674_100352088del];[90111276_99878726del]`**<br>
         The ISCN short karyotype format portion indicates than an XX individual has both X chromosomes deleted from band Xq21.31 to band Xq22.1; however, from the HGVS nomenclature portion, these deletions are not identical and are associated with compound heterozygous interstitial deletions (in trans) within the long arms of both X chromosomes. The deletions include the segment from nucleotide 89,555,674 to 100,352,088 on one homologue, and from nucleotide 90,111,276 to 99,878,726 on the other homologue. In the HGVS portion each allele is described between square brackets (**`"[ ]"`**), separated by a semicolon (**`";"`**) to indicate the variants are in trans. Since both the breakpoint and structural information is known for these deletions, both the ISCN and HGVS strings are required.

       - **`seq[GRCh38] del(X)(p22.3p22.3) or del(Y)(p11.32p11.2)`**<br>
         **`NC_000023.11:g.320651_666265del^NC_000024.10:g.320651_666265del`**<br>
         The ISCN short karyotype format portion of the nomenclature describes an interstitial deletion within the pseudoautosomal region 1 (PAR1) in an XY individual, which is consistent with either a heterozygous interstitial deletion within the short arm of chromosome X within band p22.3, or with a heterozygous interstitial deletion within the short arm of chromosome Y within band p11.2. The HGVS nomenclature describes the deletion in both X or (**`"^"`**) Y chromosome and includes the segment from nucleotide 32,065 to nucleotide 666,265. Since both the breakpoint and structural information is known for these deletions, both the ISCN and HGVS strings are required.

       - **`seq[GRCh38] 12q21.32(88534851_88545966)×0mat pat`**<br>
         **`NC_000012.12:g.[(?_88534851)_(88545966_?)del];[(?_88534851)_(88545966_?)del]`**<br>
         The ISCN short microarray format indicates an intragenic, homozygous loss is detected in the KITLG gene on chromosome 12. Neither the precise breakpoint nor structural information was detected, and the breakpoint uncertainty range is specified. The homozygous deletion includes the segment between nucleotides 88,534,851, and 88,545,966, and the uncertainty range is not specified. Both parents are known heterozygous carriers of this deletion. The HGVS nomenclature describes each allele between square brackets (**`"[ ]"`**), separated by a semicolon (**`";"`**) to indicate the variants are in trans.

       - **`seq[GRCh38] 12q21.32(88530089×2,88534851_88545966×0, 88580216×2)mat pat`**<br>
         **`NC_000012.12:g.[(88530089_88534851)_(88545966_88580216)del];[(88530089_88534851)_(88545966_88580216)del]`**<br>
         The ISCN extended microarray format indicates an intragenic, homozygous loss is detected in the KITLG gene on chromosome 12. Neither the precise breakpoint nor structural information was detected, and the breakpoint uncertainty range is specified. The homozygous deletion includes the segment between nucleotides 88,530,089 to 88,534,851, and 88,545,966 to 88,580,216. The extended microarray format indicates the neighboring proximal and distal targeted regions show normal copy number (2 copies). Both parents are known heterozygous carriers of this deletion. The HGVS nomenclature describes each allele between square brackets (**`"[ ]"`**), separated by a semicolon (**`";"`**) to indicate the variants are in trans.

        - **`seq[GRCh38] 1p22.3(86092388×2,86112508_86915211×1,86993002×2)dn,1q31.3q32.1(193249904×2,196228171_200650737×1,200658989×2)dn,2q33.1q34(201145490×2,201148901_208572138×1,209653108×2)dn`**<br>
         **`NC_000001.11:g.[(86092388_86112508)_(86915211_86993002)del](;)[(193249904_196228171)_(200650737_200658989)del]<br>
         NC_000002.12:g.(201145490_201148901)_(208572138_209653108)del`**<br>
         The ISCN extended microarray format describes three de novo interstitial losses are detected by read-depth calling where the precise breakpoint nor structural information was detected. These three heterozygous deletions include a loss of approximately 800kb in 1p22.3, a loss of approximately 4.4Mb in 1q31.3q32.1, and a loss of approximately 7.4Mb in 2q33.1q34. As no precise breakpoints or structural information was obtained from this analysis, it cannot be determined if these findings could be associated with a larger structural rearrangement, such as a translocation or pericentric inversion. The HGVS nomenclature describes the deletions on chromosome 1 on one line, with the use of (**`";"`**) to indicate that is it not known if the two deletions are in cis (same chromosome) or in trans (different chromosomes). The deletion on chromosome 2 is described on a separate line.

    - **duplication and triplication**
        - **`seq[GRCh38] dup(18)(q23q23)`**<br>
          **`NC_000018.10:g.79670244_79724961dup`**<br>
          The ISCN short karyotype format portion of the nomenclature describes a tandem duplication of sequences within chromosome 18q23. Note: because the duplication is within a single chromosome band, the ISCN nomenclature cannot distinguish the orientation of the duplicated material. The HGVS portion indicates the 54.7kb tandem duplication within chromosome 18 involves nucleotides 79,670,244 to 79,724,961.<br>
          **NOTE**: in HGVS (**`"dup"`**) (duplication) can only be used when the duplicated sequence is in tandem and in the same orientation as the reference sequence. Since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.

        - **`seq[GRCh38] dup(18)(q23q23)`**<br>
          **`NC_000018.10:g.79670243_79670244ins79670244_79724961inv`**<br>
          There is a 54.7kb duplication within chromosome band 18q23, and the ISCN short karyotype format cannot distinguish the orientation of the duplicated sequences. The HGVS nomenclature portion indicates that, compared to the reference sequence, the genomic region 79,670,244 to 79,724,961 is inserted in an inverted orientation between nucleotides 79,670,243 and 79,670,244 (i.e., proximal of the reference copy). Since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.

        - **`seq[GRCh38] dup(18)(q23q23)`**<br>
          **`NC_000018.10:g.79724961_79724962ins79670244_79724961inv`**<br>
          There is a 54.7kb duplication within chromosome band 18q23, and the ISCN short karyotype format cannot distinguish the orientation of the duplicated sequences. The HGVS description indicates the genomic region 79,670,244 to 79,724,961 is inserted in an inverted orientation between nucleotides 79,724,961 and 79,724,962 (i.e., distal of the reference copy). Since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.
          
        - **`seq[GRCh38] 18q23(79,679,933_79,718,031)×3`**<br>
          **`NC_000018.10:g.(?_79679933)_(79718031_?)[2]`**<br>
          The ISCN short microarray format indicates a duplication (three copies) of a part of chromosome band 18q23; however, the methodology used could not determine the insertion location or orientation of the duplicated sequence. The duplication includes the segment from nucleotide 79,679,933 to nucleotide 79,718,031, and the uncertainty region is not specified. The HGVS string describes that there is an additional copy (“[2]”) of the reference sequence of chromosome 18 between 79,679,933 to nucleotide 79,718,031.<br>
           **NOTE**: **`"dup"`**, **`"sup"`**, and **`"delins"`** cannot be used and should not be assumed, as the insertional location and orientation of the duplicated sequences has implications on classification, interpretation, and recurrence risk.
                 
        - **`seq[GRCh38] 18q23(79527592×2,79679933_79718031×3,79728892×2)`**<br>
          **`NC_000018.10:g.(79527592_79679933)_(79718031_79728892)[2]`**<br>
          The ISCN extended microarray format indicates a duplication (3 copies) of a part of chromosome band 18q23; however, the methodology used could not determine the insertion location or orientation of the duplicated sequence. The duplication includes the segment from nucleotide 79,679,933 to nucleotide 79,718,031. The extended microarray format indicates the neighboring proximal and distal targeted regions that show normal copy number (two copies). The HGVS string indicates that, compared to the reference sequence, there is an additional copy (**`"[2]"`**) of the chromosome 18 sequence between nucleotides 79,527,592 to 79,679,933 and 79,718,031 to 79,728,892.<br>
           **NOTE**: **`"dup"`**, **`"sup"`**, and **`"delins"`** cannot be used and should not be assumed, as the insertional location and orientation of the duplicated sequences has implications on classification, interpretation, and recurrence risk.

        - **`seq[GRCh38] 16p11.2(29,604,826_30,188,489)×3`**<br>
          **`NC_000016.10:g.(?_29604826)_(30188489_?)[2]`**<br>
          The ISCN abbreviate microarray format indicates a duplication (three copies) of material from chromosome band 16p11.2 which is consistent with the proximal recurrent duplication of 16p11.2 (BP4-BP5); however, the methodology used could not determine the insertion location or orientation of the duplicated sequence. The duplication includes the segment from nucleotide 29,604,826 to 30,188,489 and the uncertainty region is not specified. The HGVS string describes that, compared to the reference sequence, there is an extra copy (**`"[2]"`**) of the chromosome 16 sequence. <br>
           **NOTE**: **`"dup"`**, **`"sup"`**, and **`"delins"`** cannot be used and should not be assumed, as the insertional location and orientation of the duplicated sequences has implications on classification, interpretation, and recurrence risk.

        - **`seq[GRCh38] 16p11.2(29410365×2,29604826_30188489×3,30335398×2)`**<br>
          **`NC_000016.10:g.(29410365_29604826)_(30188489_30335398)[2]`**<br>
          The ISCN extended microarray format indicates a duplication chromosome band 16p11.2 which is consistent with the proximal recurrent duplication of 16p11.2 (BP4-BP5); however, the methodology used could not determine the insertion location or orientation of the duplicated sequence. The duplication includes the segment from nucleotide between 29,410,365 to 29,604,826 and 30,188,489 to 30,335,398. The HGVS string describes that, compared to the reference sequence, there is an additional copy (“[2]”) (**`"[2]"`**) of the chromosome 16 sequence. <br>
           **NOTE**: **`"dup"`**, **`"sup"`**, and **`"delins"`** cannot be used and should not be assumed, as the insertional location and orientation of the duplicated sequences has implications on classification, interpretation, and recurrence risk.

        - **`47,XY,+dic(15;15)(q13;13).seq[GRCh38] 15q11.2q13.1(22572598_28318712×4,28724458×2)`**<br>
          **`NC_000015.10:g.[(pter_22572598)_(28318712_28724458);(pter_22572598)_(28318712_28724458)inv]sup`**<br>
          The combined ISCN short karyotype and extended microarray format indicates four copies of the proximal (centromeric) region of the long arm of chromosome 15 associated with a supernumerary chromosome. The copy number change was detected by sequencing read-depth algorithms, and the precise breakpoint and structural information was not detected by this assay. Only in combination with the karyotype data is the nature of the extra copies of this region confirmed to be associated with a dicentric supernumerary chromosome, composed of inverted copies of the pter to q13.1. The region of four copies includes the segment from nucleotide 22,572,598 to 28,318,712 in bands 15q11.2 to 15q13.1; however, the proximal breakpoint is not known as it involves the most proximal region assayed for copy number, while the distal breakpoint occurs in the segmental duplication region between 28,318,712 and 28,724,458. The HGVS string describes a supernumerary chromosome composed of two copies of the short arm of chromosome 15 ((pter_22572598)_(28318712_28724458)) where, compared to the reference sequence, one is in a normal orientation and one is in an inverted orientation. The use of **`"sup"`** indicates that this finding is associated with a supernumerary chromosome, as confirmed by the karyotype.

        - **`seq[GRCh38] der(11)(pter→q22.3::q22.3→q14.3::q14.3→qter`**<br>
          **`NC_000011.10:g.106009182_106009183ins[91466078_106007033inv;91448961_106009182]`**<br>
          The ISCN detailed karyotype format indicates a triplication of 11q14.3 to q22.3, with the middle copy of the triplicated region in an inverted orientation. The HGVS portion indicates that the derivative chromosome involves additional copies of 11q material with two different sizes: one additional copy of a 14.541Mb region involving nucleotides 91,466,078 to 106,007,033 which is inserted in an inverted orientation after position 106,009,182, followed by an additional copy of a 14.560Mb region involving nucleotides 91,448,961 to 106,009,182. Since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.

        - **`seq[GRCh38] 11q14.3(91,448,700_91,465,000)×3,11q14.3q22.3(91,465,500_106,007,000)×4,11q22.3(106,008,600_106,019,700)×3`**<br>
          **`NC_000011.10:g.(?_91448700)_(91465000_91465500)[2](;)(91465500_106007000)[3](;)(106007000_106008600)_(106019700_?)[2]`**<br>
          The ISCN short microarray format indicates a 14.5Mb region of four copies of sequence from chromosome bands 11q14.3q22.3, with two smaller regions of three copies of adjacent sequence involving a 16.3kb duplication in 11q14.3, and a 11.1kb duplication in 11q22.3. The methodology used could not determine the exact breakpoints, nor the insertion location or orientation of the regions of copy number gain. The HGVS portion describes, compared to the reference sequence, the detection of one additional copy (“[2]”) of the sequence from 91,448,700 to 91,465,000, two additional copies (**`"[3]"`**) of the sequence from 91,465,500 to 106,007,000, and one additional copy (**`"[2]"`**) of the sequence from 106,008,600 to 106,009,700. The insertional locations and orientations are not known for these gains, as indicated by the use of (**`";"`**) to indicate that is it not known if the gains are in cis (same chromosome) or in trans (different chromosomes).

    - **derivative chromosome**<br>
The following examples describe copy number alterations that are associated with structural rearrangements. If multiple copy number alterations are detected without any structural information, the nomenclature can be written similar to microarray nomenclature, with the copy number alterations listed in numerical order. For complex findings, including chromothripsis, chromoanasynthesis, or other complexities that would result in a prohibitive number of abnormalities to describe in one nomenclature string, the microarray format for complex findings may be used (see Section 8.2.7 for examples).
   
        - **`seq[GRCh38] der(2)t(2;11)(p25.1;p15.2)`**<br>
          **`NC_000002.12:g.pter_8247756delins[NC_000011.10:g.pter_15825272]`**<br>
          The ISCN portion of the nomenclature describes a derivative chromosome 2 from an unbalanced translocation between the short arms of chromosomes 2 and 11. The breakpoints of the translocation are described in the HGVS portion of the nomenclature and occur at 2p25.1 (between nucleotides 8,247,756 and 8,247,757) and 11p15.2 (between nucleotides 15,825,272 and 15,825,273). The **`"delins"`** after the chromosome 2 breakpoints indicates that, compared to the reference sequence, the terminal region from chromosome 2 (2pter to 2p25.1) is deleted and is replaced by the terminal portion of chromosome 11 (11pter to 11p15.2). The HGVS portion of the nomenclature does not explicitly state that this sequence from chromosome 11 is a duplication, but the duplication is implied since there is no derivative 11 described. Since the ISCN and HGVS involve non-duplicative information, both lines should be used to describe the variant.

        - **`seq[GRCh38] 2p25.3p25.1(45,440_7,044,179)×1,11p15.5p15.2(197,297_15,247,208)×3`**<br>
          **`NC_000002.12:g.(pter_45440)_(7044179_?)del`**<br>
          **`NC_000011.10:g.(pter_197297)_(158247208_?)[2]`**<br>
          The ISCN short microarray format describes a terminal deletion of the short arm of chromosome 2 with a breakpoint in 2p25.1 using a relative copy-number detection methodology (e.g., exome sequencing), where the precise breakpoints nor structural information was detected. The deletion involves the first assayed region on the short arm of chromosome 2 (45,440) to 7,044,179. The copy number gain involves the first assayed region of the short arm of chromosome 11 (197,297) to 15,247,208. The uncertainty region of both copy number changes are not indicated.<br>
          **NOTE**: the deletion and duplication are likely terminal, but the nomenclature describes only the region of the chromosome that was assayed for copy number, similar to array nomenclature. The HGVS portion describes two variants: a likely terminal deletion of chromosome 2 sequences, and an additional copy of chromosome 11 sequences. Since no structural information was obtained from the sequencing data, the insertional location of the 11p sequences in unknown.<br>
          **NOTE**: (**`"dup"`**), (**`"sup"`**) and (**`"delins"`**) cannot be used in this circumstance, and it should not be assumed since the insertional location and orientation of the duplicated sequences has implications on classification, interpretation, and recurrence risk.
          
        - **`seq[GRCh38] der(5)t(5;10)(p13.3;q21.3)`**<br>
          **`NC_000005.10:g.pter_29658442delins[NC_000010.11:g.67539995_qterinv]`**<br>
          The ISCN short karyotype format portion of the nomenclature describes a derivative chromosome 5 from an unbalanced translocation between 5p13.3 and 10q21.3. The HGVS portion of the nomenclature describes the deletion of chromosome 5 sequences from pter to nucleotide 29,658,442, which are replaced by chromosome 10 sequences from nucleotides 67,539,995 to qter. Since, compared to the reference sequence, the orientation of the chromosome 10 sequences is inverted, **`"inv"`** is used to indicate the change in orientation. The ISCN and HGVS nomenclature portions involve non-duplicative information, and both should be used to describe the variant.

        - **`seq[GRCh38] der(2)t(2;13)(q37.2;q31.1)`**<br>
          **`NC_000002.12:g.235100310_qterdelins[NC_000013.11:g.85862019_qter]`**<br>
          The ISCN short karyotype format portion of the nomenclature describes a derivative chromosome 2 from an unbalanced translocation between 2q37.2 and 13q31.1. The HGVS portion describes the terminal deletion of chromosome 2 sequences from nucleotide 235,100,310 to qter, which are replaced by terminal chromosome 13 sequences from nucleotides 85,862,019 to qter. Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant.

        - **`seq[GRCh38] der(9)t(9;10)(q34.3;p15.3)`**<br>
          **`NC_000009.12:g.137175878_qterdelins[NC_000010.11:g.pter_2944334inv]`**<br>
          The ISCN portion of the nomenclature describes a derivative chromosome 9 from an unbalanced translocation between 9q34.3 and 10p15.3. The HGVS portion describes the absence of the sequences from nucleotide 137,175,878 to the q terminus of chromosome 9, which is replaced by nucleotides pter to 2,944,334 from chromosome 10. The **`"inv"`** is used since, compared to the reference sequence, the orientation of the chromosome 10 sequences is inverted. The ISCN and HGVS nomenclature portions involve non-duplicative information, and both should be used to describe the variant.

        - **`seq[GRCh38] der(3)(3pter→3q25.32::8q24.21→8qter)`**<br>
          **`NC_000003.12:g.158573187_qterdelins[NC_000008.11:g.(128534000_128546000)_qter]`**<br>
          The ISCN detailed karyotype format portion describes a derivative chromosome 3 from a translocation between the long arms of chromosomes 3. The breakpoint in chromosome 3 is between nucleotides 158,573,186 and 158,573,187, while the breakpoint in chromosome 8 is uncertain (as shown by the parentheses) and between nucleotides 128,534,000 and 128,546,000. Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant.

        - **`seq[GRCh38] XX,der(4)ins(4;X)(q28.3;q22.1q21.31)`**<br>
          **`NC_000004.12:g.134850793_134850794ins[NC_000023.11:g.(89555676_89556012)_(100351998_100352080)inv]`**<br>
          The ISCN short karyotype format describes an unbalanced interchromosomal insertion with duplicated X chromosome sequences inserted into the long arm of chromosome 4 in an XX individual. The inserted sequence from the X chromosome is inverted in orientation relative to the chromosome X reference sequence. Sequence data indicates the site of the insertion in chromosome 4 between 134,850,793 to 134,850,794. The duplicated X chromosome sequences has uncertain breakpoints, between 89,555,676 to 89,556,012 and 100,351,998 to 100,352,080. This duplicated region of X is inserted in an inverted orientation relative to the chromosome X reference sequence. In the ISCN nomenclature the sex chromosome complement is indicated, as it may help to interpret the clinical significance and clarify the copy number involving the inserted region of the X chromosome. Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant.

        - **`seq[GRCh38] der(6)(6pter→6q14.1::21q22.12→21qter),der(12)(6qter→6q23.2::12p13.2→12qter),der(21)(21pter→21q22.12::12p13.2→12pter)`**<br>
          **`NC_000006.11:g.78952474_qterdelins[NC_000021.8:g.35039585_qter]`**<br>
          **`NC_000012.11:g.pter_11878386delins[NC_000006.11:g.132514527_qterinv]`**<br>
          **`NC_000021.8:g.35042090_qterdelins[NC_000012.11:g.pter_11878495inv]`**<br>
          Sequencing shows a complex rearrangement between chromosomes 6, 12, and 21 resulting in three derivative chromosomes described using the ISCN detailed (karyotype) format in combination with the HGVS nomenclature to describe the sequence breakpoints. The HGVS description indicates that, compared to the reference sequence, there are deletions of 53Mb on chromosome 6 (nucleotides 78,952,474 to 132,514,527), 109bp on chromosome 12 (nucleotides 11,878,386 to 11,878,495), and 2.5kb on chromosome 21 (nucleotides 35,042,090 to 35,039,585). The deleted regions for each of the derivative chromosomes (e.g., 78,952,474 to qter for the deleted region of chromosome 6) are larger than the inserted regions (e.g., 132,514,527 to qter for the inserted region of chromosome 6). Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant.

        - **`seq[GRCh38] der(6)t(6;13)(q14.3;q31.1),der(13)t(6;13)(q14.3;q31.1)inv(6)(q14.3q14.3)del(6)(q14.3q14.3)del(6)(q14.3q16.1)`**<br>
          **`NC_000006.12:g.85897871_qterdelins[A;NC_000013.11:g.80659609_qter]`**<br>
          **`NC_000013.11:g.80659607_qterdelins[NC_000006.12:g.[85897899_85900540inv;85900541_86488291;93909933_qter]]`**<br>
          A complex rearrangement between chromosomes 6 and 13 is described using the ISCN short karyotype format in combination with the HGVS nomenclature to indicate the breakpoints. The derivative 6 involves a single base pair (A) inserted at the breakpoint between positions 85,897,871 on chromosome 6q14.3 and position 80,659,609 on chromosome 13q31.1. The derivative 13 is more complicated with an inversion and deletion within the chromosome 6 sequences that have been translocated to the derivative chromosome 13. The chromosome 6 sequences now located on the derivative 13 involves a 2.6kb inversion within 6q14.3 (85,897,899 to 85,900,540) in addition to a 7.4Mb deletion (86,488,292 to 93,909,932) of chromosome 6q14.3 to q16.1. In addition to the large chromosome 6 deletion, there are a 2bp deletion of chromosome 13 sequences (80,659,607 to 80,659,608) and a 28bp deletion (85,897,871 to 85,897,898) of chromosome 6 sequences at the break points. Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant. 

        - **`seq[GRCh38] der(5)ins(5;?)(q22.1;?)`**<br>
          **`NC_00005.10:g.112173754_112173755insN[696]`**<br>
          The ISCN short karyotype format describes the insertion of unknown sequences into the long arm of chromosome 5 at band 5q22.1. The HGVS portion describes the insertion of 696 nucleotides that are not specified (**`insN[696]`**) into chromosome 5 between nucleotides 112,173,754 and 112,173,755. Since the ISCN and HGVS nomenclature portions involve non-duplicative information, both should be used to describe the variant.

        - **`seq[GRCh38] Xp22.31p22.31(276,356_6,383,977)×1,Xp22.31q28(7,050,341_156,010,409)×2,Yp11.32q12(276,356_9,547,294)×1,Yq12(10,266,944_56,961,317×0)`**<br>
          **`NC_000023.11:g.(pter_276356)_(6383977_7050341)=(;)(6383977_7050341)_(156010409_qter)[2]`**<br>
          **`NC_000024.10:g.(9547294_10266944)_(56961317_qter)delg.?-?insNC_000024.10:g.(pter_276356)_(9547294_10266944)`**<br>
          The ISCN short microarray format describes copy number findings involving the X and Y chromosome using a read-depth based algorithm. The precise breakpoints are not indicated due to the technical limitations of the method, and no structural information is known. One copy of the distal end of the short arm of the X chromosome from 276,356 to 6,383,977 is present, with two copies for the remainder of the X chromosome (7,050,341 to 156,010,409). There is also one copy of the distal end of the short arm of the Y chromosome which includes the SRY gene (276,356 to 9,547,294); the rest of the Y chromosome is absent (10,266,944 to 56,961,317). Follow-up testing using routine cytogenetic analysis, FISH, genome mapping, or sequencing across the breakpoints is essential to confirm any associated structural alterations associated with these copy number findings, such as 46,X,der(X)t(X;Y)(p22.31;p11.2). As the precise breakpoints, phase, and structural information is unknown, the HGVS nomenclature describes each finding on a separate line, indicating which regions have normal copy number, and which regions have either additional copy of the reference (X chromosome) or are deleted (Y chromosome).

        - **`seq[GRCh38] 14q31.3q32.33(82692819×2,85528649_104180813×3,104244199×2),14q32.33(105771415×2,105837032_106881350×1)`**<br>
          **`NC_000014.9:g.(82692819_85528649)_(104180813_104244199)[3](;)(105771415_105837032)_(106881350_pter)del`**<br>
          The ISCN extended microarray format describes two imbalances in chromosome 14: an interstitial gain of approximately 18.6Mb of 14q31.3q32.33 from 85,528,649 to 104,180,813 and a terminal loss of approximately 1.2Mb of 14q32.33 from 105,837,032 to 106,881,350. A normal copy number (two copies) is found for the region of approximately 1.5Mb between these two imbalances (104,244,199 to 105,771,415). The insertional location and orientation of the duplication is not known, nor if the deletion and duplication involve the same homologue. Follow-up testing using routine cytogenetic analysis or FISH is essential to confirm the structural nature of the imbalance. The HGVS nomenclature describes the gain of the chromosome 14 sequences and the terminal deletion with uncertain phase using a semicolon in parenthesis (**`"(;)"`**).


    - **ring chromosomes**
        - **`seq[GRCh38] r(8)(p23.2q24.3)`**<br>
          **`NC_000008.11:g.(pter)_3300105del::139535561_(qter)del`**<br>
          The combined ISCN short karyotype format and HGVS nomenclature describes a ring chromosome derived from chromosome 8 with breakpoints at band p23.2 and q24.3 joining nucleotide 3,300,105 to nucleotide 139,535,561. Both termini of the ring chromosome are associated with deletions. If the structural information was not known, this finding should be described as two deletions with unknown phase (see Section 11.5.1).

        - **`47,XY,+mar.seq[GRCh38] +r(8)(p23.2q24.3)`**<br>
          **`NC_000008.11:g.3300106_139535560sup`**<br>
          A combined karyotype and sequence assay describes a supernumerary ring derived from chromosome 8 with breakpoints at band p23.2 and q24.3 joining nucleotide 3,300,106 to nucleotide 139,535,560. If the structural information was not known, this supernumerary ring chromosome should be described as a duplication of 3,300,105 to 139,535,561 using [2] (see Section 11.5.2).


    - **insertions**
        - **`seq[GRCh38] X,ins(4;X)(q28.3;q21.31q22.1)`**<br>
          **`NC_000023.11:g.89555676_100352080del`**<br>
          **`NC_000004.12:g.134850793_134850794ins[NC_000023.11:g.89555676_100352080]`**<br>
          The combined ISCN and HGVS nomenclature describes a balanced interchromosomal insertion of chromosome X long arm sequences (nucleotides 89,555,676 to 100,352,080) into the long arm of chromosome 4 (between nucleotides 134,850,793 and 134,850,794) in an XX individual. The inserted sequence from the X chromosome is in the same orientation as the reference sequence. The sex chromosome complement is indicated in the ISCN portion, as the sex chromosome complement can help to interpret the clinical significance and clarify the zygosity of the X chromosome abnormality.

        - **`seq[GRCh38] X,ins(4;X)(q28.3;q22.1q21.31)**<br>
          **`NC_000023.11:g.89555676_100352080del`**<br>
          **`NC_000004.12:g.134850793_134850794ins[NC_000023.11:g.89555676_100352080inv]`**<br>
          The combined ISCN and HGVS nomenclature describes a balanced interchromosomal insertion of chromosome X long arm sequences (nucleotides 89,555,676 to 100,352,080) into the long arm of chromosome 4 (between nucleotides 134,850,793 and 134,850,794) in an XX individual. The inserted sequence from the X chromosome is inverted in orientation relative to the reference sequence. The sex chromosome complement is indicated in the ISCN portion, as the sex chromosome complement can help to interpret the clinical significance and clarify the zygosity of the X chromosome abnormality.

        - **`seq[GRCh38] ins(3)(pter→q23::q24→q26.32::q24→q23::q26.32→qter)**<br>
          **`NC_000003.10:g.[139122717_146206645del;177128243_177128245delins[139122717_146206645inv;AA]]`**<br>
          The combined ISCN and HGVS nomenclature describes an intrachromosomal balanced insertion involving a 7.1Mb region within chromosome 3q23q24 (139,122,717 to 146,206,645) inserted into 3q26.32 (between position 177,128,243 and 177,128,245) in an inverted orientation. There is a single base deletion (177,128,244), and an insertion of two bases (AA) at the insertion breakpoint.


    - **inversions**
        - **`seq[GRCh38] inv(6)(pter→p25.3::q16.1→p25.3::q16.1→qter)`**<br>
          **`NC_000006.12:g.[776788_93191545inv;93191546T>C]`**<br>
          The combined ISCN and HGVS nomenclature describes a pericentric inversion of chromosome 6 using the detailed karyotype format in the ISCN portion. The inversion involves 776,788 to 93,191,545 with a T to C nucleotide substitution at the breakpoint (nucleotide 93,191,546).

        - **`seq[GRCh38] inv(2)(pter→p22.3::q31.1→p22.3::q31.1→qter)dn`**<br>
          **`NC_000002.12:g.[32310435_32310710del;32310711_171827243inv;171827243_171827244insG]`**<br>
          The combined ISCN and HGVS nomenclature describes a de novo pericentric inversion in chromosome 2 (nucleotides 32,310,711 to 171,827,243) with a 276bp deletion (nucleotides 32,310,435 to 32,310,710) at the short arm breakpoint and a single base pair insertion (G) at the long arm breakpoint.

        - **`seq[GRCh38] inv(2)(p22.3q31.1)mat`**<br>
          **`NC_000002.12:g.[32310435_32310710delinsG;32310711_171827243inv]`**<br>
          The combined ISCN and HGVS nomenclature describes a maternally inherited pericentric inversion in chromosome 2 (nucleotides 32,310,711 to 171,827,243) with a 276bp deletion (nucleotides 32,310,435 to 32,310,710) and a single base pair insertion (G) at the short arm breakpoint.

        - **`seq[GRCh38] inv(6)(p22.3p21.2)`**<br>
          **`NC_000006.12:g.[20271801_39524349inv;39524350A>C]`**<br>
          The combined ISCN and HGVS nomenclature describes a paracentric inversion in the short arm of chromosome 6 (nucleotides 20,271,801 to 39,524,349) with a single nucleotide substitution at the breakpoint (39,524,350 A to C).


    - **translocations**<br>
Translocations that appear balanced karyotypically may show imbalances by sequencing. The following examples use combined ISCN karyotype format and HGVS nomenclature to describe the gross structural change to chromosomes as the result of a translocation that was identified by sequencing.
        
        - **`46,XX,t(2;11)(p24;p15).seq[GRCh38] t(2;11)(p25.1;p15.4)`**<br>
          **`NC_000002.12:g.pter_8247756delins[NC_000011.10:g.pter_15825272]`**<br>
          **`NC_000011.10:g.pter_5825272delins[NC_000002.12:g.pter_8247756]`**<br>
          A translocation between the short arms of chromosomes 2 and 11 was identified by both karyotype and sequencing. The breakpoints, at bands 2p24 and 11p15 by conventional karyotyping, were further defined by sequencing to bands 2p25.1 and 11p15.4. The translocation involves the joining of chromosome 11 nucleotide 15,825,272 to chromosome 2 nucleotide 8,247,757 on the derivative chromosome 2, and the joining of chromosome 2 nucleotide 8,247,756 to chromosome 11 nucleotide 15,825,273 on the derivative chromosome

        - **`seq[GRCh38] t(2;11)(q31.1;q22.3)`**<br>
          **`NC_000002.12:g.174500009_qterdelins[NC_000011.10:g.108111987_qter]`**<br>
          **`NC_000011.10:g.108111982_qterdelins[NC_000002.12:g.174500009_qter]`**<br>
          The combined ISCN and HGVS nomenclature describes a translocation between the long arms of chromosomes 2 and 11. The translocation involves the joining of chromosome 11 nucleotide 108,111,987 to chromosome 2 nucleotide 174,500,008 on the derivative chromosome 2, and the joining of chromosome 2 nucleotide 174,500,009 to chromosome 11 nucleotide 108,111,981 on the derivative chromosome 11. There is a 5bp deletion of chromosome 11 sequence as evident from the nucleotide numbers given for the two chromosome 11 breakpoints (108,111,982 and 108,111,987).

        - **`seq[GRCh38] t(9;9)(9qter→9q31.1::9p21.2→9qter;9pter→9q31.1::9p21.2→9pter)`**<br>
          **`NC_000009.12:g.[pter_26393001delins102425452_qterinv];[102425452_qterdelinspter_26393001inv]`**<br>
          The combined ISCN and HGVS nomenclature describes a translocation between homologous chromosomes with breakpoints at 9p21.2 and 9q31.1. The different chromosome 9 homologues are indicated by the underline of the second chromosome 9 in the ISCN portion of the nomenclature. The translocation involves the joining of the short arm of the first chromosome 9 at 26,393,001 to the second chromosome 9 long arm at 102,425,453 and
the long arm of the second chromosome 9 at nucleotide 102,425,452 to the short arm of the first chromosome 9  at nucleotide 26,393,001. The HGVS nomenclature uses the “Allele” format to indicate that these findings are found in trans, indicating that both chromosome 9s are abnormal.

        - **`seq[GRCh38] t(3;14)(14qter→14q12::3p22.2→3qter;14pter→14q12::3p22.2→3pter)`**<br>
          **`NC_000003.12:g.pter_36969141delins[CATTTGTTCAAATTTAGTTCAAATGA;NC_000014.9:g.29745314_qterinv]`**<br>
          **`NC_000014.9:g.29745314_qterdelins[NC_000003.12:g.36969141_pterinv]`**<br>
          The combined ISCN and HGVS nomenclature describes a translocation between the short arm of chromosome 3 at 36,969,141 and the long arm of chromosome 14 at 29,745,314 with insertion of non-templated sequence (CATTTGTTCAAATTTAGTTCAAATGA) at the breakpoint on the derivative chromosome 3.

        - **`seq[GRCh38] t(12;21)(p13.2;q22.12)`**<br>
          **`NC_000012.1112:g.pter_11874853delins[NC_000021.89:g.34953708_qterinv]`**<br>
          **`NC_000021.89:g.34953108_qterdelins[NC_000012.1112:g.pter_11873172inv]`**<br>
          The combined ISCN and HGVS nomenclature describes a translocation between the short arm of chromosome 12 and the long arm of chromosome 21. There is a 1.7kb deletion of chromosome 12 sequence evident from the nucleotide numbers given for the two chromosome 12 breakpoints (11,873,172 and 11,874,853), and a 600bp deletion of chromosome 21 sequence evident from the nucleotide numbers given for the two chromosome 21 breakpoints (34,953,108 and 34,953,708).


## Discussion

!!! note "Is the description <code class="invalid">NM_004006.1:c.123+45_123+51TSDinsL1.603bp</code> acceptable (`TSD` = target site duplication, `insL1` indicates the nature of the insert (`L1`, `Alu` or `SVA`), `603bp` = the number of inserted base pairs)?"

    No, not really, it is not exact.
    Following HGVS recommendations, the description should be like `NG_012232.1(NM_004006.2):c.123+51_123+52ins[[XXXXXX.y:g.393_1295];123+45_123+51]`.
    So, give a genomic reference sequence to describe the intronic variant, give the site of the inserted sequence, exactly describe the inserted sequence (not like "insL1.603bp") and describe the target site duplication as an insertion (not "TSD"; by definition a duplication is only used when the duplicate sequence is inserted directly 3' of the original copy of that sequence).
    In the example, `XXXXXX.y` is a GenBank file (accession.version number), containing the inserted L1 sequence (nucleotides `g.393_1295`).
    When the inserted sequence is not known, its (estimated) size can be used, like `NG_012232.1(NM_004006.2):c.123+51_123+52ins[N[603];123+45_123+51]`.
