---
layout: recommendation
parent: DNA
title: inversion
definition: 
    Inversion: a sequence change where, compared to a reference sequence, <b>more than one nucleotide</b> replacing the original sequence are the reverse complement of the original sequence.
discussion:
    Is the change AAGC to TTCG an inversion?: No, an inversion would change AAGC to GCTT, its <b>reverse-complement</b>. TTCG is only the <b>complement</b> of AAGC.
    Is the change AAGC to CGAA an inversion?: No, an inversion would change AAGC to GCTT, its <b>reverse-complement</b>. CGAA is only the <b>reverse</b> of AAGC.<a name="dupinv"></a>
    Is it not better to describe the variant g.234_235ins123_234inv as g.123_234dupinv?: The descriptions of duplications is regularly debated <i>"Why not remove the variant type "duplication" and describe all dups as "insertion", it will make the HGVS rules in total simpler</i>. While we can not do this for historic reasons (duplications are in use since the beginning), we will restrict the use of "dup" as much as possible. Regarding a "<b>dupinv</b>" one could argue that an "inverted copy" is not "a copy inserted directly 3' of the original copy" and thus by definition this variant is not a duplication but an "insertion". Therefore the recommendation is to describe inverted duplication using the format g.122_123ins123_234inv or g.234_235ins123_234inv depending on whether the inverted copy is 5' or 3' of the original copy (reference sequence).
---
