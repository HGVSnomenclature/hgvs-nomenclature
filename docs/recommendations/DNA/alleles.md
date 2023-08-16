# alleles

## Definition

Allele: a series of variants on one chromosome.

## Description

Format (one allele):   **"prefix"["change1";"change2"]**,  e.g. g.[123G>A;345del]

* **"prefix"**  =  reference sequence used  =  g.
* **[**  =  opening symbol for allele  =  [
* **"change1"**  =  description first variant  =  123G>A
* **;**  =  separator symbol two changes  =  ;
* **"change2"**  =  description second variant  =  345del
* **]**  =  closing symbol for allele  =  ]
 
Format (two alleles):   **"prefix"["change"];["change"]**,  e.g. g.[123G>A];[345del]

* **"prefix"**  =  reference sequence used  =  g.
* **[**  =  opening symbol for allele-1  =  [
* **"change"**  =  description variant  =  123G>A
* **];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[
* **"change"**  =  description variant  =  345del
* **]**  =  closing symbol for allele-2  =  ]
 

## Notes

* humans are diploid organisms and have **two alleles** at each genetic locus, with one allele inherited from each parent
* when two variants are identified in a gene that are on **one chromosome** (in cis) this should be described as "g.[variant1**<font color="red">;</font>**variant2]".
* when two variants are identified in a gene that are **on different chromosomes** (in trans) this should be described as "g.[variant1]**<font color="red">;</font>**[variant2]".
* using allele descriptions involving two or more different variants you do not indicate the other allele does not contain the variant (unless one allele contains no variants at all). LRG\_199t1:c.[2376G>C];[3103del] is correct, LRG\_199t1:c.[2376G>C;3103=];[2376=;3103del] is not correct.
* when two variants are identified in a gene, but when it is **not known** whether these are on one chromosome (in cis) or on different chromosomes (in trans), this should be described as "**variant1<font color="red">(;)</font>variant2**", i.e. without using "[ ]".
**NOTE:** in the latest publication of the recommendations ([Den Dunnen et al. (2016)](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf)) the example given is not correct.
**NOTE:** it is recommended to determine whether the changes are on the same chromosome or not.
* descriptions combining variants based on different reference sequence types (e.g. **<font color="red">c.</font>**[76A>C];**<font color="red">g.</font>**[10091C>G]) should not be used.
## Examples

* **variants on one allele**
    * NM\_004006.2:c.[2376G>C;3103del]: one allele (chromosome) of a gene contains two different changes, c.2376G>C and c.3103del. The variants are found **in cis**.
    * NC\_000023.10:g.[30683643A>G;33038273T>G]: one allele (X-chromosome) contains two different variants in two different genes, g.30683643A>G in the GK gene and g.33038273T>G in the DMD gene.
    * NC\_000003.12:g.63912687AGC[(50\_60)]: one allele (chromosome 3) contains a repeated AGC tri-nucleotide sequence, starting at position g.6391268, containing 50 to 60 AGC copies
    * NC\_000003.12:g.63912687AGC[(60_?)]: one allele (chromosome 3) contains a repeated AGC tri-nucleotide sequence, starting at position g.6391268, containing 60 or more AGC copies
* **variants on two alleles**
    * NM\_004006.2:c.[2376G>C];[3103del]: the two alleles (chromosomes) of a gene each contain a different change, c.2376G>C and c.3103del. The variants are found **in trans**. A **heterozygous** case (compound heterozygote, e.g. in a recessive disease).: **NOTE**: do not use c.[2376G>C;3103=];[2376=;3103del], the indication "not changed" is used only when one variant was identified (like LRG\_199t1:c.[2376G>C];[2376=])
    * NM\_004006.2:c.[2376G>C];[2376G>C]: both alleles (chromosomes) of a gene contain the same variant, c.2376G>C. A **homozygous** case (e.g. in a recessive disease).: **NOTE**: it is not allowed to shorten this to c.2376[G>C];[G>C] or even c.2376G>C[];[]
    * NM\_004006.2:c.[296T>G;476T>C;1083A>C];[296T>G;1083A>C]: a sample contains variants c.296T>G and c.1083A>C on both alleles (chromosomes) and variant c.476C>T on only one allele.
    * NM\_004006.2:c.[2376G>C];[2376=]: one allele (chromosome) of a gene contains a variant, c.2376G>C, the other allele (chromosome) contains the reference sequence, c.2376= (is **wild-type**).: **NOTE**: the description c.[2376G>C];[=], containing c.2376G>C and c.=, is different since it indicates the entire coding DNA reference sequence was analysed and the only variant identified was c.2376G>C (on one allele).: **NOTE**: for other variant types the format is c.[2376del];[2376=], c.[2376\_2399dup];[2376\_2399=], c.[2376\_2377insGT];[2376\_2377=], etc. For more examples see [Proposal SVD-WG001](http://varnomen.hgvs.org/consultation/SVD-WG001/).
    * NM\_004006.2:c.[2376G>C];[?]: one allele (chromosomes) of a gene contains a variant, c.2376G>C, while a variant for the other allele is expected but not yet identified (c.?) (e.g. in individuals affected by a recessive disease).
* **alleles not certain**
    * NM\_004006.2:c.2376G>C(;)3103del: two variants in a gene, c.2376G>C and c.3103del, but it is not known whether they are on the same or on different alleles (chromosomes).: **NOTE**: in the latest publication of the recommendations ([Den Dunnen et al. (2016)](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf)) the example given is not correct. Allele brackets should not be used when it is not known whether variants are on one allele or not.
    * NM\_004006.2:c.2376G>C(;)(2376G>C): analysis detects one variant (c.2376G>C), suggesting both alleles (chromosomes) contain this variants, but it can not be excluded the other allele is deleted
    * NM\_004006.2:c.[296T>G;476T>C];[476T>C]\(;)1083A>C: a sample contains a homozygous variant (c.476T>C) and two heterozygous variants (c.296T>G and c.1083G>C) for which it is not known on which allele (chromosome) they are (although at least one, in the example c.296T>G, is on the same allele as c.476T>C).
    * NM\_004006.2:c.[296T>G];[476T>C]\(;)1083G>C(;)1406del: a sample contains heterozygous variants on different alleles (c.296T>G and c.476T>C) and two additional heterozygous variants (c.1083G>C and c.1406del) for which it is not known on which allele (chromosome) they are.
## Discussion

!!! note "Was originally the recommendation to use the format [c.76A>C+c.83G>C]?"

    Indeed, originally [den Dunnen and Antonarakis, 2000](http://dx.doi.org/10.1002/%28SICI%291098-1004%28200001%2915:1%3c7::AID-HUMU4%3e3.0.CO;2-N) the suggestion was to describe two changes in a gene on one chromosome as [c.76>C+c.83G>C], i.e. using a "+"-character to separate the two changes, while an earlier publication suggested to use a ";" ([c.76A>C;c.83G>C] [(Antonarakis and the Nomenclature Working Group, 1998](http://dx.doi.org/10.1002/%28SICI%291098-1004%281998%2911:1%3c1::AID-HUMU1%3e3.0.CO;2-O)). To prevent confusion with older publications, to improve overall consistency and to keep descriptions as short as possible, the 2000 proposal was retracted. The recommended format is c.[76A>C;83G>C].

!!! note "In recessive diseases, is it important I show which variants were found in which combination?"

    When in one individual you find more then one variant it is essential that you clearly indicate which variant(s) were found and on which allele(s);<ul><li>disease severity will depend on the combination of variants found,</li><li>in recessive disease, when two variants are on one allele an individual is a carrier or you might not have found the variant on the 2nd allele.</li></ul>

!!! note "I find the notation c.[76A>C] without describing the second allele misleading; not enough researchers know this refers to only one of the two alleles present. Would using c.[76A>C];[] be OK?"

    No, the recommended description is LRG_199t1:c.[76A>C];[76=], i.e. c.76= for "no change" on the second allele. 

!!! note "How should I describe the variants detected in males and females for a gene on the X-chromosome?"

    In <b>females</b> the description is straightforward, like LRG_199t1:c.[76A>C];[76=]. In <b>males</b> there is no second allele (X-chromosome) which can be described as LRG_199t1:c.[76A>C];[0], i.e. using "<b>c.0</b>" to indicate the absence of a second X-chromosome.

!!! note "I have a patient with hearing loss and variants in the GJB2 (c.35delG) and GJB6 (c.689_690insT) genes, how should I describe this? <i>(Nancy Carson, Ottawa, Canada)</i>"

    The recommendation is to use the format GJB2:c.[35delG] GJB6:c.[689_690insT]. This uses standard HGVS descriptions and prevents confusion regarding which variant was found in which gene. Note it is essential that you also define the coding DNA reference sequence used. Another format, coping with this directly, is to describe the variants as NM_004004.2:c.[35delG] NM_006783.1:c.[689_690insT], i.e. using the Genbank reference sequences in stead of the HGNC approved Gene Symbol.

!!! note "When for a haplotype I have a range of changes to report, is there a suggested short format to use?"

    When it is once clearly specified (e.g. in the Materials & Methods) what variants are listed and based on which reference sequence(s), alleles may be reported in a simplified format like below. Variants should be listed in genomic order and using "[ ]" for variants on the same chromosome.<ul><li>haplotype with all variants in relation to several different reference sequences, both genomic and coding DNA<ul><li>description of the reference haplotype; [M59228.1:g.250G>C;AF209160.1:g.572CA[(11_21)];Z11861.1:g.61T>C;Z16803.1:g.114A[(18_22)]]</li><li>short haplotype description; [C;13;T;21]</li></ul><li>haplotype with all variants in relation to one coding DNA reference sequence<ul><li>description of the reference haplotype; NM_004006.1:c.[837G>A;1704+51T>C;3734C>T;6438+2669T[(16_23)];6571C>T;7098+13212GT[(15_19)]]</li><li>short haplotype description; [G;C;C;18;T;17]</li></ul></ul>

!!! note "Suggestion (Peter Taschner, Leiden)"

    Nomenclature recommendations mainly apply to genotype descriptions in tables. Unfortunately, these are not very useful in the general text of a paper. For instance, OPRM1:c.118A>G or rs1799971:A>G can be used to describe the variant, but in a paper you might like to discuss the phenotypic consequences of different genotypes. In fact the current recommendation is to use OPRM1:c.[118A>G];[118A=] to describe a heterozygote and OPRM1:c.[118A=];[118A=] and OPRM1:c.[118>G];[118>G] for the homozygotes. I would like to <b>suggest</b> to describe the genotypes in the text like;<ul><li>OPRM1:c.118AA homozygotes </li><li>OPRM1:c.118GA heterozygotes </li><li>OPRM1:c.118GG homozygotes </li> </ul>The different alleles could then be designated as the OPRM1:c.118A allele and the OPRM1:c.118G allele. In combination with variants of other genes, the genotype descriptions could be OPRM1:c.118AA, GJB2:c.76AC double heterozygotes, etc.
