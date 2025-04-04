# Alleles

<!-- ## Definition -->

Allele: a series of variants in a transcript from one chromosome.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.alleles
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- humans are diploid organisms and have **two alleles** at each genetic locus, with one allele inherited from each parent.
- when two variants are identified in a transcript that derive from **one chromosome** (in cis), this should be described as `r.[variant1`<code class="spot1">;</code>`variant2]`.
- when two variants are identified in transcripts that derive from **different chromosomes** (in trans), this should be described as `r.[variant1]`<code class="spot1">;</code>`[variant2]`.
- when two variants are identified in a transcript, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as `variant1`<code class="spot1">(;)</code>`variant2`, i.e. without using `[ ]`.<br>
  **NOTE**: it is recommended to determine whether the changes are in the same transcript or not.
- when two variants are identified in two different transcripts that derive from **one variant** on the DNA level, the variants are separated using a `,`; `r.[variant1`<code class="spot1">,</code>`variant2]`.

## Examples

For more examples, see [DNA alleles](../DNA/alleles.md).

- **variants on one allele**
    - **`LRG_199t1:r.[76a>u;103del]`**<br>
      one transcript contains two different changes, `r.76a>u` and `r.103del`.
      The variants are found in _cis_.

    - **`LRG_199t1:r.[(578c>u;1339a>g;1680del)]`**<br>
      one transcript contains three different predicted changes, `r.(578c>u)`, `r.(1339a>g)`, and `r.(1680del)`.
      The variants are found in _cis_.

- **variants on two alleles**
    - **`LRG_199t1:r.[76a>u];[103del]`**<br>
      the two transcript alleles each contain a different change, `r.76a>u` and `r.103del`.
      A **heterozygous** case (compound heterozygote, e.g., in a recessive disease).
      The variants are found in _trans_.

    - **`NM_004006.2:r.[76a>u];[76a>u]`**<br>
      both transcript alleles contain the same variant, `r.76a>u`.
      A **homozygous** case (e.g., in a recessive disease).<br>
      **NOTE**: `LRG_199t1:r.76a>u(;)(76a>u)` indicates analysis detects one variant (`r.76a>u`), suggesting both transcript alleles contain this variant, but it can not be excluded the other allele is deleted or not expressed.

    - **`LRG_199t1:r.[76a>u];[76=]`**<br>
      one transcript allele contains a variant, `r.76a>u`, the other transcript allele contains at position `r.76` the reference sequence, `r.76=` (is **wild-type**).<br>
      **NOTE**: the description `r.[76a>u];[=]`, containing `r.76a>u` and `r.=`, is different since it indicates the entire coding RNA reference sequence was analysed and the only variant identified was `r.76a>u` (on one allele).

    - **`NM_004006.2:r.[76a>u];[?]`**<br>
      one transcript allele contains a variant, `r.76a>u`, while a variant in the other transcript allele is expected but not yet identified (`r.?`) (e.g., in individuals affected by a recessive disease).

- **alleles not certain**
    - **`NM_004006.2:r.76a>u(;)103del`**<br>
      two variants are found in a transcript, `r.76a>u` and `r.103del`, but it is not known whether they derive from the same or from different transcript alleles (chromosomes).<br>
      **NOTE**: when it is not known on which allele a variant is, allele brackets should not be used.

- **one allele, two transcripts**
    - **`LRG_199t1:r.[897u>g,832_960del]`**<br>
      two different transcripts, `r.897u>g` and `r.832_960del`, derive from one variant (`LRG_199t1:c.897T>G` on the DNA level).

## Discussion

!!! note "Was originally the recommendation to use the format <code class="invalid">[r.76a>c+r.83g>c]</code>?"

    Indeed, originally [den Dunnen and Antonarakis, 2000](http://dx.doi.org/10.1002/%28SICI%291098-1004%28200001%2915:1%3c7::AID-HUMU4%3e3.0.CO;2-N) the suggestion was to describe two changes in a transcript from one chromosome as <code class="invalid">[r.76a>c+r.83g>c]</code>, i.e. using a "+"-character to separate the two changes, while an earlier publication suggested to use a ";" (<code class="invalid">[r.76a>c;r.83g>c]</code> [(Antonarakis and the Nomenclature Working Group, 1998](http://dx.doi.org/10.1002/%28SICI%291098-1004%281998%2911:1%3c1::AID-HUMU1%3e3.0.CO;2-O)).
    To prevent confusion with older publications, to improve overall consistency, and to keep descriptions as short as possible, the 2000 proposal was retracted.
    The recommended format is `r.[76a>c;83g>c]`.

!!! note "In recessive diseases, is it important I show in which combination variants were found?"

    When in one individual you find more than one variant, it is essential that you clearly indicate on which transcript allele(s) variant(s) were found.

    - disease severity will depend on the combination of variants found;
    - in recessive disease, when two variants are in one transcript, an individual is a carrier or you might not have found the variant on transcripts from the second allele.

!!! note "I find the notation <code class="invalid">r.[76a>c]</code> without describing the second transcript allele misleading; not enough researchers know this refers to only one of the two transcripts present. Would using <code class="invalid">r.[76a>c];[]</code> be OK?"

    No, the recommended description is `r.76[a>c];[=]`, i.e. `r.76=` for "no change" at position `r.76` on the second transcript.

!!! note "How should I describe the variants detected in males and females for a transcript from the X-chromosome?"

    In **females**, the description is straightforward, like `LRG_199t1:r.[76a>c];[76=]`.
    In **males**, there is no transcript from the second allele (X-chromosome), which can be described as `LRG_199t1:r.[76a>c];[0]`, i.e. using `r.0` to indicate the absence of a transcript from the second X-chromosome.
