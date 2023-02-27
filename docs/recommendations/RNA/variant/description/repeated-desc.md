---
parent: RNA
title: repeated sequences
category: description
---

Format (repeat position):   **"prefix""position_repeat_unit""[""copy_number""]"**,  e.g. r.-125_-123[12]

*	**"prefix"**  =  reference sequence used  =  r.<br>
*	**"position_repeat_unit"**  =  position (range) first repeat unit  =  -125\_-123<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"copy_number"**  =  number of repeat copy  =  12<br>
*	**]**  =  closing symbol for allele  =  ]

Format (sequence):   **"prefix""position_repeat_start""repeat_sequence""[""copy_number""]"**,  e.g. r.-125cug[12]

*	**"prefix"**  =  reference sequence used  =  r.<br>
*	**"position_repeat_start"**  =  position first nucleotide repeat unit  =  -125<br>
*	**"repeat_sequence"**  =  nucleotide sequence repeat unit  =  ggc<br>
*	**[**  =  opening symbol for allele  =  [<br>
*	**"copy_number"**  =  number of repeat copy  =  12<br>
*	**]**  =  closing symbol for allele  =  ]

---

### Note

*	all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
*	reference sequences accepted are r. (coding and non-coding RNA).
*	repeated sequences include both small (mono-, di-, tri-, etc., nucleotide) and larger (kilobase-sized) repeats. 
*	the format based on **repeat position** is preferred, descriptions of the repeat sequence quickly become too lengthy.
	*	_**NOTE**_: while r.123cug[23] describes a repeat of 23 "cug" units, r.123\_125[23] describes a tri-nucleotide repeat of 23 units which **could be interrupted** with other units (e.g. a rare "cua"). The description r.123cug[23] can thus only be used when the repeat was sequenced.
*	the format r.-125\_-123cug[4], should not be used; it contains redundant information ("-125\_-123" and "cug"). 
*	for **composite repeats** the basic format can be used, successively listing each different repeat unit; r.456\_465[4]466\_489[9]490\_499[3].
