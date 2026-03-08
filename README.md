# Chabauty--Coleman on fibres of the perfect cuboid surface

This repository contains the paper and verification scripts for a Chabauty--Coleman
approach to the perfect cuboid problem.

## Main result

**Theorem A.** No perfect cuboid exists with Saunderson parameter
r in {2, 3, ..., 500}.

The proof proceeds by:

1. Constructing an explicit projection phi: C_r -> A_r from the genus-5 cuboid
   fibre to a genus-2 Prym curve (Theorem G).
2. Proving a uniform Coleman bound: rank(A_r) = 0 implies #A_r(Q) = 6
   (Theorem D, via two-differential analysis at p = 3).
3. Verifying rank(J(A_r)) = 0 for r = 2, ..., 500 by 2-Selmer descent
   (Magma Chabauty0).

## Repository structure

```
paper/
  paper.tex          LaTeX source (amsart, ~25 pages)
  references.bib     BibTeX references
  README.md          Compilation instructions

scripts/
  46_two_differential_proof.py   Theorem D verification
  51_trace_algebraic_proof.py    Theorem E verification (Frobenius trace)
  53_selmer_theory.py            2-Selmer descent (exact arithmetic)
  54_p2_local_analysis.py        2-adic local analysis
  55_full_selmer.py              Full Stoll-method framework

magma/
  magma_52_critical.txt          Magma code for TwoSelmerGroup / Chabauty0

PROOF_FINAL.md                   Full proof narrative (13 sections)
```

## Building the paper

```bash
cd paper
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

## Computational environment

- **Magma** V2.29-4 (online calculator: magma.maths.usyd.edu.au/calc/)
- **PARI/GP** 2.17.3 (L-function computation via `lfungenus2`)
- **Python** 3.x with `sympy` and `fractions` (verification scripts)

## License

MIT License. See [LICENSE](LICENSE) for details.

## Author

MAKURA

## Acknowledgments

Parts of this work were assisted by Claude (Anthropic, model claude-opus-4-6).
See the Acknowledgments section of the paper for full AI disclosure.
