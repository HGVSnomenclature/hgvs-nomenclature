---
parent: RNA
title: inversion
category: description
---

Format:   **"prefix""positions\_inverted""inv"**,  e.g. r.123\_345inv

**"prefix"**  =  reference sequence used  =  r.<br>
**"positions\_inverted"**  =  range of nucleotides inverted  =  123\_345<br>
**"inv"**  =  type of change is an inversion  =  inv

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	**prefix** reference sequences accepted are r. (coding and non-coding RNA)
*	by definition, the region inverted ("positions\_inverted") contains **more then one nucleotide**. The description r.234inv is therefore not allowed; a one nucleotide inversion should be described as a [_substitution_](/recommendations/RNA/variant/substitution/)
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
*	**inverted duplications** are described as an insertion using the format r.234\_235ins123\_234inv, not as r.123\_456dupinv
*	since exon splice signals will be inverted, large genomic inversions on the RNA level usually give [_deletion_](/recommendations/RNA/variant/deletion/) or [_deletion-insertion (indel)_](/recommendations/RNA/variant/indel/) variants
*	inversions are not used on protein level. Depending on the (predicted) consequences of an inversion on protein level, changes are usually described as either a **delins** or a **frame shift**.
