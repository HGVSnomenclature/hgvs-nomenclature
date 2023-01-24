---
parent: Protein
title: alleles
category: description
---

Format (one allele):   **"prefix"["variant1";"variant2"]**,  e.g. p.[(Ser73Arg;Asn103del)]

**"prefix"**  =  reference sequence used  =  p.<br>
**[**  =  opening symbol for allele  =  [<br>
**"variant1"**  =  description first variant  =  Ser73Arg<br>
**;**  =  separator symbol two changes  =  ;<br>
**"variant2"**  =  description second variant  =  Asn103del<br>
**]**  =  closing symbol for allele  =  ]<br>
 
Format (two alleles):   **"prefix"["variant"];["variant"]**,  e.g. p.[(Ser73Arg)];[(Asn103del)]

**"prefix"**  =  reference sequence used  =  p.<br>
**[**  =  opening symbol for allele-1  =  [<br>
**"variant"**  =  description variant  =  Ser73Arg<br>
**];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[<br>
**"variant"**  =  description variant  =  Asn103del<br>
**]**  =  closing symbol for allele-2  =  ]<br>
 
---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein)
*	predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses **inside** the square brackets, e.g. p.[<font color="red">(</font>Arg727Ser;Cys1334Trp<font color="red">)</font>]
*	when two variants are identified in a protein that derive from **one chromosome** (in cis) this should be described as "p.[variant1;variant2]"
*	when two variants are identified in proteins that derive from **different chromosomes** (in trans) this should be described as "p.[variant1];[variant2]"
*	when two variants are identified in a protein, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as "variant**<font color="red">(;)</font>**variant2", i.e. without using "[ ]"
	*	_**NOTE:**_ it is recommended to determine whether the changes are in the same protein or not
*	when two variants are identified in two different proteins that derive from **one variant** at the DNA level (giving two different transcripts) the variants are separated using a "<font color="red">,</font>"; p.[variant1<font color="red">,</font>variant2]"
