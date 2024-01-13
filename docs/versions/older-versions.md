- **Version 20.05**: Accepted proposals include [SVD-WG007](../consultation/SVD-WG007.md) and [SVD-WG008](../consultation/SVD-WG008.md):

    - SVD-WG008 (_Reference Sequences_): specifies requirements for acceptable Reference Sequences
    - SVD-WG007 (_RNA fusion_): specifies how to describe adjoined transcripts from gene fusions

- **Version 19.01**: Accepted proposals include [SVD-WG005](../consultation/SVD-WG005.md) and [SVD-WG006](../consultation/SVD-WG006.md):

    - SVD-WG006 (_circular DNA_): allows descriptions like o.16000_100del
    - SVD-WG005 (_gom/lom_): allows descriptions of changes in general methylation status like g.123_456|lom
    - <a id="SVD-WG004"></a> **Named extension ISCN**: Proposal [SVD-WG004](../consultation/SVD-WG004.md) (ISCN<>HGVS) has been accepted a "named extension ISCN"

- **Version 15.11**: Accepted proposals include [SVD-WG001](../consultation/SVD-WG001.md) and [SVD-WG002](../consultation/SVD-WG002.md):

    - SVD-WG001 (_No change_): allows descriptions like g.11890634G=, c.123G=, r.123g= and p.(Arg41=).
    - SVD-WG002 (_n. reference sequence_): allows descriptions like NR_028379.1:n.345A>G. : HGVS nomenclature **version 15.11** is described in Den Dunnen et al. (2016) [HGVS recommendations for the description of sequence variants: 2016 update. Hum.Mutat. 25: 37: 564-569](http://onlinelibrary.wiley.com/doi/10.1002/humu.22981/pdf). The most significant changes between version 15.11 and version 1.0 are [described below](#v1511).

- **Version 2.121101**: **Variants affecting translation termination** - variants that replace the translation termination codon but do not encounter a new stop in the new reading frame are described as "p._321Argext_?". Frameshift variants with the same effect are described as `p.Ile321Argfs*`? (see [Protein descriptions](../recommendations/protein/extension.md))

- **Version 2.120831**: **Protein description in parentheses** - parentheses in protein variant descriptions can be omitted when there is sufficient experimental evidence: **Variants affecting translation initiation** - at protein level, variants that generate a new upstream translation initiation codons are described using the format "p.Met1ext-5" (see [Protein extensions](../recommendations/protein/extension.md)).

- **Version 1**: The 2000 publication of Den Dunnen JT and Antonarakis SE [Mutation nomenclature extensions and suggestions to describe complex mutations: a discussion. Hum.Mutat. 15:7-12](http://www3.interscience.wiley.com/cgi-bin/fulltext/68503056/PDFSTART)) contain a more formal set of recommendations an are considered as version 1.

- **Version 0**: On the page "[History regarding the description of sequence variants](../background/history.md)" we give an overview of all publications on the description of sequence variants. These papers can be considered as pre-versions of the first recommendations, a version 0.

<a id="v1511"></a>

### Changes/additions going from the 2000 to 2016 recommendations

- **Reference sequence**: for diagnostic applications, the recommendation is to use a [Locus Reference Genomic sequence](http://www.lrg-sequence.org/) (LRG, [Dalgleish et al. 2010](http://genomemedicine.com/content/2/4/24)) as the reference sequence for variant descriptions. Prefixes for new reference sequence types have been added (e.g. **m.** and **n.**, as well as indicators to specify different transcript variants (**t1**) and protein isoforms (**p1**) annotated in the reference sequence (see [Reference Sequences](../background/refseq.md#DNAc))
- **Definitions**: the basic types of variants were defined more strictly. In addition variant types have been prioritized (see [General recommendations](../recommendations/general.md))
- **Pre-existing standards**: pre-existing standards from the IUPAC and IUBMB for the description of nucleotides and amino acids are now used throughout the recommendations. These include letter codes to describe incompletely specified residues at both DNA and protein level (see [Standards](../background/standards.md#aacode)). Description of the translation termination (stop) codon at the protein/amino acid level **changed from "X" to "Ter" / "*"** since "X" in the _IUPAC-IUB_ nomenclature means an "_unspecified_" or "_unknown_" amino acid.
- **Incorporate ISCN standards**: recommendations were made to describe changes with uncertain break points (i.e. not sequenced), obtained using technologies like FISH, arrays and MLPA. Furthermore, where possible, HGVS incorporated established ISCN standards in the recommendations, include the use of `/` (forward slash) to describe somatic variants and `//` for chimerism (see [General recommendations](../recommendations/general.md)).
- **Simplification**: in HGVS version 1.0 some symbols were used for more than one purpose leading to undesired confusion. These inconsistencies were removed.
- **Prediction / experimental proof**: to clarify a variant described at the protein level is a prediction, without experimental evidence, the recommendation was added to describe the predicted consequence in parentheses, like p.(Arg12Gly).
- **Repeated sequences**: recommendations were made to describe variability in repeated sequences (mono-, di-, tri- residue stretches, etc. see [Repeated sequences](../recommendations/DNA/repeated.md)).
