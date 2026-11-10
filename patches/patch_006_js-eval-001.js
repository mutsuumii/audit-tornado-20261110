# Code injection via eval()
# CWE-95 | Severity: CRITICAL
# File: demos/chat/static/chat.js line 58

**Risk:** eval() with dynamic input runs arbitrary JavaScript.

**Fix:** Use JSON.parse() for data. Pass function references, not strings, to setTimeout.
