# AI GRC Risk Assessment Lab

> **Fictional portfolio lab.** Northstar Retail Services and its AssistDesk internal AI customer-support assistant are invented for this assessment. The lab uses synthetic assumptions only. No real client data, production access, credentials, or implemented-control claims are included.

## Purpose

This repository demonstrates a structured, pre-pilot AI governance, risk, and compliance assessment for a fictional internal support-drafting assistant. It applies a qualitative risk method and maps assessment activities to NIST AI RMF 1.0 functions: Govern, Map, Measure, and Manage.[1]

## Deliverables

| Artifact | What it shows |
|---|---|
| [System description and scope](01_SYSTEM_SCOPE.md) | Fictional system boundary, assumptions, exclusions, and rating method |
| [AI risk register](02_RISK_REGISTER.csv) | 10 risks with likelihood, impact, rating, proposed controls, remediation, owner, and status |
| [NIST AI RMF mapping](03_NIST_AI_RMF_MAPPING.md) | Illustrative Govern, Map, Measure, and Manage alignment |
| [Control-gap analysis](04_CONTROL_GAP_ANALYSIS.md) | Eight gaps, proposed controls, evidence needed, and priority |
| [Prioritized remediation plan](05_REMEDIATION_PLAN.md) | Sequenced workstreams, exit evidence, and decision gates |
| [One-page executive summary](06_EXECUTIVE_SUMMARY.md) | Risk posture, priority counts, and decision actions |
| [Publishing kit](PUBLISHING_KIT.md) | Copy-ready GitHub and Upwork copy, skills, and screenshot sequence |
| [Portfolio QA](PORTFOLIO_QA.md) | Verification status, claim boundaries, and readiness decision |

## Methods

1. Defined the fictional system, actors, intended use, prohibited use, data boundary, and assessment limitations.
2. Identified foreseeable AI risk scenarios across privacy, reliability, security, fairness, transparency, accountability, change management, and resilience.
3. Rated inherent risk with a qualitative likelihood and impact scale from 1 to 5. Rating equals likelihood × impact.
4. Documented absent or unproven safeguards as gaps rather than presenting recommendations as implemented controls.
5. Mapped assessment actions to NIST AI RMF functions and sequenced remediation by criticality and dependency.
6. Ran a local deterministic verification script that validates required artifacts, risk-register schema, rating math, screenshot files, and unsupported-claim patterns.

## Key findings

- 10 fictional risk scenarios were documented: 7 Critical, 2 High, and 1 Moderate. No Low risks were documented.
- The fictional scenario is **conditionally positioned and not pilot-ready** until six Critical control gaps have documented design evidence and acceptance results.
- The highest priorities are data boundaries, grounded-output evaluation, retrieval security, role-aware access, controlled changes, and AI incident response.
- Recommendations in this repository are proposed only. They were not implemented or tested against a production system.

## Skills demonstrated

- AI governance and qualitative risk assessment
- NIST AI RMF profile mapping
- Control-gap analysis and risk treatment planning
- Data governance and privacy risk identification
- Retrieval-augmented AI security threat identification
- Human-oversight, monitoring, change-management, and incident-response design
- Executive risk communication and audit-ready documentation
- Evidence-based portfolio QA

## Evidence screenshots

| Screenshot | Evidence |
|---|---|
| [01 Executive Summary](evidence/01_executive_summary.png) | Fictional context, risk posture, risk profile, decision actions |
| [02 Risk Register](evidence/02_risk_register.png) | Risk ratings, owners, remediation, and Open status |
| [03 RMF, Gaps, and Plan](evidence/03_rmf_gap_remediation.png) | RMF function mapping, gaps, and remediation gates |
| [04 Verification Results](evidence/04_verification_results.png) | Local deterministic verification result |

## Verification

Run locally from the repository root:

```bash
python scripts/verify_assessment.py
```

Expected result:

```text
VERIFICATION PASSED: 4/4 required screenshot files; 10 risk records; 10/10 rating calculations valid.
```

The verifier is a documentation-quality check. It does not evaluate a live model, prove regulatory compliance, or validate any real implementation.

## Safe-use boundary

This lab is educational and portfolio-focused. It is not legal advice, a compliance certification, a production security assessment, or a substitute for organization-specific testing and counsel.

## Source

[1] NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (January 2023), https://doi.org/10.6028/NIST.AI.100-1. NIST describes the AI RMF Core through Govern, Map, Measure, and Manage functions.

## Publishing

This repository is prepared locally for Keenan to publish personally. See [PUBLISHING_KIT.md](PUBLISHING_KIT.md). No publishing action has been performed by Hermes.
