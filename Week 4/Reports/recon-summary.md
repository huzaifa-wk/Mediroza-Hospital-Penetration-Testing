# Mediroza General Hospital
## Reconnaissance Summary

**Target:** https://medirozahospital.com/
**Assessment Date:** 26 November 2026
**Assessment Type:** Black-box Web Security Assessment

### 1. DNS
- A record: 199.188.201.16
- Name servers and MX records documented.
- WHOIS information collected.

### 2. Web Server
- HTTP/2 homepage response: 200 OK
- Server identified as LiteSpeed.
- WhatWeb GET request returned 403 Forbidden.
- HEAD and GET responses returned 200 OK.

### 3. HTTP Security Headers
The captured homepage GET response did not contain:
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

These are observations requiring further assessment,
not confirmed vulnerabilities.

### 4. TLS
- TLS 1.2 connection successful.
- TLS 1.3 connection successful.
- Certificate verification returned code 0.
- Certificate validity dates recorded.

### 5. Security Disclosure
- /.well-known/security.txt returned HTTP 404.
- No security.txt file was found at that location.

### 6. Evidence Integrity
- 12 evidence files checked.
- All 12 SHA-256 checksums verified successfully.

### 7. Limitations
This reconnaissance does not establish successful
exploitation or access to restricted information.
No confidential patient records were accessed or retained.
