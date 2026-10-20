#!/usr/bin/env python3
"""Prepare the local development/test basis without replacing existing files."""
import os, subprocess
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
for command in (
    ['python3','bin/prepare-local.py'],
    ['python3','bin/build-runtime.py'],
    ['python3','bin/composer.py','install','--prefer-dist','--no-interaction','--no-progress'],
    ['npm','ci','--cache',str(Path('.local/npm-cache').resolve())],
    ['npm','run','build'],
    ['docker','compose','up','-d','--wait','mysql'],
    ['bin/php','artisan','migrate','--force'],
    ['bin/php','artisan','migrate','--env=testing','--force'],
    ['bin/php','artisan','merlin:create-local-admin'],
):
    subprocess.run(command,check=True)
