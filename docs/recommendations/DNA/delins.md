# deletion-insertion

## Definition

Deletion-Insertion (delins): a sequence change where, compared to a reference sequence, one or more nucleotides are replaced by one or more other nucleotides <b>and which is not</b> a substitution, inversion or conversion.

## Description

Format:   **"prefix""position(s)\_deleted""delins""inserted_sequence"**,  e.g. g.123\_127delinsAG

**"prefix"**  =  reference sequence used  =  g.
**"position(s)\_deleted"**  =  position nucleotide or range of nucleotides deleted  =  123\_127
**"delins"**  =  type of change is a deletion-insertion  =  delins
**"inserted\_sequence"**  =  description inserted sequence  =  AG
## Notes

* **prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
* by definition, when **one** nucleotide is replaced by **one** other nucleotide the change is a [_substitution_](/recommendations/DNA/variant/substitution/).
* changes involving two or more consecutive nucleotides are described as deletion/insertion (delins) variants
* two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
    * exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins": **NOTE:**    this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position (e.g. c.235\_237delinsTAT (p.Lys79Tyr) versus c.[235A>T;237G>T] (p.[Lys79*;Lys79Asn]).: ****NOTE:**** the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/consultation/SVD-WG010/)). The new proposal is: **two variants that are separated by fewer than two intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
* **conversions**, a sequence change where a **range of nucleotides** are replaced by a sequence from elsewhere in the genome, are described as a "delins". The previous format "con" is no longer used (see [_Community Consultation SVD-WG009_](/consultation/SVD-WG009/))
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
## Examples

* NC\_000023.11:g.32386323delinsGA: a deletion of nucleotide g.32386323 (a T, not described), replaced by nucleotides GA, changing ..CAGC<font color="red">T</font>CTTT.. to ..CAGC<font color="red">GA</font>CTTT.. The variant corresponds to LRG\_199t1:c.4661delinsTC based on a coding DNA reference sequence.: **NOTE**: the recommendation is not to describe the variant as NC\_000023.11:g.32386323delTinsGA, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NC\_000023.11:g.32386323delCinsGA).
* NM\_004006.2:c.6775\_6777delinsC : a deletion of nucleotides c.6775 to c.6777 (GAG, not described), replaced by a C nucleotide, changing ..GGAA<font color="red">GAG</font>TTGC.. to ..GGAA<font color="red">C</font>TTGC..: **NOTE**: the recommendation is not to describe the variant as NM\_004006.2:c.6775\_6777delGAGinsC, i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. NM\_004006.2:c.6775\_6777delGTGinsC ).
* LRG\_199t1:c.145\_147delinsTGG (p.Arg49Trp): a deletion replacing nucleotides c.145 to c.147 (CGC, not described) with TGG
* LRG\_199t1:c.9002\_9009delinsTTT: a deletion of nucleotides c.9002 to c.9009, replaced by nucleotides TTT: **NOTE**:    two variants separated by one nucleotide, together affecting one amino acid, should be described as a “delins”, so the description c.[145C>T;147C>G] is not correct
* LRG\_199t1:c.850\_901delinsTTCCTCGATGCCTG: a deletion of nuceotides c.850 to c.901, replaced by TTCCTCGATGCCTG: **NOTE**:    parts of the inserted sequence "align" with the reference sequence, giving an alternative description like c.[850\_869del;874\_881del;887\_897del;901\_902insG]. The **"delins" format is recommended**: it is simpler and prevents software tools making incorrect predictions for the consequences at protein level. 
* NC\_000002.12:g.pter\_8247756delins\[NC\_000011.10:g.pter\_15825266\]: nucleotides g.pter to g.8247756 of chromosome 2 are deleted and replaced by nucleotides g.pter to g.1582566 of chromosome 11: the derivative chromosome 2 from an unbalanced translocation between the short arms of chromosomes 2 and 11 (ISCN der(2)t(2;11)(p25.1;p15.2)). Example copied from [_Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/).: **NOTE**:    balanced translocations ([_see Complex (HGVS/ISCN)_](/recommendations/DNA/variant/complex/)) are described as two complementary "delins" variants.
* NC\_000022.10:g.42522624\_42522669delins42536337\_42536382: conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides g.42522624 to g.42522669 with those of the 3' flanking CYP2D7P1 gene, nucleotides g.42536337 to g.42536382 from the same genomic reference sequence (NC\_000022.10)
* NC\_000012.11:g.6128892\_6128954delins[NC\_000022.10:g.17179029\_17179091]: conversion replacing nucleotides g.6128892 to g.6128954 of the VWF gene (NM\_000552.3:c.3675-45\_3692) on chromosome 12 with nucleotides g.17179029 to g.17179091 of the VWFP1 pseudogene on chromosome 22
* NM\_000797.3:c.812\_829delins908\_925: conversion replacing nucleotides c.812 to c.829 of the DRD4 gene with nucleotides c.908 to c.925 from the same reference sequence
* NM\_004006.2:c.812\_829delinsN[12]: nucleotides c.812 to c.829 have been deleted and replaced by 12 unknown nucleotides (N[12])
## Discussion

!!! note "What is an <b>"indel"</b>?"

    The term "indel" is not used in HGVS nomenclature (<a href='http://varnomen.hgvs.org/bg-material/glossary/'><i>see Glossary</i></a>). The term is confusing, having different meanings in different disciplines.

!!! note "Can I describe a GC to TG variant as a dinucleotide substitution (g.4GC>TG)?"

    No this is not allowed. By definition a substitution changes <b>one</b> nucleotide into <b>one</b> other nucleotide (<a href='http://varnomen.hgvs.org/recommendations/DNA/variant/substitution/'><i>see Substitution</i></a>). The change TGT<font color="red">GC</font>CA to TGT<font color="red">TG</font>CA should be described as g.4_5delinsTG, i.e. a deletion/insertion (indel).

!!! note "Are there specific recommendations regarding the maximum number of unchanged nucleotides between two single nucleotide variants and whether the change is described as a "delins" or as two separate changes?"

    Yes, two variants separated by one or more nucleotides should preferably be described individually and not as a "delins" (unless they together affect one amino acid). Why?  First, the two variants may have been reported (or might occur) individually. Second, sequence analysis pipelines will describe such variants individually, giving the problem that an overlap with the description of the combined variant ("delins" description) might be missed in the annotation step (database queries).

!!! note "The BRCA1 coding DNA reference sequence from position c.2074 to c.2080 is ..CATGACA.. A variant frequently found in the population is ..CAT<font color="red">A</font>ACA.. (c.2077G>A). In a patient I found the sequence ..CAT<font color="red">A TA</font>ACA.. Can I describe this variant as c.[2077G>A;2077_2078insTA]?"

    The correct description of this variant is NM_007294.3:c.2077delinsATA.<br><b>NOTE:</b> the answer was modified, i.e. the addition "However, since the variant is likely a combination of two other variants it is acceptable to describe it as NM_007294.3:c.[2077G>A;2077_2078insTA]" was removed. 
