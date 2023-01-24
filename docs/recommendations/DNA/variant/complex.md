---
layout: recommendation
parent: DNA
title: complex (HGVS/ISCN)
definition: 
    Complex: a sequence change where, compared to a reference sequence, a range of changes occur that can not be described as one of the basic variant types (substitution, deletion, duplication, insertion, conversion, inversion, deletion-insertion, or repeated sequence).
discussion:
    Is the description NM_04006.1:c.123+45_123+51TSDinsL1.603bp acceptable (TSD = target site duplication, insL1 indicates the nature of the insert (L1, Alu or SVA), 603bp = the number of inserted base pairs)?: No, not realy, it is not exact. Following HGVS recommendations the description should be like NG_012232.1(NM_004006.2):c.123+51_123+52ins[[XXXXXX.y:g.393_1295];123+45_123+51]. So give a genomic reference sequence to describe the intronic variant, give the site of the inserted sequence, exactly describe the inserted sequence (not like "insL1.603bp") and describe the target site duplication as an insertion (not "TSD", by definition a duplication is only used when the duplicate sequence is inserted directly 3' of the original copy of that sequence). In the example XXXXXX.y is a GenBank file (accession.version number) containing the inserted L1 sequence (nucleotides g.393_1295). When the inserted sequence is not known its (estimated) size can be used, like NG_012232.1(NM_004006.2):c.123+51_123+52ins[(603);123+45_123+51].
---
