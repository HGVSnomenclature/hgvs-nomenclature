# General

Since references to websites are not yet acknowledged as citations, please mention Den Dunnen et al. (2016) [HGVS recommendations for the description of sequence variants: 2016 update. Hum.Mutat. 25: 37: 564-569](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf) when referring to these pages.
Note that although the examples on these pages mainly give examples for human (_Homo sapiens_), the recommendations can be applied to **all species**.

Make sure you have also seen the [Basics](../background/basics.md), explaining the **history** of these recommendations, the process of making **changes**, the **versioning** of the recommendations and important remarks on **terminology**.

## General recommendations

- all variants should be described at the most basic level, **the DNA level**.
  Descriptions on the RNA and/or protein level may be given in addition.
    - descriptions should make clear whether the change was **experimentally determined** or **theoretically deduced** by giving predicted consequences in parentheses.
    - descriptions on RNA/protein level should describe the changes observed on that level (RNA/protein) and not try to incorporate any knowledge regarding the change on DNA-level (see Discussion below).

- all variants should be described in relation to an accepted **reference sequence** (see [Reference Sequences](../background/refseq.md)).
    - the reference sequence file used should be **public and clearly described**, e.g., `NC_000023.10`, `LRG_199`, `NG_012232.1`, `NM_004006.2`, `LRG_199t1`, `NR_002196.1`, `NP_003997.1`, etc. (see [Reference Sequences](../background/refseq.md)).
    - the reference sequence used must contain the residue(s) described to be changed.
    - the recommended reference is a genomic reference sequence based on a recent genome build.
        - for human, the recommended reference is based on genome build GRCh38/hg38, e.g., `NC_000023.11` for chromosome X.
        - when variants are reported in relation to a transcript, the preferred reference sequence is the reference suggested by the MANE project (see [Ensembl](http://tark.ensembl.org/web/mane_project/) or [NCBI](https://www.ncbi.nlm.nih.gov/refseq/MANE/)).<br>
          **NOTE**: while [Locus Reference Genomic (LRG)](http://www.lrg-sequence.org) reference sequences are still acceptable, new LRGs are no longer generated and RefSeq or Ensembl transcripts specified by the MANE project are preferred for all genes where available to help standardize clinical reporting.
    - the reference sequence used must contain the residue(s) described to be changed.
    - a **letter prefix** is mandatory to indicate the type of reference sequence used.
      Accepted prefixes are;
        - `c` for a coding DNA reference sequence,
        - `g` for a linear genomic reference sequence,
        - `m` for a mitochondrial DNA reference sequence,
        - `n` for a non-coding DNA reference sequence,
        - `o` for a circular genomic reference sequence,
        - `p` for a protein reference sequence,
        - `r` for an RNA reference sequence (transcript).
    - the numbering of the residues (nucleotide or amino acid) in relation to the reference sequence used should **follow the approved scheme** (see [Numbering](../background/numbering.md)).

- two variants separated by one or more nucleotides should be described individually and **not** as a "delins".
    - **exception**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins".<br>
      **NOTE**: the SVD-WG is preparing a proposal to modify this recommendation.
      To apply the current rule one needs to know whether the two variants are in a coding sequence and affecting one amino acid.
      Recommendations should be general.
      The new recommendation will be: **two variants separated by less than two nucleotides should be described as a "delins"**.

- **3'rule**: for all descriptions, the most 3' position possible of the reference sequence is arbitrarily assigned to have been changed.
    - the 3'rule also applies for changes in single residue stretches and tandem repeats (nucleotide or amino acid).
    - the 3'rule applies to ALL descriptions (genome, gene, transcript, and protein) of a given variant.
    - **exception**: deletions/duplications around exon/exon junctions using **c.**, **r.** or **n.** reference sequences (see [Numbering](../background/numbering.md#DNAc)).

- descriptions on DNA, RNA, and protein level are clearly different:
    - **DNA-level**: `123456A>T`<br>
      number(s) referring to the nucleotide(s) affected, nucleotides in CAPITALS using [IUPAC-IUBMB assigned nucleotide symbols](http://www.qmul.ac.uk/sbcs/iubmb/misc/naseq.html#500).
    - **RNA-level**: `76a>u`<br>
      number(s) referring to the nucleotide(s) affected, nucleotides in lower case using [IUPAC-IUBMB assigned nucleotide symbols](http://www.qmul.ac.uk/sbcs/iubmb/misc/naseq.html#500).
    - **protein level**: `Lys76Asn`<br>
      the amino acid(s) affected in three- or one-letter code followed by a number [IUPAC-IUBMB assigned amino acid symbols](http://www.iupac.org/publications/pac/1984/pdf/5605x0595.pdf).
        - **three-letter** amino acid code is preferred (see [Standards](../background/standards.md#aacode)).
        - the `*` can be used to indicate the translation stop codon in both one- and three-letter amino acid code descriptions.

- **prioritisation**: when a description is possible according to several types, the preferred description is: (1) substitution, (2) deletion, (3) inversion, (4) duplication, (5) insertion.
    - when a variant can be described as a duplication or an insertion, prioritisation determines it should be described as a duplication.
    - descriptions removing part of a reference sequence and replacing it with part of the same sequence are not allowed (e.g., `NM_004006.2:c.[762_768del;767_774dup]`).

- only **approved** [HGNC gene symbols](http://www.genenames.org) should be used to describe genes.<br>
  **NOTE**: to avoid confusion, HGVS recommends to follow the [HGNC guidelines](https://www.genenames.org/about/guidelines/) to use **italics** to denote genes.<br>
  **NOTE**: for protein nomenclature, see the [_International Protein Nomenclature Guidelines_](https://www.ncbi.nlm.nih.gov/genome/doc/internatprot_nomenguide/), written with the involvement of the HGNC.

- HGVS recommends following the [HGNC guidelines](https://www.genenames.org/about/guidelines/) and the [VICC Gene Fusion Specification](https://fusions.cancervariants.org/en/latest) nomenclature to describe products of gene fusions.
    - The HGNC recommendations include using a `GENESYMBOL1::GENESYMBOL2` syntax for gene-level fusion descriptions, and a `GENESYMBOL1-GENESYMBOL2` syntax for read-through transcripts.
    - The VICC nomenclature extends the HGNC recommendations to include a terminology, information model, and nomenclature for gene-level and exon-level representation, with components for disambiguating regulatory fusions from chimeric transcript fusions.
    - HGVS also recommends the use of [adjoined transcripts](RNA/adjoined_transcript.md) for precise and unambiguous characterization of chimeric transcripts at the sequence level.

<a id="characters"></a>

### Characters used

In HGVS nomenclature, some **characters** have a **specific meaning**:

- `+` (plus) is used in [nucleotide numbering](../background/numbering.md); `c.123+45A>G`.
- `-` (hyphen-minus) is used in [nucleotide numbering](../background/numbering.md); `c.124-56C>T`.
- `*` (asterisk) is used in [nucleotide numbering](../background/numbering.md) and to indicate a translation termination (stop) codon (see [Standards](../background/standards.md#RNAcode)); `c.*32G>A` and `p.Trp41*`.
- `_` (underscore) is used to indicate a range; `g.12345_12678del`.
- `[ ]` (square brackets) are used for alleles (see [DNA](DNA/alleles.md), [RNA](RNA/alleles.md), [protein](protein/alleles.md)), which includes multiple inserted sequences at one position and insertions from a second reference sequence.
    - `;` (semicolon) is used to separate variants and alleles; `g.[123456A>G;345678G>C]` or `g.[123456A>G];[345678G>C]`.
    - `,` (comma) is used to separate different transcripts/proteins derived from one allele; `r.[123a>u,122_154del]`.
    - `NC_000002.11:g.48031621_48031622ins[TAT;48026961_48027223;GGC]`.
    - `NC_000002.11:g.47643464_47643465ins[NC_000022.10:35788169_35788352]`.
- `:` (colon) is used to separate the reference sequence file identifier (_accession.version_number_) from the actual description of a variant; `NC_000011.9:g.12345611G>A`.
- `:`: (double colon) is used to describe adjoined transcripts from gene fusions ([RNA Deletion-insertion](RNA/delins.md)) and to designate break point junctions creating a ring chromosome ([DNA Complex (HGVS/ISCN)](DNA/complex.md)).
- `( )` (parentheses) are used to indicate uncertainties and predicted consequences; `NC_000023.9:g.(123456_234567)_(345678_456789)del`, `p.(Ser123Arg)`.<br>
  **NOTE**: the range of the uncertainty should be described as precisely as possible (see [below](#uncertain1)).
- `?` (question mark) is used to indicate unknown positions (nucleotide or amino acid); `g.(?_234567)_(345678_?)del`.
- `^` (caret) is used as "or"; `c.(370A>C^372C>R)` as back translation of `p.Ser124Arg` (i.e. changing the `AGC` codon to `CGC`, `AGG`, or `AGA`).
- `>` (greater than) is used to describe substitution variants (DNA and RNA level); `g.12345A>T`, `r.123a>u` (see [DNA](DNA/substitution.md), [RNA](RNA/substitution.md)).
- `=` (equals) is used to indicate a sequence was tested but found unchanged; `p.(Arg234=)`.
- `/` (forward slash) is used to indicate mosaicism (see [DNA substitution](DNA/substitution.md)).
- `//` (double forward slash) is used to indicate chimerism (see [DNA substitution](DNA/substitution.md)).
- `|` (pipe) is used to indicate that not a direct change of the sequence is described but a modification (a change of state, e.g., methylation). (see [methylation](DNA/other.md)).

- **NOTE:** spaces are *not* permitted in any HGVS description

<a id="abbreviation"></a>

### Abbreviations in variant descriptions

Specific abbreviations are used to describe different variant types.

- `>` (greater than) indicates a **substitution** (DNA and RNA level); `g.123456G>A`, `r.123c>u` (see [DNA](DNA/substitution.md), [RNA](RNA/substitution.md)).
    - a substitution on the protein level is described as `p.Ser321Arg` (see [protein](protein/substitution.md)).
- `del` indicates a **deletion**; `c.76del` (see [DNA](DNA/deletion.md), [RNA](RNA/deletion.md), [protein](protein/deletion.md)).
- `dup` indicates a **duplication**; `c.76dup` (see [DNA](DNA/duplication.md), [RNA](RNA/duplication.md), [protein](protein/duplication.md)).
- `ins` indicates an **insertion**; `c.76_77insG` (see [DNA](DNA/insertion.md), [RNA](RNA/insertion.md), [protein](protein/insertion.md)).
    - duplicating insertions are described as duplications, not as insertions.
- `inv` indicates an **inversion**; `c.76_83inv` (see [DNA](DNA/inversion.md), [RNA](RNA/inversion.md)).
  Not used on protein level, usually described as [deletion-insertion](protein/delins.md).
- `fs` indicates a **frameshift**; `p.Arg456GlyfsTer17` (or `p.Arg456Glyfs*17`, see [Frameshifts](protein/frameshift.md)).
- `ext` indicates an **extension**; `p.Met1ext-5` (see [Extension](protein/extension.md)).

- HGVS/ISCN (see [Community Consultation](../consultation/SVD-WG004.md)):
    - `cen` indicates the **centromere** of a chromosome.
    - `chr` indicates a **chromosome**; `chr11:g.12345611G>A` (`NC_000011.9`).
    - `pter` indicates the **first nucleotide** of a chromosome.
    - `qter` indicates the **last nucleotide** of a chromosome.
    - `sup` indicates a **supernumerary** chromosome (marker chromosome).

- changes of state (modifications):
    - `gom` indicates a **gain of methylation**; `g.12345678_12345901`<code class="spot1">|gom</code>.
    - `lom` indicates a **loss of methylation**; `g.12345678_12345901`<code class="spot1">|lom</code>.
    - `met` indicates a **methylation**; `g.12345678_12345901`<code class="spot1">|met=</code>.

## Discussion

!!! note "Are spaces allowed within HGVS variant descriptions?"

    **Spaces have never been permitted within HGVS variant descriptions.**  Unfortunately, some databases, software, and publications display variant descriptions with internal spaces. These variants do not conform to HGVS Nomenclature and likely create problems for automated parsers.

!!! note "Some papers and websites use a "-" (hyphen-minus) to indicate a range, is this correct?"

    The sign used to indicate a range is "_" (underscore) and not a "-" (hyphen-minus).
    The minus sign should only be used as a minus in the description of variants based on a coding DNA reference sequence.
    `c.12-14del` describes a deletion of nucleotide -14 in the intron directly preceding coding DNA nucleotide 12, **not** a deletion of nucleotides `c.12` to `c.14`.

!!! note "Why is it recommended to use **three-letter amino acid code** to describe protein variants?"

    Several amino acids start with the same initial letter (`Ala`, `Arg`, `Asn`, and `Asp` start with A; `Gln`, `Glu`, and `Gly` with G; `Leu` and `Lys` with L; `Phe` and `Pro` with P; `Thr` and `Tyr` with T) but in one-letter amino acid code, this letter is used as abbreviation for only one.
    In practice, this leads to many mistakes.
    It is therefore recommended to use three-letter amino acid code abbreviations.

!!! note "When I want to report a variant on DNA, RNA, and protein level, do I need to use a specific separator?"

    No, best is to report the variant using the format `NC_000023.11:g.32849790T>A` &nbsp; `NM_004006.3:c.124A>T` &nbsp; `r.(124a>u)` &nbsp; `p.(Ser42Cys)`.<br>
    **NOTE**: when several NP_'s are annotated in the NM_ reference sequence, it is mandatory to add the NP_ reference sequence used to describe the variant on protein level.

!!! note "I found a substitution variant (DNA) which alters splicing, inserting a short sequence in the transcript (RNA), giving a frameshift on protein level. How should I list this variant, as substitution, as splice variant, as insertion or as frameshift?"

    When listing variant types, HGVS recommends listing them separately for each level, i.e. DNA, RNA, and protein.
    On DNA level you identified a substitution, on RNA level an insertion, and on protein level a frameshift.

!!! note "What do you mean with "variants should be described on the protein level and not incorporate knowledge regarding the change on the DNA-level"?"

    It means that protein variant descriptions should be derived from comparing the variant protein sequence with the reference protein sequence.
    Knowledge on the underlying change on the DNA level should not be used.
    e.g., when `MetTrpSerSer`<code class="del">Ser</code>`HisAsp..` changes to `MetTrpSerSer`<code class="del">.</code>`HisAsp..`, this is described as `p.Ser5del`.
    The information that on the DNA level the change is `..ATGTGGTCC`<code class="del">AGT</code>`TCCCACGAT..` to `..ATGTGGTCC`<code class="del">.</code>`TCCCACGAT..`, so the codon for Ser4 is deleted, is not used; the description `p.Ser4del` is not correct.

!!! note "Is it correct that when I apply **the 3'rule** for genes that are on the minus strand of a chromosome, the "g." and "c." variant descriptions differ regarding the nucleotide that I describe as deleted?"

    Yes, when a gene is on the minus strand of a chromosome (opposite transcriptional orientation) and the change is located in a repeated sequence (mono-, di-, tri-, etc. nucleotide stretches), the 3'rule has this as a consequence.
    When the chromosome sequence is `TGGG`<code class="del">G</code>`CAT..` and one of the G's is deleted (change to `TGGG`<code class="del">.</code>`CAT..`), the description based on chromosome coordinates is `g.5del`.
    When the annotated coding DNA reference sequence is on the minus strand (`ATGCCC`<code class="del">C</code>`A..`), the description is `c.7del`.
    Not only is the deleted nucleotide different (G vs. C), in fact the descriptions also point to another nucleotide, `g.5` vs. `g.2` (equivalent to `c.7`).

<a id="uncertain1"></a>
!!! note "Can I describe a deletion when I have not yet sequenced the break point?"

    Yes, using the characters to indicate uncertainties, i.e. the question mark (`?`) and parentheses (`()`), such cases can be described.
    Describe the range of uncertainty as precise as possible.
    For details, see [Uncertain](uncertain.md).
