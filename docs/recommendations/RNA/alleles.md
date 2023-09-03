# alleles

## Definition

Allele: a series of variants in a transcript from one chromosome.

## Description

Format (one allele):   **"prefix"["change1";"change2"]**,  e.g. r.[123g>a;345del]

* **"prefix"**  =  reference sequence used  =  r.
* **[**  =  opening symbol for allele  =  [
* **"change1"**  =  description first variant  =  123g>a
* **;**  =  separator symbol two changes  =  ;
* **"change2"**  =  description second variant  =  345del
* **]**  =  closing symbol for allele  =  ]
 
Format (two alleles):   **"prefix"["change"];["change"]**,  e.g. r.[123g>a];[345del]

* **"prefix"**  =  reference sequence used  =  r.
* **[**  =  opening symbol for allele-1  =  [
* **"change"**  =  description variant  =  123g>a
* **];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[
* **"change"**  =  description variant  =  345del
* **]**  =  closing symbol for allele-2  =  ]
 

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* humans are diploid organisms and have **two alleles** at each genetic locus, with one allele inherited from each parent
* when two variants are identified in a transcript that derive from **one chromosome** (in cis) this should be described as "r.[variant1**<span class="spotlight">;</span>**variant2]".
* when two variants are identified in transcripts that derive from **different chromosomes** (in trans) this should be described as "r.[variant1]**<span class="spotlight">;</span>**[variant2]".
* when two variants are identified in a transcript, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as "**variant1<span class="spotlight">(;)</span>variant2**", i.e. without using "[ ]".  **NOTE:** it is recommended to determine whether the changes are in the same transcript or not.
* when two variants are identified in two different transcripts that derive from **one variant** at the DNA level the variants are separated using a ","; p.[variant1**<span class="spotlight">,</span>**variant2]".
## Examples

For more examples see [DNA alleles](../../DNA/alleles/).

* **variants on one allele**
    * LRG\_199t1:r.[76a>u;103del]: one transcript contains two different changes, r.76a>u and r.103del. The variants are found **in cis**.
    * LRG\_199t1:r.[(578c>u;1339a>g;1680del)]: one transcript contains three different predicted changes, r.(578c>u), r.(1339a>g) and r.(1680del). The variants are found **in cis**.
* **variants on two alleles**
    * LRG\_199t1:r.[76a>u];[103del]: the two transcript alleles each contain a different change, r.76a>u and r.103del. A **heterozygous** case (compound heterozygote, e.g. in a recessive disease). The variants are found **in trans**.
    * NM\_004006.2:r.[76a>u];[76a>u]: both transcript alleles contain the same variant, r.76a>u. A **homozygous** case (e.g. in a recessive disease).: **NOTE**: LRG\_199t1:r.76a>u(;)(76a>u) indicates analysis detects one variant (r.76a>u), suggesting both transcript alleles contain this variant, but it can not be excluded the other allele is deleted or not expressed.
    * LRG_199t1:r.[76a>u];[76=]: one transcript allele contains a variant, r.76a>u, the other transcript allele contains at position r.76 the reference sequence, r.76= (is **wild-type**).: **NOTE**: the description r.[76a>u];[=], containing r.76a>u and r.=, is different since it indicates the entire coding RNA reference sequence was analysed and the only variant identified was r.76a>u (on one allele).
    * NM\_004006.2:r.[76a>u];[?]: one transcript allele contains a variant, r.76a>u, while a variant in the other transcript allele is expected but not yet identified (r.?) (e.g. in individuals affected by a recessive disease).
* **alleles not certain**
    * NM\_004006.2:r.76a>u(;)103del: two variants are found in a transcript, r.76a>u and r.103del, but it is not known whether they derive from the same or from different transcript alleles (chromosomes).: **NOTE**: when it is not known on which allele a variant is, allele brackets should not be used
* **one allele, two transcripts**
    * LRG\_199t1:r.[897u>g,832_960del]: two different transcripts, r.897u>g and r.832_960del, derive from one variant (LRG_199t1:c.897T>G at the DNA level)
## Discussion

!!! note "Was originally the recommendation to use the format [r.76a>c+r.83g>c]?"

    Indeed, originally [den Dunnen and Antonarakis, 2000](http://dx.doi.org/10.1002/%28SICI%291098-1004%28200001%2915:1%3c7::AID-HUMU4%3e3.0.CO;2-N) the suggestion was to describe two changes in a transcript from one chromosome as [r.76a>c+r.83g>c], i.e. using a "+"-character to separate the two changes, while an earlier publication suggested to use a ";" ([r.76a>c;r.83g>c] [(Antonarakis and the Nomenclature Working Group, 1998](http://dx.doi.org/10.1002/%28SICI%291098-1004%281998%2911:1%3c1::AID-HUMU1%3e3.0.CO;2-O)). To prevent confusion with older publications, to improve overall consistency and to keep descriptions as short as possible, the 2000 proposal was retracted. The recommended format is r.[76a>c;83g>c].

!!! note "In recessive diseases, is it important I show which variants were found in which combination?"

    When in one individual you find more then one variant it is essential that you clearly indicate which variant(s) were found and in which transcript alleles
    
    - disease severity will depend on the combination of variants found
    - in recessive disease, when two variants are in one transcript an individual is a carrier or you might not have found the variant on transcripts from the 2nd allele

!!! note "I find the notation r.[76a>c] without describing the second transcript allele misleading; not enough researchers know this refers to only one of the two transcripts present. Would using r.[76a>c];[] be OK?"

    No, the recommended description is r.76[a>c];[=], i.e. r.76= for "no change" at postion r.76 on the second transcript. 

!!! note "How should I describe the variants detected in males and females for a transcript from the X-chromosome?"

    In **females** the description is straightforward, like r.[76a>c];[=]. In **males** there is no transcript from the second allele (X-chromosome) which can be described as r.[76a>c];[0], i.e. using "**r.0**" to indicate the absence of a transcript from the second X-chromosome.
