# Deletion

<!-- ## Definition -->

Deletion: a sequence change where, compared to a reference sequence, one or more nucleotides are not present (deleted).

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml dna.del
```

## Notes

- `position(s)_deleted` should contain **two different positions**, e.g., `123_126`, not `123_123`.
- the `position(s)_deleted` should be listed from **5' to 3'**, e.g., `123_126`, not `126_123`.
    - **exception**: when a circular genomic reference sequnce is used ("o" and "m" prefix) nucleotide positions may be listed from 3' to 5' when the deletion includes both the last and first nucleotides of the reference sequence.
- two variants separated by one or more nucleotides should be described individually and **not** as a "delins".
    - **exception**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins".<br>
      **NOTE**: the SVD-WG has prepared a proposal to modify this recommendation (see [SVD-WG010](../../consultation/SVD-WG010.md)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant**.
- for all descriptions, the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
    - **exception**: deletions around exon/exon junctions when identical nucleotides flank the junction (see [Numbering](../../background/numbering.md#DNAc));<br>
      when `..GA`<code class="del">T</code>`gta..//..cagTCA..` changes to `..GAgta..//..cagTCA..`, based on a coding DNA reference sequence, the variant is described as `LRG_199t1:c.3921del` (`NC_000023.10:g.32459297del`) and not as `c.3922del` (which would translate to `g.32456507del`).
- † = see [Uncertain](../uncertain.md); when the position and/or the sequence of a deletion has not been defined, a description may have a format like `g.(100_150)del(15)`.

## Examples

- one nucleotide
    - **`NC_000023.11:g.33344591del`**<br>
      a deletion of the A at position `g.33344591` in the sequence `TGTG`<code class="del">A</code>`TTCT` to `TGTGTTCT`.<br>
      **NOTE**: the recommendation is not to describe the variant as <code class="invalid">NC_000023.11:g.33344591delA</code>, i.e., describe the deleted nucleotide sequence.
      This description is longer, it contains redundant information, and chances to make an error increases (e.g., <code class="invalid">NC_000023.11:g.33344591delG</code>).

    - **`NM_004006.2:c.5697del` (3'rule)**<br>
      a deletion of the A at position `c.5697` in the sequence `ATTGAAAAAAA`<code class="del">A</code>`TTAG` to `ATTGAAAAAAA`<code class="del">.</code>`TTAG`, i.e., the last A of the 8 nucleotide A-stretch running from position `c.5690` to `c.5697`.<br>
      **NOTE**: the 3'rule has been applied here stating that **"for all descriptions, the most 3' position possible is arbitrarily assigned to have been changed"** (see [General_Recommendations](../general.md)).

    - **`NC_000023.11:g.32343183del` (3'rule)**<br>
      a deletion of the T at position `g.32343183` in the sequence `CTAATTTTTTT`<code class="del">T</code>`CAAT` to `CTAATTTTTTT`<code class="del">.</code>`CAAT`, i.e., the last T of the 8 nucleotide T-stretch running from position `g.32343176` to `g.32343183`.
      **NOTE**: the T nucleotide in `NC_000023.11:g.32343183` corresponds to the A nucleotide in `NM_004006.2:c.5690`, a transcript annotated on the minus strand of the X-chromosome.
      However, applying the 3'rule, the deletion of this nucleotide based on a coding DNA reference sequence (transcript level) should be described as `NM_004006.2:c.5697del` (not as <code class="invalid">NM_004006.2:c.5690del</code>).

- several nucleotides
    - **`NC_000023.11:g.33344590_33344592del`**<br>
      a deletion of nucleotides `g.33344590` to `g.33344592` in the sequence `GTGT`<code class="del">GAT</code>`TCTG` to `GTGT`<code class="del">.</code>`TCTG`.<br>
      **NOTE**: the recommendation is not to describe the variant as <code class="invalid">NC_000023.11:g.33344590_33344592delGAT</code>, i.e., describe the deleted nucleotide sequence.
      This description is longer, it contains redundant information, and chances to make an error increases (e.g., <code class="invalid">NC_000023.11:g.33344590_33344592delTTA</code>).

    - **`NC_000023.11(NM_004006.2):c.183_186+48del`**<br>
      a deletion of nucleotides `c.183` to `c.186+48` (coding DNA reference sequence), crossing an exon/intron border.

- exon/intron/exon
    - exon/exon
        - **`LRG_199t1:c.3921del`**<br>
          the deletion of the T nucleotide at the exon/exon border in the sequence `..GA`<code class="del">T</code>`gta..//..cagTCA..` changing to `..GAgta..//..cagTCA..`.<br>
          **NOTE**: according to an exception to the 3'rule, the variant (`NC_000023.10:g.32459297del`) is not described as `c.3922del` since this would shift the position of the variant to the next exon (`c.3922` linking to `g.32456507`) (see [exception in Numbering](../../background/numbering.md#DNAc) and see [Q&A](#6del)).

    - exon/intron
        - **`LRG_199t1:c.1704+1del`**<br>
          the deletion of the G nucleotide at the exon/intron border in the sequence `GAACAG`<code class="del">g</code>`t..//..agTGCCTT` changing to `GAACAGt..//..agTGCCTT` (not `c.1704del`).<br>
          **NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or `r.1704del`.

    - intron/exon
        - **`LRG_199t1:c.1813del`**<br>
          the deletion of the G nucleotide at the intron/exon border in the sequence `CTGGCCgt..//..ag`<code class="del">G</code>`TTTTA` changing to `CTGGCCgt..//..agTTTTA` (not `c.1813-1del`).<br>
          **NOTE**: this description does not depend on the effect observed on RNA level, giving either altered splicing or `r.1813del`.

- exons
    - **`NC_000023.11(NM_004006.2):c.4072-1234_5155-246del`**<br>
      a deletion of nucleotides `c.4072-1234` to `c.5155-246` removing exon 30 (starting at position `c.4072`) to exon 36 (ending at position `c.5154`) of the _DMD_ gene.<br>
      **NOTE**: <code class="invalid">c.4072-1234_5155-246delXXXXX</code>, the size of the deletion (`XXXXX`) **should not** be described.

    - **break point not sequenced**<br>
      recommended is to describe the deletion detected as precise as possible, see [Uncertain](../uncertain.md) for examples.
      In practice, most people use the so-called **"exon-based description"**, a general description which does not contain specific information regarding the exact nucleotide positions tested.
        - **general, "exon-based" description**<br>
          `NC_000023.11(NM_004006.2):c.(4071+1_4072-1)_(5154+1_5155-1)del`<br>
          a deletion of exon 30 (starting at position `c.4072`) to exon 36 (ending at position `c.5154`) of the _DMD_ gene.
          The deletion break point has **not been sequenced**.
          Exons 29 (ending at `c.4071`) and 37 (starting at nucleotide `c.5155`) have been tested and shown to be **not deleted**.
          The deletion therefore starts in intron 29 (positions `c.4071+1` to `c.4072-1`) and ends in intron 36 (positions `c.5154+1` to `c.5155-1`).<br>
          **NOTE**: previously, the suggestion was made to describe such deletions using the format `NC_000023.11(NM_004006.2):c.4072-?_5154+?del`.
          However, since `c.4072-?` indicates an unknown position 5' of `c.4072` and `c.5154+?` to an unknown position 3' of `c.5154` this description is not correct when it is known that exons 29 and 37 are present.
          See also [SVD-WG003 (undecided)](../../consultation/SVD-WG003.md).

        - **specific description**<br>
          `NC_000023.11(NM_004006.2):c.(3996_4196)_(5090_5284)del`<br>
          **probe-based** description of a deletion, identified by MLPA, of exon 30 (deleted position tested `c.4196`) to exon 36 (deleted position tested `c.5090`) of the _DMD_ gene.
          The deletion break point has **not been sequenced**.
          Exons 29 (position tested `c.3996`) and 37 (position tested `c.5284`) are **not deleted**.

    - **deletions extending beyond the transcribed region**<br>
      following current recommendations (see [Numbering](../../background/numbering.md)), it is not allowed to describe variants in nucleotides beyond the boundaries of a reference sequence.
      Consequently, deletions extending 5' of a transcript **can not** be described like <code class="invalid">NC\_000023.11(NM\_004006.2):c.(?\_-244)\_(31+1\_32-1)del</code> (`c.-244` is the first nucleotide of NM_004006.2).
      Deletions extending 3' of a transcript **can not** be described like <code class="invalid">NC_000023.11(NM\_004006.2):c.(10086+1\_10087-1)\_(\*2691\_?)del</code> (`c.*2691` is the last nucleotide of NM_004006.2).
      Such deletions can only be described using **genomic coordinates**.
      The HGVS nomenclature committee (SVD-WG) is discussing whether a c. based format should be proposed.

- gene
    - **`NC_000023.11:g.(31060227_31100351)_(33274278_33417151)del`**<br>
      a deletion of the entire _DMD_ gene based on a SNP-array analysis where the maximum size of the deletion lies between SNPs rs396303 and rs7887548 (nucleotides 31060227 and 33417151) and the minimum size between SNPs rs808178 and rs7887103 (nucleotides 31100351 and 33274278).

    - **`NC_000023.11:g.(?_31120496)_(33339477_?)del`**<br>
      a deletion of the entire _DMD_ gene based on a MLPA assay where the nucleotide positions `g.31120496` and `g.33339477` are defined by the first nucleotide of the probe 3' of the ligation site for, respectively, the last and first exons tested.

- other
    - **`NC_000023.11:g.33344590_33344592=/del`**<br>
      a mosaic case where from position `g.33344590` to `g.33344592`, besides the normal sequence, also chromosomes are found containing a deletion of this sequence.

    - **`NC_000023.11:g.33344590_33344592=//del`**<br>
      a chimeric case, i.e. the sample is a mix of cells containing `g.33344590_33344592=` and `g.33344590_33344592del`.

## Discussion

<a id="6del"></a>
!!! note "Can I use <code class="invalid">NG_012232.1:g.123del6</code> to describe a 6 nucleotide deletion?"

    No, a deletion of more than one residue should mention the first and last residue deleted, separated using the range symbol ("_", underscore), e.g., `NG_012232.1:g.123_128del` and not <code class="invalid">NG_012232.1:g.123del6</code>.

!!! note "In the example above, `LRG_199t1:c.3921del`, should the description based on a coding DNA reference sequence not be `LRG_199t1:c.3922del`?"

    Strictly speaking, you are right.
    However, for cases like this an exception was made to prevent that when `c.3922del` is translated back to a genomic position one would end up at the wrong nucleotide in the wrong exon (`NC_000023.10:g.32456507del` instead of `NC_000023.10:g.32459297del`).

!!! note "Is the description of a deletion of exon 17 as <code class="invalid">c.EX17del</code> still allowed?"

    A description like <code class="invalid">c.EX17del</code> has never been allowed.
    Descriptions should be specific and indicate the nucleotides affected by the change.

!!! note "Deletions in the _BRCA1_ gene are usually mediated by Alu sequences having a very high homology, reaching 100% in the breakpoint region. In such cases, what nucleotide should be used to describe the deletion breakpoint?"

    In cases like this, the 3'rule applies (see [Recommendations General](http://www.HGVS.org/varnomen/recommendations/general/)), i.e., the deletion breakpoint is determined by the first nucleotide that differs after shifting the alignment as far 3' as possible.
    The first nucleotide differing is the **first nucleotide deleted**.

!!! note "PCR analysis of a gene on the X-chromosome shows products for exons 1_3, no product is detected for exons 4_14 (exon 14 is the last exon of the gene). Since PCR fails already when one primer is not hybridising, we are not sure whether exon 4 and 14 are completely absent, or only partially. To describe the deletion I would therefore like to use the last base of exon 3 with "+?" and the last base of exon 13 with a "+?". What are your recommendations? (Erik-Jan Kamsteeg, Nijmegen, Nederland)"

    Literally speaking, you are right and it is best to set the borders as precise as possible.
    When exon 3 is present, the location of the reverse primer can be used to set the most 5' border (something like `c.987+123`).
    However, for the 3' end, your reasoning does not make a difference.
    Since you do not know how far the deletion extends, you have no positive PCR limiting the deletion at the 3' end, using the location of exon 13 since exon 14 **might be present** would give the wrong impression.
    Consequently, the precise description can only be like `c.(987+123_?)del`.
    Is this really more informative then `c.(987+1_?)del`, using the exon 3 exon/intron border?

!!! note "In literature I often see the description "deltaF508" for a variant in the _CFTR_ gene in patients with Cystic Fibrosis. Is the variant detected in these patients <code class="invalid">NM_000492.3:c.1522_1524delTTT</code>?"

    No. The sequence surrounding amino acid Phe508 in the _CFTR_ gene is `..ATCTTTGGT..` (`c.1519` to `c.1527`).
    Three different deletions (`..A`<code class="del">TCT</code>`TTGGT..`, `..AT`<code class="del">CTT</code>`TGGT..`, and `..ATC`<code class="del">TTT</code>`GGT..`) would give the reported protein variant `p.Phe508del`.
    Applying the 3' rule (see [Recommendations](../general.md)) yields two different changes at DNA level, `NM_000492.3:c.1521_1523del` and `NM_000492.3:c.1522_1524del`.
    When you assume the change at DNA level is `c.1522_1524del`, deletion of exactly the Phe508 encoding triplet, you are wrong.
    The change found in patients is mostly `NM_000492.3:c.1521_1523del`.
    So, without a proper description in the manuscript, one can not be certain.

!!! note "Suggestion to use "los" for a loss from a mononucleotide stretch."

    Pat O'Neill (Burlington, USA) writes: I especially like the use of "dup" in place of "ins" when the insertion creates a run of two or more nucleotides.
    I feel that there should be a parallel term for the loss of a nucleotide from a run of two or more instead of just "del".
    This is because of the mechanistic implications of both an ins and a del of a nucleotide in a run.
    Has this been discussed? My thought for a term in place of "del" is **"los"** for loss.

    Shuji Ogino (Boston, USA) agrees, but suggests to use **"dec"** for a decrease in length.

    Reply (Johan den Dunnen, Netherlands): The "dup" nomenclature was introduced because it is **simpler, shorter and less confusing** (see above).
    The potential mechanistic relation is nice but was not decisive.
    Basically, a description should be clear/unequivocal and it is not intended to contain other information.
