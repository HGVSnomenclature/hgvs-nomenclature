# Style conventions used in this documentation

The HGVS Nomenclature is written using [Markdown](https://en.wikipedia.org/wiki/Markdown).  If you're unfamiliar with Markdown, please read [Introduction to Markdown](https://www.writethedocs.org/guide/writing/markdown/).  This page documents conventions used to apply Markdown to the HGVS Nomenclature.  Contributors should follow the styles outlined below. Inline HTML is discouraged except when necessary.

## Style Examples

{{ read_csv('style-examples.csv') }}

## Syntax blocks

When describing the syntax of class of variant, we use a structure like this:

```markdown
## Syntax

- `TYPE.[POSEDIT1;POSEDIT2]` (one allele)
- `TYPE.[POSEDIT1];[POSEDIT2]` (two alleles)

where

- `TYPE` is the reference sequence type
- `POSEDIT1` and `POSEDIT2` are the positions and changes 
```

which renders like this:

![Syntax example](syntax-example.png)


<hr>
## Scraps below
```
Current DNA alleles:

Format (one allele):   **"prefix"["change1";"change2"]**,  e.g. g.[123G>A;345del]

* **"prefix"**  =  reference sequence used  =  g.
* **[**  =  opening symbol for allele  =  [
* **"change1"**  =  description first variant  =  123G>A
* **;**  =  separator symbol two changes  =  ;
* **"change2"**  =  description second variant  =  345del
* **]**  =  closing symbol for allele  =  ]
 
Format (two alleles):   **"prefix"["change"];["change"]**,  e.g. g.[123G>A];[345del]

* **"prefix"**  =  reference sequence used  =  g.
* **[**  =  opening symbol for allele-1  =  [
* **"change"**  =  description variant  =  123G>A
* **];[**  =  closing symbol for allele-1, separator symbol two alleles, opening symbol for allele-2  =  ];[
* **"change"**  =  description variant  =  345del
* **]**  =  closing symbol for allele-2  =  ]
``` 
