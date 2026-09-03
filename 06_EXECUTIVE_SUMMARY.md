# Executive Risk Summary | One Page

## Decision context

**Fictional organization:** Northstar Retail Services  
**Fictional system:** AssistDesk, an internal AI customer-support drafting assistant  
**Assessment type:** Qualitative, desk-based pre-pilot assessment using synthetic scenario assumptions only.

## Overall risk posture: Conditional, not pilot-ready

The proposed system has useful operational potential, but the fictional scenario does not evidence the safeguards needed to manage its highest risks. Seven of ten documented risks are Critical. The most consequential risk themes are uncontrolled prompt data, confident inaccurate or stale drafts, compromised retrieval content, unauthorized retrieval access, ungoverned changes, and inadequate incident response.

This is not a finding about a real organization or a real implementation. It is an assessment conclusion for the fictional scenario only.

## Risk profile

| Priority | Count | Principal themes |
|---|---:|---|
| Critical | 7 | Privacy, reliability, retrieval security, access control, change management, incident response |
| High | 2 | Fairness, auditability |
| Moderate | 1 | User transparency |
| Low | 0 | None documented |
| Total | 10 | See `02_RISK_REGISTER.csv` |

## Top decision actions

1. Establish accountable ownership, intended and prohibited use, data classes, and risk acceptance authority.
2. Prevent unauthorized or unsafe retrieval through role-aware access, curated content, prompt-injection defenses, and adversarial testing.
3. Validate every release with synthetic evaluations, source-linked drafts, a human approval rubric, and rollback readiness.
4. Define minimum logging, an AI incident playbook, a pause mechanism, and tabletop-tested escalation.

## Recommended governance position

Do not advance the fictional system to a pilot until the Critical gaps G-01 through G-06 have documented design evidence and acceptance results. After controls are designed and tested, reassess residual risk, record the accountable decision, and monitor production-like behavior if a pilot is authorized.

## Boundary and evidence

No controls are represented as implemented. This summary is traceable to the scope, risk register, control-gap analysis, and remediation plan in this repository. The NIST AI RMF mapping is an illustrative alignment, not an attestation, certification, or legal opinion.
