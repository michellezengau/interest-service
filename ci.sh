#!/usr/bin/env bash
set -euo pipefail   # stop at the first failing command
echo "== Lint ==";   ruff check .
echo "== Format =="; ruff format --check .
echo "== Test ==";   python -m pytest -q
echo "Pipeline passed"