# Community Consultation

The HGVS Nomenclature is administed by the [HGVS Variant Nomenclature Committee
(HVNC)](../governance/), a working group of the Human Genome Organization.  The HVNC handles
requests to change or extend HGVS Nomenclature through a **Community Consultation** process.
Proposed and implemented changes will be discussed using our [GitHub
Discussions](https://github.com/HGVSnomenclature/hgvs-nomenclature/discussions) forum and summarized
here. 

## Proposal Process

- Anyone may submit a proposal for changes to Discussions. The proposal is initially considered OPEN
  and under discussion.
- Anyone may comment on an OPEN proposal.
- The HVNC will evaluate all proposals from time to time. For each proposal, the committee may
  choose to:
    - leave the proposal OPEN for further discussion;
    - mark the propossal as REJECTED with explanation if the proposal is deemed unworkable,
      incomplete, or inconsistent with the existing guidelines, or if it is similar to existing or
      recently considered proposals; or
    - move the propsal to DRAFTING to indicate that a member of the HVNC will understake drafting of
      the changes.
- When a proposal is in the DRAFTING stage, a GitHub issue is created to track writing for the
  intended documentation change. Writing will be undertaken in a branch dedicated for the assigned
  issue. A pull request will eventually be submitted and evaluated.
- Evaluation of the PR is limited to HVNC members (i.e., not for public discussion), although
  specific users may be asked for comments when warranted. If the PR is eventually merged, the
  discussion proposal is marked as ADOPTED.
- If the PR is not merged for any reason (e.g., if we realize that the PR creates unforeseen issues
  with the existing nomenclature), the proposal will either be re-opened for more discussion or
  rejected at the discretion of the committee.

## Proposals

### Open

* [SVD-WG010](SVD-WG010/) (var distance): suggests to specify the HGVS nomenclature recommendations for the description of two variants which are close to each other: **Status**: <code class="spot1">closed July 31, 2021</code> (decision pending).

### Closed

* [SVD-WG009](SVD-WG009/) (conversion): suggested to simplify the HGVS nomenclature recommendations by **discontinuing the use of the variant type "con"** to describe conversions: **Status**: <code class="spot1">accepted</code>. Closed Oct.31 (2020). Opened Aug,4 (2020).

* [SVD-WG008](SVD-WG008/) (Reference Sequences): suggested to specify the HGVS recommendations for acceptable Reference Sequences (see updated [Reference Sequences](../background/refseq/) page): **Status**: <code class="spot1">accepted</code>. Closed Sep.30 (2019). Opened Jul.20 (2019).

* [SVD-WG007](SVD-WG007/) (RNA fusion): suggests to extend the HGVS recommendations with a format to describe RNA fusion transcripts following the format to describe a fusion between two DNA molecules (translocations), i.e. using "::": **Status**: <code class="spot1">accepted</code>. Closed Jun.30 (2019). Opened Apr.10 (2019).

* [SVD-WG006](SVD-WG006/) (circular DNA): suggests to extend the HGVS recommendations allowing a **"o."** prefix for circular genomic reference sequences.: suggests to add the exception for circular genomic reference sequences ("m." and "o." prefix) to allow NC_012920.1:m.16563_13del: **Status**: <code class="spot1">accepted</code>. Closed Oct.30 (2018). Opened Aug.1 (2018).

* [SVD-WG005](SVD-WG005/) (gom/lom): suggests to extend the HGVS recommendations to allow description of changes in general methylation status.: **Status**: <code class="spot1">accepted</code>. Closed Dec.31 (2016). Opened Oct.20 (2016).

* [SVD-WG004](SVD-WG004/) (ISCN<>HGVS): suggested to extend the recommendations to cover the description of structural variants, esp. translocations and chromothripsis.: **Status**: <code class="spot1">accepted</code>. Closed Jan.15 (2016). Opened Nov.10 (2015).: **NOTE**: since SVD-WG004 covers variants that may become rather complex to describe and will be difficult to implement the proposal has been accepted as the **"named extension ISCN"** ([named extension](../background/versioning/)).

* [SVD-WG003](SVD-WG003/) (exon del/dup): suggested to describe exon deletions/duplications using the format c.(233+1\_234-1)_(1234+1\_1235-1)del.: **Status**: Oct.6 (2015) <code class="spot1">new proposal to be made</code>. Closed Jul.16 (2015). Opened May 14 (2015).
    
* [SVD-WG002](SVD-WG002/) (**n.** prefix): suggested to accept a non-coding DNA reference sequence (n.345A>G, n.224+1G>T, n.696-38544del).: **Status**: Oct.6 (2015) <code class="spot1">accepted</code>. Closed Jul.16 (2015). Opened May 14 (2015).
        
* [SVD-WG001](SVD-WG001/) (no change): suggested to allow reporting of variants that were tested but found to be unchanged (g.50377648A=, c.1823A=, r.377u=, p.Val76=). : **Status**: Oct.6 (2015) <code class="spot1">accepted</code>. Closed Jul.16 (2015). Opened May 14 (2015).