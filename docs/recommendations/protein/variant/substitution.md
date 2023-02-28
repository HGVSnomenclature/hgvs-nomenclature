---
layout: recommendation
parent: Protein
title: substitution
definition: 
    Substitution: a sequence change where, compared to a reference sequence, <b>one</b> amino acid is replaced by <b>one</b> other amino acid.
discussion:
    <a name="polymorphism"></a>Are polymorphisms described like p.2366Gln/Lys?: No, all substitutions are described as NP_003997.1:p.Gln2366Lys. In the past, the format p.2366Gln/Lys (p.2366Q/K) has been used to describe "polymorphic" sequence variants. Note that a description should be neutral, simply describe the change, and not include any other information like predicted or known functional consequences.
    Can I describe a TrpVal to CysArg variant as a amino acid substitution (p.TrpVal24CysArg)?: No, this is not allowed. By definition a substitution changes <b>one</b> amino acid into <b>one</b> other amino acid. The change TrpVal to CysArg should be described as NP_003997.1:p.Trp24_Val25delinsCysArg, i.e. a deletion/insertion (indel) (<a href='http://varnomen.HGVS.org/recommendations/DNA/variant/indel/'><i>see Deletion-Insertion</i></a>).
    How should you describe an amino acid substitution to any other amino acid?: HGVS uses IUPAC symbols (<a href='http://varnomen.hgvs.org/bg-material/standards/'><i>see Standards</i></a>). The symbol for 'any' amino acid is 'X'/'Xaa'. Since 'X' has been used to indicate a translation stop codon (nonsense variant) we suggest to use 'Xaa' three-letter amino acid code only (e.g. p.Arg782Xaa).
---
