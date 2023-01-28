---
layout: default-md
title: SVD-WG008
category: SVD-WG
---

## Community Consultation

### Proposal SVD-WG008 (Reference Sequences)

*	Status: <font color="red">accepted</font>
	:	proposal SVD-WG008 opened for **Community Consultation** on July 20 (2019), closed September 30 (2019). 

The proposal suggested to specify the HGVS recommendations for acceptable Reference Sequences. Based on the proposal the  [_Reference Sequences_](https://varnomen.hgvs.org/bg-material/refseq/){:target="\_blank"} page has been updated (April 2020).

* * *

### Background

A sequence variant is defined in the context of a **reference sequence** which must be referred to by means of a unique **sequence identifier**. Because a reference sequence defines the [_numbering system_](https://varnomen.hgvs.org/bg-material/numbering/){:target="\_blank"} and default state of a sequence (e.g. coding transcript, non-coding transcript), accurately interpreting a sequence variant requires that both the reference sequence and its reference sequence identifier are unchangeable.

### Proposal

*	reference sequences **must** come from data sources that provide stable and permanent identifiers, e.g. RefSeq (NCBI) and Ensembl (EBI). A source that permits updating of sequence records associated with an existing sequence identifier **must not** be used, i.e. a change in the reference sequence **must** trigger a change in the sequence identifier.
	*	Rationale: violating this requirement means that interpretation of a variant might change over time
*	reference sequences **must** use conventional representation, i.e. the sequence comprises a string of [_IUPAC residues_](https://varnomen.hgvs.org/bg-material/standards/){:target="\_blank"} that represents a nucleic acid or amino acid sequence using the conventional order (5'-to-3' for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences) 
*	reference sequence **must** be contiguous, undefined sequence is not permissible.
	*	this requirement applies within a **single** sequence. Alignments **between** sequences may contain gaps. For example, a coding sequence will contain intron gaps when aligned to a genomic sequence
	*	[_IUPAC symbols_](https://varnomen.hgvs.org/bg-material/standards/){:target="\_blank"} for any base (N) or any amino acid (X) are permitted within a contiguous sequence, e.g. within chromosomal reference sequences, and are not considered as undefined
*	a sequence identifier **must** only ever identify **one** reference sequence, and the sequence referred to by a sequence identifier may not be deleted or changed
	*	sequence identifiers are opaque(1). That is, the structure and meaning of an identifier is determined by the source reference sequence database
	*	versioned reference sequence identifiers are required only when the reference sequence databases use versioning to distinguish between unique sequences
		*	RefSeq and Ensembl reference sequence identifiers use version numbers to distinguish between sequences. In the context of these reference sequences, variant descriptions lacking a version number are **not** valid. 
		*	LRG provides equivalent uniqueness but does not use version numbers
		*	the sequence identifier **must** be included in **all** representations of a reference sequence, i.e. annotated records and downloadable formats such as fasta
*	only reference sequences considered to be **“complete”** (as defined in the bullet points below) are suitable for defining sequence variation. The reference sequence database **must** provide a mechanism which allows simple and definitive identification of **“complete”** sequences
	*	the mechanism that identifies a complete record may be embedded in the sequence identifier or may be defined within the reference sequence record
	*	a reference sequence representing a protein-coding transcript **must** contain a complete CDS, otherwise it should be considered the supporting evidence is insufficient to support the use of the transcript
		*	the first three bases of the CDS must be clearly annotated within the reference sequence record
		*	the translation termination codon must be clearly annotated within the reference sequence record
	*	predicted or inferred sequences **should not** be used for variant reporting
	*	if a reference sequence becomes unsupported or refuted by evidence, it should no longer be used
*	the reporting of sequence variants **must** be with respect to the most appropriate reference sequence and the entirety of the variant sequence **must** be encompassed by the selected reference sequence
	*	intronic sequences are considered to be within the boundaries of a transcript reference sequence but a valid gene or genomic reference sequence identifier **must** also be provided, NG\_012232.1(NM\_004006.2):c.93+1G>T (intronic nucleotides defined in the context of a RefSeqGene reference sequence) or NC\_000023.11(NM\_004006.2):c.93+1G>T (intronic nucleotides defined in the context of a chromosomal reference sequence)
	*	where possible, users should report sequence variation at the genome or gene level as well as the transcript level to enable accurate mapping between transcript reference sequences via the genomic or gene position(s)

### Recommended Reference Sequences types are:

*	RefSeq sequences with the prefixes NC\_, NT\_, NW\_,NG\_, NM\_, NR\_ or NP\_
	*	chromosome - NC\_000023.11
	*	genomic contigs or scaffolds - NT\_010718.17, NW\_003315950.2
	*	gene/genomic region - NG\_012232.1
	*	coding transcript - NM\_004006.2
	*	non-coding transcript - NR\_004430.2
	*	protein - NP\_003997.1
*	LRG sequences with the prefixes LRG\_#, LRG\_#t#, LRG\_#p# (see examples below)
	*	gene/genomic region - LRG\_199
	*	coding transcript (or non-coding transcript) - LRG\_199t1
	*	protein - LRG\_199p1
*	Ensembl transcript (ENST) and protein (ENSP) which are not identified by Ensembl as being incomplete, e.g. CDS 5' incomplete (cds_start_NF), CDS 3' incomplete (scs_end_NF)
	*	gene/genomic region - ENSG00000198947.15
	*	coding transcript - ENST00000357033.8
	*	non-coding transcript - ENST00000383925.1
	*	protein - ENSP00000354923.3

### Notes

(1) an [opaque identifier](https://indieweb.org/opaque){:target="\_blank"} is one that acts only as a name for an object and that is not intended to be parsed for additional meaning. Contrast with a RefSeq identifier, for example, which conveys annotation level (N versus X), type (M, R, C, etc.), and version number. So, this comment is intended to tell implementers that they **may not** rely on parsing the identifier to decide how the implementation works

Why not? Two reasons:
*	because it creates a "tight coupling" between two systems that have no coordination. For example, what if NCBI wants to change the meaning of the identifers?
*	because it precludes other systems that might have perfectly valid identifiers. In particular, the thinking here relates to future graph genome work in which segments might be referred to by other ids (perhaps ids not even shared). If the implementation were to **require** that g. variant accessions start with NC\_ (or any predefined list), it would make it impossible to use that software in other contexts
