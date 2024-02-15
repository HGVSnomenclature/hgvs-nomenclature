## Glossary

### In preparation

Please note that this Glossary is **work in progress**.
If you encounter missing terms or want to suggest definitions, please let us know.

- **3'rule**<br>
  for all descriptions, the most 3' position possible of the reference sequence is arbitrarily assigned to have been changed.
  When `ATT`<code class="del">T</code>`G` changes to `ATTG`, HGVS describes this as a change of the `T` at position 4 (not the `T` at position 2 or 3).

- **adjoined transcript**<br>
  a transcript (RNA molecule) composed of adjoined RNA from two or more contributing transcripts.

- **allele**<br>
  variant forms of the same gene ([MESH](http://www.ncbi.nlm.nih.gov/mesh?term=allele)).<br>
  **HGVS**: a series of variants on one chromosome.<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/alleles.md), [RNA](../recommendations/RNA/alleles.md), or [protein](../recommendations/protein/alleles.md).

- **amino acid**<br>
  a letter from the protein code (see [Standards](standards.md)).

- **cap site**<br>
  first nucleotide of a transcript (5' end) to which a specially altered nucleotide is added.

- **break point**<br>
  the site where two sequences, which are in different positions in the reference sequence, are joined as a consequence of genomic rearrangement (Structural Variant).

- **cDNA**<br>
  cDNA, "copy DNA" or "complementary DNA", is the DNA copy of a single stranded RNA molecule synthesized using the enzyme reverse transcriptase ([Wikipedia](https://en.wikipedia.org/wiki/Complementary_DNA), [MESH](https://www.ncbi.nlm.nih.gov/mesh/68018076)).<br>
  **NOTE**: cDNA is not the same as "coding DNA" (see below).

- **CDS**<br>
  Coding DNA Sequence, a sequence translated into an amino acid sequence (protein).

- **chimeric transcript**<br>
  an adjoined transcript derived from two or more genes.

- **chimerism**<br>
  the occurrence in one individual of two or more cell populations, derived from different zygotes, with different sequences (based on [MESH](http://www.ncbi.nlm.nih.gov/mesh?term=chimerism)).
  Opposite of _mosaicism_.<br>
  For descriptions, see [General/Characters used](../recommendations/general.md#characters).

- **cis**<br>
  two variants are **"in cis"** when they are on the same allele (DNA molecule, chromosome).

- **CNV**<br>
  Copy Number Variant (CNV), a variant in a genome where the number of copies of a large stretch of DNA differs from that in the reference genome; a copy can be missing (deleted) or be present more than once (duplicated, triplicated, ..., or amplified).<br>
  **NOTE**: a "large stretch" is not defined precisely but usually covers at least an exon of a gene or 1,000 nucleotides or more.<br>
  Alias: CNP (copy number polymorphism).

- **coding DNA**<br>
  the segments of a genome or segment of a transcript (RNA molecule) which encodes a protein.

- **coding DNA reference sequence**<br>
  a DNA reference sequence (see [Reference Sequence](refseq.md#DNAc)), based on a protein-coding transcript of a gene, which can be used for nucleotide numbering using the `c.` prefix.
  Such a reference sequence includes the coding DNA sequence (CDS) and the 5' and 3' UTR regions.<br>
  **NOTE**: a coding DNA reference sequence is **not** a cDNA sequence (see above).

- **complex**<br>
  **HGVS**: a sequence change where, compared to a reference sequence, a range of changes occur that can not be described as one of the basic variant types (substitution, deletion, duplication, insertion, inversion, deletion-insertion, or repeated sequence).

- **compound heterozygote**<br>
  used in cases of _autosomal recessive_ disease where the disease-causing variants on both alleles at a given locus are **not identical**.<br>
  Opposite of _homozygous_.

- **conversion**<br>
  **HGVS** (DNA, RNA): a sequence change where, compared to a reference sequence, a range of nucleotides are replaced by a sequence from elsewhere in the genome.<br>
  **NOTE**: conversion variants are described as deletion-insertions (see [DNA](../recommendations/DNA/delins.md) or [RNA](../recommendations/RNA/delins.md)).

- **Crick strand**<br>
  See _plus (+) strand_.

- **deletion**<br>
  **HGVS** (DNA, RNA, protein): a sequence change where, compared to a reference sequence, one or more nucleotides or amino acids are not present (deleted).<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/deletion.md), [RNA](../recommendations/RNA/deletion.md), or [protein](../recommendations/protein/deletion.md).

- **deletion-insertion (delins)**<br>
  **HGVS** (DNA, RNA, protein): a sequence change where, compared to a reference sequence, one or more nucleotides or amino acids are replaced by one or more other nucleotides, and which is not a substitution or inversion.<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/delins.md), [RNA](../recommendations/RNA/delins.md), or [protein](../recommendations/protein/delins.md).

- **der**<br>
  See _derivative chromosome_.

- **derivative chromosome**<br>
  a structurally rearranged chromosome carrying the intact centromere of the chromosome indicated (`der#`), generated by either more than one rearrangement within a single chromosome or a rearrangement involving two or more chromosomes.

- **duplication**<br>
  **HGVS** (DNA, RNA, protein): a sequence change where, compared to a reference sequence, a copy of one or more nucleotides or amino acids is inserted directly 3' of the original copy of that sequence.<br>
  **NOTE**: diagnostic assays (like MLPA) usually detect **an additional copy** of a specific sequence.
  Whether the additional copy is a duplication or an insertion remains to be determined.
  For descriptions, see Recommendations [DNA](../recommendations/DNA/duplication.md), [RNA](../recommendations/RNA/duplication.md), or [protein](../recommendations/protein/duplication.md).

- **exon**<br>
  any nucleotide sequence within a gene which, during maturation of the RNA transcript, is not removed by a process called RNA splicing ([Wikipedia](https://en.wikipedia.org/wiki/Exon), [MESH](https://www.ncbi.nlm.nih.gov/mesh/68005091)).
  Every exon, except the first and last exon, is flanked by two **introns**.

- **extension**<br>
  a sequence change extending the reference amino acid sequence at the N- or C-terminal end with one or more amino acids ([recommendations](../recommendations/protein/extension.md)).

- **frame (reading frame)**<br>
  **frame 1** is the normal reading frame, using the first nucleotide of each coding triplet of the annotated amino acid reference sequence for translation, starting at the `A` of the `ATG` translation initiation codon (nucleotide `c.1`).<br>
  **frame 2** is the reading frame using the second nucleotide of the annotated amino acid reference sequence as first nucleotide of a coding triplet for translation in the shifted reading frame.<br>
  **frame 3** is the reading frame using the third nucleotide of the annotated amino acid reference sequence as first nucleotide of a coding triplet for translation in the shifted reading frame.

- **frameshift**<br>
  a sequence change between the translation initiation (start) and termination (stop) codon where, compared to a reference sequence, translation shifts to another reading frame ([recommendations](../recommendations/protein/frameshift.md)).

- **fusion transcript**<br>
  a confusing term, HGVS nomenclature uses _adjoined transcript_ instead.

- **gene fusion**<br>
  the joining of two or more genes, resulting in a chimeric transcript and/or a novel interaction between a rearranged regulatory element with the expressed product of a partner gene (a regulatory fusion).

- **genomic rearrangement**<br>
  see _Structural Variant (SV)_.

- **haplotype**<br>
  a contiguous set of genetic variants that are co-located on one chromosome (molecule) and are inherited from the same parent.

- **hemizygous**<br>
  an individual having **only one allele** at a given locus, either because the allele is absent (X and Y chromosome in males) or lost (deleted) (based on [MESH](http://www.ncbi.nlm.nih.gov/mesh?term=hemizygous)).

- **heterozygous**<br>
  an individual in which both alleles at a given locus are **not identical** (based on [MESH](http://www.ncbi.nlm.nih.gov/mesh?term=heterozygous)).

- **homozygous**<br>
  an individual in which both alleles at a given locus are **identical** ([MESH](http://www.ncbi.nlm.nih.gov/mesh?term=homozygous)).

- **hypermorphic variant**<br>
  a variant characterized by a partial gain of gene activity (including an increase in protein production or function).

- **hypomorphic variant**<br>
  a variant characterized by a partial loss of gene activity (including a reduction in protein production or function).

- **indel**<br>
  **HGVS**: confusing term, not used.<br>
  **sometimes**: a sequence change where, compared to a reference sequence, one or more nucleotides or amino acids are replaced by one or more other nucleotides.<br>
  **sometimes**: a variant which is a deletion or an insertion.<br>
  **sometimes**: (evolutionary biology) a type of variant in which a specific nucleotide sequence is present (insertion) or absent (deletion).<br>
  [MESH](http://www.ncbi.nlm.nih.gov/mesh?term=indel): a length difference between two alleles where it is unknowable if the difference was originally caused by a sequence insertion or a sequence deletion.

- **insertion**<br>
  **HGVS** (DNA, RNA, protein): a sequence change where, compared to the reference sequence, one or more nucleotides or amino acids are inserted and where the insertion is not a copy of a sequence immediately upstream.<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/insertion.md), [RNA](../recommendations/RNA/insertion.md), or [protein](../recommendations/protein/insertion.md).

- **intron**<br>
  any nucleotide sequence within a gene which, during maturation of the RNA transcript, is removed by a process called RNA splicing ([Wikipedia](https://en.wikipedia.org/wiki/Intron), [MESH](https://www.ncbi.nlm.nih.gov/mesh/68007438)).
  Every intron is flanked by two **exons**.

- **inversion**<br>
  **HGVS** (DNA, RNA): a sequence change where, compared to a reference sequence, more than one nucleotide replacing the original sequence is the reverse complement of the original sequence.<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/inversion.md) or [RNA](../recommendations/RNA/inversion.md).

- **ISCN**<br>
  International System for Cytogenetic Nomenclature [(see ISCN)](../consultation/ISCN.md), covering the description of numerical and structural chromosomal changes detected using microscopic and cytogenetic techniques.<br>
  For descriptions, see Recommendations [DNA - Complex (HGVS<>ISCN)](../recommendations/DNA/complex.md).

- **Kozak sequence**<br>
  a consensus sequence, including the `ATG` translation initiation codon, playing a role in the initiation of translation.

- **LOH**<br>
  Loss Of Heterozygosity (LOH) is a term originally derived from the analysis of tumor samples where, as a consequence of a somatic change, a cell that had originally two different alleles **loses one allele**.
  The LOH can be caused by different molecular mechanism, including the deletion of the allele, a gene conversion or uniparental disomy.<br>
  **NOTE**: the definition given by [MESH](http://www.ncbi.nlm.nih.gov/mesh/?term=loss+of+heterozygosity), i.e. the loss of one allele at a specific locus caused by a deletion, is therefore not correct.<br>
  **NOTE**: the term LOH should thus **not** be used to indicate a **homozygous** region, i.e. a region where both chromosomes have the same sequence.

- **loss of heterozygosity**<br>
  see _LOH_.

- **minus (-) strand**<br>
  the bottom strand of the reference genome.
  Alias: _negative strand_, _Watson strand_.

- **missense**<br>
  **HGVS** (protein): a variant in a protein sequence, where compared to the reference sequence, one amino acid is replaced by another amino acid.<br>
  [MESH](https://www.ncbi.nlm.nih.gov/mesh/?term=missense): a variant in which a codon is changed to one directing the incorporation of a different amino acid.

- **mosaicism**<br>
  the occurrence in one individual of two or more cell populations, derived from a single zygote, with different sequences (based on [MESH](http://www.ncbi.nlm.nih.gov/mesh?term=mosaicism)).
  Opposite of _chimerism_.<br>
  For descriptions, see [General/Characters used](../recommendations/general.md#characters).

- **mutation**<br>
  **NOTE**: please do not use this term, see [Terminology](basics.md).
    - **HGVS**: confusing term, do not use, use **variant** (see [Basics](basics.md)).
    - **biology**: a change in the sequence.
    - **medicine**: a sequence variant **associated with a disease phenotype**.

- **negative (-) strand**<br>
  see _minus (-) strand_.

- **nonsense**<br>
  **HGVS** (protein): a variant in a protein sequence where, compared to the reference sequence, an amino acid is replaced by a translational stop codon (termination codon).<br>
  [MESH](https://www.ncbi.nlm.nih.gov/mesh/?term=nonsense): a variant that changed an amino acid-specifying codon to a stop codon (termination codon).

- **nucleotide**<br>
  a letter from the DNA code, e.g., `A`, `C`, `G`, or `T` (see [Standards](standards.md)) or the RNA code, e.g., `a`, `c`, `g`, or `u`.

- **plus (+) strand**<br>
  the top strand of the reference genome.
  Alias: _positive strand_, _Crick strand_.

- **polyA addition site**<br>
  the 3' end of a precursor messenger RNA (pre-mRNA) transcript that is cleaved and to which subsequently a tail of `A` nucleotides is added (the polyA-tail).

- **polyA signal**<br>
  a sequence in the 3' UTR of a transcript signalling the downstream cleavage and addition of a polyA tail.

- **polymorphism**<br>
  <a id="polymorphism"></a>
  **NOTE**: please do not use this term, see [Terminology](basics.md).
    - **HGVS**: confusing term, do not use, use **variant** (see [Basics](basics.md)).
    - **biology**: a sequence variant present in the population at a frequency of 1% or higher.
    - **medicine**: a sequence variant **not associated with a disease phenotype**.

- **positive (+) strand**<br>
  see _plus (+) strand_.

- **quadruplication**<br>
  a sequence change where, compared to a reference sequence, three copies of a sequence are inserted directly 3' of the original copy of that sequence (see Recommendations [DNA](../recommendations/DNA/duplication.md)).

- **quintuplication**<br>
  a sequence change where, compared to a reference sequence, four copies of a sequence are inserted directly 3' of the original copy of that sequence (see Recommendations [DNA](../recommendations/DNA/duplication.md)).

- **reading frame**<br>
  one of three possible ways to translate a nucleotide sequence into an amino acid sequence (a protein).<br>
  See also _frame_.

- **readthrough transcript**<br>
  a chimeric transcript in which the two (or more) genes involved can also be transcribed individually, and are found on the same chromosomal region, on the same strand, and typically adjacent to one another.

- **regulatory fusion**<br>
  the interaction of a gene expression regulatory element which, by a genomic rearrangement, is brought into proximity of a new partner gene, modulating the expression of the new partner gene.

- **repeated sequence**<br>
  **HGVS** (DNA, RNA, protein): a sequence where, compared to a reference sequence, a segment of one or more nucleotides or amino acids (the repeat unit) is present several times, one after the other.

- **silent**<br>
  **HGVS**: an amino acid in a protein sequence where, compared to the reference sequence, the DNA sequence changed but not the encoded amino acid.<br>
  [MESH](https://www.ncbi.nlm.nih.gov/mesh/?term=silent): a variant in a DNA sequence that does not change the amino acid sequence of the encoded protein.

- **SNP**<br>
  Single Nucleotide Polymorphism (SNP).
  The preferred term is _SNV_ (Single Nucleotide Variant), see [_polymorphism_](#polymorphism).

- **SNV**<br>
  Single Nucleotide Variant (SNV), a variant involving one nucleotide (e.g., `A>C`, `A>T`, `A>G`, `delA`, `dupA`, `insA`).

- **splice acceptor site (SA)**<br>
  the 3' splice site, at the end of the intron/start of the exon.

- **splice donor site (SD)**<br>
  the 5' splice site, at the end of the exon/start of the intron.

- **splice site**<br>
  the site in a precursor messenger RNA (pre-mRNA) transcript that is cleaved to remove the intron.

- **splicing**<br>
  the process removing specific segments (the _introns_) of a precursor messenger RNA (pre-mRNA) transcript.
  When an intron is removed, the flanking RNA segments (the _exons_) are joined together (ligated).

- **strand**<br>
  one of the two strands of a double-stranded DNA molecule.

- **Structural Variant (SV)**<br>
  a variant in a genome where compared to the reference sequence, the structure of a large stretch of DNA is changed.
  SVs include deletions/duplications (CNVs), inversions, insertions, deletion-insertions, transpositions, translocations, etc.<br>
  **NOTE**: a "large stretch" is not defined precisely, but usually covers at least an exon of a gene or 1,000 nucleotides or more.

- **substitution**<br>
  **HGVS** (DNA, RNA, protein): a sequence change where, compared to a reference sequence, one nucleotide or amino acid is replaced by one other nucleotide or amino acid.<br>
  For descriptions, see Recommendations [DNA](../recommendations/DNA/substitution.md), [RNA](../recommendations/RNA/substitution.md), or [protein](../recommendations/protein/substitution.md).

- **SV**<br>
  see _Structural Variant_.

- **trans**<br>
  two variants are **"in trans"** when they are on different alleles (DNA molecules, chromosomes).

- **transition**<br>
  a nucleotide variant changing a purine nucleotide to another purine nucleotide (`A` < > `G`), or a pyrimidine nucleotide to another pyrimidine nucleotide (`C` < > `T`).

- **translocation**
    - **HGVS** (DNA): a sequence change where, compared to a reference sequence, from a specific nucleotide position (the break point), all nucleotides upstream derive from another chromosome then those downstream.<br>
      **NOTE**: a translocation occurs when two chromosomes break and the fragments rejoin with the non-homologous chromosome.
      A full description of a (reciprocal) translocation consists of 2 parts, one describing the first junction, the second describing the other junction (e.g., the chromosome 4;X junction and the chromosome X;4 junction).
    - [MESH](https://www.ncbi.nlm.nih.gov/mesh/?term=translocation): a chromosome abnormality characterized by chromosome breakage and transfer of the broken-off portion to a non-homologous chromosome.
    - translocation, balanced: a translocation with an even exchange of DNA sequences and no segments deleted or duplicated.
    - translocation, unbalanced: a translocation with an uneven exchange of DNA sequences and segments being deleted or duplicated.

- **transposition**<br>
  a sequence change where, compared to a reference sequence, a large stretch of DNA moves from one position in the genome to another position, i.e. a deletion at one position combined with the insertion of the deleted sequence at another position.
  The variant is described as a deletion at the original location and an insertion at the new location.

- **transversion**<br>
  a nucleotide variant changing a purine nucleotide to a pyrimidine nucleotide (`A` or `G` > `T` or `C`), or a pyrimidine nucleotide to a purine nucleotide (`C` or `T` > `A` or `G`).

- **triplication**<br>
  a sequence change where, compared to a reference sequence, two copies of a sequence are inserted directly 3' of the original copy of that sequence (see Recommendations [DNA](../recommendations/DNA/duplication.md)).

- **trisomy**<br>
  the presence of a third chromosome of any one type in an otherwise diploid cell ([MESH](http://www.ncbi.nlm.nih.gov/mesh/?term=trisomy)).

- **UTR**<br>
  UnTranslated Region (UTR), the segments of a protein coding RNA molecule that is not translated.<br>
  5'UTR = UTR 5' of the tranlsation initiation codon (`ATG` start codon).<br>
  3'UTR = UTR 3' of the translation termination codon.

- **variant**<br>
  a difference between a reference sequence and an observed sequence.

- **VNTR**<br>
  Variable Number of Tandem Repeats, a nucleotide sequence consisting of units of a specific short sequence which is repeated in tandem copies and where the number of units is variable in the population.

- **Watson strand**<br>
  see _minus (-) strand_.
