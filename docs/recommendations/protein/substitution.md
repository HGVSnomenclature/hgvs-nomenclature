# substitution

## Definition

Substitution: a sequence change where, compared to a reference sequence, <b>one</b> amino acid is replaced by <b>one</b> other amino acid.

## Description

Format:   **"prefix""amino_acid""position""new_amino_acid"**,  e.g. p.(Arg54Ser)

**"prefix"**  =  reference sequence used  =  p.<br>
**"amino_acid"**  =  reference amino acid  =  Arg<br>
**"position"**  =  position amino acid subtituted  =  54<br>
**"new_amino_acid"**  =  new amino acid  =  Ser

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and protein level may be given in addition
* **prefix** reference sequence accepted is "p." (protein)
* predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g. p.(Arg727Ser)
* a **nonsense** variant, a variant changing an amino acid to a translation termination (stop) codon, is described as a **substitution**
:    **NOTE**:    a nonsense variant is not described as a [_Deletion_](/recommendations/protein/variant/deletion/) of the C-terminal end of the protein (e.g. p.Trp26\_Arg1623del)
    * variants which introduce an **immediate** translation termination (stop) codon are described as nonsense variant
    * **NOTE**:    not p.Tyr4TerfsTer1 but p.Tyr4Ter (or p.Tyr4*), not p.Tyr4\_Cys5insTerGluAsp but p.Tyr4Ter (or p.Tyr4*), not p.Cys5\_Ser6delinsTerGluAsp but p.Tyr4Ter (or p.Tyr4*)    
* a **no-stop** variant, a variant changing the translation termination codon into an amino acid codon, is described as a **extension** ([_Extension_](/recommendations/protein/variant/extension/))
* changes involving two or more consecutive amino acids are described as a deletion/insertion variant (delins) ([_see Deletion/insertion (delins)_](/recommendations/protein/variant/delins/))
    * the description p.Arg76\_Cys77delinsSerTrp is correct, the description p.[Arg76Ser;Cys77Trp] is not correct
* amino acids that have been tested and found **not changed** (silent) are described as p.Cys123= ([_see SVD-WG001 (no change)_](http://www.hgvs.org/mutnomen/accepted001.html))
## Examples

* **missense**
    * LRG\_199p1:p.Trp24Cys: amino acid Trp24 is changed to a Cys
    * NP\_003997.1:p.(Trp24Cys): amino acid Trp24is predicted to change to a Cys (no experimental proof, e.g. based on DNA level data)
* **nonsense**
    * LRG\_199p1:p.Trp24Ter (p.Trp24\*): amino acid Trp24 is changed to a stop codon (Ter, \*)<br>: **NOTE:**    this change is **not** described as a deletion of the C-terminal end of the protein (i.e. p.Trp24\_Met36853del)
* **silent**  (no change)
    * NP\_003997.1:p.Cys188=: amino acid Cys188 is not changed (DNA level change ..TGC.. to ..TGT..): **NOTE:**    the description p.= means the **entire** protein coding region was analysed and no variant was found that changes (or is predicted to change) the protein sequence.
* **translation initiation codon**  
    * no protein: LRG\_199p1:p.0: as a consequence of a variant in the translation initiation codon no protein is produced: **NOTE:**    LRG\_199p1:p.0? can be used when you predict that no protein is produced. Do not use descriptions like "p.Met1Thr", this is for sure **not** the consequence of the effect on protein translation
    * unknown: LRG\_199p1:p.(Met1?): the consequence, at the protein level, of a variant affecting the translation initiation codon can not be predicted (i.e. is unknown)
    * **new translation initiation site**
        * **<u>downstream</u>**  -  NP\_003997.1:p.Leu2\_Met124del (deletion): a variant in the translation initiation codon causes the activation of a downstream translation initiation site (Met) resulting in deletion of the first 123 amino acids (Met-1 to Val-123) of the protein.<br>: **NOTE:**    the 3' rule applies.
        * **<u>upstream</u>**  -  p.Met1_Leu2insArgSerThrVal (insertion): a variant in the translation initiation codon (Met1) changes it to a Valine (Val) and activates an upstream translation initiation site at position -4, replacing amino acid Met1 with MetArgSerThrVal. Applying the 3' rule the variant is described as an insertion.: **NOTE:**    this variant is not described as an extension
        * **<u>new</u>**  -  p.Met1ext-5 (extension): a variant in the 5’ UTR activates a new in-frame upstream translation initiation site starting with amino acid Met-5 ([_see Extension_](/recommendations/protein/variant/extension))
* translation termination codon _(stop codon, **no-stop change**)_: [_see Extension_](/recommendations/protein/variant/extension)
* splicing
    * NP\_003997.1:p.?: the predicted consequence of variant NM\_004006.2c.2622G>C is a silent change (p.(Lys874=)). Since it affects the last nucleotide of the exon it can not be excluded the variant affects splicing, having unknown consequences.: **NOTE:**    when others have reported the same variant, and were able to analyse RNA, you could consider to give the consequences they observed as the predicted consequences for the variant, e.g. r.[(2603\_2622del,2622g>c)] p.[(Ser868Argfs\*2,Ser868=)]
* uncertain
    * NP\_003997.1:p.(Gly56Ala^Ser^Cys): amino acid Gly56 is changed to an Ala, Ser or Cys ([_see Uncertain_](/recommendations/uncertain/))
* mosaic
    * LRG\_199p1:p.Trp24=/Cys: a mosaic case where at amino acid position 24 besides the normal amino acid (a Trp, described as “=”) also protein is found containing a Cys (Trp24Cys): **NOTE:**    irrespective of the frequency in which each amino acid was found, the reference is always described first: **NOTE:**    for the predicted consequences of a variant the description is LRG_199t1:p.(Trp24=/Cys)
## Discussion

!!! note "<a name="polymorphism"></a>Are polymorphisms described like p.2366Gln/Lys?"

    No, all substitutions are described as NP_003997.1:p.Gln2366Lys. In the past, the format p.2366Gln/Lys (p.2366Q/K) has been used to describe "polymorphic" sequence variants. Note that a description should be neutral, simply describe the change, and not include any other information like predicted or known functional consequences.

!!! note "Can I describe a TrpVal to CysArg variant as a amino acid substitution (p.TrpVal24CysArg)?"

    No, this is not allowed. By definition a substitution changes <b>one</b> amino acid into <b>one</b> other amino acid. The change TrpVal to CysArg should be described as NP_003997.1:p.Trp24_Val25delinsCysArg, i.e. a deletion/insertion (indel) (<a href='http://varnomen.HGVS.org/recommendations/DNA/variant/indel/'><i>see Deletion-Insertion</i></a>).

!!! note "How should you describe an amino acid substitution to any other amino acid?"

    HGVS uses IUPAC symbols (<a href='http://varnomen.hgvs.org/bg-material/standards/'><i>see Standards</i></a>). The symbol for 'any' amino acid is 'X'/'Xaa'. Since 'X' has been used to indicate a translation stop codon (nonsense variant) we suggest to use 'Xaa' three-letter amino acid code only (e.g. p.Arg782Xaa).