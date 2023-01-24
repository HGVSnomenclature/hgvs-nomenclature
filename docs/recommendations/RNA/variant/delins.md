---
layout: recommendation
parent: RNA
title: deletion-insertion
definition: 
    Deletion-Insertion (delins): a sequence change where, compared to a reference sequence, one or more nucleotides are replaced by one or more other nucleotides <b>and which is not</b> a substitution, inversion or conversion.
discussion:
    What is an <b>"indel"</b>?: The term "indel" is not used in HGVS nomenclature (<a href='http://varnomen.hgvs.org/bg-material/glossary/'><i>see Glossary</i></a>). The term is confusing, having different meanings in different disciplines.
    Can I describe a "gc" to "ug" variant as a dinucleotide substitution (r.4gc>ug)?: No this is not allowed. By definition a substitution changes <b>one</b> nucleotide into <b>one</b> other nucleotide (<a href='http://www.HGVS.org/varnomen/recommendations/RNA/variant/substitution/'><i>see Substitution</i></a>). The change "augu<font color="red">gc</font>ca" to 'augu<font color="red">ug</font>ca" should be described as r.5_6delinsug, i.e. a deletion/insertion (indel).
    The BRCA1 coding RNA reference sequence from position r.2074 to r.2080 is ..caugaca.. A variant frequently found in the population is ..cau<font color="red">a</font>aca.. (r.2077g>a). In a patient I found the sequence ..cau<font color="red">a ua</font>aca.. Can I describe this variant as r.[2077g>a;2077_2078insua]?: The shortest description of this variant is r.2077delinsaua. However, since the variant is likely a combination of two other variants it is acceptable to describe it as r.[2077g>a;2077_2078insua].
---
