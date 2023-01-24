---
layout: default-md
title: Checklist
order: 7
---

# {{ page.title }}

* * *

## Purpose

Going through publications one can easily see where people give variant descriptions that **do not correctly follow HGVS nomenclature**. The checklist below covers the most frequently offended rules. Going through should assist you while preparing a publication containing sequence variant descriptions.

* * *

## Checklist

1.	**Reference Sequence** - do you clearly mention the reference sequence used for numbering (nucleotides/amino acids) ?
	:	A publication should mention, preferably in the Materials & Methods section and/or Figure or Table legend, which reference sequence file was used to describe variants and for numbering of the residues (DNA, RNA and protein ([_see Reference Sequences_](/bg-material/refseq))).
	*	do you mention a GenBank (not _Gen**<u>e</u>**Bank_) RefSeq-file with accession  _**and version number**_ ?; do not forget the underscore in the accession number (correct is NM\_004006**.2**, not _NM004006.2_).
	*	genomic (**g.**) reference sequences start with nucleotide 1 and can not have nucleotides with additions like a +, - or *.
	*	for a coding DNA reference sequence, do you clearly state that nucleotide numbering starts with the A of the ATG translation initiation site as _**nucleotide 1**_ ?
	*	legacy numbering is only allowed _**in addition to**_ approved numbering
	*	does your reference sequence contain the residue that you describe as changed ?
	:	_**NOTE**_: **NM\_** reference sequences cover mature transcripts, do _**not contain**_ intron and gene flanking sequences, and can only be used to describe variants in introns using a "c." prefix when a genomic reference sequence is given on which the coding DNA reference sequence is annotated, e.g. "NC\_000023.10(NM\_004006.2):c.94-2A>G" or "LRG\_199t1:c.94-2A>G" ([_see Reference Sequences_](/bg-material/refseq/#DNAc))
2.	**Intronic variants** - are descriptions of intron variants correct and complete ?
	*	descriptions referring to exon or intron numbers instead of nucleotide positions, e.g."_c.IVS4-2A>G_", are **not allowed**.
	*	do you properly describe ranges in the introns ?  The format c.123-65\_123-50 is correct, the format c.123-65**\_-50** is not, it is **incomplete**.
3.	**Insertions** - are descriptions of insertions correct and complete ([_see Insertion_](/recommendations/DNA/variant/insertion))?
	*	insertions should be reported using the format c.51\_52insT.
	:	The format c.52insT is **incomplete** and not allowed.
	*	do you give the inserted sequence?
	:	Describing a variant as c.5439\_5430**ins6** is not allowed, the inserted sequence (for ins6 e.g. "TGCCAT") should be specified.
	*	is the insertion reported indeed an insertion or is it in fact a duplication?
	:	**Duplicating insertions** should be described as duplications, not as insertions ([_see Duplication_](/recommendations/DNA/variant/duplication)). 
4.	**The 3' rule** - do you correctly apply the 3' rule?
	:	For deletions, duplications and insertions the **most 3' position possible is arbitrarily assigned** to have been changed ([_see General recommendations_](/recommendations/general)). This rule also applies to variants in single residue stretches (mono-nucleotide or amino acid) or tandem repeats.
5.	**Range** - the sign used to indicate a range is the "\_" (underscore), not a "-" (minus)?  
	The correct description to indicate a deletion of coding DNA nucleotides 12 to 14 is c.12\_14del. Not correct is _c.12-14del_, this describes a deletion of nucleotide -14 in the intron directly 5' of nucleotide c.12 ([_see Numbering_](/bg-material/numbering)).
6.	**Deletion** - do you indicate the first and last residue involved in a deletion?  
	Descriptions like _g.123del3_ are not allowed, correct is g.123\_125del ([_see Deletion_](/recommendations/DNA/variant/deletion)).
7.	**Describe always at DNA-level** - do you describe all changes reported at DNA-level?  
    All changes reported **must** be described at DNA-level
	*	when descriptions at protein level are given in the text, upon first appearance, use a format like "c.76G>T (p.(Gly26Cys), RNA not analysed)" or "c.76G>T (r.76g>u p.Gly26Cys)"
7.	**RNA level descriptions**  
    HGVS nomenclature includes recommendations for the description of changes detected at the RNA level ([_see Recommendations_](/recommendations/RNA)).
    *	several transcripts derived from one allele are described using the format r.[76a>c,73\_88del] ([_see RNA_](/recommendations/RNA/variant/alleles))
9.	**protein level descriptions**
	*	the protein reference sequence should represent the primary translation product, not a processed mature protein, and thus include the starting Methionine and a signal peptide sequence
    *   the recommendation is to use **three letter amino acid code** ([_see Protein_](/recommendations/protein/))	
    *   **"Ter" or "\*" should be used** to indicate a translation stop codon; the X should not be used ([_see Protein_](/recommendations/protein/))
	*	predicted "**silent**" protein level variants are described as **p.(Leu54=)**, not as _p.Leu54Leu_ or _p.54L/L_).
	*	the description p.(Met1Val) is not allowed ([_see Protein_](/recommendations/protein/variant/substitution))
10.	**Mutation / polymorphism**  
	Do not use the terms "mutation" or "polymorphism" ([_see General recommendations_](/bg-material/basics))
	*	"polymorphic" variants should not be described using the "/" (slash), describe them as normal variants like c.127A>G and p.(Ile43Val).
11.	**Recessive diseases** - do you clearly describe which changes are found in which combination?  
	A publication describing variants in patients suffering from a recessive phenotype should, for each individual, explicitly mention **which variants were found and in which combination (per allele)**.
12.	**Tabular overview** - is the overview of all changes reported clear and complete?
	:	Preferably, a publication contains a **tabular overview** of all variants reported. This overview contains columns describing the change at the DNA-level (**absolutely essential**) and, optional, at the RNA and protein level.
	:	When data on RNA and/or protein level are provided, it should be made clear whether the data were **deduced or experimentally verified** (i.e. state explicitly when RNA was analysed, e.g. to study the consequences of a variant affecting splicing).
	:	Make sure **predicted** consequences at protein level are reported in parentheses, like p.(Arg123Ser).
13	**Variant types**
	:	When giving numbers regarding the types of variants identified do **not mix numbers** at DNA, RNA and protein level. Give numbers separately for DNA, RNA and protein. Where would you list a substitution at DNA level, giving a deletion at RNA level (since it affects splicing) and a frame shift at protein level?
14.	**Pathogenic**  
	Be careful when using the term "pathogenic" ([_see General recommendations_](/bg-material/basics)). A variant in itself is not "pathogenic", whether it can be causally related to a phenotype observed in a patient is determined by other factors. 
