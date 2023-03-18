# substitution

## Definition

Substitution: a sequence change where, compared to a reference sequence, <b>one</b> nucleotide is replaced by <b>one</b> other nucleotide.

## Description

Format:   **"prefix""position_substituted""reference_nucleotide"">"new_nucleotide"**,  e.g. g.123A>G

**"prefix"**  =  reference sequence used  =  g.
**"position_substituted"**  =  position nucleotide sustituted  =  123
**"reference_nucleotide"**  =  nucleotide at reference position =  A
**">"**  =  type of change is a substitution =  >
**"new_nucleotide"**  =  substituted nucleotide  =  G

## Notes

* **prefix** reference sequences accepted are g., m., c. and n. (genomic, mitochondrial, coding DNA and non-coding DNA).
* substitutions involving two or more consecutive nucleotides are described as deletion/insertion (delins) variants (see [Deletion/insertion (delins)](../delins/)).
* two variants separated by one or more nucleotides should be described individually and not as a "delins" of the sequence affected
    * exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins": **NOTE:** this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions (e.g. c.235\_237delinsTAT (p.Lys79Tyr) versus c.[235A>T;237G>T] (p.[Lys79*;Lys79Asn]): ****NOTE:**** the SVD-WG has prepared a proposal to modify this recommendation (see [SVD-WG010](../../../consultation/SVD-WG010/)). The new proposal is: **two variants that are separated by two or fewer intervening nucleotides (that is, not including the variants themselves) should be described as a single "delins" variant**
* nucleotides that have been tested and found **not changed** are described as c.123=, g.4567_4569= (see [SVD-WG001 (no change)](../../../consultation/SVD-WG001/)).
* it is not correct to describe "_polymorphisms_" as c.76A/G (see [Discussions](#polymorphism)).
## Examples

* NC\_000023.10:g.33038255C>A: a substitution of the C nucleotide at g.33038255 by an A
* NG\_012232.1(NM\_004006.2):c.93+1G>T: a substitution of the G nucleotide at c.93+1 (coding DNA reference sequence) by a T
* LRG\_199t1:c.79\_80delinsTT: nucleotides c.79 and c.80 are replaced by TT: **NOTE**: changes involving two or more consecutive nucleotides are described as deletion-insertion (delins) so the description c.[79G>T;80C>T] is not correct: **NOTE**: based on the definition of a substitution, i.e. **one** nucleotide replaced by **one** other nucleotide, this change can not be described as a substitution like c.79\_80GC>TT or c.79GC>TT
* NM\_004006.2:c.145\_147delinsTGG: two substitutions replacing codon CGC (position c.145 to c.147) by TGG: **NOTE**: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins" so the description c.[145C>T;147C>G] is not correct (see [deletion/insertion]())
* LRG\_199t1:c.54G>H: a substitution of the G nucleotide at c.54 (coding DNA reference sequence) by A, C or T (IUPAC code "H", see [Standards](../../../background/standards/))
* NM\_004006.2:c.123=: a screen was performed showing that nucleotide c.123 was a "C" as in the coding DNA reference sequence (the nucleotide was not changed).: **NOTE**: the description NM\_004006.2:c.= can not be used, c.= indicates the entire NM\_004006.2 coding DNA reference sequence was analysed and no change was identified.: **NOTE**: the description LRG\_199t1:c.94-23_188+33= indicates no variants where found in the region indicated (exon 3 of the DMD gene).
* LRG\_199t1:c.85=/T>C: a mosaic case where at position 85 besides the normal sequence (a T, described as "=") also chromosomes are found containing a C (c.85T>C): **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first
* NM\_004006.2:c.85=//T>C: a chimeric case, i.e. the sample is a mix of cells containing c.85= and c.85T>C.: **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first
## Discussion

!!! note "When I only sequenced RNA (cDNA) and not genomic DNA should I then give the description of a variant at DNA level in parenthesis?"

    Yes, while the variant at RNA level can be described as r.76a>g on DNA level, based on e.g. a coding DNA reference, sequence it should be described as c.(76A>G).

!!! note "How can I shorten the descriptions of SNPs in a manuscript?"

    Publications reporting linkage or association studies often use a range of different markers/SNPs. Such publications should contain at least once an <b>unequivocal description of all markers</b> used linking them to a reference sequence, preferably a genomic reference sequence. When this has been done, simplified descriptions can be used like;<ul><li><b>NM_004006.1 3G>T</b>, using a GenBank coding DNA reference sequence,</li><li><b><i>GJB2</i> 76A>C</b>, using a HGNC-approved gene symbol as reference,</li><li><b>rs2306220 T>C</b>, using a [dbSNP-identifier](http://www.ncbi.nlm.nih.gov/SNP) as a reference,</li> <li><b>DXS1219 CA[18];[21]</b> (or AFM297yd1 CA[18];[21]), using a marker DXS1219 (AFM297yd1) as reference.</li></ul>

!!! note "How should I describe a variant in the promoter region of a gene?"

    It is recommended to describe variants in the promoter region of a gene based on a genomic reference sequence, e.g. NC_000023.10:g.33357783G>A (chrX, hg19). Describing the variant in relation to a coding DNA reference sequence (for this variant NM_004006.1:c.-128354C>T or NM_000109.3:c.-401C>T) is possible but not really very informative; you do not know how long the 5'UTR is. The variant can also be described using a genomic reference sequence containing the promoter region (for this variant e.g. L01538.1:g.1407C>T), but again this is not really informative. Although NC_000023.10:g.33357783G>A seems complex, it can be used in a genome browsers helping you to quickly zoom in on the region of interest.<a name="polymorphism"></a>

!!! note "Are polymorphisms described like NM_004006.1:c.76A/G?"

    No, all substitutions are described as NM_004006.1:c.76A>G. In the past, the format c.76A/G has been used to describe "polymorphic" sequence variants. Note that a description should be neutral, simply describe the change, and not include any other information like predicted or known functional consequences.

!!! note "Can I describe a GC to TG variant as a dinucleotide substitution (NG_012232.1:g.12GC>TG)?"

    No, this is not allowed. By definition a substitution changes <b>one</b> nucleotide into <b>one</b> other nucleotide. The change GAAGCCAG to GAA<font color="red">TG</font>CAG should be described as NG_012232.1:g.12_13delinsTG, i.e. a deletion/insertion (indel) (see [Deletion-Insertion](http://varnomen.hgvs.org/recommendations/DNA/variant/delins/) and Description - Note). When phase information is not available, the variant should be described as NG_012232.1:g.12G>T(;)13C>G (see [Alleles](http://varnomen.hgvs.org/recommendations/DNA/variant/alleles/)).

!!! note "The <i>BRCA1</i> coding DNA reference sequence NM_007294.3 from position c.2074 to c.2080 is ..CATGACA.. A variant frequently found in the population is ..CAT<font color="red">A</font>ACA.. (NM_007294.3:c.2077G>A). In a patient I found the sequence ..CATA<font color="red">TA</font>ACA.. Can I describe this variant as NM_007294.3:c.[2077G>A;2077_2078insTA]?"

    The correct description of this variant is NM_007294.3:c.2077delinsATA.<br><b>NOTE:</b> the answer was modified, i.e. the addition "However, since the variant is likely a combination of two other variants it is acceptable to describe it as NM_007294.3:c.[2077G>A;2077_2078insTA]" was removed.
