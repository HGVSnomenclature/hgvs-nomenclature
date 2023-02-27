---
parent: DNA
title: conversion
category: description
---

Format: **"prefix""positions_converted""con""positions_replacing_sequence"**,  e.g. g.123\_345con888\_1110

**"prefix"**  =  reference sequence used  =  g.<br>
**"positions_converted"**  =  range of nucleotides converted  =  g.123\_345<br>
**"con"**  =  type of change is a conversion =  con<br> 
**"positions_replacing_sequence"**  =  description of replacing sequence  =  888\_1110
 
---

### Note

*	**<font color="#FF0000">NOTE:</font>** based on [_proposal SVD-WG009_](/bg-material/consultation/svd-wg009/) the variant type "con" for conversion is no longer used. Conversion variants should be described as "delins" (deletion-insertion).
*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
*	the region converted ("positions\_converted") should **start** and **end** with a variant nucleotide
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
	*	the 3'rule applies to ALL descriptions (genome, gene, transcript and protein) of a given variant
