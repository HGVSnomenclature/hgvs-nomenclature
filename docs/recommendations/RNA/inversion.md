# Inversion

<!-- ## Definition -->

Inversion: a sequence change where, compared to a reference sequence, **more than one nucleotide** replacing the original sequence are the reverse complement of the original sequence.

## Syntax

```sh exec="true"
bin/pull-syntax -c -f docs/syntax.yaml rna.inv
```

## Notes

- all variants **should be** described at the DNA level, descriptions at the RNA and/or protein level may be given in addition
- by definition, the region inverted ("positions_inverted") contains **more than one nucleotide**. The description `r.234inv` is therefore not allowed; a one nucleotide inversion should be described as a [substitution](substitution.md)
- for all descriptions the **most 3' position** possible of the reference sequence is arbitrarily assigned to have been changed (**3'rule**)
- **inverted duplications** are described as an insertion using the format `r.234_235ins123_234inv`, not as <code class="invalid">r.123_456dupinv</code>
- since exon splice signals will be inverted, large genomic inversions on the RNA level usually give [deletion](deletion.md) or [deletion-insertion (indel)](delins.md) variants
- inversions are not used on protein level. Depending on the (predicted) consequences of an inversion on protein level, changes are usually described as either a **delins** or a **frameshift**.

## Examples

- `r.177_180inv`<br>
  inversion of nucleotides `r.177` to `r.180`, changing `..agg`<code class="del">cuga</code>`uu..` to `..agg`<code class="ins">ucag</code>`uu..`
- `r.203_506inv`<br>
  inversion of the 304 nucleotides from position `r.203` to `r.506`

## Discussion

!!! note "Is the change "aagc" to "uucg" an inversion?"

    No, an inversion would change "aagc" to "gcuu", its **reverse-complement**. "uucg" is only the **complement** of "aagc".

!!! note "Is the change "aagc" to "cgaa" an inversion?"

    No, an inversion would change "aagc" to "gcuu", its **revese-complement**. "cgaa" is only the **reverse** of "aagc".

!!! note "On the [old nomenclature website](http://www.HGVS.org/mutnomen/examplesRNA.html) (bottom) you had the example <code class="invalid">r.124_500delinsoAB053210.2:r.1289-365_1289-73</code>, i.e. the "o" indicating the inserted sequence AB053210.2:r.1289-365_1289-73 was from the opposite transcriptional strand. Is the "o" still used?"

    No, the "o" is not used, the insertion is in an inverted orientation so "inv" should be used; <code class="invalid">r.124_500delins[AB053210.2:r.1289-365_1289-73inv]</code>.
