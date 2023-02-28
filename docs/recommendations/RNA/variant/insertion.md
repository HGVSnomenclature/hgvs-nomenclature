---
layout: recommendation
parent: RNA
title: insertion
definition: 
    Insertion: a sequence change where, compared to the reference sequence, one or more nucleotides are inserted <b>and</b> where the insertion is not a copy of a sequence immediately 5'
discussion:
    Can I describe a variant as r.123insg?: No, since the description is not unequivocal it is not allowed. What does the description mean, the insertion of a "g" <b>at</b> position 123 or the insertion of a "g" <b>after</b> position 123?<br>The situation becomes even more complex when using a coding RNA reference sequence a "-" character is used, e.g. r.-14insG; when the insertion is <b>after</b> nucleotide r.-14, is this position r.-13 or r.-15?
    Can I use the "^" character to describe an insertion?: No, insertions can not be described using the format r.123ˆ124insu or r.123ˆ124u. The recommendations try to restrict the number of different characters used to a minimum. Since a character was already used to indicate a range (the <i>underscore</i>) a new character was not required.
    How should I describe the change "aucg<b>aucgaucgauc</b>aggguccc" to "aucg<b>aucgaucgauc</b>a<b>aucgaucgauc</b>ggguccc"?  The fact that the inserted sequence (aucgaucgauc) is present in the original sequence suggests it derives from a duplicative event.: The variant should be described as an insertion; r.17_18ins5_16. A description using "dup" is not correct since, by definition, a duplication should be <b>directly 3'-flanking of the original copy</b> (in tandem). Note that the description given still makes it clear that the sequence inserted between r.17 and r.18 is probably derived from nearby, i.e. position r.5 to r.16, and thus likely derived from a duplicative event.
---