#!/usr/bin/env bash

set -e

./scripts/docs-build.sh

mkdocs serve --dev-addr 127.0.0.1:8008
