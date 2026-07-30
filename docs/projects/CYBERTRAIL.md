# CyberTrail — Cybersecurity Portfolio Project

## Project status

**Technical Review Build v0.1**

CyberTrail is currently in private technical review. The workbook has been packaged, documented, committed to its own private GitHub repository, and shared with a cybersecurity professional for feedback.

The next planned milestone is a focused **v0.2 beta**, not a public launch.

## The problem

Small organizations often need to track security work before they are ready for a full governance, risk, and compliance platform.

Security information may be scattered across email, notes, tickets, folders, and individual memory. That makes it difficult to answer practical questions such as:

- Which security controls have owners?
- What evidence supports each control?
- Which evidence is outdated?
- Which vulnerabilities remain unresolved?
- When were access reviews completed?
- Which vendors still need review?
- What incidents occurred and how were they handled?
- What should management see in a monthly summary?

## The solution

CyberTrail is a spreadsheet-based security evidence and activity tracker intended to provide one structured operational view.

The v0.1 workbook contains 12 tabs, including:

- Start Here
- Dashboard
- Control Register
- Evidence Log
- Security Activity
- Access Reviews
- Vulnerability Tracker
- Vendor Register
- Incident Log
- Monthly Summary
- Reference Data
- Formula Tests

## Intended users

The current leading target for v0.2 is:

**Independent IT providers and small managed service providers.**

Other possible users include small-business operators, internal IT generalists, security consultants, and vCISOs. The v0.2 process will select one primary workflow rather than trying to serve every audience equally.

## Security and product boundaries

CyberTrail is not intended to store sensitive evidence directly.

The workbook should not contain:

- Passwords
- Authentication tokens
- Private keys
- Regulated personal information
- Sensitive raw logs
- Confidential forensic evidence

Sensitive artifacts should remain in an approved secure repository. CyberTrail should record only the description, owner, date, status, and secure reference.

CyberTrail is also not presented as:

- A SIEM
- A vulnerability scanner
- A ticketing system
- A password manager
- A formal audit
- A compliance certification
- An enterprise GRC platform

## Validation completed for v0.1

- Reviewed the workbook structure and formulas
- Found no obvious spreadsheet errors during packaging
- Confirmed all seven built-in formula tests pass
- Confirmed the demonstration organization and data are fictional
- Found no obvious credentials, API keys, or real customer data
- Created a technical-review guide
- Added screenshots and product documentation
- Created a clean private GitHub repository
- Created a structured v0.2 feedback roadmap

## What I learned

This project moved beyond writing code exercises and required product-level thinking.

Key lessons included:

- A security tool must define what data should **not** be stored
- Management dashboards can create false confidence if metrics are poorly defined
- Controls, evidence, activities, findings, vulnerabilities, and incidents are related but not interchangeable
- Manual-entry products must explain that their accuracy depends on accurate input
- A product should solve one primary user workflow before expanding its audience
- Documentation, screenshots, file organization, versioning, and external review are part of the product
- Finishing, packaging, and presenting a project are different skills from initially building it

## v0.2 roadmap

The next version will be driven by external cybersecurity feedback.

Planned priorities include:

1. Select one primary target user
2. Review dashboard metrics for misleading signals
3. Improve definitions for control and evidence statuses
4. Test overdue and upcoming date behavior
5. Review access, vulnerability, vendor, and incident workflows
6. Make the Start Here tab understandable within five minutes
7. Add a first-use checklist
8. Add a realistic fictional walkthrough
9. Remove unnecessary fields before adding new ones
10. Update screenshots, documentation, and formula tests

## Portfolio significance

CyberTrail is my first substantial cybersecurity product project.

It connects several areas of my learning:

- Security operations
- Evidence management
- Vulnerability remediation
- Access governance
- Incident documentation
- Vendor risk
- Management reporting
- Secure data handling
- Git and GitHub workflows
- Product validation and external review

The goal is not to claim that the product is finished. The goal is to document the process of turning cybersecurity knowledge into a useful, responsibly scoped tool.
