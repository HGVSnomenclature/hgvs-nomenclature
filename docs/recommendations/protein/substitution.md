# Substitution

<!-- ## Definition -->

Substitution: a sequence change where, compared to a reference sequence, **one** amino acid is replaced by **one** other amino acid.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.sub
```

## Notes

- all variants **should be** described at the DNA level; descriptions at the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg727Ser)`.
- a **nonsense** variant, a variant changing an amino acid to a translation termination (stop) codon, is described as a **substitution**.
  A nonsense variant is not described as a [Deletion](deletion.md) of the C-terminal end of the protein (e.g., `p.Trp26_Arg1623del`).
    - variants which introduce an **immediate** translation termination (stop) codon are described as nonsense variant.
    - **NOTE**: not <code class="invalid">p.Tyr4TerfsTer1</code>, but `p.Tyr4Ter` (or `p.Tyr4*`); not <code="invalid">p.Tyr4_Cys5insTerGluAsp</code>, but `p.Tyr4Ter` (or `p.Tyr4*`); not <code class="invalid">p.Cys5_Ser6delinsTerGluAsp</code> but `p.Tyr4Ter` (or `p.Tyr4*`).
- a **no-stop** variant, a variant changing the translation termination codon into an amino acid codon, is described as an **extension** ([Extension](extension.md)).
- changes involving two or more consecutive amino acids are described as a deletion/insertion variant (delins) (see [Deletion/insertion (delins)](delins.md)).
    - the description `p.Arg76_Cys77delinsSerTrp` is correct, the description <code class="invalid">p.[Arg76Ser;Cys77Trp]</code> is not correct.
- amino acids that have been tested and found **not changed** (silent) are described as `p.Cys123=` (see [SVD-WG001 (no change)](../../consultation/SVD-WG001.md)).

## Examples

- **missense**
    - **`LRG_199p1:p.Trp24Cys`**<br>
      amino acid `Trp24` is changed to a `Cys`.

    - **`NP_003997.1:p.(Trp24Cys)`**<br>
      amino acid `Trp24` is predicted to change to a `Cys` (no experimental proof, e.g., based on DNA level data).

- **nonsense**
    - **`LRG_199p1:p.Trp24Ter` (`p.Trp24*`)**<br>
      amino acid `Trp24` is changed to a stop codon (`Ter`, `*`).<br>
      **NOTE**: this change is **not** described as a deletion of the C-terminal end of the protein (i.e. `p.Trp24_Met36853del`).

- **silent** (no change)
    - **`NP_003997.1:p.Cys188=`**<br>
      amino acid `Cys188` is not changed (DNA level change `..TGC..` to `..TGT..`).<br>
      **NOTE**: the description `p.=` means the **entire** protein coding region was analysed and no variant was found that changes (or is predicted to change) the protein sequence.

- **translation initiation codon**
    - **no protein: `LRG_199p1:p.0`**<br>
      as a consequence of a variant in the translation initiation codon, no protein is produced.<br>
      **NOTE**: `LRG_199p1:p.0?` can be used when you predict that no protein is produced.
      Do not use descriptions like <code class="invalid">p.Met1Thr</code>, this is for sure **not** the consequence of the effect on protein translation.

    - **unknown: `LRG_199p1:p.(Met1?)`**<br>
      the consequence, at the protein level, of a variant affecting the translation initiation codon can not be predicted (i.e. is unknown).

    - **new translation initiation site**
        - **downstream: `NP_003997.1:p.Leu2_Met124del` (deletion)**<br>
          a variant in the translation initiation codon causes the activation of a downstream translation initiation site (`Met`) resulting in deletion of the first 123 amino acids (`Met1` to `Val123`) of the protein.<br>
          **NOTE**: the 3' rule applies.

        - **upstream: `p.Met1_Leu2insArgSerThrVal` (insertion)**<br>
          a variant in the translation initiation codon (`Met1`) changes it to a Valine (`Val`) and activates an upstream translation initiation site at position -4, replacing amino acid `Met1` with `MetArgSerThrVal`.
          Applying the 3' rule, the variant is described as an insertion.<br>
          **NOTE**: this variant is not described as an extension.

        - **new: `p.Met1ext-5` (extension)**<br>
          a variant in the 5' UTR activates a new in-frame upstream translation initiation site starting with amino acid `Met5` (see [Extension](extension.md)).

- **translation termination codon _(stop codon, no-stop change)_**<br>
  see [Extension](extension.md).

- **splicing**
    - **`NP_003997.1:p.?`**<br>
      the predicted consequence of variant `NM_004006.2c.2622G>C` is a silent change (`p.(Lys874=)`).
      Since it affects the last nucleotide of the exon, it can not be excluded that the variant affects splicing, having unknown consequences.<br>
      **NOTE**: when others have reported the same variant, and were able to analyse RNA, you could consider to give the consequences they observed as the predicted consequences for the variant, e.g., `r.[(2603_2622del,2622g>c)]` &nbsp; `p.[(Ser868Argfs*2,Ser868=)]`.

- **uncertain**
    - **`NP_003997.1:p.(Gly56Ala^Ser^Cys)`**<br>
      amino acid `Gly56` is changed to an `Ala`, `Ser`, or `Cys` (see [Uncertain](../uncertain.md)).

- **mosaic**
    - **`LRG_199p1:p.Trp24=/Cys`**<br>
      a mosaic case where at amino acid position `24`, besides the normal amino acid (a `Trp`, described as `=`), also protein is found containing a `Cys` (`p.Trp24Cys`).<br>
      **NOTE**: irrespective of the frequency in which each amino acid was found, the reference is always described first.<br>
      **NOTE**: for the predicted consequences of a variant, the description is `LRG_199t1:p.(Trp24=/Cys)`.

## Discussion

!!! note "Are polymorphisms described like <code class="invalid">p.2366Gln/Lys</code>?"

    No, all substitutions are described as `NP_003997.1:p.Gln2366Lys`.
    In the past, the format `p.2366Gln/Lys` (`p.2366Q/K`) has been used to describe "polymorphic" sequence variants.
    Note that a description should be neutral, simply describe the change, and not include any other information like predicted or known functional consequences.

!!! note "Can I describe a `TrpVal` to `CysArg` variant as a amino acid substitution (<code class="invalid">p.TrpVal24CysArg</code>)?"

    No, this is not allowed.
    By definition, a substitution changes **one** amino acid into **one** other amino acid.
    The change `TrpVal` to `CysArg` should be described as `NP_003997.1:p.Trp24_Val25delinsCysArg`, i.e. a deletion/insertion (delins) (see [Deletion-Insertion](delins.md)).

!!! note "How should you describe an amino acid substitution to any other amino acid?"

    HGVS uses IUPAC symbols (see [Standards](../../background/standards.md)).
    The symbol for 'any' amino acid is `X` / `Xaa`.
    Since `X` has been used to indicate a translation stop codon (nonsense variant), we suggest to use `Xaa` three-letter amino acid code only (e.g., `p.Arg782Xaa`).
