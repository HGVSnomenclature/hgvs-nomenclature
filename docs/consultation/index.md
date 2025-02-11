# Community Consultation

The HGVS Nomenclature is administered by the [HGVS Variant Nomenclature Committee (HVNC)](../hvnc.md), a working group of the Human Genome Organization.
The HVNC handles requests to change or extend HGVS Nomenclature through a **Community Consultation** process.
Proposed and implemented changes will be discussed using our [GitHub Discussions](https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions) forum and summarized here.

## Proposal Process

- Anyone may submit a proposal for changes to Discussions.
  The proposal is initially considered OPEN and under discussion.
- Anyone may comment on an OPEN proposal.
- The HVNC will evaluate all proposals from time to time.
  For each proposal, the committee may choose to:
    - leave the proposal OPEN for further discussion;
    - mark the proposal as REJECTED with explanation if the proposal is deemed unworkable, incomplete, or inconsistent with the existing guidelines, or if it is similar to existing or recently considered proposals; or
    - move the proposal to DRAFTING to indicate that a member of the HVNC will undertake drafting of the changes.
- When a proposal is in the DRAFTING stage, a GitHub issue is created to track writing for the intended documentation change.
  Writing will be undertaken in a branch dedicated for the assigned issue.
  A pull request will eventually be submitted and evaluated.
- Evaluation of the PR is limited to HVNC members (i.e., not for public discussion), although specific users may be asked for comments when warranted.
  If the PR is eventually merged, the discussion proposal is marked as ADOPTED.
- If the PR is not merged for any reason (e.g., if we realize that the PR creates unforeseen issues with the existing nomenclature), the proposal will either be re-opened for more discussion or rejected at the discretion of the committee.

## Proposals

### Open

None.

### Closed

- **[SVD-WG010](SVD-WG010.md) (var distance)**<br>
  suggests to specify the HGVS nomenclature recommendations for the description of two variants which are close to each other.<br>
  **Status: rejected.** Opened May 15, 2021. Closed July 31, 2021.

- **[SVD-WG009](SVD-WG009.md) (conversion)**<br>
  suggested to simplify the HGVS nomenclature recommendations by **discontinuing the use of the variant type "con"** to describe conversions.<br>
  **Status: accepted.** Opened August 4, 2020. Closed October 31, 2020.

- **[SVD-WG008](SVD-WG008.md) (Reference Sequences)**<br>
  suggested to specify the HGVS recommendations for acceptable Reference Sequences (see updated [Reference Sequences](../background/refseq.md) page).<br>
  **Status: accepted.** Opened July 20, 2019. Closed September 30, 2019.

- **[SVD-WG007](SVD-WG007.md) (RNA fusion)**<br>
  suggested to extend the HGVS recommendations with a format to describe adjoined transcripts from gene fusions, following the format to describe a fusion between two DNA molecules (translocations), i.e. using `::`.<br>
  **Status: accepted.** Opened April 10, 2019. Closed June 30, 2019.

- **[SVD-WG006](SVD-WG006.md) (circular DNA)**<br>
  suggested to extend the HGVS recommendations allowing a **`o.`** prefix for circular genomic reference sequences.<br>
  Suggested to add the exception for circular genomic reference sequences (`m.` and `o.` prefix) to allow `NC_012920.1:m.16563_13del`.<br>
  **Status: accepted.** Opened August 1, 2018. Closed October 30, 2018.

- **[SVD-WG005](SVD-WG005.md) (gom/lom)**<br>
  suggested to extend the HGVS recommendations to allow description of changes in general methylation status.<br>
  **Status: accepted.** Opened October 20, 2016. Closed December 31, 2016.

- **[SVD-WG004](SVD-WG004.md) (ISCN<>HGVS)**<br>
  suggested to extend the recommendations to cover the description of structural variants, especially translocations and chromothripsis.<br>
  **Status: accepted.** Opened November 10, 2015. Closed January 15, 2016.<br>
  **NOTE**: since SVD-WG004 covers variants that may become rather complex to describe and will be difficult to implement, the proposal has been accepted as the **"named extension ISCN"** ([named extension](../versions/older-versions.md#SVD-WG004)).

- **[SVD-WG003](SVD-WG003.md) (exon del/dup)**<br>
  suggested to describe exon deletions/duplications using the format `c.(233+1_234-1)_(1234+1_1235-1)del`.<br>
  **Status: new proposal to be made** (October 6, 2015). Opened May 14, 2015. Closed July 16, 2015.

- **[SVD-WG002](SVD-WG002.md) (`n.` prefix)**<br>
  suggested to accept a non-coding DNA reference sequence (`n.345A>G`, `n.224+1G>T`, `n.696-38544del`).<br>
  **Status: accepted** (October 6, 2015). Opened May 14, 2015. Closed July 16, 2015.

- **[SVD-WG001](SVD-WG001.md) (no change)**<br>
  suggested to allow reporting of variants that were tested but found to be unchanged (`g.50377648A=`, `c.1823A=`, `r.377u=`, `p.Val76=`).<br>
  **Status: accepted** (October 6, 2015). Opened May 14, 2015. Closed July 16, 2015.
