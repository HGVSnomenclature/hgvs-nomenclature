## Community Consultation

### Proposal SVD-WG003 (exon del/dup)

!!! warning "Status: new proposal to be made"

    proposal SVD-WG003 was opened for Community Consultation on May 14, 2015, closing on July 16, 2015.
    Since several objections were received as well as proposals to use another format, the SVD-WG decided on October 6, 2015 **not yet to accept** the proposal and prepare a new proposal.
    It should be noted, however, that the format <code class="invalid">c.650-?_1331+?del</code> conflicts with basic HGVS recommendations and **should not be used**.
    The proposed format, `c.(649+1_650-1)_(1331+1_1332-1)del`, does follow current recommendations.

The [proposal](http://www.hgvs.org/mutnomen/comments003.html) suggested to describe deletions (duplications) detected by MLPA tests (testing all exons) using the format `c.(649+1_650-1)_(1331+1_1332-1)del`.

The format suggested originally to describe deletions/duplications detected by MLPA tests (testing all exons), was `c.650-?_1331+?del`, i.e. a deletion starting in the intron preceding `c.650` (first nucleotide of the first deleted exon) and ending in the intron after `c.1331` (last nucleotide of the last deleted exon).
However, this format **is in conflict with** the basic recommendation that in such cases, the description should make clear what the region of uncertainty for the break point is (see [Uncertain](../recommendations/uncertain.md)), i.e. `(last-normal-position_first-altered-position)_(last-altered-position_first-normal-position)`.
The Committee considered the format `c.(649_650)_(1331_1332)del`, which is shorter, but not specifically indicates that the expected break points of the change are in an intron.

#### Examples

- **`c.(649+1_650-1)_(1331+1_1332-1)del`**<br>
  a deletion of exons 8 to 11 (_DMD_ gene) with breakpoints in the introns between nucleotides `c.649` and `c.650` (intron 7) on one side, and nucleotides `c.1331` and `c.1332` (intron 11) on the other side.
  The flanking exons (7 and 12) on either side were tested and found not deleted.<br>
  **NOTE**: `c.(649+1_650-1)_(1331+1_1332-1)dup` describes a duplication of the same region.

- **`c.(516+1_517-1)_(1970_6774)del`**<br>
  a deletion in the _BRCA2_ gene with one break point in the intron between nucleotides `c.516` and `c.517` (intron 6), and one breakpoint in exon 10 between nucleotides `c.1970` and `c.6774`.
  Flanking exons (5 and 11) on each side were tested and found not deleted.
  Description of the break point in exon 10 was derived from the two MLPA probes tested, taken the central nucleotide position per probe.<br>
  **NOTE**: `c.(516+1_517-1)_(1970_6774)dup` describes a duplication of the same region.

### Note

To be **100% accurate**, one should theoretically not use the position of the introns in the description of the change, but the location of the probes used in the assay (see [Uncertain](../recommendations/uncertain.md)).
When one wants to use probe locations (e.g., with breakpoints in large exons), the suggestion is to use the **central position** of the probes in variant descriptions.
Proposal SVD-WG003 bears in mind that:

- it is not straightforward what probe position to use,
- the additional detail would hardly add useful information,
- we should preferably not deviate too far from the original proposal (i.e. to use flanking intron locations).

**NOTE**: the description "dup" may, by definition (see [Duplication](../recommendations/DNA/duplication.md)), only be used when the additional copy is located directly 3'-flanking the original copy (a tandem duplication).
In most cases, there will be no experimental proof; the method used only detects the presence of an additional copy that, in theory, can be inserted anywhere in the genome.
Discussions are ongoing how to include this uncertainty best in the description: a proposal will follow later.
