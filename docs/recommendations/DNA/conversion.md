# conversion

## Definition

Conversion: a sequence change where, compared to a reference sequence, a <b>range of nucleotides</b> are replaced by a sequence from <b>elsewhere</b> in the genome

## Description

Format: **"prefix""positions_converted""con""positions_replacing_sequence"**,  e.g. g.123\_345con888\_1110

**"prefix"**  =  reference sequence used  =  g.<br>
**"positions_converted"**  =  range of nucleotides converted  =  g.123\_345<br>
**"con"**  =  type of change is a conversion =  con<br> 
**"positions_replacing_sequence"**  =  description of replacing sequence  =  888\_1110
 

## Notes

* ****NOTE:**** based on [_proposal SVD-WG009_](/background/consultation/SVD-WG009/) the variant type "con" for conversion is no longer used. Conversion variants should be described as "delins" (deletion-insertion).
* **prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
* the region converted ("positions\_converted") should **start** and **end** with a variant nucleotide
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
    * the 3'rule applies to ALL descriptions (genome, gene, transcript and protein) of a given variant
## Examples

* NC\_000022.10:g.42522624\_42522669con42536337\_42536382: conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides g.42522624 to g.42522669 with those of the 3' flanking CYP2D7P1 gene, nucleotides g.42536337 to g.42536382 from the same genomic reference sequence (NC\_000022.10)
* NC\_000012.11:g.6128892\_6128954conNC\_000022.10:17179029\_17179091: conversion replacing nucleotides g.6128892 to g.6128954 of the VWF gene (NM\_000552.3:c.3675-45\_3692) on chromosome 12 with nucleotides g.17179029 to g.17179091 of the VWFP1 pseudogene on chromosome 22
* NM\_000797.3:c.812\_829con908\_925: conversion replacing nucleotides c.812 to c.829 of the DRD4 gene with nucleotides c.908 to c.925 as in the coding DNA sequence file NM\_000797.3
## Discussion

!!! note "What is a "conversion"?"

    Conversions, gene conversions, result from a nonreciprocal transfer of genetic information between two sites in the genome. The two sites often contain homologous sequences, e.g. two homologous genes. The two sites can be anywhere in the genome but are in reality often not far apart on one chromosome. After a (gene) conversion event the two sites have  an identical sequence.

!!! note "Why not describe the variants independently?"

    The converted segment is usually of considerable length (several hundred nucleotides) and will contain a whole series of sequence changes. Describing these changes all independently will make the description lengthy and rather complex. In such cases it is recommended to describe the change as a conversion using <b>"con"</b>.
---