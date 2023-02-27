---
parent: RNA
title: substitution
category: description
---

Format:   **"prefix""position_substituted""reference_nucleotide"">"new_nucleotide"**,  e.g. r.123a>g

**"prefix"**  =  reference sequence used  =  r.<br>
**"position_substituted"**  =  position nucleotide sustituted  =  123<br>
**"reference_nulceotide"**  =  nucleotide at reference position =  a<br>
**">"**  =  type of change is a substitution =  ><br>
**"new_nucleotide"**  =  substituted nucleotide  =  g

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequences accepted are r. (coding and non-coding RNA).
*	substitutions involving two or more consecutive nucleotides are described as deletion/insertions (indels) ([_see Deletion/insertion (delins)_](/recommendations/RNA/variant/delins/)).
*	two substitutions separated by one or more nucleotides should be described individually and not as a “delins”
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a “delins” (e.g. r.142\_144delinsugg (p.Arg48Trp)).
	:	_**NOTE:**_ this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position
*	nucleotides that have been tested and found **not changed** are described as r.109u=, r.4567_4569= ([_see SVD-WG001 (no change)_](http://www.hgvs.org/mutnomen/accepted001.html)).
*	it is not correct to describe "_polymorphisms_" as r.76a/g ([_see Discussions_](/recommendations/RNA/variant/substitution/#polymorphism)).
