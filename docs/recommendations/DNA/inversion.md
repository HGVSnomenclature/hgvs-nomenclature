# inversion

## Definition

Inversion: a sequence change where, compared to a reference sequence, <b>more than one nucleotide</b> replacing the original sequence are the reverse complement of the original sequence.

## Description

Format:   **"prefix""positions\_inverted""inv"**,  e.g. g.123_345inv

**"prefix"**  =  reference sequence used  =  g.
**"positions\_inverted"**  =  range of nucleotides inverted  =  123_345
**"inv"**  =  type of change is an inversion  =  inv

## Notes

* **prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
* by definition, the region inverted ("positions\_inverted") contains **more then one nucleotide**. The description g.234inv is therefore not allowed; a one nucleotide inversion should be described as a [_substitution_](/recommendations/DNA/variant/substitution/)
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
    * the 3'rule applies to ALL descriptions (genome, gene, transcript and protein) of a given variant
* **inverted duplications** are described as an insertion using the format g.234\_235ins123\_234inv, not as g.123\_456dupinv ([_see Q&A_](#dupinv))
* two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
    * exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:    ****NOTE:**** the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/consultation/SVD-WG010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
* inversions are not used on protein level. Depending on the (predicted) consequences of an inversion on protein level, changes are usually described as either a **delins** or a **frame shift**.
## Examples

* NC\_000023.10:g.32361330\_32361333inv: inversion of nucleotides g.32361330 to g.32361333, changing ..CA**TCAG**CCT.. to ..CA<font color="red">CTGA</font>CCT..
* NM\_004006.2:c.5657\_5660inv: inversion of nucleotides c.5657 to c.5660 (coding DNA reference sequence), changing ..AGGCTGATG.. to ..AGG<font color="red">TCAG</font>TG..
* NM\_004006.2:c.4145\_4160inv: inversion of the 16 nucleotides from position c.4145 to c.4160
* NC\_000023.10:g.111754331\_111966764inv: a large inversion (212,434 nucleotides) from position g.111754331 to g.111966764
* NM\_004006.2:c.849\_850ins850\_900inv: a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 5’ of the original sequence, between nucleotide c.849 and c.850
* NM\_004006.2:c.900\_901ins850\_900inv: a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 3’ of the original sequence, between nucleotide c.900 and c.901
* LRG\_199t1:c.940\_941ins[885\_940inv;A;851\_883inv]: an inverted copy of nucleotides c.851 to c.940, with a G>A substitution of nucleotide c.884, is inserted directly 3’ of the original sequence
* NM\_004006.2:c.940\_941ins[903\_940inv;851\_885inv]: an inverted copy of nucleotides c.851 to c.940, with a deletion from nucleotides c.886 to c.902, is inserted directly 3’ of the original sequence
## Discussion

!!! note "Is the change AAGC to TTCG an inversion?"

    No, an inversion would change AAGC to GCTT, its <b>reverse-complement</b>. TTCG is only the <b>complement</b> of AAGC.

!!! note "Is the change AAGC to CGAA an inversion?"

    No, an inversion would change AAGC to GCTT, its <b>reverse-complement</b>. CGAA is only the <b>reverse</b> of AAGC.<a name="dupinv"></a>

!!! note "Is it not better to describe the variant g.234_235ins123_234inv as g.123_234dupinv?"

    The descriptions of duplications is regularly debated <i>"Why not remove the variant type "duplication" and describe all dups as "insertion", it will make the HGVS rules in total simpler</i>. While we can not do this for historic reasons (duplications are in use since the beginning), we will restrict the use of "dup" as much as possible. Regarding a "<b>dupinv</b>" one could argue that an "inverted copy" is not "a copy inserted directly 3' of the original copy" and thus by definition this variant is not a duplication but an "insertion". Therefore the recommendation is to describe inverted duplication using the format g.122_123ins123_234inv or g.234_235ins123_234inv depending on whether the inverted copy is 5' or 3' of the original copy (reference sequence).
