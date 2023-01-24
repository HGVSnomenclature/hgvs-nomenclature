---
parent: DNA
title: repeated sequences
category: description
---

_**<font color="#FF0000">NOTE:</font>**_ a Community Consultation is prepared which will suggest to allow **only one format** where the entire range of the repeated sequence must be indicated, e.g. g.123\_191CAG[23] not g.123CAG[23]

Format (unique repeat):   **"prefix""position_first_nucleotide_first_repeat_unit""repeat_sequence"["copy_number"]**,  e.g. g.123CAG[23]

*	**"prefix"**  =  reference sequence used  =  g.<br>
*	**"position_first_nucleotide_first_repeat_unit"**  =  first nucleotide of first repeat unit  =  123<br>
*	**"repeat_sequence"**  =  sequence repeat unit  =  CAG<br>
*	**[**  =  opening symbol for copy number allele  =  [<br>
*	**"copy_number"**  =  number of repeat units  =  23<br>
*	**]**  =  closing symbol for copy number allele  =  ]

Format (mixed repeat):   **"prefix""range_repeated_sequence""repeat_sequence_unit1"["copy_number"]"repeat_sequence_unit2"["copy_number"]"..."**,  e.g. g.123\_191CAG[19]CAA[4]

*	**"prefix"**  =  reference sequence used  =  g.<br>
*	**"range_repeated_sequence"**  =  position first to last nucleotide repeated sequence (range)   =  123_191<br>
*	**"repeat_sequence_unit1"**  =  sequence first repeat unit  =  CAG<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"copy_number"**  =  number of repeat units  =  19<br>
*	**]**  =  closing symbol for allele  =  ]
*	**"repeat_sequence_unit2"**  =  sequence first repeat unit  =  CAA<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"copy_number"**  =  number of repeat units  =  4<br>
*	**]**  =  closing symbol for allele  =  ]
*	**...**  =  and so on for repeat_sequence_unit3, repeat_sequence_unit4, etc.

---

### Note

*	reference sequences accepted are g., o. m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA)
*	for **mixed repeats** the range of the reapeat sequence is given followed by a listing of each repeat unit and the number of repeats in each unit; NC\_000012.11:g.112036755\_112036823CTG[9]TTG[1]CTG[13].
*	NM\_000044.3:c.171GCA[23] describes a repeated sequence containing 23 GCA units (sequenced). NM\_000044.3:c.(92_331)insN[33] describes an insertion of 3 nucleotides, in the amplified region from position c.92 to c.331 (**not sequenced**), of a repeated sequence containing 24 GCA units.
*	_**exception:**_ using a coding DNA reference sequence ("c." description) a Repeated sequence variant description can be used only for repeat units with a length which is a multiple of 3, i.e. which can not affect the reading frame. Consequently, use NM\_024312.4:c.2692_2693dup and **not** NM\_024312.4:c.2686A[10], use NM\_024312.4:c.1741\_1742insTATATATA and **not** NM\_024312.4:c.1738TA[6].
