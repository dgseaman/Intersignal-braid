"""Pinned offline pack verification. No network access in this module."""
from __future__ import annotations
import hashlib
import json
import platform
import re
import sysconfig
import sys
from pathlib import Path


def target():
    return {'system':platform.system(),'machine':platform.machine().lower(),
            'python':'.'.join(map(str,sys.version_info[:2])),'implementation':platform.python_implementation(),'free_threaded':bool(sysconfig.get_config_var('Py_GIL_DISABLED'))}


def verify_pack(root: Path, expected_spec: Path | None = None):
    root=Path(root)
    meta=json.loads((root/'wheelhouse-manifest.json').read_text('utf-8'))
    if meta.get('schema')!='braid.offline-pack.v1' or meta.get('target')!=target():
        raise ValueError('Offline pack target does not match this OS/architecture/Python. Build a matching pack on a connected equivalent rig.')
    if expected_spec is not None and meta.get('dependency_spec_sha256') != hashlib.sha256(Path(expected_spec).read_bytes()).hexdigest():
        raise ValueError('Offline pack was made for a different dependency specification.')
    if not meta.get('files') or 'requirements.lock' not in meta['files']:
        raise ValueError('Incomplete offline pack.')
    for name,digest in meta['files'].items():
        if Path(name).name!=name or (root/name).is_symlink(): raise ValueError('Unsafe offline pack member.')
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise ValueError('Offline pack hash mismatch: '+name)
    wheels={p.name for p in root.glob('*.whl')}
    if wheels!={n for n in meta['files'] if n.endswith('.whl')}: raise ValueError('Unmanifested or missing offline wheel.')
    text=(root/'requirements.lock').read_text()
    if any(line.strip() and not re.fullmatch(r'[a-z0-9-]+==[a-zA-Z0-9.+!-]+ --hash=sha256:[0-9a-f]{64}',line) for line in text.splitlines()):
        raise ValueError('Offline requirements must be pinned hash-checked packages, not directives.')
    return meta
