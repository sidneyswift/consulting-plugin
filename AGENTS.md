# Consulting skill authoring

This repository is public. Review every branch before pushing it: the coordinator's later review
protects Recoup Skills publication, but cannot make an already-pushed source file private.

Author reusable capabilities in `skills/<name>/SKILL.md`; use `consulting-<short-name>` for new skills.
Keep skill code and examples suitable for public reuse: synthetic companies, no credentials, private
client examples, personal machine paths, or private business records. Keep support files inside the
skill directory. Use backtick resource paths. Read the existing skill and preserve its runtime contract.

The private workspace coordinator reviews changes merged to main before publishing them as
`recoup-internal-consulting-<short-name>` in Recoup Skills. It imports edits from that namespace back
here, preserving the source skill names. New skills get public routing fixtures and version updates. Publishing
a plugin commit locally does not update the parent repository; the coordinator updates Consulting's
plugin reference after this main advances. Polling is every five minutes, subject to GitHub delays.

Run `python3 scripts/validate_plugin.py`, `node --test tests/brand.test.mjs tests/runtime.test.mjs`, and
`python3 -m unittest discover -s tests -p 'test_*.py'` before publication. Sync proposals pass these
checks before a trusted-main receiver verifies their signature and merges their PR. Incompatible edits
or failed privacy/validation checks remain pending; do not force them over the other copy.
