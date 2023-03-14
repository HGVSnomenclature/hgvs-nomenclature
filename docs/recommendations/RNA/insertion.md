# insertion

## Definition

Insertion: a sequence change where, compared to the reference sequence, one or more nucleotides are inserted <b>and</b> where the insertion is not a copy of a sequence immediately 5'

## Description

Format: **"prefix""positions_flanking""ins""inserted_sequence"**,  e.g. r.123\_124insauc

**"prefix"**  =  reference sequence used  =  r.
**"positions_flanking"**  =  position two nucleotides flanking insertion site  =  123\_124
**"ins"**  =  type of change is an insertion  =  ins
**"inserted_sequence"**  =  inserted sequence  =  auc <sup>1</sup>

## Notes

* **prefix** reference sequences accepted are r. (coding and non-coding RNA).
* the "positions_flanking" should contain **two flanking nucleotides**, e.g. 123 and 124 but not 123 and 125.
    * the “positions_flanking” should be listed from 5’ to 3’, e.g. 123_124 not 124_123
* when a variant can be described as a duplication it **must** be desribed as a duplication and **not as an insertion** (see [_Prioritization_](/recommendations/general/)
* for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
* the **“inserted_sequence”** can be given as the nucleotides inserted (e.g. insAGC) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g. c.849_850ins858_895) or another reference (see Examples).
    * when the inserted sequence is very long it can best be submitted to a database (e.g. [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/)); the accession.version number obtained can then be used to describe the variant like r.123\_124insL37425.1:r.23\_361
* <sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like r.(100_150)ins(25)
## Examples

* LRG\_199t1:r.426\_427insa: the insertion of an "a" nucleotide between nucleotides r.426 and r.427 
* LRG\_199t1:r.756\_757insuacu: the insertion of nucleotides "uacu" between nucleotides r.756 and r.757
* NM\_004006.2:r.(222\_226)insg (p.Asn75fs): the insertion of a "g" at an unknown position in the sequence encoding amino acid 75
* NM\_004006.2:r.549\_550insn : the insertion of one not specified nucleotide (n) between position r.549 and r.550
* NM\_004006.2:r.761\_762insnnnnn (alternatively r.761\_762insn[5]): the insertion of 5 not specified nucleotides (nnnnn) between position r.761 and r.762
* LRG\_199t1:r.1149\_1150insn[100]: the insertion of 100 not specified nucleotides between position r.1149 and r.1150
* NG\_012232.1(NM\_004006.2):r.2949\_2950ins[2950-30\_2950-12;2950-4\_2950-1]: the insertion of intronic nucleotides r.2950-30 to r.2950-12 and r.2950-4 to r.2950-1 between nucleotides r.2949 and r.2950 (caused by the deletion NC\_000023.10(NM\_004006.2):c.2950-11\_2950-5del]. Alternative description r.2949\_2950ins[2950-30\_2950-12;uuag]
    * **NOTE:**    for more examples of variants affecting splicing see [_Splicing_](/recommendations/RNA/splicing/)
## Discussion

!!! note "Can I describe a variant as r.123insg?"

    No, since the description is not unequivocal it is not allowed. What does the description mean, the insertion of a "g" <b>at</b> position 123 or the insertion of a "g" <b>after</b> position 123?<br>The situation becomes even more complex when using a coding RNA reference sequence a "-" character is used, e.g. r.-14insG; when the insertion is <b>after</b> nucleotide r.-14, is this position r.-13 or r.-15?

!!! note "Can I use the "^" character to describe an insertion?"

    No, insertions can not be described using the format r.123ˆ124insu or r.123ˆ124u. The recommendations try to restrict the number of different characters used to a minimum. Since a character was already used to indicate a range (the <i>underscore</i>) a new character was not required.

!!! note "How should I describe the change "aucg<b>aucgaucgauc</b>aggguccc" to "aucg<b>aucgaucgauc</b>a<b>aucgaucgauc</b>ggguccc"?  The fact that the inserted sequence (aucgaucgauc) is present in the original sequence suggests it derives from a duplicative event."

    The variant should be described as an insertion; r.17_18ins5_16. A description using "dup" is not correct since, by definition, a duplication should be <b>directly 3'-flanking of the original copy</b> (in tandem). Note that the description given still makes it clear that the sequence inserted between r.17 and r.18 is probably derived from nearby, i.e. position r.5 to r.16, and thus likely derived from a duplicative event.
---