# Uncertain

HGVS recommendations also contain suggestions to describe variants for which not all details are available.
Missing details may include unsequenced deletion/duplication breakpoints (e.g., detected using FISH, an array, a MLPA assay, Southern blotting, etc.), variants reported on the protein level only, or variants that likely affect RNA splicing but for which RNA was not analysed.
This page summarises how to describe variants when not all information is available.

### Characters used

- `( )` (parentheses) are used to indicate uncertainties.
    - in `g.(123456_234567)_(345678_456789)del`, indicating the uncertainty about the location of the deletion breakpoints, where (`123456_234567`) and (`345678_456789`) indicate the two regions where the break points should be located.
    - in `p.(Cys123Gly)`, indicating the amino acid change is predicted from DNA level data (no experimental proof).
- `?` (question mark) is used to indicate unknown positions (nucleotide or amino acid), like in `g.(?_234567)_(345678_?)del`.
- `^` (caret) is used as "or", like `p.(Gly719Ala^Ser)`.
- IUPAC codes: all IUPAC nucleotide codes can be used to describe uncertain nucleotides (see [Standards](../background/standards.md)).
    - `N[5]`, describes five unknown nucleotides.
    - `X[5]`, describes five unknown amino acid residues.

### Examples

<a id="uncertain1"></a>

#### DNA

- **position**<br>
  When a variant has been identified, but it can not be mapped to a unique location, possible descriptions should be given separated by a `^` (caret).
    - **`NM_000517.4:c.424C>T^NM_000558.3:c.424C>T`**<br>
      describes variant `c.427T>C`, which is either in the _HBA2_ (`NM_000517.4`) or the _HBA1_ (`NM_000558.3`) gene.

    - **`NC_000023.10:g.(33038277_33038278)C>T` (`LRG_199t1:c.(71_72)G>A`)**
      describes the variant `p.Trp24Ter` in the _DMD_ gene, reported on protein level only.

- **deletion**<br>
  The standard format to describe a deletion for which the break points have not been sequenced is `(A_B)_(C_D)del`, where `B_C` describes the **minimal** extent and `A_D` the **maximal** extent of the deletion.
    - **PCR**<br>
      In PCR, a pair of oligonucleotides (the primers) is used to detect the presence (through amplification) of a specific sequence (target).
      Amplification will fail when one or both primers do not hybridise to the target sequence, either because the target sequence is absent (deleted), or because there are differences between the sequence of the target and the primer.
        - **size**<br>
          when a fragment is amplified, but only its size was used to detect a variant (and not its sequence), the variant should be reported as `g.(fragment-start_fragment-end)delN[#]`.
          In this description, `fragment-start` is the first nucleotide of the amplified fragment (i.e. after the last nucleotide of the forward primer), `fragment-end` is the last nucleotide of the amplified fragment (i.e. before the first nucleotide of the reverse primer), `del` indicates the fragment decreased in size, and `N[#]` indicates the difference in size (or estimated size) in nucleotides compared to the fragment in the reference sequence.
            - **`NC_000003.12:g.(63912602_63912844)delN[15]` or `NM_000333.3:c.(4_246)delN[15]`**<br>
              compared to the reference, the amplified fragment is 15 nucleotides shorter.
              Format based on [Repeated sequences](DNA/repeated.md).

        - **present/absent**<br>
          when a deletion was detected based on the presence/absence of a specific amplification product (PCR), it is described using the format `(last-normal-position_first-absent-position)_(last-absent-position_first-normal-position)`.
          In this description, `last-normal-position` is the last nucleotide of the amplified fragment still present 5' of the deletion, `first-absent-position` is the first nucleotide of the missing fragment, `last-absent-position` is the last nucleotide of the missing fragment, and `first-normal-position` is the first nucleotide of the amplified fragment still present 3' of the deletion.<br>
          **NOTE**: an amplified fragment runs from the first nucleotide after the forward primer to the first nucleotide before the reverse primer.<br>
          **NOTE**: amplification already fails when the binding site of one primer is absent, therefore last/first nucleotides of the amplified fragment are used to describe the deletion.
            - **`NC_000023.11:g.(31729716_31774235)_(32216847_32287541)del` (`LRG_199t1:c.(6278_6438+69)_(7310-43_7575)del`)**
              a deletion of exons 44 to 51 in the _DMD_ gene as detected by a multiplex PCR assay.
              The variant is described based on the last amplified nucleotide of exon 43 (`g.32287541` / `c.6278`), the last failed amplified nucleotide of exon 44 (`g.32216847` / `c.6438+69`), the first failed amplified nucleotide of exon 51 (`g.31774235` / `c.7310-43`), and the first amplified nucleotide of exon 52 (`g.31729716` / `c.7575`).

    - **MLPA**<br>
      An MLPA assay is used to detect Copy Number Variants (CNVs), the number of copies of a sequence present in a sample.
      In MLPA, a pair of oligonucleotide probes is used to determine the copy number of a specific sequence (mostly an exon).
      In the first step of a MLPA assay, two flanking oligonucleotide probes hybridising to a target sequence are fused by ligation.
      In the second step, the ligated oligonucleotides are amplified in a quantitative PCR assay.
      When the signal of a probe is absent, it indicates the pair of oligonucleotide sequences could not be ligated.
      Ligation will fail when one or both oligonucleotides did not hybridise to the target sequence, either because the target sequence is absent (deleted) or because there are differences between the sequence of the target and the oligonucleotide probes.<br>
      **NOTE**: in samples containing 2 alleles, a decreased signal usually indicates the absence (deletion) of one copy of the sequence tested.
        - **amount**<br>
          the description of the variant detected uses the basic format `(last-normal-position_first-altered-position)_(last-altered-position_first-normal-position)`.
          For MLPA, the probe position is the ligation site, i.e. the first nucleotide of the probe 3' of the ligation site.
          For MLPA probes containing two ligation sites, the probe position is the central nucleotide between the two ligation sites (when two nucleotides form the center the 3' rule applies and the 3'nucleotide is selected).<br>
          **Example**: for exon 24 of the _DMD_ gene (`NM_004006.2`), the ligation site is `..ATGGCCTGCCC`<code class="spot1">TT</code>`GGGGATTCAGA..`, i.e. the T nucleotides `c.3233` and `c.3234`.
          Since the _DMD_ gene is on the - strand, nucleotide `NM_004006.2:c.3233` is therefore used as the probe position in variant descriptions.<br>
          **NOTE**: in diagnostics, it is common practice to describe MLPA results using a so-called exon-based description.
          In this description, when a probe is affected, it is assumed the entire exon is affected and the description is based on the location of the exon/intron borders (except for large exons measured using several MLPA probes).<br>
          **NOTE**: the "Reading frame checker" offered through the gene home pages of the "[Global Variome shared LOVD](https://databases.lovd.nl/shared/)" might be a useful tool to generate exon-based descriptions (e.g., for the [DMD gene](https://databases.lovd.nl/shared/scripts/readingFrameChecker.php?gene=DMD&transcript=NM_004006.2).
            - **`NC_000023.11:g.(31729663_31774080)_(32216973_32287624)del` (`LRG_199t1:c.(6195_6381)_(7422_7628)del`)**<br>
              a deletion of exons 44 to 51 in the _DMD_ gene as detected by an MLPA assay.
              The deletion is described based on the last normal signal (exon 43 position `g.32287624` / `c.6195`), the first absent signal (exon 44 position `g.32216973` / `c.6381`), the last absent signal (exon 51 position `g.31774080` / `c.7422`), and the first normal signal (exon 52 position `g.31729663` / `c.7628`).

    - **array (CGH or SNP)**<br>
      An array can be used to detect Copy Number Variants (CNVs), the number of copies of a sequence present in a sample.
      In array technology, hybridisation to arrayed probe sequences is used to determine presence or absence of these sequences (target) in samples analysed.
      Hybridisation will fail when the target sequence is absent (deleted) or because there are differences between the sequence of the target and the probe.<br>
      **NOTE**: in samples containing 2 alleles, a decreased signal usually indicates the absence (deletion) of one allele.
        - **present/absent**<br>
          the description of the variant detected uses the basic format `(last-normal-position_first-altered-position)_(last-altered-position_first-normal-position)`.
          In this description, the probe position is based on the position of the nucleotide tested (SNP array) or the center of the arrayed probe (CGH array).
          Similarly, alternative descriptions have been suggested by the [ISCN guidelines](http://www.karger.com/Article/FullText/353118).
          Note also that more examples can be found under [Complex (HGVS/ISCN)](DNA/complex.md), including array-characterised translocations.
            - **`NC_000023.10:g.(32218983_32238146)_(32984039_33252615)del`**<br>
              a deletion on the X chromosome, based on reference genome build hg19 (reference sequence `NC_000023.10`), starting between nucleotides 32,218,983 to 32,238,146 and ending between nucleotides 32,984,039 to 33,252,615.

            - **`NC_000023.10:g.(?_32238146)_(32984039_?)del`**<br>
              a deletion on the X chromosome, based on reference genome build hg19, starting upstream of nucleotide 32,238,146 and ending downstream of nucleotide 32,984,039.<br>
              **NOTE**: from the description indicated, it is unclear how far the deletion extends, suggesting no up- or downstream probes were tested (and scored positively).

            - **`NC_000013.11:g.(19385993_19394916)_(25045592_25059364)del`**<br>
              a deletion on chromosome 13, based on reference genome build hg38, detected using a SNP-array.
              The deletion spans from dbSNP entries rs3929856 (`g.19394916`) to rs10507342 (`g.25045592`), both yielding a 50% reduced signal.
              On the centromeric side (q-arm), the closest probe tested normal was rs2342234 (`g.19385993`); on the telomeric side the closest probe tested normal was rs947283 (`g.25059364`).

            - **`NC_000013.11:g.(?_19394916)_(25045592_?)del`**<br>
              a deletion on chromosome 13, based on reference genome build hg38, detected using a SNP-array.
              The deletion spans from rs3929856 (`g.19394916`) to rs10507342 (`g.25045592`).
              The description indicates no flanking probes were tested normal, making it unclear how far the deletion extends.

    - **FISH**<br>
      In Fluorescent In-Situ Hybridisation (FISH) presence or absence of sequences is analysed by microscopic visualisation of a fluorescently labeled probe hybridising to a target sequence.
      Hybridisation will fail when the target sequence is absent (deleted) or will be weak when only part of the target sequence is present.<br>
      **NOTE**: in samples containing 2 alleles, both alleles can be visualised independently.
        - rearrangements detected using FISH (Fluorescence In Situ Hybridisation) can be described using [ISCN guidelines](http://www.karger.com/ISCN2016).
          When probe positions are known, variants can be described using genomic coordinates.
          The basic format is `(last-normal-probe_first-variant-probe)_(last-variant-probe_first-normal-probe)` (see [also ISCN<>HGVS](../consultation/SVD-WG004.md)).
          In this description, the probe position is based on the center of the labelled probe used during hybridisation.
            - **`NC_000023.10:g.(32057077_32364657)_(32975163_33394206)del`**<br>
              a deletion on the X-chromosome detected using FISH.
              The deletion, based on reference genome build hg19, spans from PAC probes RP4-556A22 (central position `g.32364657`) to RP11-151J4 (central position `g.32975163`), both yielding no signal.
              On the telomeric side (p-arm), the closest probe tested positive was PAC RP11-509C1 (`g.32057077`), on the centromeric side the closest probe tested positive was RP6-60B16 (`g.33394206`).

            - **`NC_000023.10:g.(?_32364657)_(32975163_?)del`**<br>
              a deletion on the X-chromosome detected using FISH.
              The deletion, based on reference genome build hg19, spans from PAC probes RP4-556A22 (central position `g.32364657`) to RP11-151J4 (central position `g.32975163`), both yielding no signal.
              No flanking positive probes were tested, making it unclear how far the deletion extends.

            - **`NC_000023.10:g.(32057077_32364657)_(32894352_33055973)del`**<br>
              a deletion on the X-chromosome detected using FISH.
              The deletion, based on reference genome build hg19, spans from PAC probe RP4-556A22 (central position `g.32364657`) to within RP11-151J4 (`g.32894352_33055973`), as indicated by the reduced signal.
              On the telomeric side (p-arm), the closest probe tested positive was PAC RP11-509C1 (`g.32057077`).

    - **Southern blotting**<br>
      In Southern blotting, presence or absence of sequences is analysed by hybridisation of a labeled probe sequence to paper-blotted DNA fragments separated by size using gel-electrophoresis after fragmentation by restriction enzyme digestion.
      Hybridisation will fail when the target sequence is absent (deleted) or will be weak when only part of the target sequence is present.
      Sometimes, details on the size of a deletion can be derived from the length of the hybridising fragment.<br>
      **NOTE**: in samples containing 2 alleles, a decreased signal usually indicates the absence (deletion) of one allele.
        - **present/absent**<br>
          the description of the variant detected uses the basic format `(last-normal-probe_first-altered-probe)_(last-altered-probe_first-normal-probe)`.
          In this description, the probe position is based on the center of the labelled probe used during hybridisation and/or the position of the restriction enzyme recognition sites of the DNA fragment.
            - **`NC_000023.11:g.(31775822_31819974)_(32217064_32278336)del` (`LRG_199t1:c.(6290+9193_6291-1)_(7309+1_7310-1630)del`)**<br>
              a deletion of exons 44 to 51 in the _DMD_ gene as detected by a HindIII digestion, Southern blotting and cDNA hybridisation.
              The variant is described based on the normal intensity of the hybridizing exon 43 fragment (`g.32278336_32289141del` / `c.6118-1440_6290+9193`), the absence of the hybridizing exon 44 fragment (`g.32214437_32218461` / `c.6291-1398_6438+2479`), the absence of the hybridizing exon 51 fragment (`g.31817965_31821709` / `c.7201-1626_7309+2010`), and the normal intensity of the hybridizing exon 52 fragment (`g.31772670_31775822` / `c.7310-1630_7542+1290`) relative to the coding DNA reference sequence.<br>
              **NOTE**: the deletion is assumed to involve the entire exon.

- **insertion**<br>
  The format to describe insertions that have not been fully characterised (sequenced) depends on the method used.
  The same recommendations apply as described above for deletions.
    - **size**<br>
      when a fragment containing an insertion has been amplified but only its size was determined (and not its sequence), the variant should be reported as `g.(fragment-start_fragment-end)insN[#]`.
        - **`NC_000003.12:g.(63912602_63912844)insN[15]` or `NM_000333.3:c.(4_246)insN[15]`**<br>
          compared to the reference, the amplified fragment is 15 nucleotides longer, giving an estimated 13-unit `CAG` / `Gln` repeat in the _ATXN7_ gene.

        - **`NC_000003.12:g.(63912602_63912844)insN[(150_180)]` or `NM_000333.3:c.(4_246)insN[(150_180)]`**<br>
          compared to the reference, the amplified fragment is 150 to 180 nucleotides larger.

    - **present/absent**<br>
      the format to describe insertions that have not been fully characterised, i.e. the inserted sequence and/or the insertion break point has not been sequenced, is `g.(left-ins-position_right-ins-position)ins(last-normal_first-inserted)_(last-inserted_first-normal)`.<br>
      **NOTE**: the description of the insertion, `ins(last-normal_first-inserted)_(last-inserted_first-normal)`, is based on the uncertainty of the extent of the inserted sequence.
      To describe the inserted sequence, follow the standard recommendations, i.e. try to describe it as precise as possible.
        - **`NC_000002.11:g.47643464_47643465ins[NC_000022.10:g.35788169_35788352]`**<br>
          the insertion on chromosome 2, between nucleotides `g.47643464` and `g.47643465` (in the _MSH2_ gene), of sequences from chromosome 22, nucleotides `g.35788169` to `g.35788352` (of the _HMOX1_ gene).

        - **`NC_000002.11:g.?_?ins[NC_000022.10:g.35788169_35788352]`**<br>
          the insertion of sequences from chromosome 22, nucleotides `g.35788169` to `g.35788352` (of the _HMOX1_ gene) at an unknown position in chromosome 2.

- **duplication**<br>
  The standard format to describe a duplication for which the break point has not been sequenced is `(A_B)_(C_D)dup`, where `B_C` describes the **minimal** extent and `A_D` the **maximal** extent of the duplication, i.e. `g.(last-normal_first-duplicated)_(last-duplicated_first-normal)dup`.<br>
  **NOTE**: many assays detect the presence of an **additional copy** of specific sequences, not the location of the extra copy.
  When there is **no evidence** the additional copy is **in tandem** with the original copy but might be anywhere in a genome, the variant should be described as an **insertion** (see above).
    - *PCR*
        - **`NC_000023.11:g.(31729716_31773911)_(32217064_32287541)dup` (`LRG_199t61:c.(6278_6291-1)_(7542+49_7575)dup`)**<br>
          a duplication of exons 44 to 51 in the _DMD_ gene as detected by a multiplex PCR assay.
          The variant is described based on the last amplified nucleotide of exon 43 (`g.32287541` / `c.6278`), the first duplicate amplified nucleotide of exon 44 (`g.32216847` / `c.6291-1`), the last duplicate amplified nucleotide of exon 51 (`g.31774235` / `c.7542+49`), and the first amplified nucleotide of exon 52 (`g.31729716` / `c.7575`).

    - *MLPA*
        - **`NC_000023.11:g.(31729662_31774079)_(32216972_32287623)dup` (`LRG_199t1:c.(6196_6382)_(7423_7629)dup`)**<br>
          a duplication of exons 44 to 51 in the _DMD_ gene as detected by an MLPA assay.
          The duplication is described based on the last normal signal (exon 43 position `g.32287623` / `c.6196`), the first duplicated signal (exon 44 position `g.32216972` / `c.6382`), the last duplicated signal (exon 51 position `g.31774079` / `c.7423`), and the first normal signal (exon 52 position `g.31729662` / `c.7629)`.<br>
          **NOTE**: in samples containing 2 alleles, an increased signal indicates the presence of an **extra copy** of the sequence tested.
          The result has no information regarding the **location** of the extra copy, it can be anywhere in the genome!

    - **Southern blotting**
        - **`NC_000023.11:g.(31775822_31817965)_(32218461_32278336)dup` (`LRG_199t1:c.(6290+9193_6291-1398)_(7309+2010_7310-1630)dup`)**<br>
          a duplication of exons 44 to 51 in the _DMD_ gene as detected by a HindIII digestion, Southern blotting and cDNA hybridisation.
          The variant is described based on the normal intensity of the hybridizing exon 43 fragment (`g.32278336_32289141` / `c.6118-1440_6290+9193`), the double intensity of the hybridizing exon 44 fragment (`g.32214437_32218461` / `c.6291-1398_6438+2479`), the double intensity of the hybridizing exon 51 fragment (`g.31817965_31821709` / `c.7201-1626_7309+2010`), and the normal intensity of the hybridizing exon 52 fragment (`g.31772670_31775822` / `c.7310-1630_7542+1290`) relative to the coding DNA reference sequence.

#### RNA

- **`r.?`**<br>
  used to indicate that an effect on the RNA level is expected, but that it is not possible to give a reliable prediction of the consequences.

- **`r.0?`**<br>
  used to indicate that possibly, no transcript is generated.

- **`r.(=)`**<br>
  used to indicate that no changes on the RNA level are expected (RNA not analysed).

- **`r.spl`**<br>
  used to indicate that it is **very likely** that splicing is affected (RNA not analysed).
  The format is used for variants changing the +1, +2, -2 and -1 position of an intron, i.e. affecting the `GT` splice donor and `AG` splice acceptor site (excluding `GT` to `GC` and `GC` to `GT` variants).

- **`r.spl?`**<br>
  frequently used to indicate that normal splicing **might** be affected (RNA not analysed).
  The format is used for variants in the first or last nucleotide of an exon, the +3 to +5 intron position (splice donor site), and variants generating a new `AG`-dinucleotide close to the normal splice acceptor site (`AG`).

- **`r.(76a>c)`**<br>
  used to indicate that RNA was not analysed, but the variant `r.(306g>u)` is expected to be detected.

- **`r.(?)`**<br>
  frequently used to indicate that RNA was not analysed but that no changes on the RNA level are expected other than those simply derived from the change on the DNA level.

#### Protein

- **`p.?`**<br>
  used to indicate that an effect on the protein level is expected, but that it is not possible to give a reliable prediction of the consequences.

- **`p.0?`**<br>
  used to indicate that possibly, no protein is generated.

- **`p.(=)`**<br>
  used to indicate that no changes on the protein level are expected (RNA not analysed).

- **`p.(Ala123_Pro131)Ter`**<br>
  used to describe that at an unknown position between amino acids `Ala123` and `Pro131`, an amino acid is substituted for a translation termination (stop) codon.

- **`p.(Ala123_Pro131)fs`**<br>
  used to describe there is a frameshift variant starting at an unknown position between amino acids `Ala123` and `Pro131`.

- **`p.(Ala123_Pro131)insX[4]`**<br>
  used to describe there is an insertion of four unknown amino acids (`X`) at an unknown position between amino acids `Ala123` and `Pro131`.<br>
  **NOTE**: `X` is the IUPAC symbol for an unnown amino acid, **NOT** to indicate a translation termination (stop) codon.

- **`p.Gly719(Ala^Ser)fsTer23`**<br>
  used to describe there is a frameshift variant starting in the codon for amino acid `Gly719`, changing it to either `Ala` or `Ser` and ending at a termination codon at position 23 (`fsTer23`).

- **`p.(Gly23GlufsTer7^Gly23CysfsTer26)`**<br>
  used to describe there is a predicted frameshift variant starting in the codon for amino acid `Gly23` giving either `p.(Gly23GlufsTer7)` or `p.(Gly23CysfsTer26)`.
