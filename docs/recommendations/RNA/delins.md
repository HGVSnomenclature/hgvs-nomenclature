# Deletion-Insertion

<!-- ## Definition -->

Deletion-Insertion (delins): a sequence change where, compared to a reference sequence, one or more nucleotides are replaced by one or more other nucleotides **and which is not** a substitution or inversion.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.delins
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- by definition, when **one** nucleotide is replaced by **one** other nucleotide, the change is a [substitution](substitution.md).
- two variants separated by one or more nucleotides should be described individually and **not** as a "delins".
    - **exception**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins" (e.g., `r.142_144delinsugg` `p.(Arg48Trp)`).<br>
      **NOTE**: this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position.<br>
    - HGVS requires that insertion, duplication, and deletion variants are "shuffled" toward the 3' (nucleotide) or C terminus (amino acid). However, for the purposes of evaluating adjacency, the 3' or C-terminus shifted variant should also be shifted in the opposite direction to determine the point of closest distance.
      Example: the variant `AG`<code class="sub">C</code>`TTTAGC` to `AG`<code class="sub">G</code>`TTT`<code class="ins">T</code>`AGC` is described as `g.3_4delinsGT`, not as `g.[3C>G;6dup]`.<br>
      **NOTE**: data providers may report adjacent variants independently and may merge nearby (non-adjacent) variants if they believe that those forms are more suitable for their data.
      The intention of HGVS recommendations is to encourage a convenient convention for the most common classes of variant comparisons while not precluding other forms when appropriate.
- **conversions**, a sequence change where a **range of nucleotides** are replaced by a sequence from elsewhere in the genome, are described as a "delins".
  The previous format "con" is no longer used (see [Community Consultation SVD-WG009](../../consultation/SVD-WG009.md)).
- Adjoined transcripts from gene fusions represent a special case of deletion-insertion variant.
  The fusion break point is described using **`::`**.<br>
  **NOTE**: to avoid confusion, HGVS recommends to follow the [HGNC guidelines](https://www.genenames.org/about/guidelines/) to describe products of gene translocations or fusions (format `GENESYMBOL1::GENESYMBOL2`) and readthrough transcripts (format `GENESYMBOL1-GENESYMBOL2`).
- for all descriptions, the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).

## Examples

- **`r.775delinsga`**<br>
  a deletion of nucleotide `r.775` (a `u`, not described), replaced by nucleotides `ga`, changing `..aggc`<code class="del">u</code>`cauu..` to `..aggc`<code class="ins">ga</code>`cauu..`.

- **`r.775_777delinsc`**<br>
  a deletion of nucleotides `r.775` to `r.777` (`uca`, not described), replaced by nucleotide `c`, changing `..aggc`<code class="del">uca</code>`uu..` to `..aggc`<code class="ins">c</code>`uu..`.

- **`r.902_909delinsuuu`**<br>
  a deletion of nucleotides `r.902` to `r.909`, replaced by nucleotides `uuu`.

- **`r.142_144delinsugg` (`p.Arg48Trp`)**<br>
  a deletion replacing nucleotides `r.142` to `r.144` (`cga`, not described) with `ugg`.<br>
  **NOTE**: the variant can also be described as `r.[142c>u;144a>g]`, i.e. two substitutions.
  This format is preferred when either of the two variants is known as a frequently occurring variant ("polymorphism").

- RNA conversion (based on [SVD-WG009](../../consultation/SVD-WG009.md))
    - **`NM_004006.2:r.2623_2803delins2804_2949`**<br>
      conversion replacing nucleotides `r.2623` to `r.2803` (exon 21) with nucleotides `r.2804` to `r.2949` (exon 22) as found in the _DMD_ coding RNA sequence file `NM_004006.2`.

    - **`r.415_1655delins[AC096506.5:g.409_1649]`**<br>
      conversion replacing nucleotides `r.414` to `r.1655` with nucleotides `g.409` to `g.1649` as found in the genomic reference sequence `AC096506.5`.

    - **`r.1401_1446delins[NR_002570.3:r.1513_1558]`**<br>
      conversion in exon 9 of the _CYP2D6_ gene, replacing exon 9 nucleotides `r.1401` to `r.1446` with those of the 3' flanking _CYP2D7P1_ gene, nucleotides `r.1513` to `r.1558`.

- Example adjoined transcripts from gene fusions are discussed in the [adjoined transcript recommendations](adjoined_transcript.md).

## Discussion

!!! note "What is an **"indel"**?"

    The term "indel" is not used in HGVS nomenclature (see [Glossary](../../background/glossary.md)).
    The term is confusing, having different meanings in different disciplines.

!!! note "Can I describe a `gc` to `ug` variant as a di-nucleotide substitution (<code class="invalid">r.4gc>ug</code>)?"

    No, this is not allowed.
    By definition, a substitution changes **one** nucleotide into **one** other nucleotide (see [Substitution](substitution.md)).
    The change `augu`<code class="del">gc</code>`ca` to `augu`<code class="ins">ug</code>`ca` should be described as `r.5_6delinsug`, i.e. a deletion/insertion (delins).

!!! note "The _BRCA1_ coding RNA reference sequence `NM_007294.3` from position `r.2074` to `r.2080` is `cau`<code class="sub">g</code>`aca`. A variant frequently found in the population is `cau`<code class="sub">a</code>`aca` (`NM_007294.3:r.2077g>a`). In a patient I found the sequence `cau`<code class="sub">a</code><code class="ins">ua</code>`aca`. Can I describe this variant as <code class="invalid">NM_007294.3:r.[2077g>a;2077_2078insua]</code>?"

    The correct description of this variant is `NM_007294.3:r.2077delinsaua`.<br>
    **NOTE**: the answer was modified, i.e. the addition "However, since the variant is likely a combination of two other variants, it is acceptable to describe it as <code class="invalid">NM_007294.3:r.[2077g>a;2077_2078insua]</code>." was removed.
