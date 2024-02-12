# Deletion

<!-- ## Definition -->

Deletion: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, one or more amino acids are not present (deleted).

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.del
```

## Notes

- all variants **should be** described at the DNA level; descriptions at the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg727_Ser783del)`.
- the "positions_deleted" should contain **two different** positions, i.e. `Cys76_Glu79`, not `Cys76_Cys76`.
    - the "positions_deleted" should be listed from **5' to 3'**, i.e. `Cys76_Glu79`, not `Glu79_Cys76`.
- for all descriptions, the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- a **nonsense** variant, a variant changing an amino acid to a translation termination (stop) codon, is described as a **substitution** (`p.Trp26Ter` or `p.Trp26*`; see [Substitution](substitution.md)).
  A nonsense variant is not described as a [Deletion](deletion.md) of the C-terminal end of the protein (e.g., `p.Trp26_Arg1623del`).
- variants extending the amino acid sequence at the C-terminal end with one or more amino acids, are described as an [Extension](extension.md).
- deletions at the DNA or RNA level that
    - introduce an **immediate** translation termination (stop) codon, are described as a nonsense variant.
    - encode an open reading frame which **after** the deleted sequence shifts to another reading frame, are described as a [frameshift](frameshift.md).

## Examples

### one amino acid

- **`NP_003997.2:p.Val7del`**<br>
  a deletion of amino acid `Val7` in the reference sequence `NP_003997.2`.

- **`NP_003997.2:p.(Val7del)`**<br>
  the **predicted** consequence on the protein level is a deletion of amino acid `Val7` in the reference sequence `NP_003997.2`.

- **`NP_003997.2:p.Trp4del`**<br>
  a deletion of amino acid `Trp4` in the sequence `MetLeuTrp`<code class="del">Trp</code>`Glu` to `MetLeuTrpGlu`.<br>
  **NOTE**: for deletions in single amino acid stretches or tandem repeats, the most C-terminal residue is arbitrarily assigned to have been deleted.

### several amino acids

- **`NP_003997.2:p.Lys23_Val25del`**<br>
  a deletion of amino acids `Lys23` to `Val25` in reference sequence `NP_003997.2`.

- **`NP_003997.2:p.(Pro458_Gly460del)`**<br>
  a deletion of amino acids `Pro458`, `Pro459`, and `Gly460` in reference sequence `NP_003997.2`.<br>
  **NOTE**: the underlying DNA variant `LRG_232t1:c.1365_1373del` affects amino acids `Pro455`, `Pro456`, and `Gly457`, but the 3'rule needs to be applied.

### one or more exons

- **`NP_003997.2:p.(His321_Glu383del)`**<br>
  the predicted consequences of a deletion of exon 10 of the _DMD_ gene, deleting amino acids `His321` to `Glu383` in reference sequence `NP_003997.2`.

- **`NP_003997.2:p.(Asp90_Val120del)`**<br>
  the predicted consequences of a deletion of exon 5 of the _DMD_ gene, deleting amino acids `Asp90` to `Val120` in reference sequence `NP_003997.2`.<br>
  **NOTE**: since the 3'rule needs to be applied, the description <code class="invalid">p.(Val89_Gln119del)</code> is not correct.

- **`NP_003997.2:p.(His321Leufs*3)`**<br>
  the predicted consequences of a deletion of exons 10 to 11 of the _DMD_ gene, creating a frameshift starting at amino acid `His321`, replacing it with `Leu` and terminating after three codons.

- **`NP_003997.2:p.?`**<br>
  the predicted consequences of a deletion of exons 1 to 2 of the _DMD_ gene, deleting the translation initiation codon.<br>
  **NOTE**: since exon 1 and the translation initiation codon are deleted, no reliable predictions can be made.
  Possibly, no transcript is generated and no protein (`p.0?`).

- **`NP_003997.2:p.?`**<br>
  the predicted consequences of a deletion of exons 74 to 79 of the _DMD_ gene, deleting the translation termination codon.<br>
  **NOTE**: since the last exon (exon 79) is deleted, it is not known what sequences after exon 73 are added to the transcript, and no reliable predictions can be made.

### other examples

- **`p.Gly2_Met46del`**<br>
  a deletion of amino acids `Gly2` to `Met46` as a consequence of a variant silencing translation initiation at `Met1`, but activating a new downstream translation initiation site (at `Met46`).<br>
  **NOTE**: the 3' rule has been applied.

- **`p.Trp26Ter` (`p.Trp26*`)**<br>
  amino acid `Trp26` is changed to a stop codon (`Ter`, `*`).<br>
  **NOTE**: this change is by definition **not** described as a deletion of the C-terminal end of the protein (i.e. `p.Trp26_Arg1623del`).

- **`NP_003997.1:p.Val7=/del`**<br>
  a mosaic case where at amino acid position `7`, besides the normal amino acid (a `Val`, described as `Val7=`), also protein is found containing a deletion (`p.Val7del`).<br>
  **NOTE**: for the predicted consequences of a variant, the description is `NP_003997.1:p.(Val7=/del)`.

## Discussion

!!! note "Can I use <code class="invalid">p.Arg45del6</code> to describe a 6 amino acid deletion?"

    No, a deletion of more than one residue should mention the first and last residue deleted, separated using the range symbol (`_`, underscore), e.g., `p.Arg45_Gly50del`, and not <code class="invalid">p.Arg45del6</code>.

!!! note "Is the description of a deletion of exon 17 as <code class="invalid">p.EX17del</code> still allowed?"

    A description like <code class="invalid">p.EX17del</code> has never been allowed.
    Descriptions should be specific and indicate the amino acids affected by the change.

!!! note "In literature I often see the description "deltaF508", "ΔF508"or "F508del" for a variant in the _CFTR_ gene in patients with Cystic Fibrosis. Is this according to HGVS nomenclature a correct description?"

    No, the correct description of this variant is `LRG_663t1:c.1521_1523del` &nbsp; `r.(?)` &nbsp; `p.(Phe508del)`.
    According to the HGVS nomenclature, all variants should be described at the most basic level, the DNA level.
    For protein studies, the variant can be described as `NP_000483.3:p.Phe508del` (NOTE: the protein reference sequence should be given).

!!! note "What do you mean with "variants should be described on the protein level and not incorporate knowledge regarding the change at the DNA-level"?"

    It means that protein variant descriptions should be derived from comparing the variant protein sequence with the reference protein sequence.
    Knowledge on the underlying change at the DNA level should not be used.
    E.g., when `MetTrpSerSer`<code class="del">Ser</code>`HisAsp..` changes to `MetTrpSerSerHisAsp..`, this is described as `p.Ser5del`.
    The information that at the DNA level the change is `..ATGTGGTCC`<code class="del">AGT</code>`TCCCACGAT..` to `..ATGTGGTCCTCCCACGAT..`, so the codon for `Ser4` is deleted, is not used; the description `p.Ser4del` is not correct.
