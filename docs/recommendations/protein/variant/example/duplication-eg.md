---
parent: Protein
title: duplication
category: example
---

*	one amino acid
	*	NP\_003997.2:p.Val7dup
	:	a duplication of amino acid Val7 in the reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Val7dup)
	:	the **predicted** consequence at the protein level is a duplication of amino acid Val7 in the reference sequence NP\_003997.2
	*	NP\_003997.2:p.Trp4dup
	:	a duplication of amino acid Trp4 in the sequence MetLeuTrpTrpGlu to MetLeuTrpTrp**<font color="red">Trp</font>**Glu
	:	_**NOTE:**_ for duplications in single amino acid stretches or tandem repeats, the most C-terminal residue is arbitrarily assigned to have been duplicated	
*	several amino acids
	*	NP\_003997.2:p.Lys23\_Val25dup
	:	a duplication of amino acids Lys23 to Val25 in reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Pro458\_Gly460dup)
	:	a duplication of amino acids Pro458-Pro459-Gly460 in reference sequence NP\_003997.2
	:	_**NOTE:**_ the underlying DNA variant (LRG\_232t1:c.1365\_1373dup) affects amino acids Pro455-Pro456-Gly457 but the 3'rule needs to be applied
*	one or more exons
	*	NP\_003997.2:p.(His321\_Glu383dup)
	:	the predicted consequences of a duplication of exon 10 of the DMD gene, duplicating amino acids His321 to Glu383 in reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Asp90\_Val120dup)
	:	the predicted consequences of a duplication of exon 5 of the DMD gene, duplicating amino acids Asp90 to Val120 in reference sequence NP\_003997.2
	:	_**NOTE:**_ since the 3'rule needs to be applied the description p.(Val89\_Gln119dup) is not correct
	*	NP\_003997.2:p.(Asn444Lysfs\*15)
	:	the predicted consequences of a duplication of exons 10 to 11 of the DMD gene, creating a frame shift starting at amino acid Asn444, replacing it with Lys and terminating after fifteen codons.
	*	NP\_003997.2:p.?
	:	the predicted consequences of a duplication of exons 1 to 2 of the DMD gene
	:	_**NOTE:**_ since the duplication adds a second promoter/exons 1 to a normal copy of the gene, a reliable prediction of the consequences can not be made. The duplication may have no consequences, it may give a duplication of exon 2 in the transcript, it might produce both transcripts, etc.
	*	NP\_003997.2:p.?
	:	the predicted consequences of a duplication of exons 74 to 79 of the DMD gene
	:	_**NOTE:**_ since the duplication adds a second last exon (exon 79) to a normal copy of the gene, a reliable prediction of the consequences can not be made. The duplication may have no consequences, it may give a duplication of exons 74 to 78 in the transcript, it might produce both transcripts, etc.
*	NP\_003997.1:p.Val7=/dup
	:	a mosaic case where at amino acid position 7 besides the normal amino acid (a Val, described as “Val7=”) also protein is found containing a duplication (Val7dup)
	:	_**NOTE:**_ for the predicted consequences of a variant the description is NP\_003997.1:p.(Val7=/dup)
