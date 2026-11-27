# Mediroza General Hospital – Penetration Testing Project

**NetworkWalks Cybersecurity Internship | Week 4**

## Project Overview

This repository contains the work completed during Week 4 of the NetworkWalks Cybersecurity Internship. The project focuses on black-box reconnaissance and non-invasive security assessment of the Mediroza General Hospital website.

**Target Website:** https://medirozahospital.com

## Objectives

- Perform website reconnaissance and footprinting.
- Identify publicly observable website technologies.
- Inspect HTTP responses and security headers.
- Review publicly accessible login page structures.
- Examine TLS certificate information and supported protocols.
- Collect and document assessment evidence.
- Prepare a technical penetration testing report.

## Tools Used

- Kali Linux
- WhatWeb
- cURL
- OpenSSL
- DNS lookup utilities
- WHOIS
- SHA256SUMS

## Assessment Activities

### 1. Website Technology Fingerprinting
Identified publicly observable web server and technology information using WhatWeb.

### 2. HTTP Response Inspection
Examined HTTP response headers and compared GET and HEAD responses.

### 3. DNS and Domain Reconnaissance
Collected publicly available DNS and domain registration information.

### 4. TLS Certificate Inspection
Reviewed the website's TLS certificate, validity period, and certificate issuer.

### 5. TLS Protocol Assessment
Observed support for TLS 1.2 and TLS 1.3.

### 6. Public Login Page Inspection
Inspected publicly accessible staff and patient login pages and documented visible form structures and response headers.

### 7. Evidence Integrity
Generated SHA-256 checksums for collected evidence files.

## Repository Structure

```text
Week4-Mediroza/
├── Evidence/
├── Local-Lab/
│   └── SQLi/
├── Recon/
├── Reports/
│   ├── Final-Penetration-Testing-Report.md
│   ├── findings-register.md
│   └── recon-summary.md
└── README.md
```

## Key Observations

- The website responded with different HTTP status codes during different reconnaissance requests.
- LiteSpeed server information was observed.
- Some commonly reviewed security headers were not present in the captured responses.
- The website's TLS certificate was valid during the assessment period.
- TLS 1.2 and TLS 1.3 were successfully negotiated.
- The public security.txt request returned HTTP 404.

These observations are informational and should not automatically be interpreted as confirmed vulnerabilities.

## Scope and Limitations

This report documents reconnaissance and non-invasive security observations. Authenticated exploitation, successful SQL injection, unauthorized access, and retrieval of confidential patient or staff information were not established or completed.

Testing was limited to the authorized project scope.

## Conclusion

The Week 4 project provided practical experience in web reconnaissance, footprinting, HTTP inspection, DNS enumeration, TLS analysis, evidence collection, and professional security reporting.

**Prepared by:** Huzaifa Waheed Khan  
**Program:** NetworkWalks Cybersecurity Internship  
**Submission Date:** 27 November 2026
