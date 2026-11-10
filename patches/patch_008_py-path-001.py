# Path traversal via unsanitized input
# CWE-22 | Severity: HIGH
# File: tornado/test/web_test.py line 2507

**Risk:** File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
