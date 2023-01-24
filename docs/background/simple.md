---
layout: default-md
title: HGVS Simple
order: 5
---

# HGVS simple

**Changes** in DNA, RNA and protein sequences, also called **variants** (and sometimes mutations or polymorphisms), are described using a specific language. To prevent confusion regarding its meaning a **standard** has been developed for this language, the so called **HGVS nomenclature standard**. The standard is used world-wide, especially in human health and clinical diagnostics.
This page will try to explain the standard, **briefly and in simple terms**. After reading you should be able to understand the basics of the HGVS nomenclature and be able to use the internet to find more information about specific variants. In addition, while searching, you should be able to prevent making mistakes leading to misinterpretation of the variant and its possible consequences. More details, on all subjects, are availble elsewhere on the HGVS nomenclature pages.

* * *

## The format

The format of a complete variant description is **"reference : description"** (spaces added for clarity only), e.g.;

	*	NM_004006.2:c.4375C>T
	*	NC_000023.11:g.32389644G>A

All variants are described in relation to a reference, the so called **reference sequence**, in the examples **NM\_004006.3** ([from the GenBank database](https://www.ncbi.nlm.nih.gov/nucleotide/NM_004006.3){:target="\_blank"}) **NC\_000023.11** ([from the GenBank database](https://www.ncbi.nlm.nih.gov/nucleotide/NC_000023.1){:target="\_blank"}). After the reference a description of the variant is given, in the examples **c.4375C>T** and **g.32389644G>A**.

A description without a reference sequence is near useless. Additional information will then be required to **guess** what reference sequence may have been used. When the guess you made is wrong you of course end up with a variant description which is wrong and the information you retrieved is also not correct. So be **very careful** when you make a guess; it is better to check the source of the original description and ask for the reference sequence that was used.
Additional information to make a guess may come from the **name of the gene** containing the variant, the associated **phenotype** studied (disease), the **chromosome number** and from possibly predicted consequences of the variant on the RNA and/or protein level. Since reference sequences usually change over time, the date of the report describing the variant can give useful information as well.

### DNA > RNA > protein

In nature the DNA code is first transcribed in to a **RNA** molecule ([see Wikipedia](https://en.wikipedia.org/wiki/RNA{:target="\_blank"})). Next, there are two options:
*	the RNA molecule is translated in to a **protein** and the protein is the final product of a gene. Proteins perform a vast array of functions, including catalysing metabolic reactions, DNA replication, responding to stimuli, providing structure to cells, and organisms, transporting molecules from one location to another, etc. ([see Wikipedia](https://en.wikipedia.org/wiki/Protein){:target="\_blank"})).
*	the RNA molecule is the final product of the gene (so the RNA is not translated in to a protein). RNA molecules perform a vast array of functions, including e.g. rRNAs (ribosomal RNA) and tRNAs (transfer RNAs) both active in protein translation. 

Variants are usually detected by reading the DNA code, a method called DNA **sequencing**. A proper report **always** contains the variant described on the DNA level. In addition, a report usually contains a description of the predicted consequence of the variant on the protein, rarely the consequence on RNA. In rare cases, not following current standards, only the predicted consequences at the protein level are reported.

Some variants have an effect on how the transcript (RNA) is generated and consequently on its translation in to protein. When only DNA has been analysed, the consequences of the variant at the RNA and the protein level can only be predicted. The HGVS standard demands predicted consequences have to be **reported in parenthesis**. The predicted consequence of the variant NM\_004006.2:c.4375C>T at the protein level is described as p.(Arg1459*). The "()" warn the variant described is a predicted consequence only.

* * *

## Reference sequences

Variants described on the DNA level are mostly reported in relation to a specific **gene** based on a so called **"coding DNA reference sequence"**. When a coding DNA reference sequence is used, the description of the variant starts with **"c."** (in the example c.4375C>T). Since we nowadays have a reliable reference sequence of the complete human genome, it becomes more common to (also) give the description based on a **"genomic reference sequence"**, starting with **"g."** (g.32407761G>A). In addition the (predicted) consequences on the RNA level (starting with **"r."**) and/or the protein level (starting with **"p."**) may be given. _**NOTE:**_ the "p." addition is often missing when the predicted protein consequences are reported. For details [_see "Reference Sequences"_](http://varnomen.hgvs.org/bg-material/refseq/).

Reference sequences have a format like **NC\_000023.10**, where **NC\_000023** is the **accession number** of the reference sequence and "**.10**" its **version number**. Version numbers are required since we started to use reference sequences at a time our knowledge of the human genome was far from complete. The version number directly follows the accession number and increases over time.

#### Example descriptions

*	genomic (nucleotide)
	*	NC\_ a genomic reference sequence based on a chromosome
		*	NC\_000023.9:g.32317682G>A  (Mar.2006: hg18, NCBI36)
		*	NC\_000023.10:g.32407761G>A  (Feb.2009: h19, GRCh37)
		*	NC\_000023.11:g.32389644G>A  (Dec.2013: hg38, GRCh38)
	*	NG\_ a genomic reference sequence based on a Gene or Genomic region
		*	NG\_012232.1:g.954966C>T
	*	LRG\_ a genomic reference sequence, used in a diagnostic setting, based on a Gene or Genomic region
		*	LRG\_199:g.954966C>T
*	transcript (RNA, nucleotide)
	*	NM\_ a reference sequence based on a protein coding RNA (mRNA)
		*	NM\_004006.2:c.4375C>T
	*	NR\_ a reference sequence based on a non-protein coding RNA
		*	NR_002196.1:n.601G>T
*	protein (amino acid)
	*	NP\_ a reference sequence based on a protein (amino acid) sequence
		*	NP\_003997.1:p.Arg1459* (p.Arg1459Ter)

### Genomic reference sequences

For human the reference sequence **accession number** directly in front of the version number gives the number of the chromosome: 1-22, 23 for the X-chromosome and 24 for the Y-chromosome. In NC\_000023.10 this number is "23" so a reference sequence of human **chromosome X**.

In many cases the reference sequence is not given but a so called genome build is mentioned. The genome build has two formats, either "hg" and a number (hg18, hg19, hg38) or "GRCh/NCBI" and a number (NCBI35, NCBI36, GRCh37, GRCh38). A **genome build** is an attempt to reconstruct the full human genome sequence based on all data available at the time of building the reference sequence. The most frequently used genome builds are called hg18 / NCBI36 (from March 2006), hg19 / GRCh37 (from February 2009) and hg38 / GRCh38 (from December 2013). Having the genomic reference sequence (like NC\_000023.10) is most precise. When the reference sequence is missing you need to know the genome build used. **In addition**, when using a website or database to find more information on the variant, make sure you know the genome build (reference sequence) used by the database.
_**NOTE:**_	genome builds are versioned as well, using so called **"patches"** (e.g. p1) in which errors are corrected.

Genomic reference sequences can also be based on smaller sequences not covering an entire chromosome. They usually cover only a specific gene or specific genomic segment. The most frequently used are **LRG's** (Locus Genomic Reference sequences, format LRG\_199) or NG's (RefSeq Gene reference sequences, format NG\_012232.1).

### Coding DNA reference sequences

In a human diagnostic setting the most frequently used reference is a **"coding DNA reference sequence"** (description starting with **"c."**, e.g. NM\_004006.3:c.4375C>T). Variant descriptions based on this format are very popular because they directly link to the encoded protein. In protein coding DNA reference sequences numbering **starts** with 1 at the first position of the protein coding region, the A of the translation initiating ATG triplet. Numbering **ends** at the last position of the ending triplet, the last position of the translation stop codon (TAA, TAG or TGA). When you divide the position number from a "c." description by three you get the affected amino acid residue from the protein sequence (description starting with "p."); for NM\_004006.3:c.4375C>T (with predicted consequence on protein level p.(Arg1459*)), i.e. 4375 divided by three gives amino acid 1459.
_**NOTE:**_	positions in front of the protein coding sequence get a minus sign (e.g. **"c.-26"**), those after the translation stop an asterisk (e.g. **"c.\*85"**). Numbering in intronic sequences has a format like c.530+6 or c.531-23. For details [_see "Reference Sequences"_](http://varnomen.hgvs.org/bg-material/refseq/).
	The most frequently used coding DNA reference sequences are the NM's (RefSeq gene transcript sequences, e.g. NM\_004006.2) and LRG's (Locus Genomic Reference sequences, e.g. LRG\_199t1).

* * *

## Variants

Depending on the change found, the description of the variant can have many different formats. For a detailed overview we refer to the specific pages on this website [_see header "Recommendations"_](http://varnomen.hgvs.org/recommendations){:target="\_blank"}. Here we will list and briefly explain, the major variant types.

A standard variant description has the format **"prefix.position(s)\_change"**. In the variant description c.4375C>T the prefix **"c."** indicates the type of reference sequence used ("c." indicating a coding DNA reference sequence), **"4375"** the position of the nucleotide(s) affected and **"C>T"** the change (a C changed to T).

### Types of variants

All variants given are in the DMD gene and reported in relation to coding DNA reference sequence LRG\_199t1 (NM\_004006.3).

*	substitution
	:	one letter (nucleotide) of the DNA code is replaced (substituted) by one other letter. On DNA and RNA level a substitution is indicated using **">"**.
	*	c.4375C>T
		:	the C nucleotide at position c.4375 changed to a T
*	deletion
	:	one or more letters of the DNA code are missing (deleted). A deletion is indicated using **"del"**.
	*	c.4375\_4379del
		:	the nucleotides from position c.4375 to c.4379 (CGATT) are missing (deleted). Also reported as c.4375\_4379delCGATT.
*	duplication
	:	one or more letters of the DNA code are present twice (doubled, duplicated). A duplication is indicated using **"dup"**.
	*	c.4375\_4385dup
		:	the nucleotides from position c.4375 to c.4385 (CGATTATTCCA) are present twice (duplicated). Often reported as c.4375\_4385dupCGATTATTCCA or c.4385\_4386insCGATTATTCCA (not a correct HGVS description).
*	insertion
	:	one or more letters in the DNA code are new (inserted). An insertion is indicated using **"ins"**.
	*	c.4375\_4376insACCT
		:	the new sequence "ACCT" was found inserted between positions c.4375 and c.4376.
*	deletion/insertion (indel)
	:	one or more letters in the DNA code are missing and replaced by several new letters. A deletion/insertion is indicated using **"delins"**.
	*	c.4375\_4376delinsAGTT
		:	the nucleotides from position c.4375 to c.4376 (CG) are missing (deleted) and replaced by the new sequence "AGTT". Also reported as c.4375\_4376delCGinsAGTT.
	
There are more variant types yet these occur less frequently. For details [_see header "Recommendations"_](http://varnomen.hgvs.org/recommendations){:target="\_blank"}.

### Aliases

It should be noted that **one variant**, based on different reference sequences used, can be described in many different ways. Variant c.5234G>A in the DMD gene can be described based on different genomic reference sequences (e.g. NC\_000023.9:g.32290917C>T, NC\_000023.10:g.32380996C>T, NC\_000023.11:g.32362879C>T, NG_012232.1:g.981731G>A, LRG_199:g.981731G>A) as well as different coding DNA reference sequences (e.g. LRG\_199t1:c.5234G>A, NM\_004006.3:c.5234G>A, NM\_004009.3:c.5222G>A, NM\_000109.3:c.5210G>A, NM\_004007.2:c.4865G>A, NM\_004010.3:c.4865G>A, NM\_004011.3:c.1211G>A, NM\_004012.3:c.1202G>A). These alternative descriptions are rather confusing, especially when reference sequences are not properly listed. Consequently, when databases or the internet are queried for information regarding the potential consequences of specific variants, errors are easily made. 

* * *

### Other descriptions

Sometimes variants are not described using the format **reference:description** (NM\_004006.3:c.4375C>T) explained above but using an identifier (ID) in another database. Common formats include a rs ID (from dbSNP, [_rs128627255_](http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs128627255){:target="\_blank"}), OMIM ID (from OMIM, [_OMIM300377:0073_](http://omim.org/entry/300377#0073){:target="\_blank"}), LOVD ID (from LOVD, [_DMD\_000073_](http://www.LOVD.nl/DMD_000073){:target="\_blank"}), RCV ID (from ClinVar, [_RCV000012030_](https://www.ncbi.nlm.nih.gov/clinvar/RCV000012030/){:target="\_blank"}), etc. In most cases, using these IDs, the database can be used to find the full description of the variant using the approved HGVS format **reference:description**.

* * *

## Missing information

When a reference sequence is not known the best way forward is to try and get the name of the gene that is affected by the variant. All genes have an official abbreviation, the so called **gene symbol**. For the Duchenne muscular dystrophy gene the gene symbol is "DMD". The [HGNC](http://www.genenames.org){:target="\_blank"} (HUGO Gene Nomenclature Committee) keeps a catalog of all approved gene symbols (and their aliases/synonyms). The HGNC site can be used to find the gene symbol and check whether the name/symbol you have is the officially approved one. Using "dystrophin", the name of a protein, you will see this is an alias for the Duchenne muscular dystrophy gene, official gene symbol ["DMD"](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2928){:target="\_blank"}. HGNC, and many other sources, can also tell you on which human chromosome a gene is so to which chromosome the variant description you have may relate.

When you are interested in what is known about a specific variant the best start is a Gene variant database, also called Locus-Specific Database (LSDB)... _in preparation_ ...
