## Community Consultation

### Proposal SVD-WG009 (conversion)

- Status: <code class="spot1">accepted</code>: proposal SVD-WG009 opened for **Community Consultation** on August 1 (2020), closed October 31 (2020).

Based on the proposal the HGVS nomenclature pages have been updated (November 2020); the specific conversion pages were removed, information was merged with the [Deletion-Insertion pages](../recommendations/DNA/delins.md).

The proposal suggested to simplify the HGVS nomenclature by **discontinuing the use of the variant type "con" to describe conversions**.

According to the HGVS definition a **conversion** is a sequence change where, compared to a reference sequence, a range of nucleotides are replaced by a sequence from elsewhere in the genome.

- the HGVS recommendations do not need the "con" format since such variants can be described using the existing "delins" format (simply replace "con" by "delins" in the description).
- the format is rarely used, so the change should not cause significant problems
- stopping the use will help to simplify the HGVS recommendations

#### Examples

- NC_000022.10:g.42522624_42522669delins42536337_42536382: previously NC_000022.10:g.42522624_42522669con42536337_42536382, a conversion in exon 9 of the CYP2D6 gene on chromosome 22 (NC_000022.10) replacing exon 9 nucleotides g.42522624 to g.42522669 with nucleotides g.42536337 to g.42536382 of the 3' flanking CYP2D7P1 gene

- NC_000012.12:g.6128479_6128749delins[NC\_000022.11:g.17178616\_17178886]: previously NC_000012.12:g.6128479_6128749con[NC\_000022.11:g.17178616\_17178886], a gene conversion in the VWF gene converting the chromosome 12 sequence (NC_000012.12) from position g.6128479 to g.6128749 with the sequence from chromosome 22 (NC_000022.11) from position g.17178616 to g.17178886.: **NOTE:** for inserted sequences derived from another reference sequence the prefix of the reference sequence type ("g." in the example) needs to be provided.
