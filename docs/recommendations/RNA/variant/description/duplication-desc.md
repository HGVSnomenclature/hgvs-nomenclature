### Note

* all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
* **prefix** reference sequences accepted are r. (coding and non-coding RNA).
* “positions_duplicated” should contain two different positions, e.g. 123_126 not 123_123.
* the “positions_duplicated” should be listed from 5’ to 3’, e.g. 123_126 not 126_123.
* by definition, duplication may only be used when the additional copy is **directly 3’-flanking** of the original copy (a “tandem duplication”).
    * when a variant can be described as a duplication it **must** be desribed as a duplication and not as e.g. an insertion (see [_Prioritization_](/recommendations/general/))
    * when there is no evidence that the extra copy of a sequence detected is in tandem (directly 3'-flanking) the original copy, the change can not be described as a duplication, it should be described as **an insertion** ([_see Insertion_](/recommendations/RNA/variant/insertion/)).
    * **inverted duplications** are described as insertion (r.234\_235ins123\_234inv), not as a duplication ([_see Inversion_](/recommendations/RNA/variant/inversion))
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
    * the 3'rule also applies for changes in single residue stretches and tandem repeats
    * **NOTE:** the exception to the 3'rule for duplications around exon/exon junctions  [_see Duplications_](/recommendations/DNA/variant/duplication/) does not apply when describing variants based on a RNA reference sequence