# Fresh-clone reproduction and provenance

See [README.md](README.md) for the package map and requirements. The repository contains both complete Phase 6/7 PDFs and all ten figures needed by the LaTeX files, along with the Figure 3/4 historical visualizations. It is possible to rebuild both PDFs from a fresh clone without downloading a ChatGPT ZIP.

## Scientific computation

```bash
python -m pip install -r requirements-lock.txt
bash tools/run_regression.sh
```

Runs nested Phase 2/3/4 exact-model regressions and Phase 5 Monte Carlo twice with labeled, deterministic streams. Results are tested in a temporary copy. The research source contains no observational coin-flip dataset: every reported value is mathematically stipulated or simulated.

## Publication build

The GitHub Actions workflow installs a compatible TeX Live distribution, Ghostscript, and Poppler. With those installed locally:

```bash
sha256sum --check publication/ASSET_SHA256SUMS.txt
python tools/verify_publication.py
bash tools/build_publications.sh
```

The first step verifies the **checked-in, original published assets**. The last step regenerates graphs and PDFs from source, which may have different file hashes owing to LaTeX, Ghostscript, font, Matplotlib, timestamps and dependency environments. It verifies pages, visual references, and extractable text, not bit-for-bit PDF identity.

## Integrity boundaries

- The internal Phase 6 and Phase 7 audits are research records, not external peer review or plagiarism certification.
- The original nested ZIP archives from Phases 2–7 are available in the source conversation but are *not* stored here because the underlying source files and figures are already published individually.
- Some historical archive-only checkers require those frozen ZIPs; those **are not** advertised as clean-clone CI commands.
- Canon mechanics and numerical luck values are not primary-panel-verified. No novel theorem or empirical fictional-event result is claimed.
- The GitHub Actions run is the authoritative external-runner verification; local checks alone do not establish cloud CI success.
