#!/usr/bin/env python3
"""Create missing local secrets/config only; never replace existing credentials."""
import base64, os, secrets
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
local=Path('.local'); local.mkdir(mode=0o700,exist_ok=True)
for name in ('mysql-root','dev-password','test-password','admin-password'):
    f=local/name
    if not f.exists(): f.write_text(secrets.token_hex(24)+'\n'); f.chmod(0o600)
# MySQL runs as uid 999. The parent directory remains private on the host.
(local/'mysql-root').chmod(0o644)
password=lambda name:(local/name).read_text().strip()
sql=local/'mysql-init.sql'
if not sql.exists():
    sql.write_text("CREATE DATABASE merlin_nova_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;\nCREATE DATABASE merlin_nova_test CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;\n"+
        ''.join(f"CREATE USER 'merlin_{kind}'@'%' IDENTIFIED BY '{password(kind+'-password')}';\nGRANT ALL PRIVILEGES ON merlin_nova_{kind}.* TO 'merlin_{kind}'@'%';\n" for kind in ('dev','test')))
sql.chmod(0o644)
for filename,kind in (('.env','dev'),('.env.testing','test')):
    f=Path(filename)
    if f.exists(): continue
    key=base64.b64encode(secrets.token_bytes(32)).decode()
    f.write_text(f'''APP_NAME="Merlin Nova"
APP_ENV={'local' if kind=='dev' else 'testing'}
APP_KEY=base64:{key}
APP_DEBUG=true
APP_URL=http://127.0.0.1:8000
APP_LOCALE=de
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=merlin_nova_{kind}
DB_USERNAME=merlin_{kind}
DB_PASSWORD={password(kind+'-password')}
SESSION_DRIVER={'database' if kind=='dev' else 'array'}
CACHE_STORE={'database' if kind=='dev' else 'array'}
QUEUE_CONNECTION=sync
MAIL_MAILER=log
LOCAL_ADMIN_EMAIL=admin@merlin.invalid
BCRYPT_ROUNDS={12 if kind=='dev' else 4}
''');f.chmod(0o600)
print('Local configuration exists; no existing credentials replaced.')
