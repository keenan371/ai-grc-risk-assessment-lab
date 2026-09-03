# System Description and Assessment Scope

## Fictional scenario

**Northstar Retail Services** is a fictional organization. **AssistDesk** is a fictional internal AI customer-support assistant. This lab uses invented architecture, synthetic examples, and documented assumptions only. It does not assess a real client, production deployment, or live model.

## System description

AssistDesk is a retrieval-augmented chat assistant proposed for internal support agents. It summarizes internal knowledge-base articles, drafts suggested replies, and routes unresolved questions to a human agent. The assistant is not authorized to send messages, change orders, issue refunds, make employment decisions, or make binding decisions. Human agents remain responsible for every customer-facing response.

### Assumed components

| Component | Assumed role | Data boundary |
|---|---|---|
| Agent web interface | Accepts an internal support-agent prompt and displays a draft | Internal access only |
| Orchestration service | Applies prompt templates, retrieval rules, and output handling | Receives prompt and retrieved excerpts |
| Approved knowledge base | Provides curated support articles | No customer records intended |
| Hosted language model API | Produces the draft response | Contractual and technical data-handling terms are not evidenced in this lab |
| Human agent | Reviews, edits, approves, or rejects the draft | Final decision authority |
| Logging service | Records minimal operational events for investigation | Retention and access controls are assessed as gaps unless evidenced |

## Assessment objective

Identify and prioritize foreseeable AI governance, privacy, security, reliability, fairness, transparency, and operational risks before a hypothetical pilot. The assessment uses a qualitative 1-5 likelihood and impact scale and maps recommendations to NIST AI RMF 1.0 functions.[1]

## In scope

- The proposed internal-assistant use case and data flows
- Retrieval content governance and prompt-input handling
- Human oversight, monitoring, incident response, and change management
- A qualitative risk register and prioritized remediation roadmap

## Out of scope

- Penetration testing, vulnerability scanning, source-code review, and model red teaming
- Legal advice, regulatory compliance determination, or vendor due diligence
- Production telemetry, live customer data, real user testing, and performance claims
- Any implementation or validation of the recommendations

## Assumptions and limitations

This is a desk-based portfolio lab. Control status is based only on the fictional scenario and the artifacts in this repository. “Gap” and “proposed control” mean a control is not evidenced, not that it is absent in a real environment. Ratings are illustrative priorities, not measured probabilities or compliance conclusions.

## Rating method

- **Likelihood:** 1 Rare, 2 Unlikely, 3 Possible, 4 Likely, 5 Almost certain
- **Impact:** 1 Negligible, 2 Minor, 3 Moderate, 4 Major, 5 Severe
- **Inherent rating:** likelihood × impact
- **Priority bands:** 15-25 Critical, 10-14 High, 5-9 Moderate, 1-4 Low

## Source

[1] NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (January 2023), https://doi.org/10.6028/NIST.AI.100-1. The framework organizes AI risk-management activities into Govern, Map, Measure, and Manage functions.
