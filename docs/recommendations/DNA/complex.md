# complex (HGVS/ISCN)

## Definition

Complex: a sequence change where, compared to a reference sequence, a range of changes occur that can not be described as one of the basic variant types (substitution, deletion, duplication, insertion, conversion, inversion, deletion-insertion, or repeated sequence).

## Description

Sequence changes can be very complex, involving a range of changes at one specific location. Complex changes, including translocations, are described using the recommendations of the accepted HGVS nomenclature **named extension ISCN**, based on the original proposal [SVD-WG004 (ISCN<>HGVS)](../../../consultation/SVD-WG004/)). The named ISCN extension has been developed in collaboration with [Standing Committee on Human Cytogenomic Nomenclature (ISCN)](../../../consultation/ISCN/), covering the description of numerical and structural chromosomal changes detected using microscopic and cytogenetic techniques. It should be noted there is a basic difference between ISCN and HGVS: while ISCN describes the structure of the resulting chromosome(s), HGVS describes the **variant(s) detected**. It should be noted that the description of complex changes can become rather complicated and at some point, although literally correct, becomes effectively meaningless.

The named ISCN extension has been introduced in 2016 and was modified last in May 2020.

- only aberrant findings, linked to defined chromosomal positions, are described
- each rearranged chromosome is described in a separate line
- X, Y, 1, 2, 3, ..., 21, 22: changes affecting sex chromosomes (X then Y) are listed first, followed by those affecting autosomes (numbers from low to high): **NOTE:** changed in ISCN2020. ISCN2016 had: _aberrations affecting autosomes are listed first (numbers from low to high), followed by those affecting sex chromosomes (X then Y)_
- specific symbols
  - pter, cen, qter: the start of the chromosome is described as "**pter**", the end as "**qter**", the centromere as "**cen**"
    - (pter)\_# and #\_(qter): for deletions extending from a known nucleotide position (#) to an unknown position in the direction of the telomere the format "(pter)\_#" or "#\_(qter)" is used.: **NOTE:** added in ISCN2020
  - sup: the presence of an additional sequence which is not attached to other chromosomal material (i.e. trisomy, marker or ring chromosome) is indicated by "**sup**" (supernumerary chromosome): **NOTE:** the description of the supernumerary molecule is given using "[ ]sup": **NOTE:** changed in ISCN2020. ISCN2016 had: _"add" for additional sequence_
  - ::: a double colon (::) is used to designate break point junctions creating a ring chromosome.: **NOTE:** "::"" changed in ISCN2020. ISCN2016 had: _is used to designate break point junctions involving sequences from different chromosomes (translocation, transposition), chromothripsis break point junctions and junctions creating a ring chromosome_: **NOTE:** the "**::**" (double colon) is also used to designate the junction of fusion transcripts
- chromosomal banding patterns are translated to genomic coordinates based the translation tables provided by NCBI (see [Standards](../../../background/standards/#ISCN))
- in ISCN it is allowed to describe nucleotide positions using commas to indicate thousands and millions (e.g. "108,111,982"), in HGVS this is not allowed.
- 3'rule: to determine the location of the break point, the general HGVS rule of maintaining the longest unchanged sequence applies (the 3' rule). Break point location is determined by the first break point encountered, i.e. from pter of the chromosome to be listed first
  - pter to qter: multiple breakpoints in one chromosome are listed in order of occurrence from pter to qter
  - variant descriptions are always in the forward orientation (from pter to qter, the end of the chromosome), determined by the chromosomal origin of the intact centromere ("**cen**")

## Examples

**The description of translocations has changed** In the original proposal (SVD-WG004) **one identical derivative chromosome** would receive **two different descriptions**, depending on whether it was identified in a balanced or an unbalanced case. In a balanced case the description would use a "::" format joining the breakpoints, while in an unbalanced case the description would use a "delins" format. HGVS recommendations try to avoid such conflicts wherever possible. HGVS therefore recommends to describe translocations exclusively using a "delins" format.

- **translocations**
  - **balanced**
    - t(2;11)(p25.1;p15.2): _(involving short arms chromosomes 2 and 11)_
      - NC_000002.12:g.pter_8247756delins[NC\_000011.10:g.pter\_15825272]: **NC_000011.10:g.pter_5825272delins[NC\_000002.12:g.pter\_8247756]**: **NOTE:** corrected for NC_000002.12::g.pter_8247756::NC_000011.10:g.15825273_cen_qter and NC_000011.10:g.pter_15825272::NC_000002.12:g.8247757_cen_qter in ISCN2016
      - ISCN: chr2:g.pter_8,247,756::chr11:g.15,825,273_cen_qter (der11) and chr11:g.pter_15,825,272::chr2:g.8,247,757_cen_qter (der2)
    - t(2;11)(q31.1;q22.3): _(involving long arms chromosomes 2 and 11, with 5 bp deletion of chr11 sequence)_
      - NC_000002.12:g.17450009_qterdelins[NC\_000011.10:g.108111987\_qter]: **NC_000011.10:g.108111982_qterdelins[NC_000002.12:g.17450009_qter**
      - ISCN: chr2:g.pter_cen_174500098::chr11:g.108111987_qter (der2) and chr11:g.pter_cen_108111981::chr2:g.174500099_qter (der11): **NOTE:** coupling chr11:108111981 to 108111987 implies nucleotides 108111982_108111986 are deleted
    - t(3;14)(14qter->14q12::3p22.2->3qter;14pter->14q12::3p22.2->3pter): _(between short arm chromosome 3 and long arm chromosomes 14, with an inserted sequence at the break point on the derivative chromosome 3)_
      - NC_000003.12:g.pter_36969141delins[CATTTGTTCAAATTTAGTTCAAATGA;NC\_000014.9:g.29745314\_qterinv]: **NC_000014.9:g.29745314_qterdelins[NC\_000003.12:g.36969141\_pterinv]**
      - ISCN: chr14:g.pter_cen_29,745,313::chr3:g.pter_36,969,141inv (der14) and chr14:g.29,745,314_qterinv::CATTTGTTCAAATTTAGTTCAAATGA::chr3:g.36,969,142_cen_qter (der3)
    - NC*000009.12:g.pter_26393001delins102425452_qterinv: **NC_000009.12:g.102425452_qterdelinspter_26393001inv**: for ISCN t(9;9)(9qter->9q22.33::9p21.2->9qter;9pter->9q22.33::9p21.2->9pter): *(between homologous chromosomes, based on [Ordulu et al. example](<https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4>))\_
  - **unbalanced**
    - NC*000002.12:g.pter_8247756delins[NC\_000011.10:g.pter\_15825266]: for ISCN der(2)t(2;11)(p25.1;p15.2): *(derivative chromosome 2, translocation between short arms chromosomes 2 and 11)\_
    - NC*000003.12:g.158573187_qterdelins[NC\_000008.11:g.(128534000\_128546000)\_qter]: for ISCN der(3)(3pter->3q25.32::8q24.21->8qter): *(derivative chromosome 3, translocation between long arms chromosomes 3 and 8, with an estimated nucleotide range for the break point on chromosome 8, based on uncertain break point localization example from [Ordulu et al. example](<https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4>))\_
    - NC*000005.10:g.29658442delins[NC\_000010.11:g.67539995\_qterinv]: for ISCN der(5)t(5;10)(p13.3;q21.3): *(derivative chromosome 5, translocation between short arm chromosome 5 and long arm chromosome 10 with homology at the break point (chr5 29658440*29658442 and chr10 67539995_67539997), based on Homology examples in [Ordulu et al. example](<https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4>))*
- **inversion, pericentric**
  - NC*000006.12:g.[776788\_93191545inv;93191546T>C]: for ISCN inv(6)(pter->p25.3::q16.1->p25.3::q16.1->qter): *(with substitution at break point)\_
  - NC*000002.12:g.[32310435\_32310710del;32310711\_171827243inv;insG]: for ISCN inv(2)(pter->p22.3::q31.1->p22.3::q31.1->qter)dn: *(de novo, with 275 bp deletion and 1 bp insertion at break points)\_: **NOTE:** the HGVS description does not include the de novo occurrence of the variant
- **deletion**
  - NC*000023.11:g.(86200001_103700000)del: for ISCN del(X)(q21.31q22.2): *(within a chromosome, breakpoint not sequenced)\_
  - NC*000022.11:g.pter\_(12200001_14700000)del::(37600001_410000000)\_qterdel: for ISCN r(22)(p11.1q13.1): *(ring chromosome derived from chromosome 22, breakpoint not sequenced)\_: **NOTE:** "::" is used to indicate the join instead of ";" to describe two not connected deletions
- **insertion**
  - **duplication** (tandem)
    - NC*000008.11:g.(127300001_131500000)\_(131500001_136400000)dup: for ISCN dup(8)(q24.21q24.22): *(within a chromosome, breakpoint not sequenced)\_
    - NC*000008.11:g.(131500001_136400000)ins[(127300001\_131500000)\_(131500001\_136400000)inv]: for ISCN dup(8)(q24.22q24.21): *(within a chromosome, orientation reversed relative to original sequence, breakpoint not sequenced)\_
  - **insertion**
    - NC*000004.12:g.134850793_134850794ins[NC\_000023.11:g.89555676\_100352080inv]: for ISCN der(4)ins(4;X)(q28.3;q22.2q21.31): *(inserted sequence reversed in orientation relative to chromosome sequence containing centromere)\_
  - **transposition**
    - **balanced** (deletion + insertion elsewhere)
      - HGVS NC*000004.12:g.134850793_134850794ins[NC\_000023.11:g.89555676\_100352080] and NC_000023.11:g.89555676_100352080del: for ISCN ins(4;X)(q28.3;q21.31q22.2): *(balanced intrachromosomal, inserted sequence same orientation as chromosome sequence containing centromere, based on [Ordulu et al. Fig.1C](<https://www.cell.com/ajhg/fulltext/S0002-9297(14)00172-4>))\_
      - NC*000004.12:g.134850793_134850794ins[NC\_000023.11:g.89555676\_100352080inv] and NC_000023.11:g.89555676_100352080del: for ISCN ins(4;X)(q28.3;q22.2q21.31): *(balanced intrachromosomal, inserted sequence reversed in orientation relative to chromosome sequence containing centromere)\_
    - **unbalanced** (copy inserted elsewhere): describe as insertion
- **supernumerary chromosome**
  - NC*000022.11:g.[pter\_(12200001\_14700000)del::(37600001\_410000000)\_qterdel]sup: for ISCN +r(22)(p11.1q13.1): *(supernumerary ring chromosome derived from chromosome 22, breakpoint not sequenced)\_: **NOTE:** changed in ISCN2020. ISCN2016 had: "add" for additional sequence

## Discussion

!!! note "Is the description NM_04006.1:c.123+45_123+51TSDinsL1.603bp acceptable (TSD = target site duplication, insL1 indicates the nature of the insert (L1, Alu or SVA), 603bp = the number of inserted base pairs)?"

    No, not realy, it is not exact. Following HGVS recommendations the description should be like NG_012232.1(NM_004006.2):c.123+51_123+52ins[[XXXXXX.y:g.393_1295];123+45_123+51]. So give a genomic reference sequence to describe the intronic variant, give the site of the inserted sequence, exactly describe the inserted sequence (not like "insL1.603bp") and describe the target site duplication as an insertion (not "TSD", by definition a duplication is only used when the duplicate sequence is inserted directly 3' of the original copy of that sequence). In the example XXXXXX.y is a GenBank file (accession.version number) containing the inserted L1 sequence (nucleotides g.393_1295). When the inserted sequence is not known its (estimated) size can be used, like NG_012232.1(NM_004006.2):c.123+51_123+52ins[(603);123+45_123+51].
