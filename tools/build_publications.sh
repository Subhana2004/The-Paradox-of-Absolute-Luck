#!/usr/bin/env bash
# Rebuild figure assets and both paper PDFs using source files checked into Git.
set -euo pipefail
# Print TeX diagnostic tails on CI failures instead of discarding the error.
report_failure() {
  local exitcode=$?
  if [[ $exitcode -ne 0 ]]; then
    echo "PDF build failed (exit $exitcode); TeX diagnostics follow:"
    for log in /tmp/absolute-luck-manuscript-latex.log /tmp/absolute-luck-essay-latex.log; do
      if [[ -f "$log" ]]; then
        echo "---- $log ----"
        tail -n 90 "$log"
      fi
    done
  fi
}
trap report_failure EXIT
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export MPLBACKEND=Agg
export SOURCE_DATE_EPOCH=1794018600
export TZ=UTC
python research/phase-5/phase5_figures.py --data-dir research/phase-5 --output-dir manuscript/figures
python essay/source/draw_figures.py
(
 cd manuscript
 pdflatex -interaction=nonstopmode -halt-on-error Absolute_Luck_Phase6_Manuscript.tex >/tmp/absolute-luck-manuscript-latex.log
 pdflatex -interaction=nonstopmode -halt-on-error Absolute_Luck_Phase6_Manuscript.tex >>/tmp/absolute-luck-manuscript-latex.log
)
(
 cd essay
 xelatex -interaction=nonstopmode -halt-on-error Absolute_Luck_Phase7_Essay.tex >/tmp/absolute-luck-essay-latex.log
 xelatex -interaction=nonstopmode -halt-on-error Absolute_Luck_Phase7_Essay.tex >>/tmp/absolute-luck-essay-latex.log
)
# PDF 1.4 for compatibility with browser/embedded viewers; keep embedded text/vectors.
for spec in "manuscript/Absolute_Luck_Phase6_Manuscript" "essay/Absolute_Luck_Phase7_Essay"; do
  gs -q -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH -dSAFER -sOutputFile="$spec.compat.pdf" "$spec.pdf"
  mv "$spec.compat.pdf" "$spec.pdf"
done
python tools/verify_publication.py
