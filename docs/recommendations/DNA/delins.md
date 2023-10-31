# deletion-insertion

## Definition

Deletion-Insertion (delins): a sequence change where, compared to a reference sequence, one or more nucleotides are replaced by one or more other nucleotides **and which is not** a substitution, inversion or conversion.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml dna.delins
```

## Notes

- The `coordinate_type` must be one of `g.,` `m.,` c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
- by definition, when **one** nucleotide is replaced by **one** other nucleotide the change is a [substitution](substitution.md).
- changes involving two or more consecutive nucleotides are described as deletion/insertion (delins) variants
- two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
  - exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins": **NOTE:** this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position (e.g. `c.235_237delinsTAT` `(p.Lys79Tyr)` versus `c.[235A>T;237G>T]` `(p.[Lys79*;Lys79Asn])`.: **NOTE:** the SVD-WG has prepared a proposal to modify this recommendation (see [SVD-WG010](../../consultation/SVD-WG010.md)). The new proposal is: **two variants that are separated by fewer than two intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant**
- **conversions**, a sequence change where a **range of nucleotides** are replaced by a sequence from elsewhere in the genome, are described as a "delins". The previous format "con" is no longer used (see [Community Consultation SVD-WG009](../../consultation/SVD-WG009.md))
- for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)

## Examples

- `NC_000023.11:g.32386323delinsGA`: a deletion of nucleotide `g.32386323` (a T, not described), replaced by nucleotides GA, changing <code>..CAGC<code class="spot1">T</code>CTTT..</code> to <code>..CAGC<code class="spot1">GA</code>CTTT..</code> The variant corresponds to LRG_199t1:c.4661delinsTC based on a coding DNA reference sequence.: **NOTE**: the recommendation is not to describe the variant as `NC_000023.11:g.32386323delTinsGA,` i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. `NC_000023.11:g.32386323delCinsGA)`.
- `NM_004006.2:c.6775_6777delinsC` : a deletion of nucleotides `c.6775` to `c.6777` (GAG, not described), replaced by a C nucleotide, changing <code>..GGAA<code class="spot1">GAG</code>TTGC..</code> to <code>..GGAA<code class="spot1">C</code>TTGC..</code>: **NOTE**: the recommendation is not to describe the variant as `NM_004006.2:c.6775_6777delGAGinsC,` i.e. describe the deleted nucleotide sequence. This description is longer, it contains redundant information and chances to make an error increase (e.g. `NM_004006.2:c.6775_6777delGTGinsC` ).
- LRG_199t1:c.145_147delinsTGG `(p.Arg49Trp)`: a deletion replacing nucleotides `c.145` to `c.147` (CGC, not described) with TGG
- LRG_199t1:c.9002_9009delinsTTT: a deletion of nucleotides `c.9002` to `c.9009,` replaced by nucleotides TTT: **NOTE**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins", so the description `c.[145C>T;147C>G]` is not correct
- `LRG_199t1:c.850_901delinsTTCCTCGATGCCTG`: a deletion of nuceotides `c.850` to `c.901,` replaced by `TTCCTCGATGCCTG`: **NOTE**: parts of the inserted sequence "align" with the reference sequence, giving an alternative description like `c.[850_869del;874_881del;887_897del;901_902insG]`. The **"delins" format is recommended**: it is simpler and prevents software tools making incorrect predictions for the consequences at protein level.
- `NC_000002.12:g.pter_8247756delins\[NC_000011.10:g.pter_15825266\]`: nucleotides `g.pter` to `g.8247756` of chromosome 2 are deleted and replaced by nucleotides `g.pter` to `g.1582566` of chromosome 11: the derivative chromosome 2 from an unbalanced translocation between the short arms of chromosomes 2 and 11 (ISCN der(2)t(2;11)(p25.1;p15.2)). Example copied from [Complex (HGVS/ISCN)](complex.md).: **NOTE**: balanced translocations (see [Complex (HGVS/ISCN)](complex.md)) are described as two complementary "delins" variants.
- `NC_000022.10:g.42522624_42522669delins42536337_42536382`: conversion in exon 9 of the CYP2D6 gene replacing exon 9 nucleotides `g.42522624` to `g.42522669` with those of the 3' flanking CYP2D7P1 gene, nucleotides `g.42536337` to `g.42536382` from the same genomic reference sequence (NC_000022.10)
- `NC_000012.11:g.6128892_6128954delins[NC_000022.10:g.17179029_17179091]`: conversion replacing nucleotides `g.6128892` to `g.6128954` of the VWF gene (NM_000552.3:c.3675-45_3692) on chromosome 12 with nucleotides `g.17179029` to `g.17179091` of the VWFP1 pseudogene on chromosome 22
- `NM_000797.3:c.812_829delins908_925`: conversion replacing nucleotides `c.812` to `c.829` of the DRD4 gene with nucleotides `c.908` to `c.925` from the same reference sequence
- `NM_004006.2:c.812_829delinsN[12]`: nucleotides `c.812` to `c.829` have been deleted and replaced by 12 unknown nucleotides (N[12])

## Discussion

!!! note "What is an **"indel"**?"

    The term "indel" is not used in HGVS nomenclature (see [Glossary](../../background/glossary.md)). The term is confusing, having different meanings in different disciplines.

!!! note "Can I describe a GC to TG variant as a dinucleotide substitution (g.4GC>TG)?"

    No this is not allowed. By definition a substitution changes **one** nucleotide into **one** other nucleotide (see [Substitution](substitution.md)). The change <code>TGT<code class="spot1">GC</code>CA</code> to <code>TGT<code class="spot1">TG</code>CA</code> should be described as `g.4_5delinsTG,` i.e. a deletion/insertion (indel).

!!! note "Are there specific recommendations regarding the maximum number of unchanged nucleotides between two single nucleotide variants and whether the change is described as a "delins" or as two separate changes?"

    Yes, two variants separated by one or more nucleotides should preferably be described individually and not as a "delins" (unless they together affect one amino acid). Why?  First, the two variants may have been reported (or might occur) individually. Second, sequence analysis pipelines will describe such variants individually, giving the problem that an overlap with the description of the combined variant ("delins" description) might be missed in the annotation step (database queries).

!!! note "The BRCA1 coding DNA reference sequence from position `c.2074` to `c.2080` is ..CATGACA.. A variant frequently found in the population is ..CAT<code class="spot1">A</code>ACA.. (c.2077G>A). In a patient I found the sequence <code>..CAT<code class="spot1">A TA</code>ACA..</code> Can I describe this variant as `c.[2077G>A;2077_2078insTA]`?"

    The correct description of this variant is `NM_007294.3:c.2077delinsATA`.

    **NOTE:** the answer was modified, i.e. the addition "However, since the variant is likely a combination of two other variants it is acceptable to describe it as `NM_007294.3:c.[2077G>A;2077_2078insTA]"` was removed.
