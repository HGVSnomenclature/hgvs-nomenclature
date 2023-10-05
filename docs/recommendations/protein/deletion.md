# deletion

## Definition

Deletion: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, one or more amino acids are not present (deleted)

## Description

Format: **"prefix""amino_acid(s)+position(s)\_deleted""del"**, e.g. p.(Cys76_Glu79del)

**"prefix"** = reference sequence used = p. **"amino_acid(s)+position(s)\_deleted"** = amino acid with position or range (first amino acid with position to last amino acids with position) deleted = Cys76_Glu79 **"del"** = type of change is a deletion = del

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and protein level may be given in addition
- **prefix** reference sequence accepted is "p." (protein).
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727_Ser783del).
- the "amino_acids+positions_deleted" should contain **two different** positions, i.e. Cys76_Glu79, not Cys76_Cys76.
  - the "positions_deleted" should be listed from **5' to 3'**, i.e. Cys76_Glu79, not Glu79_Cys76.
- for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- in theory, a **nonsense** variant can be considered as a deletion removing the C-terminal end of the protein (e.g. p.Trp26_Arg1623del). By definition, nonsense variants are described as an amino acid substitution (p.Trp26Ter or p.Trp26\* see [Substitution](../substitution)) replacing the first amino acid affected by a translation termination (stop) codon.
- variants extending the amino acid sequence at the C-terminal end with one or more amino acids, are described as [Extension](../extension).
- deletions at the DNA or RNA level
  - which introduce an **immediate** translation termination (stop) codon are described as nonsense variant.
  - **starting N-terminal of and including** the translation termination (stop) codon are described as [Frame shift](../frameshift).

## Examples

- one amino acid
  - NP_003997.2:p.Val7del: a deletion of amino acid Val7 in the reference sequence NP_003997.2
  - NP_003997.2:p.(Val7del): the **predicted** consequence at the protein level is a deletion of amino acid Val7 in the reference sequence NP_003997.2
  - NP_003997.2:p.Trp4del: a deletion of amino acid Trp4 in the sequence MetLeuTrpTrpGlu to MetLeuTrp<code class="spot1">\_</code>Glu: **NOTE:** for deletions in single amino acid stretches or tandem repeats, the most C-terminal residue is arbitrarily assigned to have been deleted
- several amino acids
  - NP_003997.2:p.Lys23_Val25del: a deletion of amino acids Lys23 to Val25 in reference sequence NP_003997.2
  - NP_003997.2:p.(Pro458_Gly460del): a deletion of amino acids Pro458-Pro459-Gly460 in reference sequence NP_003997.2: **NOTE:** the underlying DNA variant (LRG_232t1:c.1365_1373del) affects amino acids Pro455-Pro456-Gly457 but the 3'rule needs to be applied
- one or more exons
  - NP_003997.2:p.(His321_Glu383del): the predicted consequences of a deletion of exon 10 of the DMD gene, deleting amino acids His321 to Glu383 in reference sequence NP_003997.2
  - NP_003997.2:p.(Asp90_Val120del): the predicted consequences of a deletion of exon 5 of the DMD gene, deleting amino acids Asp90 to Val120 in reference sequence NP_003997.2: **NOTE:** since the 3'rule needs to be applied the description p.(Val89_Gln119del) is not correct
  - NP_003997.2:p.(His321Leufs\*3): the predicted consequences of a deletion of exons 10 to 11 of the DMD gene, creating a frame shift starting at amino acid His321, replacing it with Leu and terminating after three codons.
  - NP_003997.2:p.?: the predicted consequences of a deletion of exons 1 to 2 of the DMD gene, deleting the translation initiation codon: **NOTE:** since exon 1 and the translation initiation codon are deleted no reliable predictions can be made. Possibly no transcript is generated and no protein (p.0?)
  - NP_003997.2:p.?: the predicted consequences of a deletion of exons 74 to 79 of the DMD gene, deleting the translation termination codon: **NOTE:** since the last exon (exon 79) is deleted, it is not known what sequences after exon 73 are added to the transcript and no reliable predictions can be made
- p.Gly2_Met46del: a deletion of amino acids Gly2 to Met46 as a consequence of a variant silencing translation initiation at Met1 but activating a new downstream translation initiation site (at Met46) **NOTE:** the 3' rule has been applied.
- p.Trp26Ter (p.Trp26\*): amino acid Trp26 is changed to a stop codon (Ter, \*) **NOTE:** this change is by definition **not** described as a deletion of the C-terminal end of the protein (i.e. p.Trp26_Arg1623del)
- NP_003997.1:p.Val7=/del: a mosaic case where at amino acid position 7 besides the normal amino acid (a Val, described as "Val7=") also protein is found containing a deletion (Val7del): **NOTE:** for the predicted consequences of a variant the description is NP_003997.1:p.(Val7=/del)

## Discussion

!!! note "Can I use p.Arg45del6 to describe a 6 amino acid deletion?"

    No, a deletion of more than one residue should mention the first and last residue deleted, separated using the range symbol ("_", underscore), e.g. p.Arg45_Gly50del and not p.Arg45del6.

!!! note "Is the description of a deletion of exon 17 as p.EX17del still allowed?"

    A description like p.EX17del has never been allowed. Descriptions should be specific and indicate the amino acids affected by the change.

!!! note "In literature I often see the description "deltaF508", "ΔF508"or "F508del" for a variant in the CFTR gene in patients with Cystic Fibrosis. Is this according to HGVS nomenclature a correct description?"

    No, the correct description of this variant is LRG_663t1:c.1521_1523del r.(?) p.(Phe508del). According to HGVS all variants should be described at the most basic level, the DNA level. For protein studies the variant can be described as NP_000483.3:p.Phe508del (NOTE the protein reference sequence should be given).

!!! note "What do you mean with "variants should be described on the protein level and not incorporate knowledge regarding the change at the DNA-level"?"

    It means that protein variant descriptions should be derived from comparing the variant protein sequence with the reference protein sequence. Knowledge on the underlying change at the DNA level should not be used. E.g. when MetTrpSerSerSerHisAsp.. changes to MetTrpSerSer<code class="spot1">_</code>HisAsp.. this is described as p.Ser5del. The information that at the DNA level the change is ..ATGTGGTCCAGTTCCCACGAT.. to ..ATGTGGTCC<code class="spot1">_</code>TCCCACGAT.., so the codon for Ser4 is deleted, is not used; the description p.Ser4del is not correct.
