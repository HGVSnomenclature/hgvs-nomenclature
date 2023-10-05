# substitution

## Definition

Substitution: a sequence change where, compared to a reference sequence, **one** nucleotide is replaced by **one** other nucleotide.

## Description

Format: **"prefix""position_substituted""reference_nucleotide"">"new_nucleotide"**, e.g. r.123a>g

**"prefix"** = reference sequence used = r. **"position_substituted"** = position nucleotide sustituted = 123 **"reference_nulceotide"** = nucleotide at reference position = a **">"** = type of change is a substitution = > **"new_nucleotide"** = substituted nucleotide = g

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- **prefix** reference sequences accepted are r. (coding and non-coding RNA).
- substitutions involving two or more consecutive nucleotides are described as deletion/insertions (indels) (see [Deletion/insertion (delins)](../delins/)).
- two substitutions separated by one or more nucleotides should be described individually and not as a "delins"
  - exception: two variants separated by one nucleotide, together affecting one amino acid, should be described as a "delins" (e.g. r.142_144delinsugg (p.Arg48Trp)).: **NOTE:** this prevents tools predicting the consequences of a variant to make conflicting and incorrect predictions of two different substitutions at one position
- nucleotides that have been tested and found **not changed** are described as r.109u=, r.4567_4569= (see [SVD-WG001 (no change)](http://www.hgvs.org/mutnomen/accepted001.html)).
- it is not correct to describe "_polymorphisms_" as r.76a/g (see [Discussions](#polymorphism)).

## Examples

- NM_004006.3:r.76a>c: a substitution of the "a" nucleotide at r.76 with a "c"
- NM_004006.3:r.76_77delinsug : **NOTE**: based on the definition of a substitution, i.e. **one** nucleotide replaced by **one** other nucleotide, this change can not be described as a substitution like r.76_77aa>ug or r.76aa>ug
- NM_004006.3:r.(1388g>a): the predicted consequences at RNA level is a substitution of the "g" nucleotide at r.1388 with a "g"
- NM_004006.3:r.123=: a screen was performed showing that nucleotide r.123 was a "c" as in the coding DNA reference sequence (the nucleotide was not changed).
- NM_004006.1:r.-14a>c: a "a" to "c" substitution 14 nucleotides 5' of the ATG translation initiation codon
- NM_004006.3:r.\*41u>a: a "u" to "a" substitution 41 nucleotides 3' of the translation termination codon
- NM_004006.3:r.[897u>g,832\_960del]: two different transcripts, 897u>g and r.832_960del, derive from one variant (NM_004006.3:c.897T>G at the DNA level): **NOTE**: for more examples of variants affecting splicing see [RNA splicing](../splicing/)
- NM_004006.1:r.0: no RNA from the variant allele could be detected
- NM_004006.3:r.spl: RNA has not been analysed but it is very likely that splicing is affected
- NM_004006.3:r.?: an effect on the RNA level is expected but it is not possible to give a reliable prediction of the consequences (RNA not analysed)
- NM_004006.3:r.85=/u>c: a mosaic case where at position 85 besides the normal sequence (a U, described as "=") also transcripts are found containing a C (r.85u>c): **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first
- NM_004006.3:r.85=//u>c: a chimeric case, i.e. the sample is a mix of cells containing r.85= and r.85u>c.: **NOTE**: irrespective of the frequency in which each nucleotide was found, the reference is always described first

## Discussion

!!! note "When I only sequenced RNA (cDNA) and not genomic DNA should I then give the description of a variant at DNA level in parenthesis?"

    Yes, while the variant at RNA level can be described as r.76a>g on DNA level, based on a coding DNA reference, sequence it should be described as c.(76A>G).

!!! note "<a id="polymorphism"></a>Are polymorphisms described like r.76a/g?"

    No, all substitutions are described as r.76a>g. In the past, the format r.76a/g has been used to describe "polymorphic" sequence variants. Note that a description should be neutral, simply describe the change, and not include any other information like predicted or known functional consequences.

!!! note "I found a variant on DNA level which is a well-characterised splice variant. Is it correct to describe the variant as concluded from literature?"

    No, you should report what **you** have found. You can however use the published data to give the predicted consequences on RNA/protein level, e.g. NM_004006.3:c.3430C>T r.(3277_3432del) p.(Leu1093_Gln1144del).
