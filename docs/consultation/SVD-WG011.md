## Community Consultation

### Proposal SVD-WG011 (RNA insertions)

**Status: open**

    proposal SVD-WG011 opened for Community Consultation on xxxx, xxx, closing on xxx, xxx.

The proposal suggests to specify the HGVS nomenclature recommendations for the description of variants on the RNA level, more specifically the insertion of intron sequences.


**Background**

As the r. prefix refers to mature (coding/non-coding) RNA molecules, descriptions using the r. prefix can not refer to intronic nucleotide positions. Therefore, variant descriptions like NC_000023.10(NM_004006.3):r.5448_5449ins5448+1_5448+66 are actually invalid.

**Proposal**

- the proposal applies to variant description on the RNA level.
- HGVS nomenclature requires that inserted sequences derived from intron sequences using a coding/non-coding DNA reference sequence (NM_ or NR_) are described using the format **"ins[c.5448+1_5448+66]"**, i.e. referencing the coding/non-coding DNA reference sequence and using the **"c./n."** prefix.

**NOTE:** officially the insertion should be described using the format "ins[NC_000023.11(NM_004006.3):c.5448+1_5448+66]", however, since the description at the DNA level already includes the reference sequences used (NC_000023.11 and NM_004006.3) specifying them again would mean the unnecessary use of redundant information.


#### Examples

- **`r.5448_5449ins[c.5448+1_5448+66]`**<br>
on RNA level, variant NM_004006.3:c.5448+67A>G gives the insertion of intronic nucleotides **c.5448+1 to c.5448+66** between nucleotides r.5448 and 5449.<br>
**NOTE:** since HGVS nomenclature demands that variants must be described on DNA level, a full description of the variant is like NC_000023.11:g.32348339T>C NM_004006.3:c.5448+67A>G r.5448_5449ins[c.5448+1_5448+66]

- **`r.1704_1705ins[GA;c.1704+3_1704+11]`**<br>
on RNA level, variant NM_004006.3:c.1704+2T>A gives the insertion of nucleotides **"GA"** and **"c.1704+3 to c.1704+11"** between nucleotides r.1704 and r.1705.<br>
**NOTE:** since HGVS nomenclature demands that variants must be described on DNA level, a full description of the variant is like NC_000023.11:g.32573743A>T NM_004006.3:c.1704+2T>A r.5448_5449ins[c.5448+1_5448+66]<br>
**NOTE:** since nucleotide c.1704+2 changes from T to A the insertion **can not** be described as r.1704_1705ins[c.1704+1_1704+11]

- **`r.94_264delins[NC_000008.10:g.16369356_16369419inv]`**<br>
on RNA level, a DNA variant gives the deletion of nucleotides **r.94 to r.264**, being replaced with the insertion, in an inverted orientation, of nucleotides **NC_000008.11:g.16511847to g.165119109** from chromosome 8.<br>
**NOTE:** since HGVS nomenclature demands that variants must be described on DNA level, a full description of the variant is like NC_000023.11:g.32854892_32854897delins[CCA;NC_000008.11:g.16489201_16564934] NM_004006.3:c.94-5077_94-5072delins[NC_000008.10:g.16346710_16422443inv;TGG]  	r.94_264delins[NC_000008.11:g.16511847_16511910inv]
