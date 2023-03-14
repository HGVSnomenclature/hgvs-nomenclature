# inversion

## Definition

Inversion: a sequence change where, compared to a reference sequence, <b>more than one nucleotide</b> replacing the original sequence are the reverse complement of the original sequence.

## Description

Format:   **"prefix""positions\_inverted""inv"**,  e.g. r.123\_345inv

**"prefix"**  =  reference sequence used  =  r.
**"positions\_inverted"**  =  range of nucleotides inverted  =  123\_345
**"inv"**  =  type of change is an inversion  =  inv

## Notes

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* **prefix** reference sequences accepted are r. (coding and non-coding RNA)
* by definition, the region inverted ("positions\_inverted") contains **more then one nucleotide**. The description r.234inv is therefore not allowed; a one nucleotide inversion should be described as a [_substitution_](../substitution/)/
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
* **inverted duplications** are described as an insertion using the format r.234\_235ins123\_234inv, not as r.123\_456dupinv
* since exon splice signals will be inverted, large genomic inversions on the RNA level usually give [_deletion_](../deletion/)/ or [_deletion-insertion (indel)_](../indel/)/ variants
* inversions are not used on protein level. Depending on the (predicted) consequences of an inversion on protein level, changes are usually described as either a **delins** or a **frame shift**.
## Examples

* r.177\_180inv: inversion of nucleotides r.177 to r.180, changing ..agg**cuga**uu.. to ..agg<font color="red">ucag</font>uu..
* r.203\_506inv: inversion of the 304 nucleotides from position r.203 to r.506
## Discussion

!!! note "Is the change "aagc" to "uucg" an inversion?"

    No, an inversion would change "aagc" to "gcuu", its <b>revese-complement</b>. "uucg" is only the <b>complement</b> of "aagc".

!!! note "Is the change "aagc" to "cgaa" an inversion?"

    No, an inversion would change "aagc" to "gcuu", its <b>revese-complement</b>. CGAA is only the <b>reverse</b> of "aagc".

!!! note "On the <a href="http"

    //www.HGVS.org/mutnomen/examplesRNA.html">old nomenclature website</a> (bottom) you had the example r.124_500delinsoAB053210.2:r.1289-365_1289-73, i.e. the "o" indicating the inserted sequence AB053210.2:r.1289-365_1289-73 was from the opposite transcriptional strand. Is the "o" still used?: No, the "o" is not used, the insertion is in an inverted orientation so "inv" should be used; r.124_500delinsAB053210.2:r.1289-365_1289-73inv.
