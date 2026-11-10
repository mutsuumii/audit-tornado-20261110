# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: tornado/test/web_test.py line 864

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
