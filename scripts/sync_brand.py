#!/usr/bin/env python3
"""Vendor the reviewed brand snapshot into independently installable media skills."""
import argparse
import hashlib
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skills/consulting-tasteful-design/brand'
CONSUMERS = ('consulting-graphics', 'consulting-generative-post', 'consulting-article-illustrator',
             'consulting-higgsfield', 'consulting-proposal-designer', 'consulting-hyperframes-video')

def inventory(folder):
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = inventory(SOURCE)
    stale = []
    for name in CONSUMERS:
        target = ROOT / 'skills' / name / 'brand'
        if args.check:
            if inventory(target) != expected:
                stale.append(name)
        else:
            # Only this generated directory is owned by the synchronizer.
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(SOURCE, target)
    if stale:
        raise SystemExit('Brand copies drifted: ' + ', '.join(stale))
    print(f'{len(CONSUMERS)} brand copies ' + ('match the canonical package' if args.check else 'updated'))

if __name__ == '__main__':
    main()
