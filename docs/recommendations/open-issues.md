---
layout: default-md
title: Open Issues
order: 8
---

# {{page.title}}

* * *

## Community Consultation

There are currently no proposals open for Community Consulation.

* * *

<a name ="opentopics"></a>

## Ongoing discussions

For closed topics [see below](/recommendations/open-issues#closedtopics).

* * *

## Introduction

At the time the first HGVS recommendations for the description of variants were made “history” had a large impact. History meaning the format proposed was heavily influenced by the formats already in use to describe variants. Would HGVS be designed from scratch, it might well be we would only use deletion (del), insertion (ins) and deletion-insertion (delins) because using these three any variant can be described. Substitution (>) might be added because of its simplicity and long history, although “delins” can be used to describe substitutions as well. Variant types like “inversion” (inv) and “duplication” (dup) might well be left out, they can be described as a “delins”. The same holds true for “conversions” (con), a variant type that was discontinued from HGVS recommendations a few years ago (see SVD-WG009).

Basically, these variant types refer to the (expected) biological process generating the variant, e.g. inserting a copy of segment of DNA (duplication), turning around a segment of DNA (inversion) or replacing a segment of DNA with a copy of a segment from elsewhere (conversion). The number of nucleotides involved in such cases is usually large, i.e. several hundred nucleotides or more. However, for overall consistency within the recommendations, the formats for description are general, irrespective of the length of the variant. Duplications can be as short as one nucleotide and inversions as small as two (prioritisation determines one-nucleotide inversions are described as substitution), although for these variants a link with the biological process generating them is unlikely. It should be noted that some of the problems described below are associated with these historic choices.

* * *

<a name ="beyond"></a>

### Beyond transcripts

Current HGVS recommendations state ([_see Reference Sequences_](/bg-material/refseq/)):  "5’ and 3’ flanking sequences are considered to be **outside the boundaries** of a transcript reference sequence and **can not be used** to describe variants". As a consequence, variants removing an entire gene or the 5' or 3' end of a transcript can only be described using chromosomal genomic coordinates (g.). This complicates variant reporting for diagnostic laboratories, usually reporting variants based on a coding DNA reference sequence (c.). In addition, such variants can not be shown in databases listing variants based on a "c." description.

The HGVS nomenclature committe received several requests to suggest a format to describe such variants. So far, the committee has the opinion such a format is not required; these variants can be described accurately using a chromosomal refenrence sequence (g.). Although the proposal "[_Numbering gene flanking nucleotides_](/recommendations/open-issues#geneflanking)" has been rejected, the issue is not silenced. The [_Global Variome shared LOVD_](http://databases.lovd.nl/shared/genes/DMD){:target="\_blank"} currently uses a format using {0} (deletion) and {2} (duplication) in combination with the first and last nucleotide of the coding DNA reference sequence to describe variants which go outside the boundaries of the transcript (c.-244 and c.*2691 in the examples below).

*	NM\_004006.2:c.-244\_\*2691{0}
	: describes a deletion of the entire coding DNA reference sequence of the DMD gene
*	NM\_004006.2:c.-244\_187{0}
	: describes a deletion including the transcription start site (cap site) of the DMD gene
*	NM\_004006.2:c.\*1162\_\*2691{2}
	: describes a duplication including the transcription termination site (polyA-addition site) of the DMD gene

The description is always given _**in addition**_ to a decription based on the X-chromosome genomic reference sequence (g.), indicating the extent of the variant. The description should not lead to confusion since it is clearly different from other formats, like NM\_004006.2:c.-244\_\*2691del (suggesting the deletion break point was sequenced) and c.0 (not very specific and can not be used when the start/end of the transcript is affected).

<a name ="frameshift"></a>

### Frame shifts

The HGVS recommended format to describe frame shift variants gives the length of the shifted reading frame, it does not indicate the length of the reference protein sequence that has been deleted. Both the length of the shifted open reading frame, as well as the length of the deleted reference protein sequence will be important to predict the possible deleterious consequence of the variant: the larger the new/deleted sequence the more likely it will be deleterious. The question has been raised whether the description of a **frame shift** variant should also **include the length of the protein sequence deleted**.

The format to describe frame shift variants has a **historic** background, it has the format already used before the HGVS nomenclature recommendations were first published (in 2000). [_In HGVS_](/recommendations/protein/variant/frameshift/), the frame shift is a special type of amino acid deletion/insertion which does not include the deletion from the site of the change to the C-terminal end of the protein (translation termination (stop) codon). From the consequence of variant NM_004006.3:c.2453del on protein level, p.Leu818CysfsTer2, one can therefore only see the new reading frame is just one amino acid long, not how many amino acids have been deleted. Describing this frame shift as a deletion-insertion, i.e. p.Leu818_Met3685delinsCys, would make it immediately clear the single Cys-residue replaces 2868 amino acids, undoubtedly having deleterious consequences.

<a name ="inshow"></a>

### Insertions

The format for the description of insertions needs specification. Following current recommendations, insertions can be described either by giving the inserted sequence, or by giving the nucleotide positions of a copy of the inserted sequence.

For example, the insertion of "GAAGTACTG" between nucleotides NM\_004006.3:c.299 and c.300 can be described as NM\_004006.3:c.299\_300insGAAGTACTG or as NM\_004006.3:c.299\_300ins284\_293. A third format, meant for large insertions is to refer to a reference sequence file containing the inserted sequence, e.g. NM\_000553.4:c.3050\_3051ins\[NM\_004006.3:c.284\_293\]. Since the current recommendations do not specify when to use which of these formats, one variant can be described using different formats. This is undesired, HGVS recommendations should be extended by specifying when to use which format.

<a name ="repseqs"></a>

### Repeated sequences

The repeated sequence format is part of the HGVS recommendations to describe variants in the number of units of a repeated sequence. The format is especially used to describe variants in so called tri-nucleotide repeat expansion disorders, like Huntingtons' disease, Fragile-X syndrome, etc. The format recommended was based on the format used before the HGVS recommendations were first proposed. The basic format is: g.123\_191CAG[25], i.e. describing the range of the segment in the reference sequence containing the repeat sequence (g.123 to g.191), describing the repeat unit ("CAG") and the number of repeat unit identified in the sample analysed ("[25]").

The format overlaps with the format to describe deletions and duplications/insertions. This means that e.g. both g.186_191del and g.123\_191CAG[21] are correct following current HGVS recommendations. HGVS recommendations therefore require further specifications to indicate when to use which format.

Discontinuing the use of the repeated sequence format will not solve all problems. E.g. how to describe a repeat expansion which is larger than the length of the repeat in the reference sequence. While g.123\_191dup equals g.123\_191CAG[46], how to describe g.123\_191CAG[47]. Another problem emerges when the repeat unit in not perfect but interrupted with another unit, e.g. an occasional CAA in the CGA unit (frequent in Fragile-X syndrome). The repeated sequence format has clear advantages here.

A new user group of the repeated sequence format is the forensics community. Originally this group described variants using the length of the fragment analysed. However, it is nowadays more common to use a sequence-based analysis. Sequencing revealed an additional level of complexity where alleles with the same length turn out to have a different sequence. In general, using the repeated sequence format, it is rather simple to describe the alleles observed. However, the repeated sequences analysed are often extensive and may contain a mix of different repeat units. The problem then emerges how to describe the reference format of the repeat. Is it CAG[4]CAA[1]CAG[2]CAA[1]CAG[2]CAA[1]CAG[2] or CAG[4][CAA[1]CAG[2]][3] or even another format. Making precise specifications, although necessary, will probably make it very difficult to apply for a human. The solution might be to let the computer decide by designing a HGVS-approved standardised algorithm including all specifications.

<a name ="extensions"></a>

### Protein Extensions

Would you consider a small change in the suggested nomenclature for the [_description of extensions_](/recommendations/protein/variant/extension/) from p.\*110Glnext\*17 to p.\*110Glnext17? (_Yael Shinar, Tel Hashomer, Israel_)

The description of extensions can probably indeed be simplified. While for **extensions** we currently give the position of the new translation initiation (start) codon as "5" or of the termination (stop) codon as "\*17" this is strictly speaking not necessary. By defenition the extension goes upstream for an N-terminal change and downstream for a C-terminal change. Using p.Met1ext5 (now p.Met1ext-5) and p.\*110Glnext17 (now p.\*110Glnext\*17) therefore seems sufficient.

<a name ="modifications"></a>

### Modifications

Aug.24 (2011) - JT den Dunnen
HGVS nomenclature does currently not have recommendations for the descriptions of modifications of DNA, RNA or protein molecules. The most pressing need for a recommendation is are DNA methylation and RNA editing. Proposal [_SVD-WG005 (gom/lom)_](/bg-material/consultation/svd-wg005/) makes a start to get recommendations on this topic. SVD-WG005 introduces the use of the “|” character (“pipe”) to indicate that not a direct change of the sequence is described but a modification (change of state).

<a name ="amount"></a>

#### Amount

Due to a variant, e.g. in the promotor region of a gene, the amount of RNA and protein produced might be reduced or increased. HGVS nomenclature currently does not have a way to describe this. Using the “\|” character (“pipe”) these consequences could be described as r.=\|red or r.=\|inc (p.=\|red, p.=\|inc) or more spcifically like r.=\|0.40 (reduced to 0.40) or r.=\|3.10 (increased to 3.10).

The same format could be applied to specify the fraction of the different RNA molecules when a variant e.g affects splicing generating several different transcripts, like r.[646\_792del|0.73,792\_793ins[792+1\_792+38|0.27].

<a name ="RNAedit"></a>

#### RNA editing

Addition of RNA editing data to a DNA variant database seems a sensible thing to do. An RNA-based sequencing study might reveal an interesting variant which, when checked in the database, is listed (...RNA editing data is not recorded). This will trigger a DNA sequencing experiment, trying to confirm the variant, which will fail since the variant is not present at the DNA level and valuable resources are spoiled.

The suggestion is to describe RNA editing using "**|@**";

*	g.1287\|@ (based on a genomic reference sequence)
*	c.143\|@ (based on a coding DNA reference sequence)
*	n.143\|@ (based on a non-coding DNA reference sequence)
*	r.143c>u on RNA level
*	p.(His48Pro) on protein level (i.e. the predicted consequence)

The use of the "**@**" character versus other characters (&, $, ~, #) is of course debatable. Another option is to use a three-letter abbreviation like "del" and "ins", e.g. "**edt**" (g.1287C\|edt, c.143C\|edt) but this is seems less attractive (longer and potentially confusing). The "**@**" should serve as a simple mark, indicating 'note this site, something is happening at ("**@**") this position.

Using the description r.143c>u on RNA level suggests a substitution. There are several types of RNA editing and "r.143c" probably does not really change to a "u". All we can say is that the polymerases used to make a copy inserted an "a". At some point we probably need to suggest ways to exactly describe the chemical modification made by the RNA editing enzyme but we can do that later. Making such recommendations can then be combined with those for DNA modifications (like methylation with methyl or hydroxy-methyl groups) making sure they follow the same rules.

The question is whether we need a specific description at the DNA level indicating that the nucleotide is known to be modified at RNA level. The main purpose of this mark would be to facilitate easy database retrieval of such sites. Approval of proposal [_SVD-WG001_](/bg-material/consultation/svd-wg001/) more or less opened the option for such marks.

<a name ="exonnumbering"></a>

### Exon Numbering

HGVS nomenclature does not give specific recommendations for the **numbering of exons**. For variant descriptions exon numbers are not required, **nucleotide position are sufficient**. In many genes there is no consensus on exon/intron numbering and several old numbering schemes may exist that had to be revised to include newly discovered exons (internal as well as 5' and/or 3' of the gene). This led to all kinds of numbering schemes with no clear structure, making it very difficult for non-experts in the specific gene to keep track of all details (see also [Dalgleish 2010](http://www.genomemedicine.com/content/pdf/gm145.pdf){:target="\_blank"} and [NCBI RefSeqGene](http://www.ncbi.nlm.nih.gov/refseq/rsg/faq/#exon){:target="\_blank"})). To prevent confusion and with the increasing use of genome browsers, numbering exons simply as 1, 2, 3, etc., from start to the end is the only logical option.
	Although this is probably difficult to accept by the experts, we can not keep on confusing newcomers by forever using legacy numbering systems. We should realize that, at some point, wrong assumptions will be made with as a consequence a patient will receive an erroneous diagnosis. This is of course unacceptable.

*	The CBS gene was originally thought to contain 16 exons. Later it was recognised that exon 15 does not exist, and recently two additional non-translated 5' exons were detected. The current gene structure therefore includes 17 exons, of which exons 3 to 17 are translated. Should the exons of a gene be counted from the exon that contains the start codon rather than the beginning of the cDNA?  If so, should exons preceding the start codon be counted 0, -1, -2, etc. or should the 0 be skipped?  Is there an agreement on how to deal with changes in exon numbering?
	:	For the description of sequence changes it does not matter how exons are numbered,  exon (and intron) numbers are not used in the descriptions, only nucleotide positions. For exon numbering the only logical thing to do is to start with 1 for the first exon and number all following exons successively. Using other numbering schemes problems will emerge at some point. Note that when alternative numbering schemes are used, these will only be recognised by experts in the field knowing their history; newcomers just blindly assume that the first exon annotated in the genome is exon 1. Consequently, when legacy numbering schemes are used, this will cause confusion and at some point wrong assumptions will be made and a patient might end up with an erroneous diagnosis. In papers, when used, specifically mention how exons were numbered (M&M, Figure and Table legends). For tables, consider to add a column listing the historic / old exon numbers.


* * *

<a name ="closedtopics"></a>

## Closed topics

<a name ="circular"></a>

### Circular molecules

<font color="#FF0000">The proposal has been ACCEPCTED for circular reference sequences</font>
HGVS nomenclature assumes reference sequences are linear. However, the mitochondrial genome and many other DNA molecules (plasmids, viral genomes) are circular. How should one describe a variant involving the "first" and "last" nucleotides of the circular molecule?  For now the suggestion is to describe the variant as m.[1del;16569del]. The question is whether m.16569_1del should be allowed (NOTE: includes an exception to the rule that in Y\_Xdel X should be smaller then Y). Do you have a suggestion??

<a name ="imperfectcopy"></a>

### Imperfect copies

<font color="#FF0000">The proposal has been REJECTED</font>
Accepting the proposal, without a whole range of specifications, would add **too many** options to decribe specific variants.

HGVS nomenclature has excellent possibilities to describe large duplications, inversions, conversions and insertions. However, no clear recommendations are available what to do when the nucleotides involved are not a perfect copy of the original sequence. The suggestion has been made ([_Taschner PEM, Den Dunnen JT (2011). Hum.Mutat. 32:507-511_](http://onlinelibrary.wiley.com/doi/10.1002/humu.21427/pdf){:target="\_blank"}) to use "**{ }**" (curly braces) as a kind of "_sub-alleles_" to describe the variants in the altered region.
*	g.24\_65dup{46G>T}
	:	a duplication of nucleotides g.24 to g.65 with variant g.46G>T in the duplicated copy.
After careful consideration the decision was made **not to accept** this proposal. The proposal would introduce a kind of "nesting" which is very diifcult to control. 

<a name ="geneflanking"></a>

### Numbering gene flanking nucleotides

<font color="#FF0000">The proposal has been REJECTED</font>
The current recommendation to describe variants based on a coding DNA reference sequence is to use "c.-" numbers for nucleotides 5' of the ATG translation initiation codon and "c.\*" numbers for nucleotides 3' of the translation termination codon [_see Numbering_](/bg-material/numbering/). However, such descriptions do not show whether the nucleotides are **inside or outside** the transcribed region. The request has been filed (_PEM Taschner, Leiden, Nederland_) to make a discrimination between transcribed and un-transcribed nucleotides using the format;

*	c.-N-uM  =  nucleotide uM is at position -M upstream (u) of nucleotide c.-N, the transcription initiation site (cap-site) of the reference transcript, e.g. c.-237-u29A>G (currently c.-266A>G)
	:	_**NOTE**_:	restricted to nucleotides 5' of the transcription initiation site (cap site), i.e. upstream of the gene (incl. the promoter)
*	c.\*N+dM  =  nucleotide dM is at position +M downstream (d) of nucleotide c.\*N, the polyA-addition site of the reference transcript, e.g. \*237+d133A>G (currently c.\*370A>G)
	:	_**NOTE**_:	restricted to nucleotides 3' of the polyA-addition site, i.e. downstream of the gene

This proposal has been rejected since: (i) genes often have several transcription initiation sites as well as polyA-addition sites, (ii) the transcription initiation (cap-site) is often ill-defined, (iii) variants that lie outside of a transcript can not be described based on a coding DNA reference sequence (c.), it does not contain the reference nucleotide, and should be described based on a gene or chromosome reference sequence. Use NC\_000023.10:g.33229820A>G or LRG\_199t1:c.-391T>C **and not** NC\_000023.10(NM\_004006.2):c.-244-u147T>C, LRG\_199t1:c.-244-147T>C or similar descriptions. 
