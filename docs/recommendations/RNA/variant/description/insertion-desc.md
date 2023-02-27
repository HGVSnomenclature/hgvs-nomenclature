---
parent: RNA
title: insertion
category: description
---

Format: **"prefix""positions_flanking""ins""inserted_sequence"**,  e.g. r.123\_124insauc

**"prefix"**  =  reference sequence used  =  r.<br>
**"positions_flanking"**  =  position two nucleotides flanking insertion site  =  123\_124<br>
**"ins"**  =  type of change is an insertion  =  ins<br> 
**"inserted_sequence"**  =  inserted sequence  =  auc <sup>1</sup>

---

### Note

*	**prefix** reference sequences accepted are r. (coding and non-coding RNA).
*	the "positions_flanking" should contain **two flanking nucleotides**, e.g. 123 and 124 but not 123 and 125.
	*	the “positions_flanking” should be listed from 5’ to 3’, e.g. 123_124 not 124_123
*	when a variant can be described as a duplication it **must** be desribed as a duplication and **not as an insertion** (see [_Prioritization_](/recommendations/general/)
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
*	the **“inserted_sequence”** can be given as the nucleotides inserted (e.g. insAGC) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g. c.849_850ins858_895) or another reference (see Examples).
	*	when the inserted sequence is very long it can best be submitted to a database (e.g. [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/){:target="\_blank"}); the accession.version number obtained can then be used to describe the variant like r.123\_124insL37425.1:r.23\_361
*	<sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like r.(100_150)ins(25) 
