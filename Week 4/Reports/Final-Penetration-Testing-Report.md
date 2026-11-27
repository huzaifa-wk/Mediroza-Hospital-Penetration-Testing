# PENETRATION TESTING REPORT

## Mediroza General Hospital

**Target:** https://medirozahospital.com/

**Assessment Type:** Black-Box Security Assessment

**Assessment Period:** 22–26 November 2026

**Prepared By:** [Your Name]

**Organization / Internship:** NetworkWalks — Batch B083

**Report Date:** 26 November 2026

**Classification:** Confidential — Internship Assessment

---

# 1. Executive Summary

A preliminary black-box security assessment was conducted against the publicly accessible domain of Mediroza General Hospital.

The assessment focused on non-invasive reconnaissance, DNS information gathering, web-server technology identification, HTTP response-header inspection, TLS certificate inspection, and TLS protocol support.

The assessment identified publicly available infrastructure information, LiteSpeed web-server identification, and several security-header configuration observations requiring further verification.

The server successfully established TLS 1.2 and TLS 1.3 connections during testing, and OpenSSL reported successful certificate verification for both.

No exploitable vulnerability was confirmed through the activities documented in this report.

The assessment was limited to non-invasive checks. Authentication bypass, exploitation, access to confidential patient records, employee salary information, and shareholder information were not attempted.

## Overall Assessment

The collected evidence provides an initial view of the target's publicly observable security configuration. A complete security assessment would require additional authorized testing in a controlled staging environment using synthetic data.

---

# 2. Scope and Objectives

## 2.1 Target

The assessment target was:

- Domain: medirozahospital.com
- HTTPS URL: https://medirozahospital.com/
- Resolved IPv4 address: 199.188.201.16

Testing was restricted to the specified target domain.

## 2.2 Objectives

The assessment objectives included:

1. Gather publicly available DNS information.
2. Identify publicly observable web technologies.
3. Inspect HTTP response headers.
4. Review the TLS certificate information.
5. Verify TLS 1.2 and TLS 1.3 connection support.
6. Document observations and potential security improvements.
7. Maintain evidence integrity and prepare a professional security report.

## 2.3 Testing Limitations

The following activities were not performed:

- Unauthorized access or authentication bypass.
- Brute-force attacks.
- Denial-of-service testing.
- Exploitation of the live hospital website.
- Retrieval or disclosure of real patient reports.
- Access to employee salary or confidential shareholder information.
- Testing outside the authorized target scope.

Additional testing of sensitive functionality requires explicit authorization and a controlled environment containing synthetic test data.

---

# 3. Methodology

The assessment followed a structured reconnaissance and configuration-review methodology.

## Phase 1: DNS Reconnaissance

DNS records were inspected to identify the target's publicly available network information.

Tools:
- dig
- whois

Records reviewed:
- A record
- NS records
- MX records
- WHOIS information

## Phase 2: Web Technology Identification

WhatWeb was used with low aggression settings to identify publicly observable website technologies.

The tool identified LiteSpeed and HTML5. Its request received an HTTP 403 response.

## Phase 3: HTTP Header Inspection

Curl was used to issue two HTTP HEAD requests to the target homepage.

Both recorded responses returned HTTP/2 200 and displayed consistent headers.

## Phase 4: TLS Certificate Inspection

OpenSSL was used to retrieve the TLS certificate's subject, issuer, and validity dates.

## Phase 5: TLS Protocol Verification

OpenSSL connection tests were conducted separately for TLS 1.2 and TLS 1.3.

Both connections succeeded, and certificate verification returned a successful result.

---

# 4. Findings and Evidence

## F-01: Public DNS Information

**Category:** Informational  
**Risk Rating:** Informational  
**Status:** Observed

The DNS inspection identified the following publicly available information:

- IPv4 address: 199.188.201.16
- Nameservers: dns1.namecheaphosting.com and dns2.namecheaphosting.com
- Mail servers: mx1-hosting.jellyfish.systems, mx2-hosting.jellyfish.systems, and mx3-hosting.jellyfish.systems

**Evidence:**
- Recon/dns-a.txt
- Recon/dns-ns.txt
- Recon/dns-mx.txt
- Recon/whois.txt

**Assessment:**

These records represent normal public DNS functionality. Their disclosure alone does not establish a security vulnerability.

**Recommendation:**

Review DNS records periodically and remove outdated or unnecessary records.

---

## F-02: Web Server Technology Identification

**Category:** Information Disclosure Observation  
**Risk Rating:** Informational  
**Status:** Observed

WhatWeb identified:

- Web server: LiteSpeed
- Technology: HTML5
- IP address: 199.188.201.16

The WhatWeb request received an HTTP 403 Forbidden response.

**Evidence:**
- Recon/whatweb.txt

**Assessment:**

Technology fingerprinting provides information about the website's infrastructure. The identification of LiteSpeed does not independently establish a vulnerability.

**Recommendation:**

Review server configuration and minimize unnecessary technology information disclosure where practical.

---

## F-03: HTTP Security Header Observation

**Category:** Security Configuration Observation  
**Risk Rating:** Informational — Requires Further Verification  
**Status:** Observed

Two consecutive HTTP HEAD requests returned identical responses.

The following headers were observed:

- HTTP/2 200
- Content-Type: text/html
- Server: LiteSpeed
- Content-Length: 5445
- Last-Modified: Fri, 04 Sep 2026

The following commonly recommended security headers were not present in the captured responses:

- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

**Evidence:**
- Recon/http-headers.txt
- Recon/http-headers-second.txt

**Assessment:**

The absence of these headers in the captured homepage responses is a configuration-hardening observation. Further verification across relevant application responses is necessary before determining whether an actual security weakness exists.

**Recommendation:**

Review and implement appropriate security headers, including HSTS, CSP, X-Content-Type-Options, and suitable framing and referrer policies.

---

## F-04: TLS Certificate Inspection

**Category:** Security Configuration Observation  
**Risk Rating:** Informational  
**Status:** Observed

The TLS certificate presented by the target contained:

- Subject: CN=medirozahospital.com
- Issuer: SSL.com TLS Issuing RSA CA R1
- Valid From: 14 August 2026
- Expiry Date: 28 February 2027

**Evidence:**
- Recon/tls-certificate.txt

**Assessment:**

The certificate was successfully retrieved. Its displayed validity period includes the assessment date.

This inspection does not independently establish the complete certificate-chain validity or overall TLS security.

**Recommendation:**

Monitor certificate expiration and periodically review certificate-chain validation and TLS configuration.

---

## F-05: TLS Protocol Support

**Category:** Positive Security Observation  
**Risk Rating:** No vulnerability established  
**Status:** Verified

Two TLS connection tests were conducted.

TLS 1.2:
- Protocol: TLS 1.2
- Cipher: ECDHE-RSA-CHACHA20-POLY1305
- Certificate verification: 0 (ok)

TLS 1.3:
- Protocol: TLS 1.3
- Cipher: TLS_AES_256_GCM_SHA384
- Certificate verification: 0 (ok)

**Evidence:**
- Recon/tls-protocols.txt

**Assessment:**

The server successfully negotiated both tested protocol versions. These results are positive observations but do not establish that obsolete protocols are disabled or that the entire TLS configuration is secure.

**Recommendation:**

Maintain support for TLS 1.2 and TLS 1.3, review cipher-suite configuration, and disable obsolete protocols where applicable.

---

# 5. Risk Rating Summary

| Finding | Risk Rating |
|---|---|
| F-01: DNS Information | Informational |
| F-02: Technology Identification | Informational |
| F-03: HTTP Header Observation | Informational / Further Verification |
| F-04: TLS Certificate | Informational |
| F-05: TLS Protocol Support | Positive Observation |

**Confirmed exploitable vulnerabilities:** None established by the tests documented in this report.

---

# 6. Recommendations and Remediation

The following improvements are recommended:

1. Periodically review public DNS records.
2. Review web-server configuration and unnecessary technology disclosures.
3. Implement and validate appropriate HTTP security headers.
4. Monitor TLS certificate expiration.
5. Maintain secure TLS protocol and cipher-suite configurations.
6. Conduct periodic authorized security assessments.
7. Perform deeper application testing in an approved staging environment using synthetic patient and employee records.
8. Maintain centralized security logging and monitor suspicious access attempts.

---

# 7. Conclusion

The preliminary assessment successfully collected publicly observable DNS, HTTP, web technology, and TLS configuration information.

The target accepted TLS 1.2 and TLS 1.3 connections, and certificate verification succeeded during both tests.

The captured HTTP responses also revealed opportunities for further security-header configuration review.

No exploitable vulnerability or unauthorized access was demonstrated through the activities performed.

Further application-level testing should only proceed within an explicitly approved scope and a controlled environment that does not expose real patient or employee information.

---

# 8. Evidence Directory

The following evidence files were collected during the assessment:

**Recon/**
- dns-a.txt
- dns-ns.txt
- dns-mx.txt
- whois.txt
- whatweb.txt
- http-headers.txt
- http-headers-second.txt
- tls-certificate.txt
- tls-protocols.txt

**Evidence/**
- recon-checksums.txt

**Reports/**
- findings-register.md

---

**End of Report**

Prepared for NetworkWalks Batch B083 Internship Assessment.
