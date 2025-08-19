#!/bin/bash
set -e

PROJECT_BASE=$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd) || exit 1

echo "[INFO] Initializing application environment..."
export PROJECT_BASE
export APP_ROOT="${PROJECT_BASE}"/src/python
export PYTHONPATH=${APP_ROOT}:${PROJECT_BASE}/libs/python

set -a
source "${PROJECT_BASE}"/.env
set +a

echo "[INFO] Environment initialized."
echo "[INFO] PROJECT_BASE: ${PROJECT_BASE}"
echo "[INFO] PYTHONPATH: ${PYTHONPATH}"
