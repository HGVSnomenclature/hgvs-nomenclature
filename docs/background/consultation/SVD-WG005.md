---
layout: default-md
title: SVD-WG005
category: SVD-WG
---

## Community Consultation

### Proposal SVD-WG005 (gom/lom)

*	Status: <font color="red">accepted</font>
	:	proposal SVD-WG005 opened for **Community Consultation** on October 20 (2016), and closed on Dec.31 (2016). Since no major objections were received the SVD-WG decided to accept the proposal.

The proposal suggests to extend the HGVS recommendations to allow description of changes in general methylation status. The abbreviation <font color="red">gom</font> to indicate a general gain of methylation (hypermethylation), the abbreviation <font color="red">lom</font> to indicate a general loss of methylation (hypomethylation). The "\|" character ("pipe") is introduced to indicate that not a direct change of the sequence is described but a **modification** (change of state, here methylation).

* * *

#### Examples

*	g.12345678\_12345901|gom
	:	compared to the reference (normal situation), the region between nucleotides g.12345678 and 12345901 showed general gain in methylation (increased methylation, hypermethylated)

*	g.23456789\_23456901|lom
	:	compared to the reference (normal situation), the region between nucleotides g.23456789 and 23456901 showed general loss in methylation (reduced methylation, hypomethylated)

* * *

### Note

The proposal ("lom" and "gom") follows the current standard to use three-letter abbreviations. The "\|" character ("pipe") is used to indicate a **modification** of the sequence is reported, a change in state (here methylation), not a change in the sequence itself. Introduction of the "\|" facilitates future additions when recommendations would be requested to describe other types of modification, e.g. of protein sequences (phosphorylation). In addition introduction of the "\|" facilitates backward compatibility, modifications can be easily stripped from the description. The current proposal does not include recommendations to add a numerical description of the amount of methylation detected. The SVD-WG is interested to learn whether such an extension is desired and, when yes, how to add it. 
