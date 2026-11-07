# Reproducibility and archive status

This repository holds the **text-source subset** of the Absolute Luck project, including full mathematical arguments, Monte Carlo scripts, exact-result tables and audit records. It is not yet the complete historical ZIP/PDF/figure archive.

## Python checks
Install the requirements, then run checks from their folders because the Phase 3 and Phase 4 scripts expect nested preserved source copies:

```bash
python -m pip install -r requirements.txt
python research/phase-2/phase2_verify.py
python research/phase-3/phase3_verify.py
python research/phase-4/phase4_verify.py
python research/phase-5/phase5_experiments.py --output-dir /tmp/absolute-luck-phase5-replay
```

These scripts produce or overwrite some validation files; run against a **throwaway checkout or copy** if you want to preserve their archived outputs byte-for-byte.

The LaTeX documents reference figures not yet published as binary assets here. Their complete original PDFs, editable figure sources and nested archive ZIPs are preserved in the ChatGPT source-deliverables and need separate binary import before a clean GitHub-only build is possible. Do not claim this repository is a complete independently reproducible publication package until that step is finished.

## Mathematical scope
All numerical scenarios are hypothetical; no canonical WEBTOON measurements or novel probability theorem are claimed. Internal audits are not external peer review.
