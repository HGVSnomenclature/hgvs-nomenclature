## Community Consultation

### Proposal SVD-WG010 (var distance)

!!! warning "Status: decision pending"

    proposal SVD-WG010 opened for Community Consultation on May 15, 2021, closing on July 31, 2021.
    The decision on this proposal is **still pending**.

The proposal suggests to specify the HGVS nomenclature recommendations for the description of two variants which are close to each other.

- two variants that are separated by fewer than two intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant.
    - the recommendation applies to DNA, RNA, and protein level.
    - HGVS requires that insertion, duplication, and deletion variants are "shuffled" toward the 3' (nucleotide) or C terminus (amino acid).
      However, for the purposes of evaluating adjacency, the 3' or C-terminus shifted variant should also be shifted in the opposite direction to determine the point of closest distance.
      Example: the variant `AG`<code class="sub">C</code>`GTTTAGC` to `AG`<code class="sub">G</code>`GTTT`<code class="ins">T</code>`AGC` is described as `g.3_4delinsGGT`, not as `g.[3C>G;7dup]`.
    - **pairs of variants should be considered in order of increasing sequencing position.
      If variants A, B, and C occur in that order on a sequence, and A and B might be merged, and B and C might be merged, A, B, and C should be merged and described as a single "delins" variant.**<br>
      **NOTE**: adjacent variants in cis should be described as a single "delins" variant.
      Data providers may report adjacent variants independently and may merge nearby (non-adjacent) variants if they believe that those forms are more suitable for their data.
      The intention of HGVS recommendations is to encourage a convenient convention for the most common classes of variant comparisons while not precluding other forms when appropriate.

**Background**

According to the current recommendations, the description of two variants which are close to each other depends on whether they are in a protein coding sequence or not.

- making a discrimination between variants in protein-coding and non-coding sequences **is undesired** and makes application of the recommendations unnecessarily complex.
- the proposal **does ensure** that tools predicting the consequences of a variant on the protein level do not make conflicting and incorrect predictions (e.g., `c.235_237delinsTAT` &nbsp; `p.(Lys79Tyr)` versus `c.[235A>T;237G>T]` &nbsp; `p.[(Lys79*;Lys79Asn)]`).

**NOTE**: the current recommendation is:

- two variants separated by one or more nucleotides should be described individually and **not** as a "delins".
- **exception**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins".

#### Examples

- **`LRG_199t1:c.235_236delinsTT`**<br>
  variants `c.235A>T` and `c.236A>T` are separated by fewer than two nucleotides and described as a "delins" variant (both affect the same amino acid residue).<br>
  **NOTE**: when the method used does not allow to determine whether the variants are on the same allele or not, the variant should be described as `LRG_199t1:c.235A>T(;)237G>T` (see [Alleles](../recommendations/DNA/alleles.md)).

- **`LRG_199t1:c.235_237delinsTAT`**<br>
  variants `c.235A>T` and `c.237G>T` are separated by fewer than two nucleotides and described as a "delins" variant (both affect the same amino acid residue).

- **`LRG_199t1:c.[235A>T;238G>T]`**<br>
  variants `c.235A>T` and `c.238G>T` are separated by two nucleotides and described as separate variants, not as "delins" (`c.235_238delinsTAGT`).

- **`NC_000023.10:g.32862927_32862929delinsATA`**<br>
  variants `g.32862927C>A` and `g.32862929T>A` are separated by fewer than two nucleotides and described as a "delins" variant.

- **`LRG_199t1:c.992_1004delinsAC`**<br>
  variants `c.992_1002del` and `c.1004T>C` are separated by fewer than two nucleotides and described as a "delins" variant.

- **`NP_003997.1:p.Ser988_Gln990delinsAlaLeuHis`**<br>
  variants `p.Ser988` and `p.Gln990` (`LRG_199t1:c.[2962T>G;2970A>T]`) are separated by fewer than two amino acids and described as a "delins" variant, not as `p.[Ser988Ala;Gln990His]`.
