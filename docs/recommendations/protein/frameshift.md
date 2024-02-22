# Frameshift

<!-- ## Definition -->

Frameshift: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, translation shifts to another reading frame.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.fs
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg123LysfsTer34)`.
- for all descriptions, the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- frameshifts are a special type of amino acid **deletion/insertion** which, by definition, do not include the deletion from the site of the change to the C-terminal end of the protein (translation termination (stop) codon), like `Arg123_Leu833del`, nor the amino acid sequence inserted.
    - the description of a frameshift starts with the **first new** amino acid, this might not be first codon affected by the variant on the DNA level.
    - the position of the translation termination (stop) codon in the new reading frame is calculated **starting** at the first amino acid changed by the frameshift (codon 1), and **ending** at the first stop codon encountered (`Ter#` or `*#`).<br>
      **NOTE**: the number of amino acids in the new C-terminal sequence is "#-1" amino acids.<br>
      **NOTE**: the shortest frameshift variant possible contains `fsTer2`; variants which introduce an **immediate** translation termination (stop) codon are described as nonsense variant, e.g., `p.Tyr4Ter` (or `p.Tyr4*`) not `p.Tyr4TerfsTer1` (see [Substitution](substitution.md)).
    - frameshifts can also be described using a **short format**; `p.Arg123fs`, i.e. indicating the first amino acid changed, its position and `fs` without further detail.
- the (predicted) amino acid changes of additional variants on the same allele (in cis) downstream of the frameshift are not described unless they change the amino acid sequence or length of the shifted reading frame (i.e. introduce an amino acid substitution, an earlier translational termination (stop) codon or affect the termination codon of the shifted frame).
- deletions starting 5' of and including the translation termination (stop) codon are described as **frameshift**.
- inserted sequences on DNA or RNA level that
    - extend the amino acid sequence at the C-terminal end with one or more amino acids are described as an [Extension](extension.md).
    - **encode a translation stop codon** in the inserted sequence are on the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    - encode an open reading frame which **after** the inserted sequence shifts to another reading frame, are described as a [frameshift](frameshift.md).

## Examples

- **`p.Arg97ProfsTer23` (short `p.Arg97fs`) / `p.Arg97Profs*23`**<br>
  a variant with `Arg97` as the first amino acid changed, shifting the reading frame, replacing it for a `Pro` and terminating at position `Ter23`.

- **`p.(Tyr4*)`**<br>
  the predicted consequence on the protein level is a `Tyr` to translation termination codon.
  This might arise from a `c.12del` deletion in `ATGGATGCA`<code class="stop">TA</code><code class="del">C</code><code class="stop">G</code>`TCACG` to create a <code class="stop">TAG</code> stop codon.<br>
  **NOTE**: the variant is described as a substitution, not as a frameshift (<code class="invalid">p.Tyr4TerfsTer1</code>).

- **`p.Glu5ValfsTer5` (short `p.Glu5fs`)**<br>
  the predicted consequence on the protein level of the variant `ATGGA`<code class="spot1">TGCATACG</code>`AGATGAGG` to `ATGGA`<code class="spot1">TGCATACG</code><code class="ins">TGCATACG</code>`AGATGAGG` (`c.6_13dup`).

- **`p.Ile327Argfs*?` (short `p.Ile327fs`)**<br>
  the predicted consequence of a frameshifting variant changes `Ile327` to an `Arg`, but the new reading frame does not encounter a new translation termination (stop) codon.

- **`p.Gln151Thrfs*9` (not <code class="invalid">p.His150Hisfs*10</code>)**<br>
  the first codon on the DNA level affected by a variant is `His150` and the shifted frame starts with a `HisThrSer`.
  Since frameshift variants start with the **first amino acid changed**, the description <code class="invalid">p.His150HisfsTer10</code> (or <code class="invalid">p.His150Hisfs*10</code>) is not correct.

## Discussion

!!! note "What do you mean with "variants should be described on the protein level and not incorporate knowledge regarding the change on the DNA-level"?"

    It means that protein variant descriptions should be derived from comparing the variant protein sequence with the reference protein sequence.
    Knowledge on the underlying change on the DNA level should not be used.
    For example, when `MetTrpSerSer`<code class="del">Ser</code>`HisAsp..` changes to `MetTrpSerSerHisAsp..`, this is described as `p.Ser5del`.
    The information that on the DNA level the change is `..ATGTGGTCC`<code class="del">AGT</code>`TCCCACGAT..` to `..ATGTGGTCCTCCCACGAT..`, so the codon for `Ser4` is deleted, is not used; the description `p.Ser4del` is not correct.
