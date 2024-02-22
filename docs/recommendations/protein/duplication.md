# Duplication

<!-- ## Definition -->

Duplication: a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, a copy of one or more amino acids is inserted **directly C-terminal** of the original copy of that sequence.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml aa.dup
```

## Notes

- all variants **should be** described on the DNA level; descriptions on the RNA and/or protein level may be given in addition.
- predicted consequences, i.e. without experimental evidence (no RNA or protein sequence analysed), should be given in parentheses, e.g., `p.(Arg727_Ser783dup)`.
- the "positions_duplicated" should contain **two different** positions, i.e. `Cys76_Glu79`, not `Cys76_Cys76`.
    - the "positions_duplicated" should be listed from **5' to 3'**, i.e. `Cys76_Glu79`, not `Glu79_Cys76`.
- by definition, duplication may only be used when the additional copy is **directly C-terminal** of the original copy (a "tandem duplication").
    - when the extra copy is, on the protein level, not in tandem (directly C-terminal), the change should be described as **insertion** (see [Insertion](insertion.md)).
    - duplications extending the amino acid sequence at the C-terminal end with one or more amino acids are described as an [Extension](extension.md).
- for all descriptions, the **most C-terminal position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**).
- duplications on the DNA or RNA level, **starting N-terminal of and including** the translation termination (stop) codon usually have no (predicted) effect on the protein level.
- duplications on DNA or RNA level that
    - introduce an **immediate** translation termination (stop) codon on the protein level, are described as a nonsense variant.
    - **encode a translation stop codon** in the duplicated sequence are on the protein level described as an insertion of this sequence, not as a deletion-insertion removing the entire C-terminal amino acid sequence.
    - encode an open reading frame which **after** the duplicated sequence shifts to another reading frame, are described as a [frameshift](frameshift.md).

## Examples

- one amino acid
    - **`NP_003997.2:p.Val7dup`**<br>
      a duplication of amino acid `Val7` in the reference sequence `NP_003997.2`.

    - **`NP_003997.2:p.(Val7dup)`**<br>
      the **predicted** consequence on the protein level is a duplication of amino acid `Val7` in the reference sequence `NP_003997.2`.

    - **`NP_003997.2:p.Trp4dup`**<br>
      a duplication of amino acid `Trp4` in the sequence `MetLeuTrpTrpGlu` to `MetLeuTrpTrp`<code class="ins">Trp</code>`Glu`.<br>
      **NOTE**: for duplications in single amino acid stretches or tandem repeats, the most C-terminal residue is arbitrarily assigned to have been duplicated.

- several amino acids
    - **`NP_003997.2:p.Lys23_Val25dup`**<br>
      a duplication of amino acids `Lys23` to `Val25` in reference sequence `NP_003997.2`.

    - **`NP_003997.2:p.(Pro458_Gly460dup)`**<br>
      a duplication of amino acids `Pro458`, `Pro459`, and `Gly460` in reference sequence `NP_003997.2`.<br>
      **NOTE**: the underlying DNA variant (`LRG_232t1:c.1365_1373dup`) affects amino acids `Pro455`, `Pro456`, and `Gly457`, but the 3'rule needs to be applied.

- one or more exons
    - **`NP_003997.2:p.(His321_Glu383dup)`**<br>
      the predicted consequences of a duplication of exon 10 of the _DMD_ gene, duplicating amino acids `His321` to `Glu383` in reference sequence `NP_003997.2`.

    - **`NP_003997.2:p.(Asp90_Val120dup)`**<br>
      the predicted consequences of a duplication of exon 5 of the _DMD_ gene, duplicating amino acids `Asp90` to `Val120` in reference sequence `NP_003997.2`.<br>
      **NOTE**: since the 3'rule needs to be applied, the description `p.(Val89_Gln119dup)` is not correct.

    - **`NP_003997.2:p.(Asn444Lysfs*15)`**<br>
      the predicted consequences of a duplication of exons 10 to 11 of the _DMD_ gene, creating a frameshift starting at amino acid `Asn444`, replacing it with `Lys` and terminating after fifteen codons.

    - **`NP_003997.2:p.?`**<br>
      the predicted consequences of a duplication of exons 1 to 2 of the _DMD_ gene.<br>
      **NOTE**: since the duplication adds a second promoter/exons 1 to a normal copy of the gene, a reliable prediction of the consequences can not be made.
      The duplication may have no consequences, it may give a duplication of exon 2 in the transcript, it might produce both transcripts, etc.

    - **`NP_003997.2:p.?`**<br>
      the predicted consequences of a duplication of exons 74 to 79 of the _DMD_ gene.<br>
      **NOTE**: since the duplication adds a second last exon (exon 79) to a normal copy of the gene, a reliable prediction of the consequences can not be made.
      The duplication may have no consequences, it may give a duplication of exons 74 to 78 in the transcript, it might produce both transcripts, etc.

- other
    - **`NP_003997.1:p.Val7=/dup`**<br>
      a mosaic case where at amino acid position 7, besides the normal amino acid (a `Val`, described as `Val7=`), also protein is found containing a duplication (`p.Val7dup`).<br>
      **NOTE**: for the predicted consequences of a variant, the description is `NP_003997.1:p.(Val7=/dup)`.

## Discussion

!!! note "Why do we not describe a duplication as an insertion?"

    Although duplications are basically a special type of insertion, there are several reasons why the recommendation is to describe duplications separately.

    - the description is simple and shorter;
    - it is clear and prevents confusion regarding the position when an insertion is incorrectly reported, like <code class="invalid">p.Ala22insGly</code>;
    - insertion more or less means "coming from elsewhere".
      Mechanistically, a duplication is most likely caused by a local event, DNA polymerase slippage, duplicating a local sequence.

!!! note "How should I describe the change `MetArgThr`<code class="spot1">GlySerSer</code>`HisGlnTrpPhe` to `MetArgThr`<code class="spot1">GlySerSer</code>`His`<code class="ins">GlySerSer</code>`GlnTrpPhe`? The fact that the inserted sequence (<code class="ins">GlySerSer</code>) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; `p.His7_Gln8insGly4_Ser6`.
    A description using "dup" is not correct since, by definition, a duplication should be **directly 3'-flanking of the original copy** (in tandem).
    Note that the description given still makes it clear that the sequence inserted between `p.His7` and `p.Gln8` is probably derived from nearby, i.e. position `p.Gly4` to `p.Ser6`, and thus likely derived from a duplicative event.

!!! note "What do you mean with "variants should be described on the protein level and not incorporate knowledge regarding the change on the DNA-level"?"

    It means that protein variant descriptions should be derived from comparing the variant protein sequence with the reference protein sequence.
    Knowledge on the underlying change on the DNA level should not be used.
    E.g., when `MetTrpSerSerSerHisAsp..` changes to `MetTrpSerSerSer`<code class="ins">Ser</code>`HisAsp..`, this is described as `p.Ser5dup`.
    The information that on the DNA level the change is `..ATGTGGTCCAGTTCCCACGAT..` to `..ATGTGGTCCAGT`<code class="ins">AGT</code>`TCCCACGAT..`, so the codon for `Ser4` is duplicated, is not used; the description `p.Ser4dup` is not correct.
