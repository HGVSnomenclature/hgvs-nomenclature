# HGVS simple

**Changes** in DNA, RNA, and protein sequences, also called **variants** (and sometimes mutations or polymorphisms), are described using a specific language.
To prevent confusion regarding its meaning, a **standard** has been developed for this language: the **HGVS nomenclature**.
This standard is used world-wide, especially in human health and clinical diagnostics.
This page will try to explain the standard, **briefly and in simple terms**.
After reading, you should be able to understand the basics of the HGVS nomenclature and be able to use the internet to find more information about specific variants.
In addition, while searching, you should be able to prevent making mistakes leading to misinterpretation of the variant and its possible consequences.
More details, on all subjects, are available elsewhere on the HGVS nomenclature pages.

## The format

The format of a complete variant description is **"reference : description"** (spaces added for clarity only), e.g.;

- `NM_004006.2:c.4375C>T`
- `NC_000023.11:g.32389644G>A`

All variants are described in relation to a reference, the **reference sequence**; in the examples above, **NM_004006.3** ([from the GenBank database](https://www.ncbi.nlm.nih.gov/nucleotide/NM_004006.3)) and **NC_000023.11** ([from the GenBank database](https://www.ncbi.nlm.nih.gov/nucleotide/NC_000023.1)).
After the reference, a description of the variant is given; in the examples above, **c.4375C>T** and **g.32389644G>A**.

A description without a reference sequence is near useless.
Additional information will then be required to **guess** what reference sequence may have been used.
When the guess you made is wrong, you of course end up with a variant description which is wrong, and the information you retrieved is also not correct.
So be **very careful** when you make a guess; it is better to check the source of the original description and ask for the reference sequence that was used.
Additional information to make a guess may come from the **name of the gene** containing the variant, the associated **phenotype** studied (disease), the **chromosome number** and from possibly predicted consequences of the variant on the RNA and/or protein level.
Since reference sequences usually change over time, the date of the report describing the variant can give useful information as well.

### DNA > RNA > protein

In nature, the DNA code is first transcribed into an **RNA** molecule (see [Wikipedia](https://en.wikipedia.org/wiki/RNA)).
Next, there are two options:

- the RNA molecule is translated into a **protein** and the protein is the final product of a gene.
  Proteins perform a vast array of functions, including catalysing metabolic reactions, DNA replication, responding to stimuli, providing structure to cells and organisms, transporting molecules from one location to another, etc. (see [Wikipedia](https://en.wikipedia.org/wiki/Protein)).
- the RNA molecule is the final product of the gene (so the RNA is not translated into a protein).
  RNA molecules perform a vast array of functions, including, e.g., rRNAs (ribosomal RNA) and tRNAs (transfer RNAs), both active in protein translation.

Variants are usually detected by reading the DNA code, a method called DNA **sequencing**.
A proper report **always** contains the variant described on the DNA level.
In addition, a report usually contains a description of the predicted consequence of the variant on the protein; rarely, the consequence on RNA is mentioned.
In rare cases, not following current standards, only the predicted consequences on the protein level are reported.

Some variants have an effect on how the transcript (RNA) is generated, and consequently, on its translation into protein.
When only DNA has been analysed, the consequences of the variant on the RNA and the protein level can only be predicted.
The HGVS nomenclature demands predicted consequences have to be **reported in parentheses**.
The predicted consequence of the variant `NM_004006.2:c.4375C>T` on the protein level is described as `p.(Arg1459Ter)`.
The "()" warn the variant described is a predicted consequence only.

## Reference sequences

Variants described on the DNA level are mostly reported in relation to a specific **gene** based on a so-called **"coding DNA reference sequence"**.
When a coding DNA reference sequence is used, the description of the variant starts with **"c."** (like in the example `c.4375C>T`).
Since we nowadays have a reliable reference sequence of the complete human genome, it becomes more common to (also) give the description based on a **"genomic reference sequence"**, starting with **"g."** (`g.32407761G>A`).
In addition, the (predicted) consequences on the RNA level (starting with **"r."**) and/or the protein level (starting with **"p."**) may be given.<br>
**NOTE**: the "p." addition is sometimes incorrectly left out when the predicted protein consequences are reported.

Reference sequences have a format like **NC_000023.10**, where **NC_000023** is the **accession number** of the reference sequence and "**.10**" its **version number**.
Version numbers are required since we started to use reference sequences, at a time our knowledge of the human genome was far from complete.
The version number directly follows the accession number and increases over time.

For details, see ["Reference Sequences"](refseq.md).

#### Example descriptions

- genomic (nucleotide)
    - `NC_`: a genomic reference sequence based on a chromosome
        - `NC_000023.9:g.32317682G>A` (Mar.2006: hg18, NCBI36)
        - `NC_000023.10:g.32407761G>A` (Feb.2009: h19, GRCh37)
        - `NC_000023.11:g.32389644G>A` (Dec.2013: hg38, GRCh38)
    - `NG_`: a genomic reference sequence based on a Gene or Genomic region
        - `NG_012232.1:g.954966C>T`
    - `LRG_`: a genomic reference sequence, used in a diagnostic setting, based on a Gene or Genomic region
        - `LRG_199:g.954966C>T`
- transcript (RNA, nucleotide)
    - `NM_`: a reference sequence based on a protein coding RNA (mRNA)
        - `NM_004006.2:c.4375C>T`
    - `NR_`: a reference sequence based on a non-protein coding RNA
        - `NR_002196.1:n.601G>T`
- protein (amino acid)
    - `NP_`: a reference sequence based on a protein (amino acid) sequence
        - `NP_003997.1:p.Arg1459Ter` (`p.Arg1459*`)

### Genomic reference sequences

For human, the reference sequence **accession number** directly in front of the version number gives the number of the chromosome: 1-22, 23 for the X-chromosome, and 24 for the Y-chromosome.
In `NC_000023.10` this number is "23", so a reference sequence of human **chromosome X**.

In many cases, the reference sequence is not given, but a genome build is mentioned.
The genome build has two formats, either "hg" and a number (hg18, hg19, hg38), or "GRCh/NCBI" and a number (NCBI35, NCBI36, GRCh37, GRCh38).
A **genome build** is an attempt to reconstruct the full human genome sequence based on all data available at the time of building the reference sequence.
The most frequently used genome builds are hg18 / NCBI36 (from March 2006), hg19 / GRCh37 (from February 2009), and hg38 / GRCh38 (from December 2013).
Having the genomic reference sequence (like `NC_000023.10`) is most precise.
When the reference sequence is missing, you need to know the genome build used.
**In addition**, when using a website or database to find more information on the variant, make sure you know the genome build (reference sequence) used by the database.<br>
**NOTE**: genome builds are versioned as well, using **"patches"** (e.g., p1), in which errors are corrected.

Genomic reference sequences can also be based on smaller sequences not covering an entire chromosome.
They usually cover only a specific gene or specific genomic segment.
The most frequently used are **NGs** (RefSeq Gene reference sequences, format `NG_012232.1`) or LRGs (Locus Genomic Reference sequences, format `LRG_199`).

### Coding DNA reference sequences

In a human diagnostic setting, the most frequently used reference is a **"coding DNA reference sequence"** (description starting with **"c."**, e.g., `NM_004006.3:c.4375C>T`).
Variant descriptions based on this format are very popular because they directly link to the encoded protein.
In protein coding DNA reference sequences, numbering **starts** with 1 at the first position of the protein coding region; the `A` of the translation initiating `ATG` triplet.
Numbering **ends** at the last position of the ending triplet; the last position of the translation stop codon (`TAA`, `TAG`, or `TGA`).
When you divide the position number from a "c." description by three, you get the affected amino acid residue from the protein sequence (description starting with "p."); for `NM_004006.3:c.4375C>T` (with predicted consequence on protein level `p.(Arg1459Ter)`), i.e. 4375 divided by three gives amino acid 1459.<br>
**NOTE**: positions before the protein coding region get a hyphen-minus sign (e.g., **"c.-26"**), those after the translation stop an asterisk (e.g., `c.*85`).
Numbering in intronic sequences has a format like `c.530+6` or `c.531-23`.
For details, see ["Reference Sequences"](refseq.md).
The most frequently used coding DNA reference sequences are the NMs (RefSeq gene transcript sequences, e.g., `NM_004006.2`) and LRGs (Locus Genomic Reference sequences, e.g., `LRG_199t1`).

## Variants

Depending on the change found, the description of the variant can have many different formats.
For a detailed overview, please see the specific pages on this website.
Here, we will list and briefly explain the major variant types.

A standard variant description has the format **"prefix . position(s) change"** (spaces added for clarity only).
In the variant description `c.4375C>T`, the prefix **"c."** indicates the type of reference sequence used ("c." indicating a coding DNA reference sequence), **"4375"** is the position of the nucleotide affected, and **"C>T"** the change (a `C` changed to a `T`).

### Types of variants

All variants given are in the _DMD_ gene and reported in relation to coding DNA reference sequence `NM_004006.3` (`LRG_199t1`).

- **substitution**<br>
  one letter (nucleotide) of the DNA code is replaced (substituted) by one other letter.
  On DNA and RNA level, a substitution is indicated using **">"**.
    - **`c.4375C>T`**<br>
      the `C` nucleotide at position `c.4375` changed to a `T`.

- **deletion**<br>
  one or more letters of the DNA code are missing (deleted).
  A deletion is indicated using **"del"**.
    - **`c.4375_4379del`**<br>
      the nucleotides from position `c.4375` to `c.4379` (`CGATT`) are missing (deleted).
      Sometimes misreported as `c.4375_4379delCGATT`.

- **duplication**<br>
  one or more letters of the DNA code are present twice (doubled, duplicated).
  A duplication is indicated using **"dup"**.
    - **`c.4375_4385dup`**<br>
      the nucleotides from position `c.4375` to `c.4385` (`CGATTATTCCA`) are present twice (duplicated).
      Sometimes misreported as `c.4375_4385dupCGATTATTCCA` or `c.4385_4386insCGATTATTCCA` (not a correct HGVS description).

- **insertion**<br>
  one or more letters in the DNA code are new (inserted).
  An insertion is indicated using **"ins"**.
    - **`c.4375_4376insACCT`**<br>
      the new sequence `ACCT` was found inserted between positions `c.4375` and `c.4376`.

- **deletion/insertion (delins)**<br>
  one or more letters in the DNA code are missing and replaced by several new letters.
  A deletion/insertion is indicated using **"delins"**.
    - **`c.4375_4376delinsAGTT`**<br>
      the nucleotides from position `c.4375` to `c.4376` (`CG`) are missing (deleted) and replaced by the new sequence, `AGTT`.
      Sometimes misreported as `c.4375_4376delCGinsAGTT`.

There are more variant types, yet these occur less frequently.

### Aliases

It should be noted that **one variant**, based on different reference sequences used, can be described in many different ways.
Variant `c.5234G>A` in the _DMD_ gene can be described based on different genomic reference sequences (e.g., `NC_000023.9:g.32290917C>T`, `NC_000023.10:g.32380996C>T`, `NC_000023.11:g.32362879C>T`, `NG_012232.1:g.981731G>A`, and `LRG_199:g.981731G>A`) as well as different coding DNA reference sequences (e.g., `LRG_199t1:c.5234G>A`, `NM_004006.3:c.5234G>A`, `NM_004009.3:c.5222G>A`, `NM_000109.3:c.5210G>A`, `NM_004007.2:c.4865G>A`, `NM_004010.3:c.4865G>A`, `NM_004011.3:c.1211G>A`, `NM_004012.3:c.1202G>A`, etc.).
These alternative descriptions are rather confusing, especially when reference sequences are not properly listed.
Consequently, when databases or the internet are queried for information regarding the potential consequences of specific variants, errors are easily made.

### Other descriptions

Sometimes, variants are not described using the format **reference:description** (`NM_004006.3:c.4375C>T`) explained above, but using an identifier (ID) in another database.
Common formats include a rs ID (from dbSNP, [rs128627255](https://www.ncbi.nlm.nih.gov/snp/rs128627255)), OMIM ID (from OMIM, [OMIM300377:0073](http://omim.org/entry/300377#0073)), LOVD ID (from LOVD, [DMD_000073](http://www.LOVD.nl/DMD_000073)), RCV ID (from ClinVar, [RCV000012030](https://www.ncbi.nlm.nih.gov/clinvar/RCV000012030/)), etc.
In most cases, using these IDs, the database can be used to find the full description of the variant using the approved HGVS format **reference:description**.

## Missing information

When a reference sequence is not known, the best way forward is to try and get the name of the gene that is affected by the variant.
All genes have an official abbreviation: the **gene symbol**.
For the Duchenne muscular dystrophy gene, the gene symbol is "_DMD_".
The [HGNC](http://www.genenames.org) (HUGO Gene Nomenclature Committee) keeps a catalog of all approved gene symbols and their aliases/synonyms.
The HGNC site can be used to find the gene symbol and check whether the name/symbol you have is the officially approved one.
Using "dystrophin", the name of a protein, you will see this is an alias for the Duchenne muscular dystrophy gene, official gene symbol ["_DMD_"](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2928).
HGNC, and many other sources, can also tell you on which human chromosome a gene is, so to which chromosome the variant description you have may relate.

When you are interested in what is known about a specific variant, the best start is a gene variant database, also called Locus-Specific Database (LSDB)... _in preparation_ ...
