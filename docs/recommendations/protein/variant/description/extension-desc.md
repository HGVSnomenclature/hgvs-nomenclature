---
parent: Protein
title: extension
category: description
---

Format (**<font color="red">N-terminal</font>**):  **"prefix""Met1""ext""position_new_initiation_site"**,  e.g. p.Met1ext-5

**"prefix"**  =  reference sequence used  =  p.<br>
**"Met1"**  =  normal translation initiation site  =  Met1<br>
**"ext"**  =  type of change is an extension =  ext<br>
**"position_new_initiation_site"**  =  position new upstream translation initiation site =  -5

Format (**<font color="red">C-terminal</font>**):  **"prefix""Ter_position""new_amino_acid""ext""Ter""position_new_termination_site"**,  e.g. p.Ter110Glnext\Ter17

**"prefix"**  =  reference sequence used  =  p.<br>
**"Ter_position"**  =  normal translation termination site  =  Ter110<br>
**"new_amino_acid"**  =  amino acid encoded by variant termination codon  =  Gln<br>
**"ext"**  =  type of change is an extension =  ext<br>
**"Ter"**  =  termination codon = Ter / \*<br>
**"position_new_termination_site"**  =  position new downstream translation termination site =  17

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequence accepted is "p." (protein).
*	**extension** variants have been accepted on <font color="red">2012-08-31</font>.
*	**predicted consequences**, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Ter110GlnextTer17) or p.(\*110Glnext\*17).
*	variants affecting the translation initiation site (Met1) activating an upstream (N-terminal) translation initiation site are described as [_deletion-insertion_](/recommendations/protein/variant/delins/), those activating a downstream (C-terminal)  initiation site as a [_deletion_](/recommendations/protein/variant/deletion/).
*	**prioritisation**: (1) extension, (2) frame shift or deletion-insertion.
