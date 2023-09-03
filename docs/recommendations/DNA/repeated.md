# repeated sequences

## Definition

Repeated sequence: a sequence where, compared to a reference sequence, a segment of <b>one or more</b> nucleotides (the repeat unit) is present several times, one after the other.

## Description

****NOTE:**** a Community Consultation is prepared which will suggest to allow **only one format** where the entire range of the repeated sequence must be indicated, e.g. g.123\_191CAG[23] not g.123CAG[23]

Format (unique repeat):   **"prefix""position_first_nucleotide_first_repeat_unit""repeat_sequence"["copy_number"]**,  e.g. g.123CAG[23]

* **"prefix"**  =  reference sequence used  =  g.
* **"position_first_nucleotide_first_repeat_unit"**  =  first nucleotide of first repeat unit  =  123
* **"repeat_sequence"**  =  sequence repeat unit  =  CAG
* **[**  =  opening symbol for copy number allele  =  [
* **"copy_number"**  =  number of repeat units  =  23
* **]**  =  closing symbol for copy number allele  =  ]

Format (mixed repeat):   **"prefix""range_repeated_sequence""repeat_sequence_unit1"["copy_number"]"repeat_sequence_unit2"["copy_number"]"..."**,  e.g. g.123\_191CAG[19]CAA[4]

* **"prefix"**  =  reference sequence used  =  g.
* **"range_repeated_sequence"**  =  position first to last nucleotide repeated sequence (range)   =  123_191
* **"repeat_sequence_unit1"**  =  sequence first repeat unit  =  CAG
* **[**  =  opening symbol for allele  =  [
* **"copy_number"**  =  number of repeat units  =  19
* **]**  =  closing symbol for allele  =  ]
* **"repeat_sequence_unit2"**  =  sequence first repeat unit  =  CAA
* **[**  =  opening symbol for allele  =  [
* **"copy_number"**  =  number of repeat units  =  4
* **]**  =  closing symbol for allele  =  ]
* **...**  =  and so on for repeat_sequence_unit3, repeat_sequence_unit4, etc.

## Notes

* reference sequences accepted are g., o. m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
* for **mixed repeats** the range of the reapeat sequence is given followed by a listing of each repeat unit and the number of repeats in each unit; NC\_000012.11:g.112036755\_112036823CTG[9]TTG[1]CTG[13].
* NM\_000044.3:c.171_239GCA[34] describes a repeated sequence containing 34 GCA units (sequenced, the reference sequence contains 23 GCA units). NM\_000044.3:c.(92_331)insN[33] describes an insertion of 33 nucleotides in the amplified region from position c.92 to c.331 (**not sequenced**), containing a repeated sequence of 24 GCA units in the reference sequence.
* **exception:** using a coding DNA reference sequence ("c." description) a Repeated sequence variant description can be used only for repeat units with a length which is a multiple of 3, i.e. which can not affect the reading frame. Consequently, use NM\_024312.4:c.2692_2693dup and **not** NM\_024312.4:c.2686A[10], use NM\_024312.4:c.1741\_1742insTATATATA and **not** NM\_024312.4:c.1738TA[6].
## Examples

* **unique repeat**
    * **sequenced**
        * NC\_000014.8:g.101179660\_101179695TG[14]: a repeated TG di-nucleotide sequence starting at position g.101179660 on human chromosome 14, with 14 TG copies
        * NC\_000014.8:g.[101179660\_101179695TG[14]];[101179660\_101179695TG[18]]: a repeated TG di-nucleotide sequence starting at position g.101179660 on human chromosome 14, is present with 14 TG copies on one allele and 18 TG copies on the other allele
    * **repeat expansion disorders**
        * **sequenced**
            * NM\_023035.2(CACNA1A):c.6955\_6993CAG[26]  (or c.6955_6993dup): a repeated CAG tri-nucleotide sequence starting at position c.6955 in the CACNA1A gene with 26 CAG copies (p.(Gln2319[26] or p.(Gln2319_Gln2331dup))
            * NC\_000003.12:g.63912687\_63912716AGC[13] | c.89\_118AGC[13]: a repeated AGC tri-nucleotide sequence in the ATXN7 gene on chromosome 3, starting at position g.63912687/c.89, with 13 AGC copies  (the reference sequence has 10 copies): **NOTE**:    in literature the tri-nucleotide repeat, encoding a poly-Gln repeat on protein level, is known as the CAG repeat. However, based on the ATXN7 coding DNA reference sequence (GenBank LRG_866t1 or NM\_000333.3) and applying the **3'rule**, the repeat has to be described as an AGC repeat
        * **not sequenced**
            * NC\_000003.12:g.(63912602\_63912844)insN[9] | NM\_000333.3:c.(4\_246)insN[9]: a fragment containing the AGC repeat in the ATXN7 gene was amplified (from nucleotide g.63912602/c.4 to g.63912844/c.246) and its size determined to be 9 nucleotides larger ( "insN[9]" ) compared to that of the reference sequence.: **NOTE**:    since the fragment was not sequenced the variant can not be described as g.63912687\7\_63912716AGC[13] / c.89\_118AGC[13].
            * NC\_000003.12:g.(63912602\_63912844)delN[15] | NM\_000333.3:c.(4\_246)delN[15]: a fragment containing the AGC repeat in the ATXN7 gene was amplified (from nucleotide g.63912602/c.4 to g.63912844/c.246) and its size determined to be 15 nucleotides smaller ( "delN[15]" ) then that of the reference sequence.
    
* **mixed repeat reference sequence**
    * **repeat expansion disorders**
        * **FMR1 repeat**  (reference sequence GGC[9]GGA[1]GGC[10]): in literature the Fragile-X tri-nucleotide repeat is described as a CGG-repeat. However, based on a coding DNA reference sequence (GenBank NM\_002024.5) and applying the **3'rule**, the repeat has to be described as a mixed GGC-GGA-GGC repeat
            * NM\_002024.5:c.-128\_-69GGC[10]GGA[1]GGC[9]GGA[1]GGC[10]: a sequenced GGC tri-nucleotide repeat from position c.-128 to c.-69 contains 10 GGC, 1 GGA, 9 GGC, 1 GGA and 10 GGC units (31 repeat units)
            * NM\_002024.5:c.-128\_-69GGC[68]GGA[1]GGC[10]: a repeated CGG tri-nucleotide sequence starting at position c.-129 with 79 repeat units: **NOTE**:    since the reference sequence contains a mixed repeat (CGG and AGG units), the variant **can not** be described as NM\_002024.5:c.-129CGG[79]. NM\_002024.5:c.-129CGG[79] would cover only the sequence up to the first AGG interruption (position c.-99).
            * NM\_002024.5:c.-128\_-69GGM[108]: a repeated mixed tri-nucleotide sequence starting at position c.-129 with 108 GGC/GGA copies
            * NM\_002024.5:c.(-144\_-16)insN[(1800\_2400)]: the amplified region containing the FMR1 repeat region (between nucleotides c.-144 and c.-16) contains an insertion of 1800 to 2400 nucleotides (600 to 800 GGC/GGA units)
        * **HTT repeat**  (reference sequence LRG\_763t1:52\_153CAG[21]CAA[1]CAG[1]CCG[1]CCA[1]CCG[7]CCT[2]): in literature the Huntington's Disease tri-nucleotide repeat, encoding a variable poly-Gln followed by a variable poly-Pro repeat on protein level, is known as the CAG repeat. Based on the HTT (huntingtin) coding DNA reference sequence (GenBank LRG\_763t1 or NM\_002111.8) and applying the **3'rule**, the Poly-Gln encoding repeat has to be described as an AGC-AAC-AGC repeat.
            * LRG\_763t1:c.54\_110GCA[23]: a sequenced GCA tri-nucleotide repeat starting at position c.54 contains 23 units, on protein level described as NP\_002102.4:p.(Gln18)[25]: **NOTE:** the GCA repeat is followed by ACAGCA extending the encoded Gln-repeat by 2
        * **CFTR intron 9**: NM\_000492.3:c.1210-33\_1210-6GT[11]T[6]: the mixed repeat sequence form position c.1210-33 to c.1210-6 contains 11 GT and 6 T copies: **NOTE**:    when only the variable T-stretch is described the format is NM\_000492.3:c.1210-12\_1210-6T[7] (see Q&A below)
        * **HTT repeat**  (reference sequence LRG\_763t1:c.52\_153CAG[21]CAA[1]CAG[1]CCG[1]CCA[1]CCG[7]CCT[2]): in literature the Huntington's Disease tri-nucleotide repeat, encoding a variable poly-Gln followed by a variable poly-Pro repeat on protein level, is known as the CAG repeat. Based on the HTT (huntingtin) coding DNA reference sequence (GenBank LRG\_763t1 or NM\_002111.8) and applying the **3'rule**, the Poly-Gln encoding repeat has to be described as an AGC-AAC-AGC repeat.
            * LRG\_763t1:c.53AGC[23]: a sequenced AGC tri-nucleotide repeat starting at position c.53 contains 23 units, on protein level described as NP\_002102.4:p.(Gln18)[25]: **NOTE:** the AGC repeat is followed by AACAGC extending the encoded Gln-repeat by 2)
        * **CFTR intron 9**: NM\_000492.3:c.1210-33\_1210-6GT[11]T[6]: the mixed repeat sequence form position c.1210-33 to c.1210-6 contains 11 GT and 6 T copies: **NOTE**:    when only the variable T-stretch is described the format is NM\_000492.3:c.1210-12T[7] (see Q&A below)
    * NC\_000012.11:g.112036755\_112036823CTG[9]TTG[1]CTG[13]: a complex repeated sequence from position g.112036755 to g.112036823 on chromosome 12 with first a CTG unit present in 9 copies, then a TTG unit present in 1 copy and then a CTG unit present in 13 copies
* differing genomic (g.) and coding DNA (c.) descriptions: NC\_000001.11:g.57367047\_57367121ATAAA[15] and NM\_021080.3:c.-136-75952\_-136-75878ATTTT[15] describe the same repeat allele in intron 3 of the DAB1 gene: **NOTE**:    based on the **3' rule** and the transcriptional orientation of the gene (minus strand) the description of the repeat units differs
## Discussion

!!! note "Intron 9 of the CFTR gene ends with the sequence ...tgtgtgtgtgtttttttaacag[exon_10]. Both the TG and T stretches are variable in length (from 9 to 13 and 5 to 9 resp.). The reference sequence has 11 TG copies and 7 T's. Is it correct to describe an allele as c.1210-14TG[13]T[5] or for the T stretch as c.1210-6T[5]?"

    A complex case. First note that by applying the <b>3'rule</b> it is a <b>variable GT and not TG stretch</b>. When the coding DNA reference sequence has TG11 followed by T7, the reference allele is described as c.1210-33_1210-6GT[11]T[6]. When only variability of the T-stretch is reported, the reference allele is described as c.1210-12T\_1210-6[7].<br>To indicate the overall variability found in the population the description is c.1210-33_1210-6GT[9_13]T[4_8] for the combined repeat and c.1210-12T[5_9] for the T-stretch.
