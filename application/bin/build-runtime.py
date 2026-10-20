#!/usr/bin/env python3
"""Build the local PHP image with the existing proxy/trust configuration."""
import os, socket, subprocess
from pathlib import Path
from urllib.parse import urlparse
os.chdir(Path(__file__).resolve().parents[1])
env=os.environ.copy()
if not env.get('DOCKER_CONFIG'):
    path=Path('.local/docker-config').resolve();path.mkdir(parents=True,exist_ok=True)
    env['DOCKER_CONFIG']=str(path)
args=['docker','build','--network=host']
seen=set()
for name in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','NO_PROXY','no_proxy'):
    if env.get(name):
        args+=['--build-arg',name]
        if name.lower()!='no_proxy':
            host=urlparse(env[name]).hostname
            if host and host not in seen:
                seen.add(host)
                args+=['--add-host',f'{host}:{socket.gethostbyname(host)}']
cert=env.get('SSL_CERT_FILE') or env.get('CODEX_PROXY_CERT')
if cert and Path(cert).is_file():args+=['--secret',f'id=proxy_ca,src={cert}']
args+=['-t','merlin-nova-php:local','docker/php']
subprocess.run(args,env=env,check=True)
