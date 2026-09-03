# NIST AI RMF 1.0 Mapping

This illustrative mapping uses NIST AI RMF 1.0 as a voluntary risk-management framework. NIST identifies Govern, Map, Measure, and Manage as its Core functions, with Govern designed as a cross-cutting function.[1] This document is a proposed profile for the fictional AssistDesk scenario, not a certification or compliance assessment.

| Function | Assessment activity | Illustrative outcome | Supporting artifact | State |
|---|---|---|---|---|
| Govern | Name accountable owners, risk tolerance, and lifecycle decisions | Governance roles and decision rights are documented | `01_SYSTEM_SCOPE.md`, `02_RISK_REGISTER.csv` | Gap documented |
| Govern | Establish data, security, change, and incident policies for the use case | Policy baseline and escalation path are defined | `04_CONTROL_GAP_ANALYSIS.md` | Proposed |
| Map | Define intended use, prohibited use, actors, data, and impact pathways | Context and affected parties are understood | `01_SYSTEM_SCOPE.md` | Documented assumption |
| Map | Identify foreseeable harms including privacy, inaccurate drafts, and access failures | Risk scenarios are cataloged and prioritized | `02_RISK_REGISTER.csv` | Documented |
| Measure | Build scenario-based evaluation, adversarial tests, and quality metrics | Risk is evaluated against agreed thresholds | `04_CONTROL_GAP_ANALYSIS.md`, `05_REMEDIATION_PLAN.md` | Proposed |
| Measure | Monitor source freshness, approval behavior, overrides, and incidents | Monitoring metrics and review cadence are defined | `05_REMEDIATION_PLAN.md` | Proposed |
| Manage | Treat critical risks before pilot with accountable owners and dates | Critical risks have remediation actions | `02_RISK_REGISTER.csv`, `05_REMEDIATION_PLAN.md` | Planned |
| Manage | Define pause, rollback, escalation, and post-incident actions | Harmful behavior can be contained and learned from | `04_CONTROL_GAP_ANALYSIS.md` | Proposed |

## Traceability by risk

| Risk IDs | Primary RMF function(s) | Rationale |
|---|---|---|
| R-01, R-04, R-08 | Govern, Map, Manage | Establish data and access accountability, map flows, enforce handling and logging controls |
| R-02, R-05, R-06 | Map, Measure, Manage | Characterize output harms, test against scenarios, then enforce release criteria and escalation |
| R-03, R-09, R-10 | Govern, Measure, Manage | Set secure-development expectations, validate changes and adversarial behavior, respond to incidents |
| R-07 | Govern, Map | Define user expectations, limitations, and appropriate human use |

## Source

[1] NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (January 2023), https://doi.org/10.6028/NIST.AI.100-1.
