---
parent: Protein
title: deletion
category: example
---

*	one amino acid
	*	NP\_003997.2:p.Val7del
	:	a deletion of amino acid Val7 in the reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Val7del)
	:	the **predicted** consequence at the protein level is a deletion of amino acid Val7 in the reference sequence NP\_003997.2
	*	NP\_003997.2:p.Trp4del
	:	a deletion of amino acid Trp4 in the sequence MetLeuTrpTrpGlu to MetLeuTrp**<font color="red">_</font>**Glu
	:	_**NOTE:**_ for deletions in single amino acid stretches or tandem repeats, the most C-terminal residue is arbitrarily assigned to have been deleted	
*	several amino acids
	*	NP\_003997.2:p.Lys23\_Val25del
	:	a deletion of amino acids Lys23 to Val25 in reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Pro458\_Gly460del)
	:	a deletion of amino acids Pro458-Pro459-Gly460 in reference sequence NP\_003997.2
	:	_**NOTE:**_ the underlying DNA variant (LRG\_232t1:c.1365\_1373del) affects amino acids Pro455-Pro456-Gly457 but the 3'rule needs to be applied
*	one or more exons
	*	NP\_003997.2:p.(His321\_Glu383del)
	:	the predicted consequences of a deletion of exon 10 of the DMD gene, deleting amino acids His321 to Glu383 in reference sequence NP\_003997.2
	*	NP\_003997.2:p.(Asp90\_Val120del)
	:	the predicted consequences of a deletion of exon 5 of the DMD gene, deleting amino acids Asp90 to Val120 in reference sequence NP\_003997.2
	:	_**NOTE:**_ since the 3'rule needs to be applied the description p.(Val89\_Gln119del) is not correct
	*	NP\_003997.2:p.(His321Leufs\*3)
	:	the predicted consequences of a deletion of exons 10 to 11 of the DMD gene, creating a frame shift starting at amino acid His321, replacing it with Leu and terminating after three codons.
	*	NP\_003997.2:p.?
	:	the predicted consequences of a deletion of exons 1 to 2 of the DMD gene, deleting the translation initiation codon
	:	_**NOTE:**_ since exon 1 and the translation initiation codon are deleted no reliable predictions can be made. Possibly no transcript is generated and no protein (p.0?)
	*	NP\_003997.2:p.?
	:	the predicted consequences of a deletion of exons 74 to 79 of the DMD gene, deleting the translation termination codon
	:	_**NOTE:**_ since the last exon (exon 79) is deleted, it is not known what sequences after exon 73 are added to the transcript and no reliable predictions can be made
*   p.Gly2\_Met46del
	:	a deletion of amino acids Gly2 to Met46 as a consequence of a variant silencing translation initiation at Met1 but activating a new downstream translation initiation site (at Met46)<br>
	_**NOTE:**_ the 3' rule has been applied.
*	p.Trp26Ter (p.Trp26\*)
	:	amino acid Trp26 is changed to a stop codon (Ter, \*)<br>
	:	_**NOTE:**_ this change is by definition **not** described as a deletion of the C-terminal end of the protein (i.e. p.Trp26\_Arg1623del)
*	NP\_003997.1:p.Val7=/del
	:	a mosaic case where at amino acid position 7 besides the normal amino acid (a Val, described as “Val7=”) also protein is found containing a deletion (Val7del)
	:	_**NOTE:**_ for the predicted consequences of a variant the description is NP\_003997.1:p.(Val7=/del)
