---
layout: default-md
title: SVD-WG006
category: SVD-WG
---

## Community Consultation

### Proposal SVD-WG006 (circular DNA)

*	Status: <font color="red">accepted</font>
	:	proposal SVD-WG006 opened for **Community Consultation** on August 1 (2018), closed on Oct.30 (2018). 

The proposal suggests to extend the HGVS recommendations to improve the description of variants affecting circular DNA molecules by;

*	allowing the description of variants based on a circular genomic reference sequence indicated by the **prefix "o."**. In a circular genomic reference sequence nucleotide numbering starts with 1 at the first nucleotide of the sequence and ends at the last nucleotide.
*	adding the exception that for circular genomic reference sequences ("o." and "m." prefix) the nucleotide positions **may be listed from 3’ to 5’** when the rearrangement includes both the last and first nucleotides of the reference sequence

* * *

#### Examples

*	NC\_012920.1:m.16563\_13del
	:	compared to the mitochondrial reference sequence (NC\_012920.1, a circular DNA molecule) the region from nucleotides m.16563 to m.13 is deleted
	:	_**NOTE:**_	for mitochondrial reference sequences the "m." prefix will be used
*	J01749.1:o.4344_197dup
	:	compared to the circular genomic reference sequence of plasmid pBR322 (J01749.1) the region from nucleotides o.4344 to o.197 is duplicated

* * *

### Note

For deletions the current recommendations state: the “position(s)\_deleted” **should be listed from 5’ to 3’**, e.g. 123_126 not 126_123. As a consequence a deletion involving the start/end of a mitochondrial reference sequence can not be described as NC\_012920.1:m.16563\_13del. Adding the exception simplifies the description of rearrangements involving both the last and first nucleotides of circular DNA molecules.
The suggestion to use the **"o." prefix** should help to discriminate circular from non-circular genomic reference sequences. While less relevant for human genetics, circular DNA sequences are common in nature (e.g. viruses, bacterial genomes, plasmids, chloroplast). Allowing the "o." prefix simplifies recognition of circular reference sequences, simplifies the description of deletions/duplications involving both the last and first nucleotides and promotes the wider implementation of HGVS nomenclature. The "o." prefix will also help computational tools to check correct variant descriptions. 
