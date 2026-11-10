# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: tornado/test/security_corpus_test.py line 92

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
