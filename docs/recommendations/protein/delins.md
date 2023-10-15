# deletion-insertion

## Definition

Deletion-Insertion (delins): a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, one or more amino acids are replaced with one or more other amino acids and which is not a substitution, frame shift or conversion.

## Syntax

```sh exec="true"
bin/pull-syntax -f docs/syntax.yaml aa.delins
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- **prefix** reference sequence accepted is "p." (protein).
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg123_Lys127delinsSerAsp).
- by definition, when **one** amino acid is replaced with **one** other amino acid, the change is a [substitution](substitution.md), not a deletion-insertion.
- changes involving two or more consecutive amino acids are described as a deletion/insertion variant (delins) (see [Substitution](substitution.md).
  - **NOTE**: this does not mean that at the DNA or RNA level the variant is described as a "delins" variant as well; on DNA level other rules may apply.
  - the description p.Arg76_Cys77delinsSerTrp is correct, the description p.[Arg76Ser;Cys77Trp] is not correct.
  - two variants separated by one or more amino acids should be described individually and not as a "delins".
- for all descriptions the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- when the inserted amino acid sequence is large the insertion may be described by its length, e.g. p.Lys2_Leu3insX[34] (open reading frame insertion) or p.Lys2_Leu3insTer12 (translation stop in inserted sequence).
  - **NOTE**: the inserted amino acid sequence can be derived from the description od the variant at DNA or RNA level.
- deletion/insertion variants extending the full-length amino acid sequence at the C-terminal end with one or more amino acids are described as [Extension](extension.md).
- deletion-insertion variants at the DNA or RNA level.
  - which introduce an **immediate** translation termination (stop) codon at the protein level are described as a nonsense variant, e.g. p.Tyr4Ter (or p.Tyr4\*) not p.Cys5_Ser6delinsTerGluAsp.
  - **encoding a translation stop codon** in the inserted sequence are described as deletion-insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
  - encoding an open reading frame which **after** the inserted sequence shift to another reading frame are described as a [frame shift](frameshift.md).
  - **starting N-terminal (5') of and including** the translation termination (stop) codon are described as [frame shift](frameshift.md).
- fusion proteins represent a special case of deletion-insertion variant. The fusion break point is described using **"::"**: **NOTE:** to avoid confusion, HGVS recommends to follow the [HGNC guidelines](https://www.genenames.org/about/guidelines/) to describe products of gene translocations or fusions (format GENESYMBOL1::GENESYMBOL2) and readthrough transcripts (format GENESYMBOL1-GENESYMBOL2)

## Examples

- p.Cys28delinsTrpVal: a deletion of amino acid Cys28, replaced with TrpVal
- p.Cys28_Lys29delinsTrp: a deletion of amino acids Cys28 and Ly29, replaced with Trp
- NP_004371.2:p.(Asn47delinsSerSerTer): the predicted change at the protein level resulting from DNA variant NM_004380.2:c.139delinsTCATCATGAGCTG is a deletion of amino acid Asn47 replaced with SerSerTer (alternatively SerSer\*).: **NOTE**: the deletion-insertion is not described as "delinsSerSerTerAlaAsp", amino acids after the translation termination codon are **not** listed.
- p.(Pro578_Lys579delinsLeuTer): the predicted change at the protein level resulting from DNA variant NM_080877.2c.1733_1735delinsTTT is a deletion of amino acids Pro578 and Lys579 replaced with LeuTer (alternatively Leu\*): **NOTE**: the predicted consequence of variant NM_080877.2:c.1732_1794del is p.(Pro578_Gln598del). Although the proteins resulting from the changes NM_080877.2:c.1733_1735delinsTTT and c.1732_1794del are identical, their HGVS description is different. **NOTE**: example derives from the SLC34A3 gene.
- NP_000213.1:p.(Val559_Glu561del): the predicted change at the protein level resulting from DNA variant NM_000222.3:c.1676_1684del. The variant is **not** described as p.(Val559_Glu562delinsGlu), where Glu562 would be replaced by a Glu which effectively is no change. Example derives from the KIT gene.
- NP_003070.3:p.(Glu125_Ala132delinsGlyLeuHisArgPheIleValLeu): the predicted change at the protein level resulting from DNA variant NM_003079.4:c.374_395inv is a deletion of amino acids Glu125 to Ala132 replaced with GlyLeuHisArgPheIleValLeu.: **NOTE**: the predicticted consequence from the inversion on DNA level is described as a deletion-insertion (inversions are not used at protein level)
- p.[Ser44Arg;Trp46Arg]: the change of two variants affecting amino acids separated by another amino acid.: **NOTE**: the variant is not described as p.Ser44_Trp46delinsArgLeuArg

## Discussion

!!! note "What is an "indel"?"

    The term "indel" is not used in HGVS nomenclature (see [Glossary](../../background/glossary.md). The term is confusing, having different meanings in different disciplines.

!!! note "Can I describe a TrpSer to CysArg variant as a amino acid substitution (p.TrpSer23CysArg)?"

    No, this is not allowed. By definition a substitution changes **one** amino acid into **one** other amino acid. The change TrpSer to CysArg should be described as p.Trp23_Ser24delinsCysArg, i.e. a deletion/insertion (indel) (see [Deletion-Insertion](delins.md)).
