**NOTE:** We have updated our glossary and nomenclature to align with the [VICC Gene Fusion Specification](https://fusions.cancervariants.org/en/latest) terminology, and clarify the distinction between chimeric transcript fusions (the biological concept) and adjoined transcripts (a nomenclature structure). The "fusion transcript" concept adopted in this consultation was relabeled to "adjoined transcript" accordingly.

## Community Consultation

### Proposal SVD-WG007 (RNA fusion)

- Status: <code class="spot1">accepted</code>: proposal SVD-WG007 opened for **Community Consultation** on April 10 (2019), and closed June 30 (2019).

Based on the proposal the [RNA Deletion-insertion page](../recommendations/RNA/delins.md) has been updated (April 2020).

The proposal suggests to extend the HGVS recommendations with a format to describe adjoined transcripts derived from gene fusions

- Adjoined transcripts are described following the format to describe a gene fusion between two DNA molecules (translocations), i.e. using **"::"**.

#### Examples

- translocation-derived adjoined transcript: NM_152263.2:r.-115_775::NM_002609.3:r.1580\_\*1924: an adjoined transcript from a TPM3::PDGFRB gene fusion, where nucleotides r.-115 to r.775 (reference transcript NM_152263.2, TPM3 gene) are coupled to nucleotides r.1580 to r.\*1924 (reference transcript NM_002609.3, PDGFRB gene)
- deletion-derived adjoined transcript: NM_002354.2:r.-358_555::NM_000251.2:r.212\_\*279: an adjoined transcript from an EPCAM::MSH2 gene fusion, where nucleotides r.-358 to r.555 (reference transcript NM_002354.2, EPCAM gene) are coupled to nucleotides r.212 to r.\*279 (reference transcript NM_000251.2, MSH2 gene)
- NOTES
    - ::aggcucccuugg::: a format like "**::aggcucccuugg::**" is used to indicate the insertion of a 12 nucleotide sequence (aggcucccuugg) between two adjoined transcripts
    - NM_152263.2:r.?\_775::NM_002609.3:r.1580\_?: when only the sequence adjacency and not the entire transcript has been analysed, the format NM_152263.2:r.?\_775::NM_002609.3:r.1580\_? should be used

#### NOTE

All adjoined transcripts are described using the same format irrespective of whether they derive from inter-chromosomal or intra-chromosomal DNA rearrangements (translocation, deletion, inversion) or other mechanisms (trans-splicing).
