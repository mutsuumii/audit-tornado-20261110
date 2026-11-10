# Security audit: tornadoweb/tornado

Date: 2026-11-10 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 13 issue(s): 5 critical, 8 high.

## Findings

### 1. [HIGH] Path traversal via unsanitized input

**CWE-22** | `tornado/autoreload.py` line 233

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
subprocess.Popen([sys.executable] + argv)
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 2. [HIGH] Hardcoded credentials

**CWE-798** | `demos/facebook/facebook.py` line 36

Credentials hardcoded in source. Anyone with repo access can extract them.

```
cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 3. [HIGH] Hardcoded credentials

**CWE-798** | `tornado/test/security_corpus_test.py` line 92

Credentials hardcoded in source. Anyone with repo access can extract them.

```
COOKIE_SECRET = "secret"
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 4. [CRITICAL] Insecure deserialization

**CWE-502** | `tornado/test/httputil_test.py` line 567

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
unpickled = pickle.loads(pickled)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 5. [CRITICAL] Insecure deserialization

**CWE-502** | `tornado/test/simple_httpclient_test.py` line 1222

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
e2 = pickle.loads(pickle.dumps(e))
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 6. [CRITICAL] Code injection via eval()

**CWE-95** | `demos/chat/static/chat.js` line 58

eval() with dynamic input runs arbitrary JavaScript.

```
if (callback) callback(eval("(" + response + ")"));
```

**Fix:** Use JSON.parse() for data. Pass function references, not strings, to setTimeout.
---

### 7. [CRITICAL] Code injection via eval()

**CWE-95** | `demos/chat/static/chat.js` line 102

eval() with dynamic input runs arbitrary JavaScript.

```
updater.newMessages(eval("(" + response + ")"));
```

**Fix:** Use JSON.parse() for data. Pass function references, not strings, to setTimeout.
---

### 8. [HIGH] Path traversal via unsanitized input

**CWE-22** | `tornado/test/web_test.py` line 2507

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
with open(self.public + ":secret", "wb") as f:
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 9. [CRITICAL] Insecure deserialization

**CWE-502** | `tornado/test/web_test.py` line 4823

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
e2 = pickle.loads(pickle.dumps(e))
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 10. [HIGH] Hardcoded credentials

**CWE-798** | `tornado/test/web_test.py` line 117

Credentials hardcoded in source. Anyone with repo access can extract them.

```
def __init__(self, cookie_secret="0123456789", key_version=None):
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 11. [HIGH] Hardcoded credentials

**CWE-798** | `tornado/test/web_test.py` line 864

Credentials hardcoded in source. Anyone with repo access can extract them.

```
COOKIE_SECRET = "WebTest.COOKIE_SECRET"
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 12. [HIGH] Hardcoded credentials

**CWE-798** | `tornado/test/web_test.py` line 4113

Credentials hardcoded in source. Anyone with repo access can extract them.

```
headers=self.cookie_headers(token="deadbeef"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 13. [HIGH] Hardcoded credentials

**CWE-798** | `demos/google_auth/main.py` line 105

Credentials hardcoded in source. Anyone with repo access can extract them.

```
cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---
