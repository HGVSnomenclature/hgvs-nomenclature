# insertion

## Definition

Insertion: a sequence change where, compared to the reference sequence, one or more nucleotides are inserted <b>and</b> where the insertion is not a copy of a sequence immediately 5'

## Description

Format: **"prefix""positions_flanking""ins""inserted_sequence"**,  e.g. g.123\_124insAGC

**"prefix"**  =  reference sequence used  =  g.
**"positions_flanking"**  =  position two nucleotides flanking insertion site  =  123\_124
**"ins"**  =  type of change is an insertion  =  ins
**"inserted_sequence"**  =  inserted sequence  =  AGC <sup>1</sup>

## Notes

* **prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
* the "positions flanking" should contain **two flanking nucleotides**, e.g. 123 and 124 but not 123 and 125.
    * <sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like g.(100_150)ins(25)
    * the “positions_flanking” should be listed from 5’ to 3’, e.g. 123_124 not 124_123
* tandem duplications are described as a duplication (g.123\_456**dup**), not an insertion (g.456\_457ins123\_456, see [_Prioritization_](/recommendations/general/))
    * **inverted duplications** are described as insertion (g.234\_235ins123\_234inv), not as a duplication ([_see Inversion_](/recommendations/DNA/variant/inversion))
* two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
    * exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:    ****NOTE:**** the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/background/consultation/SVD-WG010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
* the **"inserted_sequence"** can be given as the nucleotides inserted (e.g. insAGC) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g. c.849\_850ins858_895) or another reference (e.g. NC\_000002.11:g.47643464\_47643465ins[NC\_000022.10:g.35788169\_35788352]). When the inserted sequence is not present in the reference genome it should be submitted to a database (e.g. [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/)) and the accession.version number obtained to refer to it.
    * <sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like g.(100\_150)insN[25]
## Examples

* simple insertions
    * NC\_000023.10:g.32867861\_32867862insT  (NM\_004006.2:c.169\_170insA): the insertion of an T nucleotide between nucleotides g.32867861 and g.32867862 
    * NC\_000023.10:g.32862923\_32862924insCCT (LRG\_199t1:c.240\_241insAGG): the insertion of nucleotides CCT between nucleotides g.32862923 and g.32862924
    * NM\_004006.2:c.849\_850ins858\_895: the insertion of a copy of nucleotids c.858 to c.895 between nuclotides c.849 and c.850
    * NC\_000002.11:g.47643464\_47643465ins[NC\_000022.10:g.35788169\_35788352]: the insertion of nucleotides g.35788169 and g.35788352 as found in NC\_000022.10 between nucloetides g.47643464 and g.47643465
* complex insertions
    * NM\_004006.2:c.419\_420ins[T;401\_419]: the insertion of T followed by a copy of the sequence from c.401 to c.419 (a duplication not directly flanking the original sequence)
    * LRG\_199t1:c.419\_420ins[T;450\_470;AGGG]: the insertion of T followed by a copy of the sequence from c.450 to c.470, followed by AGGG
    * NC\_000006.11:g.10791926\_10791927ins[NC\_000004.11:g.106370094\_106370420;A[26]]: the insertion of a copy of an Alu-repeat sequence (from chromosome 4 nucleotides g.106370094 to g.106370420), and a stretch of 26 A nucleotides, between nucleotides g.10791926 and g.10791927 on chromosome 6. 
* insertion of inverted duplicated copies
    * NM\_004006.2:c.849\_850ins850\_900inv: a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 5' of the original sequence, between nucleotide c.849 and c.850
    * NM\_004006.2:c.900\_901ins850\_900inv: a copy of nucleotides c.850 to c.900 is inserted, in inverted orientation, 3' of the original sequence, between nucleotide c.900 and c.901
    * LRG_199t1:c.940\_941ins[885\_940inv;A;851\_883inv]: an inverted copy of nucleotides c.851 to c.940, with a G>A substitution of nucleotide c.884, is inserted directly 3' of the original sequence
    * NM\_004006.2:c.940\_941ins[903\_940inv;851\_885inv]: an inverted copy of nucleotides c.851 to c.940, with a deletion from nucleotides c.886 to c.902, is inserted directly 3' of the original sequence
* incomplete descriptions, preferably use exact descriptions only
    * NM\_004006.2:c.(222\_226)insG: the insertion of a G at an unknown position in the sequence encoding amino acid 75
    * NC\_000004.11:g.(3076562\_3076732)insN[12]: the insertion of 12 nucleotides (not specified) at an unknown position between nucleotides g.3076562 and g.3076732 (exon 1 of the HTT gene containing the Gln/Pro repeat region)
    * NC\_000023.10:g.32717298\_32717299insN  (NM\_004006.2:c.761\_762insN) : the insertion of one not specified nucleotide (N) between position g.32717298 and g.32717299
    * NM\_004006.2:c.761\_762insNNNNN (alternatively NM\_004006.1:c.761\_762insN[5]): the insertion of 5 not specified nucleotides (NNNNN) between position c.761 and c.762
    * NC\_000023.10:g.32717298\_32717299insN[100]: the insertion of 100 nucleotides (not specified) between position g.32717298 and g.32717299
    * NC\_000023.10:g.32717298\_32717299insN[(80_120)]: the insertion of 80 to 120 nucleotides between position g.32717298 and g.32717299
    * NC\_000023.10:g.32717298\_32717299insN[?]: the insertion of an unknown number of nucleotides between position g.32717298 and g.32717299
    * NC\_000006.11:g.8897754\_8897755ins[N[543];8897743\_8897754]: the insertion of an undefined sequence of 543 nucleotides (N[543]), and a 12 nucleotide target site duplication (g.8897743 to g.8897754), between nucleotides g.8897754 and g.8897755 on chromosome 6. 
* g.?\_?ins[NC\_000023.10:(12345\_23456)\_(34567\_45678)]: the insertion of a sequence from the X-chromosome (NC\_000023.10), maximally involving nucleotides 12345\_45678 but certainly nucleotides 23456\_34567, at an unknown position (g.?\_?) in the genome ([_see Uncertain_](/recommendations/uncertain))
## Discussion

!!! note "Can I describe a variant as g.123insG?"

    No, since the description is not unequivocal it is not allowed. What does the description mean, the insertion of a G <b>at</b> position 123 or the insertion of a G <b>after</b> position 123?<br>The situation becomes even more complex when using a coding DNA reference sequence a "-" character is used, e.g. c.-14insG or c.456-13insG. In the description c.456-13insG, when the insertion is <b>after</b> intronic nucleotide c.456-13, is this position c.456-12 or c.456-14?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format g.123ˆ124insG or g.123ˆ124G. The recommendations try to restrict the number of different characters used to a minimum. Since a character was already used to indicate a range (the <i>underscore</i>) a new character was not required.

!!! note "How should I describe the change ATCG<b>ATCGATCGATCG</b>AGGGTCCC to ATCG<b>ATCGATCGATCG</b>A<b>ATCGATCGATC</b>GGGTCCC?  The fact that the inserted sequence (ATCGATCGATCG) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; g.17_18ins5_16. A description using "dup" is not correct since, by definition, a duplication should be <b>directly 3'-flanking of the original copy</b> (in tandem). Note that the description given still makes it clear that the sequence inserted between g.17 and g.18 is probably derived from nearby, i.e. position g.5 to g.16, and thus likely derived from a duplicative event.

!!! note "A variant in the CDKN2A gene, duplicating the first 24 nucleotides of the coding DNA reference sequence, has been described as c.23ins24. My interpretation is it should be described as c.1_24dup, is this correct?"

    Since the sequence in that region si cagc<b><u>ATGGAGCC</u>GGCGGCGGGGAGCAGC</b><u>ATGGAGCC</u>TTCG.. the correct decription is c.9_32dup (p.(Ala4_Pro11dup)). c.1_24dup seems correct but neglects the <b>3'rule</b> (3' shift possible for the underlined region). c.23ins24 is not correct since the position of the insertion is not described properly and because ins"24" does not define the sequence inserted.
---