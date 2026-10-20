#!/usr/bin/env python3
"""Run Composer in the PHP runtime; retain cache and use existing proxy CA."""
import os, subprocess, sys
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
args=['docker','run','--rm','--network','host','--user',f'{os.getuid()}:{os.getgid()}',
      '-e','COMPOSER_HOME=/app/.local/composer','-v',f'{Path.cwd()}:/app','-w','/app']
for name in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','NO_PROXY','no_proxy'):
    if os.environ.get(name):args+=['-e',name]
cert=os.environ.get('SSL_CERT_FILE') or os.environ.get('CODEX_PROXY_CERT')
if cert and Path(cert).is_file():args+=['-e','COMPOSER_CAFILE=/tmp/cloud-ca.pem','-v',f'{cert}:/tmp/cloud-ca.pem:ro']
args+=['merlin-nova-php:local','composer',*sys.argv[1:]]
raise SystemExit(subprocess.run(args).returncode)
