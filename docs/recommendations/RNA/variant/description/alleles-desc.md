---
parent: RNA
title: alleles
category: description
---

Format (one allele):   **"prefix"["change1";"change2"]**,  e.g. r.[123g>a;345del]

*	**"prefix"**  =  reference sequence used  =  r.<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"change1"**  =  description first variant  =  123g>a<br>
*	**;**  =  separator symbol two changes  =  ;<br>
*	**"change2"**  =  description second variant  =  345del<br>
*	**]**  =  closing symbol for allele  =  ]
 
Format (two alleles):   **"prefix"["change"];["change"]**,  e.g. r.[123g>a];[345del]

*	**"prefix"**  =  reference sequence used  =  r.<br>
*	**[**  =  opening symbol for allele-1  =  [<br>
*	**"change"**  =  description variant  =  123g>a<br>
*	**];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[<br>
*	**"change"**  =  description variant  =  345del<br>
*	**]**  =  closing symbol for allele-2  =  ]
 
---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	humans are diploid organisms and have **two alleles** at each genetic locus, with one allele inherited from each parent
*	when two variants are identified in a transcript that derive from **one chromosome** (in cis) this should be described as "r.[variant1**<font color="red">;</font>**variant2]".
*	when two variants are identified in transcripts that derive from **different chromosomes** (in trans) this should be described as "r.[variant1]**<font color="red">;</font>**[variant2]".
*	when two variants are identified in a transcript, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as "**variant1<font color="red">(;)</font>variant2**", i.e. without using "[ ]".  _**NOTE:**_ it is recommended to determine whether the changes are in the same transcript or not.
*	when two variants are identified in two different transcripts that derive from **one variant** at the DNA level the variants are separated using a “,”; p.[variant1**<font color="red">,</font>**variant2]”.
