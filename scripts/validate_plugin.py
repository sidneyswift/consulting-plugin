#!/usr/bin/env python3
"""Offline structural and syntax validation; no provider calls or dependency installation."""
import ast
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'node_modules', '.git', '.venv', '__pycache__'}


def main():
    errors = []
    files = [p for p in ROOT.rglob('*') if p.is_file() and not SKIP.intersection(p.relative_to(ROOT).parts)]
    skills = [p for p in files if p.name == 'SKILL.md']
    names = set()
    for path in skills:
        text = path.read_text()
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        if not match:
            errors.append(f'{path.relative_to(ROOT)}: missing frontmatter'); continue
        name = re.search(r'^name:\s*[\'"]?([a-z0-9-]+)', match[1], re.M)
        if not name or name[1] != path.parent.name or name[1] in names:
            errors.append(f'{path.relative_to(ROOT)}: invalid or duplicate skill name')
        else:
            names.add(name[1])
        if not re.search(r'^description:\s*\S', match[1], re.M):
            errors.append(f'{path.relative_to(ROOT)}: missing description')
    brand_check = subprocess.run([sys.executable, str(ROOT / 'scripts/sync_brand.py'), '--check'],
                                 capture_output=True, text=True)
    if brand_check.returncode:
        errors.append(brand_check.stdout + brand_check.stderr)
    versions = set()
    for folder in ['.claude-plugin', '.cursor-plugin', '.codex-plugin']:
        doc = json.loads((ROOT / folder / 'plugin.json').read_text()); versions.add(doc['version'])
        if doc['name'] != 'consulting-os' or not (ROOT / doc['skills']).is_dir():
            errors.append(f'{folder}: invalid plugin name or skills root')
    for folder in ['.claude-plugin', '.cursor-plugin']:
        versions.add(json.loads((ROOT / folder / 'marketplace.json').read_text())['metadata']['version'])
    if len(versions) != 1:
        errors.append('Plugin and marketplace versions differ')
    for path in files:
        if path.suffix == '.py':
            try: ast.parse(path.read_text(), filename=str(path))
            except SyntaxError as exc: errors.append(f'{path.relative_to(ROOT)}: {exc}')
        if path.name == 'package.json':
            try: json.loads(path.read_text())
            except ValueError as exc: errors.append(f'{path.relative_to(ROOT)}: {exc}')
    commands = []
    for path in files:
        if path.suffix in {'.js', '.mjs', '.cjs'}:
            commands.append(('node', ['--check', str(path)], path))
        if path.suffix == '.sh':
            commands.append(('bash', ['-n', str(path)], path))
    def check(item):
        binary, args, path = item
        if not shutil.which(binary): return f'{binary} is required for syntax validation'
        result = subprocess.run([binary, *args], capture_output=True, text=True)
        return f'{path.relative_to(ROOT)}: {result.stderr.strip()}' if result.returncode else None
    with ThreadPoolExecutor(max_workers=4) as pool:
        errors.extend(e for e in pool.map(check, commands) if e)
    print(f'{len(skills)} skill entrypoints; manifest version {", ".join(sorted(versions))}; {len(commands)} JS/shell syntax checks')
    if errors:
        print('\n'.join(errors)); return 1
    print('Structural and syntax checks passed. Provider behavior and example privacy require separate review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
