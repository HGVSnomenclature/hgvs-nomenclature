---
parent: DNA
title: alleles
category: description
---

Format (one allele):   **"prefix"["change1";"change2"]**,  e.g. g.[123G>A;345del]

*	**"prefix"**  =  reference sequence used  =  g.<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"change1"**  =  description first variant  =  123G>A<br>
*	**;**  =  separator symbol two changes  =  ;<br>
*	**"change2"**  =  description second variant  =  345del<br>
*	**]**  =  closing symbol for allele  =  ]
 
Format (two alleles):   **"prefix"["change"];["change"]**,  e.g. g.[123G>A];[345del]

*	**"prefix"**  =  reference sequence used  =  g.<br>
*	**[**  =  opening symbol for allele-1  =  [<br>
*	**"change"**  =  description variant  =  123G>A<br>
*	**];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[<br>
*	**"change"**  =  description variant  =  345del<br>
*	**]**  =  closing symbol for allele-2  =  ]
 
---

### Note

*	humans are diploid organisms and have **two alleles** at each genetic locus, with one allele inherited from each parent
*	when two variants are identified in a gene that are on **one chromosome** (in cis) this should be described as "g.[variant1**<font color="red">;</font>**variant2]".
*	when two variants are identified in a gene that are **on different chromosomes** (in trans) this should be described as "g.[variant1]**<font color="red">;</font>**[variant2]".
*	using allele descriptions involving two or more different variants you do not indicate the other allele does not contain the variant (unless one allele contains no variants at all). LRG\_199t1:c.[2376G>C];[3103del] is correct, LRG\_199t1:c.[2376G>C;3103=];[2376=;3103del] is not correct.
* when two variants are identified in a gene, but when it is **not known** whether these are on one chromosome (in cis) or on different chromosomes (in trans), this should be described as "**variant1<font color="red">(;)</font>variant2**", i.e. without using "[ ]".<br>
_**NOTE:**_ in the latest publication of the recommendations ([Den Dunnen et al. (2016)](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf){:target="\_blank"}) the example given is not correct.<br>
_**NOTE:**_ it is recommended to determine whether the changes are on the same chromosome or not.
*	descriptions combining variants based on different reference sequence types (e.g. **<font color="red">c.</font>**[76A>C];**<font color="red">g.</font>**[10091C>G]) should not be used.
