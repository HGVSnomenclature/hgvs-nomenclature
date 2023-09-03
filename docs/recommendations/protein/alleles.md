# alleles

## Definition

Allele: a series of variants in a protein encoded by one chromosome.

## Description

Format (one allele):   **"prefix"["variant1";"variant2"]**,  e.g. p.[(Ser73Arg;Asn103del)]

**"prefix"**  =  reference sequence used  =  p.
**[**  =  opening symbol for allele  =  [
**"variant1"**  =  description first variant  =  Ser73Arg
**;**  =  separator symbol two changes  =  ;
**"variant2"**  =  description second variant  =  Asn103del
**]**  =  closing symbol for allele  =  ]
Format (two alleles):   **"prefix"["variant"];["variant"]**,  e.g. p.[(Ser73Arg)];[(Asn103del)]

**"prefix"**  =  reference sequence used  =  p.
**[**  =  opening symbol for allele-1  =  [
**"variant"**  =  description variant  =  Ser73Arg
**];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[
**"variant"**  =  description variant  =  Asn103del
**]**  =  closing symbol for allele-2  =  ]
## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* **prefix** reference sequence accepted is "p." (protein)
* predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses **inside** the square brackets, e.g. p.[<span class="spotlight">(</span>Arg727Ser;Cys1334Trp<span class="spotlight">)</span>]
* when two variants are identified in a protein that derive from **one chromosome** (in cis) this should be described as "p.[variant1;variant2]"
* when two variants are identified in proteins that derive from **different chromosomes** (in trans) this should be described as "p.[variant1];[variant2]"
* when two variants are identified in a protein, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as "variant**<span class="spotlight">(;)</span>**variant2", i.e. without using "[ ]"
    * **NOTE:** it is recommended to determine whether the changes are in the same protein or not
* when two variants are identified in two different proteins that derive from **one variant** at the DNA level (giving two different transcripts) the variants are separated using a "<span class="spotlight">,</span>"; p.[variant1<span class="spotlight">,</span>variant2]"
## Examples

For more examples see [DNA alleles](../../DNA/alleles/).

* **variants on one allele**
    * NP\_003997.1:p.[Ser68Arg;Asn594del]: a protein allele contains two different variants, p.Ser68Arg and p.Asn594del (the variants are found **in cis**)
    * NP\_003997.1:p.[(Ser68Arg;Asn594del)]: a protein allele contains two different **predicted** variants, p.(Ser68Arg) and p.(Asn594del) (the variants are found **in cis**): **NOTE**: the parentheses are placed **inside** of the allele brackets, the description p.([Ser68Arg;Asn594del]) is not correct
* **variants on different alleles**
    * **homozygous**
        * NP\_003997.1:p.[Ser68Arg];[Ser68Arg]: two protein alleles contain the same variant, p.Ser68Arg (the variants are found **in trans**, e.g. in a recessive disease)
        * NP\_003997.1:p.[(Ser68Arg)];[(Ser68Arg)]: two protein alleles contain the same variant with a **predicted** consequence p.(Ser68Arg): **NOTE**: the parentheses are placed **inside** of the allele brackets, the description p.([Ser68Arg];[Ser68Arg]) is not correct
        * NP\_003997.1:p.(Ser68Arg)(;)(Ser68Arg): a possible homozygous case where one protein allele contains predicted variant p.(Ser68Arg), but where it can not be excluded the other allele is deleted
    * **heterozygous**
        * NP\_003997.1:p.[Ser68Arg];[Asn594del]: two protein alleles each contain a different variant, p.Ser68Arg and p.Asn594del (compound heterozygote, e.g. in a recessive disease, the variants are found **in trans**)
        * NP\_003997.1:p.[(Ser68Arg)];[?]: one protein allele contains a variant, with predicted consequence p.(Ser68Arg), while a variant for the other protein allele is expected but not yet identified (p.(?)) (e.g. in individuals affected by a recessive disease).
        * NP\_003997.1:p.[Ser68Arg];[Ser68=]: one protein allele contains a variant, p.Ser68Arg, the other allele contains at this position the reference sequence, Ser68= (is **wild-type**).: **NOTE**: for other variant types the format is p.[Ser68del];[Ser68=], p.[Ser68\_Arg70dup];[Ser68\_Arg70=], p.[Ser68\_Ala74insSerGln];[Ser68\_Ala74=], etc. (based on [Proposal SVD-WG001](http://varnomen.hgvs.org/consultation/SVD-WG001/)).: **NOTE**: using p.[=] would mean the entire NP_003997.1 protein reference sequence was tested and found not changed
    * **allele unknown**
        * NP\_003997.1:p.(Ser68Arg)(;)(Asn594del): two predicted protein variants are found, p.(Ser68Arg) and p.(Asn594del), but it is not known whether they are on the same or on different alleles (chromosomes).: **NOTE**: when it is not known on which allele a variant is, allele brackets are not used
        * NP\_003997.2:p.[(Asn158Asp)(;)(Asn158Ile)]^[(Asn158Val)]: for the variants NM\_004006.3:c.472A>G and c.473A>T it is not known whether they are on the same or on different alleles (chromosomes). The predicted consequence when the variants are on different alleles is p.(Asn158Asp)(;)(Asn158Ile), when the variants are on the same allele (i.e. c.472_473delinsGT) the predicted consequence is p.(Asn158Val). To discriminate between the two possibilities square brackets need to be used.
* **one allele encoding two proteins**
    * NP\_003997.1:p.[Lys31Asn,Val25\_Lys31del]: two different proteins, p.Lys31Asn and p.Val25\_Lys31del, derive from a variant on one allele (c.93G>T at the DNA level with r.[83g>u,73\_93del] at the RNA level).
## Discussion

!!! note "Was originally the recommendation to use the format [p.Ser73Arg+p.Asn103del]?"

    Indeed, originally [den Dunnen and Antonarakis, 2000](http://dx.doi.org/10.1002/%28SICI%291098-1004%28200001%2915:1%3c7::AID-HUMU4%3e3.0.CO;2-N) the suggestion was to describe two changes in a protein encoded by one chromosome as [p.Ser73Arg+p.Asn103del], i.e. using a "+"-character to separate the two changes, while an earlier publication suggested to use a ";" ([p.Ser73Arg;p.Asn103del] [(Antonarakis and the Nomenclature Working Group, 1998](http://dx.doi.org/10.1002/%28SICI%291098-1004%281998%2911:1%3c1::AID-HUMU1%3e3.0.CO;2-O)). To prevent confusion with older publications, to improve overall consistency and to keep descriptions as short as possible, the 2000 proposal was retracted. The recommended format is p.[Ser73Arg;Asn103del].

!!! note "Can I describe the predicted protein consequences of two variants on the same allele as p.([Phe233Leu;Cys690Trp])?"

    No, this should be described as p.[(Phe233Leu;Cys690Trp)], i.e. with the parentheses **inside** the square brackets of the allele and around each variant. This format is used for overall consistency; with the parentheses **inside** the square brackets variants can be described as p.[Phe233Leu;(Cys690Trp)] which would not be possible when they were allowed outside of the square brackets.

!!! note "In recessive diseases, is it important I show which variants were found in which combination?"

    When in one individual you find more then one variant it is essential that you clearly indicate which variant(s) were found and in the protein from which allele(s);
    
    - disease severity will depend on the combination of variants found
    - in recessive disease, when two variants are in the protein from one allele an individual is a carrier or you might not have found the variant in the protein from the 2nd allele

!!! note "I find the notation p.[Ser73Arg] without describing the second protein allele misleading; not enough researchers know this refers to only one of the two alleles present. Would using p.[Ser73Arg];[] be OK?"

    No, the recommended description is p.[Ser73Arg];[Ser73=], i.e. p.Ser73= for "no change" on the second protein allele.

!!! note "How should I describe the variants detected in males and females for a protein encoded by the X-chromosome?"

    In **females** the description is straightforward, like p.[Ser86Arg];[Ser86=]. In **males** there is no second allele (X-chromosome) which can be described as p.[Ser86Arg];[0], i.e. using "**p.0**" to indicate the absence of a protein from the second X-chromosome. A description like p.[Ser86Arg];[0] is also possible for a female but, since variant descriptions on protein level can only be given **in addition to** a description on DNA level, it will be linked to either the description of a deletion on DNA level or the absence of RNA (r.0), e.g. caused by non-random X-inactivation.
    
