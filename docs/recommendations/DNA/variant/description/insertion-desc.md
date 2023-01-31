### Note

*	**prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
*	the "positions flanking" should contain **two flanking nucleotides**, e.g. 123 and 124 but not 123 and 125.
	*	<sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like g.(100_150)ins(25)
	*	the “positions_flanking” should be listed from 5’ to 3’, e.g. 123_124 not 124_123
*	tandem duplications are described as a duplication (g.123_456**dup**), not an insertion (g.456_457ins123_456, see [_Prioritization_](/recommendations/general/))
	*	**inverted duplications** are described as insertion (g.234_235ins123_234inv), not as a duplication ([_see Inversion_](/recommendations/DNA/variant/inversion))
*	two variants separated by one or more nucleotides should be described individually and **not** as a "delins"
	*	exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins"
:	****NOTE:**** the SVD-WG has prepared a proposal to modify this recommendation ([_see SVD-WG010_](/background/consultation/SVD-WG010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single “delins” variant**
*	for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
*	the **"inserted_sequence"** can be given as the nucleotides inserted (e.g. insAGC) or, for larger insert sequences, by referring to the sequence in the reference sequence (e.g. c.849_850ins858_895) or another reference (e.g. NC_000002.11:g.47643464_47643465ins[NC_000022.10:g.35788169_35788352]). When the inserted sequence is not present in the reference genome it should be submitted to a database (e.g. [GenBank](http://www.ncbi.nlm.nih.gov/genbank/submit/)) and the accession.version number obtained to refer to it.
	*	<sup>1</sup> = [_see Uncertain_](/recommendations/uncertain/); when the postion and/or the sequence of an inserted sequence has not been defined, a description may have a format like g.(100_150)insN[25]
