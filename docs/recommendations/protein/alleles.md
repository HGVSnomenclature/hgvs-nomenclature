# Alleles

<!-- ## Definition -->

Allele: a series of variants in a protein encoded by one chromosome.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.alleles
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses inside the square brackets, e.g., `p.[`<code class="spot1">(</code>`Arg727Ser;Cys1334Trp`<code class="spot1">)</code>`]`.
- when two variants are identified in a protein that derive from **one chromosome** (in cis), this should be described as `p.[variant1`<code class="spot1">;</code>`variant2]`.
- when two variants are identified in proteins that derive from **different chromosomes** (in trans), this should be described as `p.[variant1]`<code class="spot1">;</code>`[variant2]`.
- when two variants are identified in a protein, but when it is **not known** whether these derive from one chromosome (in cis) or from different chromosomes (in trans), this should be described as `variant`<code class="spot1">(;)</code>`variant2`, i.e. without using `[ ]`.<br>
  **NOTE**: it is recommended to determine whether the changes are in the same protein or not.
- when two variants are identified in two different proteins that derive from **one variant** on the DNA level (giving two different transcripts), the variants are separated using a `,`; `p.[variant1`<code class="spot1">,</code>`variant2]`.

## Examples

For more examples, see [DNA alleles](../DNA/alleles.md).

### variants on one allele

- **`NP_003997.1:p.[Ser68Arg;Asn594del]`**<br>
  a protein allele contains two different variants, `p.Ser68Arg` and `p.Asn594del` (the variants are found **in cis**).

- **`NP_003997.1:p.[(Ser68Arg;Asn594del)]`**<br>
  a protein allele contains two different **predicted** variants, `p.(Ser68Arg)` and `p.(Asn594del)` (the variants are found **in cis**).<br>
  **NOTE**: the parentheses are placed **inside** of the allele brackets; the description <code class="invalid">p.([Ser68Arg;Asn594del])</code> is not correct.

### variants on different alleles

#### homozygous

- **`NP_003997.1:p.[Ser68Arg];[Ser68Arg]`**<br>
  two protein alleles contain the same variant, `p.Ser68Arg` (the variants are found **in trans**, e.g., in a recessive disease).

- **`NP_003997.1:p.[(Ser68Arg)];[(Ser68Arg)]`**<br>
  two protein alleles contain the same variant with a **predicted** consequence `p.(Ser68Arg)`.<br>
  **NOTE**: the parentheses are placed **inside** of the allele brackets; the description <code class="invalid">p.([Ser68Arg];[Ser68Arg])</code> is not correct.

- **`NP_003997.1:p.(Ser68Arg)(;)(Ser68Arg)`**<br>
  a possible homozygous case where one protein allele contains predicted variant `p.(Ser68Arg)`, but where it can not be excluded the other allele is deleted.

#### heterozygous

- **`NP_003997.1:p.[Ser68Arg];[Asn594del]`**<br>
  two protein alleles each contain a different variant, `p.Ser68Arg` and `p.Asn594del` (compound heterozygote, e.g., in a recessive disease, the variants are found **in trans**).

- **`NP_003997.1:p.[(Ser68Arg)];[?]`**<br>
  one protein allele contains a variant, with predicted consequence `p.(Ser68Arg)`, while a variant for the other protein allele is expected but not yet identified (`p.(?)`) (e.g., in individuals affected by a recessive disease).

- **`NP_003997.1:p.[Ser68Arg];[Ser68=]`**<br>
  one protein allele contains a variant, `p.Ser68Arg`, the other allele contains at this position the reference sequence, `Ser68=` (is **wild-type**).<br>
  **NOTE**: the description `p.[Ser68Arg];[=]`, containing `p.Ser68Arg` and `p.=`, is different since it indicates the entire protein reference sequence was analysed and the only variant identified was `p.Ser68Arg` (on one allele).<br>
  **NOTE**: for other variant types, the format is `p.[Ser68del];[Ser68=]`, `p.[Ser68_Arg70dup];[Ser68_Arg70=]`, `p.[Ser68_Ala74insSerGln];[Ser68_Ala74=]`, etc.
  For more examples, see [Proposal SVD-WG001](../../consultation/SVD-WG001.md).

#### allele unknown

- **`NP_003997.1:p.(Ser68Arg)(;)(Asn594del)`**<br>
  two predicted protein variants are found, `p.(Ser68Arg)` and `p.(Asn594del)`, but it is not known whether they are on the same or on different alleles (chromosomes).<br>
  **NOTE**: when it is not known on which allele a variant is, allele brackets are not used.

- **`NP_003997.2:p.[(Asn158Asp)(;)(Asn158Ile)]^[(Asn158Val)]`**<br>
  for the variants `NM_004006.3:c.472A>G` and `c.473A>T` it is not known whether they are on the same or on different alleles (chromosomes).
  The predicted consequence when the variants are on different alleles is `p.(Asn158Asp)(;)(Asn158Ile)`, when the variants are on the same allele (i.e. `c.472_473delinsGT`), the predicted consequence is `p.(Asn158Val)`.
  To discriminate between the two possibilities, square brackets need to be used.

#### one allele encoding two proteins

- **`NP_003997.1:p.[Lys31Asn,Val25_Lys31del]`**<br>
  two different proteins, `p.Lys31Asn` and `p.Val25_Lys31del`, derive from a variant on one allele (`c.93G>T` on the DNA level with `r.[83g>u,73_93del]` on the RNA level).

## Discussion

!!! note "Was originally the recommendation to use the format <code class="invalid">[p.Ser73Arg+p.Asn103del]</code>?"

    Indeed, originally [den Dunnen and Antonarakis, 2000](http://dx.doi.org/10.1002/%28SICI%291098-1004%28200001%2915:1%3c7::AID-HUMU4%3e3.0.CO;2-N) the suggestion was to describe two changes in a protein encoded by one chromosome as <code class="invalid">[p.Ser73Arg+p.Asn103del]</code>, i.e. using a "+"-character to separate the two changes, while an earlier publication suggested to use a ";" (<code class="invalid">[p.Ser73Arg;p.Asn103del]</code> [(Antonarakis and the Nomenclature Working Group, 1998](http://dx.doi.org/10.1002/%28SICI%291098-1004%281998%2911:1%3c1::AID-HUMU1%3e3.0.CO;2-O)).
    To prevent confusion with older publications, to improve overall consistency, and to keep descriptions as short as possible, the 2000 proposal was retracted.
    The recommended format is `p.[Ser73Arg;Asn103del]`.

!!! note "Can I describe the predicted protein consequences of two variants on the same allele as <code class="invalid">p.([Phe233Leu;Cys690Trp])</code>?"

    No, this should be described as `p.[(Phe233Leu;Cys690Trp)]`, i.e. with the parentheses **inside** the square brackets of the allele and around each variant.
    This format is used for overall consistency; with the parentheses **inside** the square brackets, variants can be described as `p.[Phe233Leu;(Cys690Trp)]`, which would not be possible when they were allowed outside of the square brackets.

!!! note "In recessive diseases, is it important I show in which combination variants were found?"

    When in one individual you find more than one variant, it is essential that you clearly indicate from which allele(s) variant(s) were found.

    - disease severity will depend on the combination of variants found;
    - in recessive disease, when two variants are in one protein, an individual is a carrier or you might not have found the variant in the protein from the second allele.

!!! note "I find the notation `p.[Ser73Arg]` without describing the second protein allele misleading; not enough researchers know this refers to only one of the two alleles present. Would using <code class="invalid">p.[Ser73Arg];[]</code> be OK?"

    No, the recommended description is `p.[Ser73Arg];[Ser73=]`, i.e. `p.Ser73=` for "no change" at position `p.Ser73` on the second protein allele.

!!! note "How should I describe the variants detected in males and females for a protein encoded by the X-chromosome?"

    In **females**, the description is straightforward, like `p.[Ser86Arg];[Ser86=]`.
    In **males**, there is no second allele (X-chromosome), which can be described as `p.[Ser86Arg];[0]`, i.e. using `p.0` to indicate the absence of a protein from the second X-chromosome.
    A description like `p.[Ser86Arg];[0]` is also possible for a female but, since variant descriptions on protein level can only be given **in addition to** a description on DNA level, it will be linked to either the description of a deletion on DNA level or the absence of RNA (`r.0`), e.g., caused by non-random X-inactivation.
