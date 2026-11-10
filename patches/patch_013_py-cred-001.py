# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: demos/google_auth/main.py line 105

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
