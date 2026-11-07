#!/usr/bin/env bash
# Execute the archived programs from a throwaway copy so tracked data stay unchanged.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cp -a "$ROOT/research" "$TMP/"
for phase in 2 3 4; do
  echo "Running Phase ${phase}"
  python "$TMP/research/phase-$phase/phase${phase}_verify.py" > "$TMP/phase${phase}.log"
  tail -2 "$TMP/phase${phase}.log"
done
python "$TMP/research/phase-5/phase5_experiments.py" --output-dir "$TMP/phase5-generated" > "$TMP/phase5.log"
tail -1 "$TMP/phase5.log"
# Check deterministic output against an independently repeated run under same dependency versions.
python "$TMP/research/phase-5/phase5_experiments.py" --output-dir "$TMP/phase5-second" > /dev/null
for name in phase5_metrics.csv phase5_identifiability.csv phase5_coverage.csv phase5_paired_contrasts.csv phase5_convergence.csv phase5_validation.json; do
  cmp "$TMP/phase5-generated/$name" "$TMP/phase5-second/$name"
done
echo 'PASS: math regression + deterministic Phase 5 outputs (same environment)'
