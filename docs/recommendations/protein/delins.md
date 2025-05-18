# Deletion-Insertion

<!-- ## Definition -->

Deletion-Insertion (delins): a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, one or more amino acids are replaced by one or more other amino acids **and which is not** a substitution or frameshift.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.delins
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg123_Lys127delinsSerAsp)`.
- by definition, when **one** amino acid is replaced by **one** other amino acid, the change is a [substitution](substitution.md), not a deletion-insertion.
- changes involving two or more consecutive amino acids are described as a deletion/insertion variant (delins).
    - **NOTE**: this does not mean that on the DNA or RNA level the variant is described as a "delins" variant as well; on DNA level, other rules may apply.
    - the description `p.Arg76_Cys77delinsSerTrp` is correct, the description <code class="invalid">p.[Arg76Ser;Cys77Trp]</code> is not correct.
    - two variants separated by one or more amino acids should be described individually and not as a "delins".
- for all descriptions, the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- when the inserted amino acid sequence is large, the insertion may be described by its length, e.g., `p.Lys2_Leu3insXaa[34]` (open reading frame insertion) or `p.Lys2_Leu3insTer12` (translation stop in inserted sequence).<br>
  **NOTE**: the inserted amino acid sequence can be derived from the description of the variant on the DNA or RNA level.
- deletion/insertion variants extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as an [Extension](extension.md).
- deletion-insertion variants on the DNA or RNA level that
    - introduce an **immediate** translation termination (stop) codon on the protein level, are described as a nonsense variant, e.g., `p.Tyr4Ter` (or `p.Tyr4*`), not <code class="invalid">p.Cys5_Ser6delinsTerGluAsp</code>.
    - **encode a translation stop codon** in the inserted sequence are described as deletion-insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    - encode an open reading frame which **after** the inserted sequence shifts to another reading frame, are described as a [frameshift](frameshift.md).
    - **start N-terminal (5') of and including** the translation termination (stop) codon, are described as [frameshift](frameshift.md).
- chimeric proteins represent a special case of deletion-insertion variant.
  The protein sequence junction is described using **`::`**.<br>
  **NOTE**: to avoid confusion, HGVS recommends to follow the [HGNC guidelines](https://www.genenames.org/about/guidelines/), [VICC Gene Fusion Specification](https://fusions.cancervariants.org/en/latest), and [adjoined transcripts](../RNA/adjoined_transcript.md) to describe the products of gene fusions.

## Examples

- **`p.Cys28delinsTrpVal`**<br>
  a deletion of amino acid `Cys28`, replaced by `TrpVal`.

- **`p.Cys28_Lys29delinsTrp`**<br>
  a deletion of amino acids `Cys28` and `Lys29`, replaced by `Trp`.

- **`NP_004371.2:p.(Asn47delinsSerSerTer)`**<br>
  the predicted change on the protein level resulting from DNA variant `NM_004380.2:c.139delinsTCATCATGAGCTG` is a deletion of amino acid `Asn47` replaced by `SerSerTer` (alternatively `SerSer*`).<br>
  **NOTE**: the deletion-insertion is not described as <code class="invalid">delinsSerSerTerAlaAsp</code>, amino acids after the translation termination codon are **not** listed.

- **`p.(Pro578_Lys579delinsLeuTer)`**<br>
  the predicted change on the protein level resulting from DNA variant `NM_080877.2c.1733_1735delinsTTT` is a deletion of amino acids `Pro578` and `Lys579` replaced by `LeuTer` (alternatively `Leu*`).<br>
  **NOTE**: the predicted consequence of variant `NM_080877.2:c.1732_1794del` is `p.(Pro578_Gln598del)`.
  Although the proteins resulting from the changes `NM_080877.2:c.1733_1735delinsTTT` and `c.1732_1794del` are identical, their HGVS description is different.
  Example derived from the _SLC34A3_ gene.

- **`NP_000213.1:p.(Val559_Glu561del)`**<br>
  the predicted change on the protein level resulting from DNA variant `NM_000222.3:c.1676_1684del`.
  The variant is **not** described as <code class="invalid">p.(Val559_Glu562delinsGlu)</code>, where `Glu562` would be replaced by a `Glu`, which effectively is no change.
  Example derived from the _KIT_ gene.

- **`NP_003070.3:p.(Glu125_Ala132delinsGlyLeuHisArgPheIleValLeu)`**<br>
  the predicted change on the protein level resulting from DNA variant `NM_003079.4:c.374_395inv` is a deletion of amino acids `Glu125` to `Ala132` replaced by `GlyLeuHisArgPheIleValLeu`.<br>
  **NOTE**: the predicted consequence of the inversion on DNA level is described as a deletion-insertion (inversions are not used on protein level).

- **`p.[Ser44Arg;Trp46Arg]`**<br>
  the change of two variants affecting amino acids separated by another amino acid.<br>
  **NOTE**: the variant is not described as `p.Ser44_Trp46delinsArgLeuArg`.

## Discussion

!!! note "What is an **"indel"**?"

    The term "indel" is not used in HGVS nomenclature (see [Glossary](../../background/glossary.md)).
    The term is confusing, having different meanings in different disciplines.

!!! note "Can I describe a `TrpVal` to `CysArg` variant as a amino acid substitution (<code class="invalid">p.TrpVal24CysArg</code>)?"

    No, this is not allowed.
    By definition, a substitution changes **one** amino acid into **one** other amino acid.
    The change `TrpVal` to `CysArg` should be described as `NP_003997.1:p.Trp24_Val25delinsCysArg`, i.e. a deletion/insertion (delins).
