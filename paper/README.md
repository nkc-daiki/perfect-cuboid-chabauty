# Perfect Cuboid 論文ファイル

## ファイル構成

| ファイル | 内容 |
|---------|------|
| `paper.tex` | 論文本体（amsart, 8セクション） |
| `references.bib` | 参考文献（BibTeX, 20エントリ） |
| `README.md` | このファイル |

## コンパイル方法

```bash
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

## 論文の構成

1. **Introduction** — 問題定義、先行研究、主要結果（Theorem A, D, G）
2. **The cuboid surface and its fibrations** — 曲面S、C_r、A_r の定義
3. **The projection φ: C_r → A_r** — Theorem G（明示的射影）
4. **Arithmetic invariants** — Torsion、局所障害、Trace zero、Nodal reduction
5. **Two-differential Coleman bound** — Theorem D（比 27/10 の独立性）
6. **2-Selmer analysis** — delta rank=4、Magma RankBound=0
7. **Computational evidence** — Chabauty結果、L(A_r,1)データ、Conductor表
8. **Discussion** — 残課題、Silvermanの限界、Horie-Yamauchiとの接続

## 投稿先候補

- **Mathematics of Computation** (AMS) — 理論+計算の組合せに最適
- **Experimental Mathematics** (Taylor & Francis) — 計算的数論の標準誌
- **Journal of Number Theory** (Elsevier) — 純粋数論寄り

## 元データとの対応

| 論文の定理 | 元ファイルの定理 | 検証スクリプト |
|-----------|-----------------|--------------|
| Theorem A | Theorem A (PROOF_FINAL §8) | Magma Chabauty0 |
| Theorem C | Theorem C (PROOF_FINAL §6) | — (代数的証明) |
| Theorem D | Theorem D (PROOF_FINAL §7) | `46_two_differential_proof.py` |
| Theorem E | Theorem E (PROOF_FINAL §9) | `51_trace_algebraic_proof.py` |
| Theorem F | Theorem F (PROOF_FINAL §9) | — (代数的証明) |
| Theorem G | Theorem G (PROOF_FINAL §10) | sympy 検証 |
| Prop 6.1 (delta rank) | Theorem 9.9 | `53_selmer_theory.py` |
| Prop 6.2 (rank=0) | Theorem 9.9 | Magma RankBound |

## 注意事項

- 既存ファイル（PROOF_FINAL.md等）は一切変更していない
- 論文はPROOF_FINAL.mdの内容を英語論文形式に再構成したもの
- AI disclosure を Acknowledgments に記載済み
