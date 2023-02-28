# conversion

## Definition

Conversion: a sequence change where, compared to a reference sequence, a <b>range of nucleotides</b> are replaced by a sequence from <b>elsewhere</b> in the genome

## Description

Format: **"prefix""positions_converted""con""positions_replacing_sequence"**,  e.g. r.123\_345con888\_1110

**"prefix"**  =  reference sequence used  =  g.<br>
**"positions_converted"**  =  range of nucleotides converted  =  r.123\_345<br>
**"con"**  =  type of change is a conversion =  con<br> 
**"positions_replacing_sequence"**  =  description of replacing sequence  =  888\_1110
 

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* **prefix** reference sequences accepted are r. (coding and non-coding RNA)
* the region converted ("positions\_converted") should **start** and **end** with a variant nucleotide
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
    * the 3'rule applies to ALL descriptions (genome, gene, transcript and protein) of a given variant
## Examples

* r.415\_1655conAC096506.5:409\_1649: conversion replacing nucleotides r.414 to r.1655 with nucleotides r.409 to r.1649 as found in the genomic reference sequence AC096506.5
* r.1401\_1446conNR\_002570.3:1513\_1558: conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides r.1401 to r.1446 with those of the 3' flanking CYP2D7P1 gene, nucleotides r.1513 to r.1558
* r.15\_355conNM\_004006.1:20\_360: conversion replacing nucleotides r.15 to r.355 with nucleotides r.20 to r.360 as found in the coding RNA sequence file NM\_004006.1
## Discussion

!!! note "What is a "conversion"?"

    Conversions, gene conversions, result from a nonreciprocal transfer of genetic information between two sites in the genome. The two sites often contain homologous sequences, e.g. two homologous genes. The two sites can be anywhere in the genome but are in reality often not far apart on one chromosome. After a (gene) conversion event the two sites have  an identical sequence.

!!! note "Why not describe the variants independently?"

    The converted segment is usually of considerable length (several hundred nucleotides) and will contain a whole series of sequence changes. Describing these changes all independently will make the description lengthy and rather complex. In such cases it is recommended to describe the change as a conversion using <b>"con"</b>.
---