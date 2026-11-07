# The Paradox of Absolute Luck

[![Verify mathematical research and rebuild PDFs](https://github.com/Subhana2004/The-Paradox-of-Absolute-Luck/actions/workflows/verify.yml/badge.svg)](https://github.com/Subhana2004/The-Paradox-of-Absolute-Luck/actions/workflows/verify.yml)

**Can probability favor everyone?** An independent, *expository* mathematical investigation of conflicting success guarantees, higher-order dependence, finite exchangeability, and probability allocation, inspired by Sehoon Kim's fictional *Hardcore Leveling Warrior* ability, *Absolute Luck*.

> **Research integrity:** All 99%, 99.5%, 200-coin and allocation scenarios are intentionally constructed mathematical thought experiments—not observed data or verified operating rules from the webtoon. The results apply to the stated probability models; no new theorem, independently verified canon mechanism, or external peer review is claimed.

## Read the completed documents

| Work | PDF | Editable source |
|---|---|---|
| Phase 6: formal expository research manuscript | [Research manuscript, 10 pages](manuscript/Absolute_Luck_Phase6_Manuscript.pdf) | [LaTeX](manuscript/Absolute_Luck_Phase6_Manuscript.tex) |
| Phase 7: accessible mathematical essay | [Mathematical essay, 5 pages](essay/Absolute_Luck_Phase7_Essay.pdf) | [Markdown](essay/Absolute_Luck_Phase7_Essay.md) · [LaTeX](essay/Absolute_Luck_Phase7_Essay.tex) |

The PDFs are normalized for browser-friendly PDF 1.4 viewing. The five diagrams for each document are available in `manuscript/figures` or `essay/figures`, in source-friendly vector SVG and publication formats.

## Reproducibility (fresh checkout)

The repository contains the original verification programs and preserved nested regression fixtures used by the published expository investigation. To run locally, install Python 3.13 and a LaTeX distribution that supplies `pdflatex`, `xelatex`, fonts and Ghostscript/Poppler tools. The GitHub Actions workflow provisions these on Ubuntu.

```bash
python -m pip install -r requirements-lock.txt
sha256sum --check publication/ASSET_SHA256SUMS.txt
sha256sum --check publication/CSV_SHA256SUMS.txt
bash tools/run_regression.sh
bash tools/build_publications.sh
```

`run_regression.sh` performs exact/proof-oriented Phase 2–4 regressions, the seeded Phase 5 simulation, and a second same-environment run compared byte-for-byte, all in a temporary copy so the archived results are not overwritten. `build_publications.sh` regenerates five research figures and five essay diagrams, compiles both documents and validates PDF structure and extractable text. CI also uploads its newly generated PDFs/figures as build artifacts.

### Research layout

- [`research/phase-0`](research/phase-0) and [`phase-1`](research/phase-1): fictional-source boundary and literature/novelty audits.
- [`research/phase-2`](research/phase-2): collision and multiplication paradoxes.
- [`research/phase-3`](research/phase-3): probability models, higher-order dependence and comparative predictions.
- [`research/phase-4`](research/phase-4): proofs, extendibility bounds and adversarial checks.
- [`research/phase-5`](research/phase-5): reproducible synthetic Monte Carlo experiments and statistical reporting.
- [`manuscript`](manuscript): formal Phase 6 paper and figures.
- [`essay`](essay): Phase 7 expository narrative and diagrams.
- [`audits`](audits): internal mathematics/citation audits; not external certification.
- [`publication/ASSET_SHA256SUMS.txt`](publication/ASSET_SHA256SUMS.txt): hashes of checked-in PDFs and figures.

## How to read the science

A *single* mutually exclusive duel cannot make two individuals' winning chances both 99% in the same probability space. But two individuals might each have 99% odds against a baseline opponent and 50% odds against one another under a weighted-choice model. Separately, 200 events can each have 99.5% reliability while a finitely dependent law assigns zero probability to all 200 succeeding; exchangeability and conditional-independence constraints sharply change that conclusion.

These are applications and interpretations of established probability, optimization and exchangeability theory. The manuscripts cite prior literature. This repository is a research exposition and model study, **not a claim of new mathematical discovery**.

## Rights, credits, and readiness

Fictional inspiration: *Hardcore Leveling Warrior* by Sehoon Kim. This project is not affiliated with its publisher or creator. No comic imagery is included. Figure diagrams were generated for this mathematical project.

Repository maintainer identifier in `CITATION.cff` is **not a final scientific-authorship determination**. Verify authorship, permissions, and AI-use disclosures before academic submission. **No blanket license** has been selected; consult the owner before redistribution or reuse beyond applicable law.

The source-backed mathematical checks and document builds are automated, but that is **not independent peer review or proof of originality**. Canon-specific claims still require verification against primary publication panels. For changes, see [CONTRIBUTING.md](CONTRIBUTING.md).


## Phase 9 — Research integrity verdict

The [Phase 9 research audit](audits/PHASE9_RESEARCH_AUDIT_2026-11-07.md) **reverified the published mathematical constructions and bibliography**, with 23 independently rederived math/data checks and GitHub computational reproduction. Its conclusion is **conditional**, not a certificate of peer review or submission approval. Original comic-panel mechanics, scientific authorship and AI disclosures, licensing, and independent human mathematical review remain open. Run `python audits/phase9_independent_math_checks.py` to replay the cross-checks.

## Phase 10 — Publication venue planning

The [Phase 10 venue strategy](publication/phase-10/README.md) compares Chalkdust, Math Horizons, Tom Rocks Maths and other outlets, and publishes a [venue matrix](publication/phase-10/VENUE_MATRIX.csv), [human-first editorial plan and unsent queries](publication/phase-10/REWRITE_AND_EDITOR_QUERIES.md), and [submission gates](publication/phase-10/SUBMISSION_GATES.md). **Strategy completed; submission still on hold** pending final human authorship, true AI-use disclosures, external review, prior-posting/rights clearance and venue-specific permission. No manuscript has been submitted.
