# Mediroza General Hospital — Findings Register

## Assessment Information

- Target: https://medirozahospital.com/
- Assessment type: Black-box security assessment
- Evidence collection date: 26 November 2026
- Testing approach: Limited, non-invasive reconnaissance

## Findings

### F-01: DNS Information Disclosure
- Category: Informational
- Status: Observed
- Evidence: `Recon/dns-a.txt`, `Recon/dns-ns.txt`, `Recon/dns-mx.txt`
- Observation: Public DNS records disclose the domain's IP address, nameservers, and mail-server configuration.
- Assessment: Normal public DNS functionality; no vulnerability established.

### F-02: Web Server Technology Identification
- Category: Informational
- Status: Observed
- Evidence: `Recon/whatweb.txt`
- Observation: WhatWeb identified LiteSpeed and HTML5. Its request received HTTP 403.
- Assessment: Technology fingerprinting alone does not establish a vulnerability.

### F-03: HTTP Security Header Observation
- Category: Informational
- Status: Observed
- Evidence: `Recon/http-headers.txt`, `Recon/http-headers-second.txt`
- Observation: Several commonly recommended security headers were absent from the captured homepage HEAD responses.
- Assessment: Requires further verification; no exploitable vulnerability established.

### F-04: TLS Certificate Inspection
- Category: Informational
- Status: Observed
- Evidence: `Recon/tls-certificate.txt`
- Observation: Certificate identifies medirozahospital.com and was issued by SSL.com TLS Issuing RSA CA R1. The displayed validity period includes the assessment date.
- Assessment: Certificate retrieved successfully. Full chain and configuration assessment not completed.

### F-05: TLS Protocol Support
- Category: Positive Security Observation
- Status: Verified
- Evidence: `Recon/tls-protocols.txt`
- Observation: TLS 1.2 and TLS 1.3 connections succeeded, and OpenSSL reported successful certificate verification.
- Assessment: Positive result for the tested protocol connections. Older protocol support and the complete TLS configuration remain unverified.

## Assessment Limitations

- Only limited, non-invasive reconnaissance was performed against the live domain.
- No authentication bypass or exploitation was attempted.
- No real patient records, employee salary information, or confidential shareholder information were accessed or collected.
- No denial-of-service, brute-force, or intrusive testing was performed.
- Further testing requires an explicitly approved staging environment and synthetic test data.

## Overall Preliminary Assessment

The collected evidence confirms publicly observable DNS information, web-server technology identification, HTTP response characteristics, and successful TLS 1.2 and TLS 1.3 connections.

No exploitable vulnerability has been confirmed by the tests documented in this register.

## Observation: Security Response Headers

**Target:** https://medirozahospital.com/

**HTTP Status:** 200 OK

**Evidence:** Recon/http-get-headers.txt

**SHA-256:**
225ca6b403e6402847d28aba68721b2b3e040e1774fc5f015a6f1f4ec9dfa0fc

**Observed:**
The captured homepage GET response did not include the following
security headers:

- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

**Assessment:** Informational observation; security impact has not
yet been established.

**Recommendation:** Review and configure appropriate HTTP security
headers after compatibility testing.

## Observation: security.txt Not Found

**Target:** https://medirozahospital.com/.well-known/security.txt

**HTTP Status:** 404 Not Found

**Evidence:** Recon/security-txt.txt

**SHA-256:**
b8c08d83a9f7e0e937dba5909d87d5f4ccc50c7a5b9a696f60851bcf4e7d9590

**Observation:**
The standard security.txt resource was not found at the requested
location. The server returned a LiteSpeed 404 response.

**Assessment:** Informational. This does not establish a vulnerability.

**Recommendation:** Publish a security.txt file containing an
appropriate security contact and vulnerability disclosure policy.

## Observation: Different Login Response Configurations

**Target:**
- /staff/login.php
- /patient/login.php

**Evidence:**
- Recon/staff-login-headers-redacted.txt
- Recon/patient-login-headers-redacted.txt

**SHA-256 — Staff:**
ef3dee8af6acb37f0b32955daef69098674d171b3029a67cdc0a2ae97458d984

**SHA-256 — Patient:**
217e8227086a27274f771b2e5e6bc82e81f43ecd4c5bff667d3aae6206041c4f

**Observation:**
Both login pages returned HTTP 200 and disclosed PHP 8.2.36.
The patient login response issued a PHPSESSID cookie and
included no-cache directives. The staff response did not
show a PHPSESSID cookie in the captured response.

**Assessment:**
Informational difference. Security impact is not established.

**Recommendation:**
Review session initialization, cookie attributes and
cache-control policies across both portals.
