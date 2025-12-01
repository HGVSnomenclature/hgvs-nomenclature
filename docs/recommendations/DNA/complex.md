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

        - **`seq[GRCh38] 10p15.3(49,086_2,944,634)×1dn`**<br>
          **`NC_000010.11:g.(pter)_49086_(2944634_?)del`**<br>
          The ISCN short microarray format describes a de novo terminal deletion of the short arm of chromosome 10 with a breakpoint in 10p15.3 using a relative copy-number detection methodology (e.g., targeted short-read NGS sequencing) where the neither the precise breakpoint nor structural information were determined. The deletion involves the region 49,086 to 2,944,634 and the uncertainty range is not specified. Note: this deletion is likely terminal, but the nomenclature describes only the region of the chromosome that was assayed for copy number, similar to array nomenclature. HGVS nomenclature indicates that the deletion is likely terminal, with the use of **`"pter"`** for the 5′ breakpoint, and the use of a question mark (**`"?"`**) for the undefined 3′ breakpoint.


.....

## Discussion

!!! note "Is the description <code class="invalid">NM_004006.1:c.123+45_123+51TSDinsL1.603bp</code> acceptable (`TSD` = target site duplication, `insL1` indicates the nature of the insert (`L1`, `Alu` or `SVA`), `603bp` = the number of inserted base pairs)?"

    No, not really, it is not exact.
    Following HGVS recommendations, the description should be like `NG_012232.1(NM_004006.2):c.123+51_123+52ins[[XXXXXX.y:g.393_1295];123+45_123+51]`.
    So, give a genomic reference sequence to describe the intronic variant, give the site of the inserted sequence, exactly describe the inserted sequence (not like "insL1.603bp") and describe the target site duplication as an insertion (not "TSD"; by definition a duplication is only used when the duplicate sequence is inserted directly 3' of the original copy of that sequence).
    In the example, `XXXXXX.y` is a GenBank file (accession.version number), containing the inserted L1 sequence (nucleotides `g.393_1295`).
    When the inserted sequence is not known, its (estimated) size can be used, like `NG_012232.1(NM_004006.2):c.123+51_123+52ins[N[603];123+45_123+51]`.
