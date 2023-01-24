---
layout: default-md
title: Reference Sequences
order: 2
---

# {{ page.title }}

* * *

## Definition

a sequence file that is used as a **reference to describe variants** that are present in a sequence analysed.

* * *

_**NOTE:**_ this section has been updated based on the accepted proposal [_SVD-WG008 (Reference Sequences)_](http://varnomen.hgvs.org/bg-material/consultation/svd-wg008/).

A sequence variant is defined in the context of a **reference sequence** which must be referred to by means of a unique **sequence identifier**. Because a reference sequence defines the [_numbering system_](https://varnomen.hgvs.org/bg-material/numbering/){:target="\_blank"} and default state of a sequence (e.g. coding transcript, non-coding transcript), accurately interpreting a sequence variant requires that both the reference sequence and its corresponding identifier are unchangeable.

*	reference sequences **must** come from data sources that provide stable and permanent identifiers, e.g. RefSeq (NCBI) and Ensembl (EBI). A source that permits updating of sequence records associated with an existing sequence identifier **must not** be used, i.e. a change in the reference sequence **must** trigger a change in the sequence identifier
	*	rationale: violating this requirement means that interpretation of a variant might change over time
*	reference sequences **must** use conventional representation, i.e. the sequence comprises a string of [_IUPAC codes_](https://varnomen.hgvs.org/bg-material/standards/){:target="\_blank"} that represents a nucleic acid or amino acid sequence using the conventional order (5'-to-3' for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences) 
*	reference sequence **must** be contiguous; undefined sequence is not permissible
	*	this requirement applies within a **single** sequence. Alignments **between** sequences may contain gaps. For example, a coding sequence will contain intron gaps when aligned to a genomic sequence
	*	[_IUPAC codes_](https://varnomen.hgvs.org/bg-material/standards/){:target="\_blank"} for any nucleotide (N) or any amino acid (X) are permitted within a contiguous sequence, e.g. within chromosomal reference sequences, and are not considered as undefined
*	a sequence identifier **must** only ever identify **one** reference sequence, and the sequence referred to by a sequence identifier may not be deleted or changed
	*	sequence identifiers are opaque ([_note 1_](#note)), i.e. the structure and meaning of an identifier is determined by the source reference sequence database
	*	versioned reference sequence identifiers are required only when the reference sequence databases use versioning to distinguish between unique sequences
		*	RefSeq and Ensembl reference sequence identifiers use version numbers to distinguish between sequences. In the context of these reference sequences, variant descriptions lacking a version number are **not** valid. NM\_004006**<font color="red">.3</font>** is correct, NM\_004006 is not correct (lacks the essential version number)
		*	the sequence identifier **must** be included in **all** representations of a reference sequence, i.e. annotated records and downloadable formats such as fasta files
*	only reference sequences considered to be **“complete”** (as defined in the bullet points below) are suitable for defining sequence variation. The reference sequence database **must** provide a mechanism which allows simple and definitive identification of **"complete"** sequences
	*	the mechanism that identifies a complete record may be embedded in the sequence identifier or may be defined within the reference sequence record
	*	a reference sequence representing a protein-coding transcript **must** contain a complete CDS, otherwise it should be considered that the supporting evidence is insufficient to support the use of the transcript
		*	the first three nucleotides of the CDS must be clearly annotated within the reference sequence record
		*	the translation termination codon must be clearly annotated within the reference sequence record
	*	predicted or inferred sequences **should not** be used for variant reporting
	*	if a reference sequence becomes unsupported or refuted by evidence, it should no longer be used
*	a "**<font color="red">:</font>**" (colon) is used as a separator between the reference sequence file identifier (_accession.version-number_) and the actual description of a variant; NC\_000011.9**<font color="red">:</font>**g.12345611G>A
*	the **recommended reference** is a genomic reference sequence based on a recent genome build, e.g. NC\_000023.11 (for _Homo sapiens_ chromosome X, build GRCh38/hg38)
*	specifications to a specific annotated segment of a reference sequence can be given in parentheses directly after the reference sequence
	*	NG\_012232.1(NM\_004006.2) indicates that the variant to be described, is based on the coding DNA reference sequence NM\_004006.2 as annotated in NG\_012232.1
	*	accepted specifications include transcripts (NM\_004006.2) and proteins (NP\_003997.1). Gene symbols should **not** be used as specification. **Exception:** genes annotated on a genomic reference for which no transcript reference sequence is available, e.g. the Homo sapiens mitochondrion complete genome (GenBank NC\_012920.1).
*	the reporting of sequence variants **must** be with respect to the most appropriate reference sequence and the entirety of the variant sequence **must** be encompassed by the selected reference sequence
	*	the reference sequence used **must contain** the variant residue that is described as being changed
	*	a **coding** or **non-coding** DNA reference sequence does not contain intron or 5' and 3' gene flanking sequences and **can not be used** to describe variants in introns and up/down-stream of the gene
		*	5' and 3' flanking sequences are considered to be **outside the boundaries** of a transcript reference sequence and **can not be used** to describe variants
		*	intronic sequences are considered to be **within the boundaries** of a transcript reference sequence and may be used to describe a variant when a genomic reference sequence identifier is provided, e.g.  NC\_000023.11(NM\_004006.2):c.93+1G>T (intronic nucleotides defined in the context of a chromosomal reference sequence) or NG\_012232.1(NM\_004006.2):c.93+1G>T (intronic nucleotides defined in the context of a RefSeqGene reference sequence)
			*	**not correct:** NM\_004006.2:c.357+1G>A, LRG\_199:c.357+1G>A
			*	**correct:** NC\_000023.10(NM\_004006.2):c.357+1G>A, NG\_012232.1(NM\_004006.2):c.357+1G>A, LRG\_199t1:c.357+1G>A
	*	where possible, users should report sequence variation at the genome or gene level as well as the transcript level to enable accurate mapping between transcript reference sequences via the genome or gene position(s)

### Recommended Reference Sequences types are:

*	RefSeq sequences with the prefixes NC\_, NT\_, NW\_,NG\_, NM\_, NR\_ or NP\_
	*	chromosome - NC\_000023.11
	*	genomic contigs or scaffolds - NT\_010718.17, NW\_003315950.2
	*	gene/genomic region - NG\_012232.1
	*	coding transcript - NM\_004006.2
	*	non-coding transcript - NR\_004430.2
	*	protein - NP\_003997.1
*	Ensembl transcript (ENST) and protein (ENSP) which are not identified by Ensembl as being incomplete, e.g. CDS 5' incomplete (cds_start_NF), CDS 3' incomplete (cds_end_NF)
	*	gene/genomic region - ENSG00000198947.15
	*	coding transcript - ENST00000357033.8
	*	non-coding transcript - ENST00000383925.1
	*	protein - ENSP00000354923.3
*	LRG sequences with the prefixes LRG\_#, LRG\_#t#, LRG\_#p# (see examples below)
	*	gene/genomic region - LRG\_199
	*	coding transcript (or non-coding transcript) - LRG\_199t1
	*	protein - LRG\_199p1

* * *

## Reference Sequence Types

Depending on the variants to be reported, different reference sequence files are used at the DNA, RNA or protein level. It is mandatory to indicate the type of reference sequence file using a **prefix** preceding the variant description. Approved reference sequence types are **c.**, **g.**, **m.**, **n.**, **o.**, **p.** and **r.**: 

*	#### DNA
	*	**g.**	=	[linear genomic reference sequence](#DNAg)
	*	**o.**	=	[circular genomic reference sequence](#DNAo)
	*	**m.**	=	[mitochondrial reference](#DNAg) (special case of a circular genomic reference sequence)
	*	**c.**	=	[coding DNA reference sequence](#DNAc) (based on a protein coding transcript)
	*	**n.**	=	[non-coding DNA reference sequence](#DNAn) (based on a transcript not coding for a protein)
*	#### RNA
	*	**r.**	=	[RNA reference sequence](#RNAr)
*	#### protein
	*	**p.**	=	[protein reference sequence](#proteinp)
*	the recommended DNA reference is a genomic reference sequence

* * *

{:#DNAg}

### DNA - genomic reference sequence (g.)

*	linear genomic reference sequences are indicated using a **g.** prefix 
	:	genomic reference sequences include all **linear** DNA molecules and are preferably based on a recent genome build
	:	for human the recommended reference is based on genome build GRCh38/hg38, e.g. NC_000023.11 for the chromosome X
	:	_**NOTE:**_  since new LRG’s are no longer generated, the recommendation to use for diagnostic applications preferably a [Locus Reference Genomic sequence (LRG)](http://www.lrg-sequence.org/){:target="\_blank"} has been retracted
*	a gene-based genomic reference sequence (NG_, LRG_);
	*	should include all known exons and cover all known transcripts
	*	to facilitate the description of variants in immediate gene flanking regions (e.g. the promoter region), should contain several kilobases of 5' upstream (recommended is 5 kb) and 3' downstream (recommended 2 kb) sequences
*	when a complete genomic reference sequence is not available, a coding DNA reference sequence should be used.
*	tools like the [Mutalyzer suite](http://www.mutalyzer.nl/position-converter){:target="\_blank"} and [Variant Validator](http://www.variantvalidator.org){:target="\_blank"} can help to predict the consequences of a variant on all properly annotated transcripts, incl. when they derive from overlapping genes.


{:#DNAo}

### DNA - circular genomic reference sequence (o.)

*	circular genomic reference sequences are indicated using a **o.** prefix
	:	circular genomic reference sequences include chloroplast sequences, plasmid sequence, viral resuence, etc.
	:	_**Exception:**_  the **m.** prefix for a mitochondrial reference sequence is well-established, universally used, unequivocal, and therefore recommended for reporting variants in a mitochondrial sequence.


{:#DNAm}

### DNA - mitochondrial reference sequence (m.)

*	mitochondrial genomic reference sequences are indicated using a **m.** prefix
	:	a mitochondrial reference sequence is a special type of circular genomic reference sequence. Since the **m.** prefix is well-established, universally used and unequivocal the use of a mitochondrial reference sequence is indicated using the **m.** prefix
*	the preferred human mtDNA reference sequence is the [_Homo sapiens_ mitochondrion, complete genome (GenBank NC_012920.1)](http://www.ncbi.nlm.nih.gov/nucleotide/NC_012920.1){:target="\_blank"}.
	:	_**NOTE:**_	the mtDNA reference sequence is a **circular molecule** ([_see Open Issues_](/recommendations/open-issues/#circular))


{:#DNAc}

### DNA - coding DNA reference sequence (c.)

*	coding DNA reference sequences are indicated using a **c.** prefix	
*	a coding DNA reference sequence is a DNA reference sequence, based on a protein-coding transcript of a gene, which can be used for nucleotide numbering using the  **c.** prefix. Such a reference sequence includes the coding DNA sequence (CDS) and the 5' and 3' UTR regions.
	*	for human the recommended transcript to be used to describe variants is the transcript recommended by the **MANE project** (see [Ensembl](http://tark.ensembl.org/web/mane_project/){:target="\_blank"} or [NCBI](https://www.ncbi.nlm.nih.gov/refseq/MANE/){:target="\_blank"}). The MANE project is a joint initiative between EMBL-EBI’s Ensembl project and NCBI’s RefSeq project to release a genome-wide transcript set containing at least one well-supported transcript per protein-coding locus. All transcripts in the MANE set perfectly align to GRCh38 and will represent 100% identity (5’ UTR, coding sequence, 3’ UTR) between the corresponding RefSeq (NM\_) and the Ensembl (ENST) transcript.
*	a coding DNA reference sequence does **not contain** intron or 5' and 3' gene flanking sequences and can **not be used** to describe variants in introns and up/down-stream of the gene. Intronic sequences are considered to be **within the boundaries** of a transcript reference sequence and may be used to describe a variant when a genomic reference sequence identifier is provided.
*	when, based on a genomic reference sequence, variants are reported using a "**c.**" prefix, the transcript variant used should be indicated
	*	for NC\_ or NG\_ reference sequences the annotated transcript used is given in parentheses directly following the accession.version number, giving variant descriptions like NC\_000023.10(NM\_004006.3):c.357+1G>A or NG\_012232.1(NM\_004006.2):c.357+1G>A
	*	for LRG\_'s an annotated "**transcript variant 1**" is described as "**<font color="red">t1</font>**", e.g. LRG\_199**<font color="red">t1</font>**:c.11T>G
*	the coding DNA reference sequence should be complete, cover the major and largest transcript known
	*	for human, [EBI](http://www.ensembl.org/Help/Glossary?id=346){:target="\_blank"} uses the following hierarchy to select the prefered transcript: **1.** longest CCDS translation with no stop codons. **2.** if no (1), choose the longest Ensembl/Havana merged translation with no stop codons. **3.** if no (2), choose the longest translation with no stop codons. **4.** if no translation, choose the longest non-protein-coding transcript.
*	when a **gene is located on the minus strand** the location of a variant nucleotide may differ when described based on a genomic or a coding DNA reference sequence. Applying the 3'rule, NC\_000023.10:g.32361300del describes the deletion of a T from a mononucleotide stretch in the DMD gene. On the opposite strand NC\_000023.10:g.32361300 links to nucleotide NM\_004006.1:c.5690. However, applying the 3'rule, based on a coding DNA reference sequence this variant is described as NM\_004006.1:c.5697del (linking to NC\_000023.10:g.32361293). See also [different genomic (g.) and coding DNA (c.) descriptions](/recommendations/DNA/variant/repeated/).

{:#DNAn}

### DNA - non-coding DNA reference sequence (n.)

*	non-coding DNA reference sequences are indicated using a **n.** prefix
*	a non-coding DNA reference sequence is a DNA reference sequence, based on a transcript of a gene which does not encode a protein. It can be used for nucleotide numbering using the  **n.** prefix.
*	a non-coding DNA reference sequence does **not contain** intron or 5' and 3' gene flanking sequences and can **not be used** to describe variants in introns and up/down-stream of the gene. Intronic sequences are considered to be **within the boundaries** of a transcript reference sequence and may be used to describe a variant when a genomic reference sequence identifier is provided.
	*	for human the recommended transcript to be used to describe variants is the transcript recommended by the **MANE project** (see [Ensembl](http://tark.ensembl.org/web/mane_project/){:target="\_blank"} or [NCBI](https://www.ncbi.nlm.nih.gov/refseq/MANE/){:target="\_blank"}).
*	when, based on a genomic reference sequence, variants are reported using a "**n.**" prefix, the transcript variant used should be indicated
	*	for LRG\_'s the annotated "**transcript variant 1**" is described as "**<font color="red">t1</font>**", e.g. LRG\_163**<font color="red">t1</font>**:n.5C>T
*	the non-coding DNA reference sequence should be complete, cover the major and largest transcript known
*	when a **gene is located on the minus strand** the location of a variant nucleotide may differ when described based on a genomic or a coding DNA reference sequence (see example under coding DNA reference sequence).

---

{:#RNAr}

### RNA reference sequence (r.)

*	RNA reference sequences are indicated using a **r.** prefix
	*	(human) the recommended transcript to be used to describe variants in a gene is the transcript recommended by the MANE project (see [Ensembl](http://tark.ensembl.org/web/mane_project/){:target="\_blank"} or [NCBI](https://www.ncbi.nlm.nih.gov/refseq/MANE/){:target="\_blank"})
*	when, based on a genomic reference sequence, variants are reported using a "r." prefix, the transcript variant used should be indicated
	*	for NC\_ or NG\_ reference sequences the annotated transcript used is given in parentheses directly following the accession.version number, giving variant descriptions like NC\_000023.10(NM\_004006.2):r.357\_358ins357+1\_357+12 or NG\_012232.1(NM\_004006.2):r.357\_358ins357+1\_357+12
	*	for LRG\_'s the annotated "**transcript variant 1**" is described as "**<font color="red">t1</font>**", e.g. LRG\_199**<font color="red">t1</font>**:r.11u>g
*	nucleotide numbering for a RNA reference sequencing follows that of the associated coding or non-coding DNA reference sequence; nucleotide r.123 relates to c.123 or n.123.
* 	the RNA reference sequence includes the entire transcript, excluding the poly A-tail.
*	when a **gene is located on the minus strand** the location of a variant nucleotide may differ when described based on a genomic or a coding DNA reference sequence (see example under coding DNA reference sequence).

---

{:#proteinp}

### protein reference sequence (p.)

*	protein reference sequences are indicated using a **p.** prefix
	*	(human) the recommended transcript to be used to describe variants in a gene is the transcript recommended by MANE project (see [Ensembl](http://tark.ensembl.org/web/mane_project/){:target="\_blank"} or [NCBI](https://www.ncbi.nlm.nih.gov/refseq/MANE/){:target="\_blank"})
*	a protein reference sequence should **correspond exactly** with the associated DNA and RNA reference sequence used
*	when, based on a genomic reference sequence, variants are reported using a "p." prefix, the reference protein isoform used should be indicated
	*	for LRG\_'s the annotated "**protein isoform 1**" is described as "**<font color="red">p1</font>**", e.g. LRG\_199**<font color="red">p1</font>**:p.(Val25Gly)
*	a protein reference sequence should represent the primary translation product, not a processed mature protein, and thus includes the starting Methionine, any signal peptide sequences, etc.

* * *

{:#note}

## Notes

(1) an [opaque identifier](https://indieweb.org/opaque){:target="\_blank"} is one that acts only as a name for an object and that is not intended to be parsed for additional meaning. Contrast with a RefSeq identifier, for example, which conveys annotation level (N versus X), type (M, R, C, etc.), and version number. So, this comment is intended to tell implementers that they **may not** rely on parsing the identifier to decide how the implementation works

Why not? Two reasons:
*	because it creates a "tight coupling" between two systems that have no coordination. For example, what if NCBI wants to change the meaning of the identifers?
*	because it precludes other systems that might have perfectly valid identifiers. In particular, the thinking here relates to future graph genome work in which segments might be referred to by other identifiers (perhaps identifiers not even shared). If the implementation were to **require** that g. variant accessions start with NC\_ (or any predefined list), it would make it impossible to use that software in other contexts

* * *

{:#discuss}

## Q&A

*	Which reference sequence type should I use?
	:	Discussions on the **best reference sequence type to be used** have been very lively. In general it can be concluded that all suggestions made have their pro's and con's and there is no perfect solution.
	**Theoretically**, a genomic reference sequence is the best choice. By simply numbering nucleotides from 1 to the end of the file no problems occur with complex gene structures like multiple transcription start sites (promoters / 5'-first exons), multiple translation initiation sites (ATG-codons), exons and alternative splicing and the use of different 3'-terminal exons and poly-A addition sites.
	**In practice** a coding DNA reference sequence is mostly preferred. The most important reason is that from the description one immediately gets some information regarding the location of the variant; exonic or intronic, 5' of the ATG or 3' of the stop codon and, by dividing the nucleotide number by 3, the position of the amino acid residue that is affected ([_see Nucleotide numbering_](/bg-material/numbering)).

*	When I use a human genome reference sequence is it sufficient to mention the genome build, e.g. hg19 or GRCh37?
	:	No. A genome build is not a real reference sequence which one can download easily to refer to. The original genome assembly is also updated continuously when new sequences become available and when errors are corrected. These updates are published as so called <b>"patches"</b>. While writing this answer, human genome assembly GRCh38/hg38 is at patch version 11 ([GRCh38.p11](https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.37#/def_asm_Primary_Assembly){:target="\_blank"}), dated June 14, 2017. When you report to have used genome build hg38 it is thus not clear whether you mean the original assembly or a specific patched version. The preferred genomic reference sequence is a <b>"NC_" file</b>, e.g. NC_000001.10 for human chromosome 1 from the first release of genome build hg19/GRCh37.

*	Why is it necessary to give both the accession AND version number of a reference sequence?
	:	When for a reference sequence no version number is given it is not possible to correctly deduce the variant described. Take variant NM\_002111:c.211C>T. The description is based on a coding DNA reference sequence of the human HTT (huntingtin) gene. The sequence contains a triplet repeat sequence which is variable in length in the population. Over the years this reference sequence had 8 different versions, from NM\_002111.1 to NM\_002111.8. One of the differences between these sequences is that the length of the Gln-encoding triplet changed in length from 0 to 23 to 21 to 23. As a consequence, when one does not know the version number of NM_002111, one can not know what variant is described with c.358C>T (note that ALL versions have a C nucleotide at position c.358 so there are three different posibilities).

*	What are the disadvantages of using a genomic reference?
	:	**For a human**, a variant described using genomic reference sequence does not contain any useful information; the nucleotide number is just a big number between 1 and 250,000,000. In addition;
	:	*	descriptions of variants are very long making them impractical to use, e.g. NC\_000006.11:g.117198495\_117198496del compared to LRG\_199t1:c.57\_58del.
	:	*	genomic reference sequence file are very big making downloading time consuming and storage problematics.
	:	*	the transcriptional orientation of the gene of interest may be on the minus (-)  strand, complicating variant reporting using "c." and "r." prefixes; nucleotide numbering on coding DNA and RNA level are based on the transcriptional orientation of the gene and goes in the opposite direction, creating confusing situations.

*	What are the disadvantages of using a coding DNA reference?
	:	A gene may have several transcripts, using different promoters / 5'-first exons, alternatively spliced exons, different 3'-terminal exons and polyA-addition sites. In such cases, which transcript should then be used?  Every choice will mean some regions (exons) are not in the reference sequence, complicating variant description.
	The different transcripts may encode different proteins (isoforms) with, when different promoters are used, different N-terminal sequences and even using different reading frames in one or more exons (e.g. the CDKN2A gene encoding the p14 and p16 protein isoforms).
	When different genes (partly) overlap, using the same or an opposite transcriptional orientation, which reference sequence should one use to describe the variant and to which gene should it be assigned?

*	Making a judgment on what is the "wild type" (wt) nucleotide for some sequences seems arbitrary at best, correct?
	:	All variants are described in relation to a **"reference sequence**". The reference sequence is considered to be the "**wild type**" sequence, the major allele present in the human population, and the allele used in the latest genome build. Note that everybody has influence on the reference sequence selected and can thus request that a sequence is changed to represent the most common allele. However, the debate about what is wild type becomes arbitrary when variants are very common (near 50%) or differ between populations.

*	When description in relation to a reference sequence is problematic, could one specify the variant by giving 20 bp of flanking sequence on both sides?
	:	In many cases this would be OK, but for recently duplicated genes or genes which contain repeated segments, giving 20 nucleotides to either side will not be sufficient. Furthermore, descriptions will become very long. For problematic cases the best method is probably to include the raw data, i.e. submit the sample sequence to [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit){:target="\_blank"} and give the accession.version number obtained.

{:#mtDNA}

*	How should sequence variants in the mitochondrial DNA (mtDNA) be described ? (_M Paalman, Human Mutation_)
	:	The mtDNA genome is rather small and completely sequenced. Variants in the mitochondrial DNA should therefore be described in relation to a the full mitochondrial DNA sequence, i.e. for human [the _Homo sapiens_ mitochondrion, complete genome (GenBank NC\_012920.1)](http://www.ncbi.nlm.nih.gov/nucleotide/NC_012920.1){:target="\_blank"}. The mtDNA encodes a range of different proteins. Changes at protein level should be described based on a protein reference sequence, e.g. YP\_003024031.1:p.Leu156Pro.
	:	_**NOTE**_:	for issues related to mitochondrial DNA sequences [see MITOMAP](http://www.mitomap.org/){:target="\_blank"}
	:	_**NOTE**_:	by exception, it is for this mitochondrial reference sequence allowed to specify the gene affected
	*	NC\_012920.1:m.3243A>G describes variant 3243A>G based on the mitochondrial reference sequence NC\_012920.1
	*	NC\_012920.1(MT-TL1):m.3243A>G describes variant 3243A>G in the MT-LT1 gene based on the mitochondrial reference sequence NC\_012920.1
	*	NC\_012920.1(MT-TL1):n.14A>G describes variant 14A>G based on the annotated MT-TL1 non-coding DNA reference sequence of the MT-TL1 gene in NC\_012920.1
<br>
*	For mitochondrial variants we use the format MT-ND1{NC\_012920.1}: m.[3460G>A], i.e. the gene in front of the reference sequence in curly brackets, a colon, an m and full stop and then the variant in square brackets, and a change in the protein as MT-ND1{YP\_003024026.1}: p.[(Ala52Thr)]. To be clear, is it not longer required to report/state the gene in front of the reference sequence?
	:	The format your give does not (nor did ever) follow HGVS recommendations. Correct HGVS formats are NC\_012920.1:m.3460G>A and YP\_003024026.1:p.(Ala52Thr). By exception, it is for this mitochondrial reference sequence allowed, to specify the gene affected (e.g. NC\_012920.1(MT-ND1):m.3460G>A) and give the description NC\_012920.1(MT-ND1):m.3460G>A p.(Ala52Thr).

*	How should variants be described in genes that produce only RNA (so no protein), e.g. ncRNA, miRNA, and others?
	:	To describe variants in genes that produce an RNA molecule but no protein a genomic reference sequence can be used ("**g.**" description). When a non-coding DNA reference sequence is available, e.g. a LRG (NR\_002196.1 for the H19 transcript) or a RefSeq transcript (NR\_000020.1 for the small nucleolar RNA, C/D box 33 (SNORD33) gene), variants can be described using the prefix "**n.**" see [_Community Consultation SVD-WG002_](/bg-material/community/SVD-WG002) and [_Nucleotide numbering_](/bg-material/numbering)).

*	We are preparing an annotated set of Hox genes from the zebrafish for publication. If the coding DNA sequence is not completely known, but only an EST lacking 5' sequence and a genomic sequence covering the EST, how do you describe variants?  Do I number it in relation to the EST or the genomic sequence?  Furthermore, if there is a mismatch between the genomic and the EST sequence, and you don't know which one is correct, how do you define e.g. whether the genomic sequence has an insertion or the EST has a deletion?
	:	Variants are described **compared to a reference sequence**. This implies the reference sequence is considered to be the "correct sequence. When a genomic sequence covering this EST is available the recommendation is to use this as the reference to describe variants.
