# Control-Gap Analysis

## Interpretation

A **gap** means the fictional scenario does not provide evidence of the control. It is not proof that a real organization lacks the control. Recommendations are design inputs only and have not been implemented or tested in this lab.

| Gap ID | Control domain | Observed assessment condition | Risk linkage | Gap | Proposed control | Evidence needed before pilot | Priority |
|---|---|---|---|---|---|---|---|
| G-01 | Data governance | No approved data classification or prompt-input policy is described | R-01 | Sensitive customer data could enter prompts without a defined boundary | Define permitted data classes, input warnings, sensitive-data detection, and escalation | Approved policy, configuration evidence, test cases | Critical |
| G-02 | Grounded output quality | No evaluation set, source citation requirement, or approval rubric is described | R-02, R-05 | Incorrect or stale drafts may appear credible | Require curated retrieval, source references, review checklist, and quality threshold | Evaluation report, source-freshness process, agent training record | Critical |
| G-03 | Retrieval security | No content trust boundary or injection testing is described | R-03 | Retrieved content may manipulate instructions or responses | Isolate instructions, sanitize retrieved content, review article changes, adversarially test | Threat model, test results, content workflow | Critical |
| G-04 | Identity and access | No role-aware retrieval filter is described | R-04 | Agents may see content outside their work need | Enforce least-privilege retrieval and access review | Access-control design, test evidence, audit sample | Critical |
| G-05 | AI change management | No model, prompt, or knowledge-base release gate is described | R-09 | Updates may silently degrade performance or safety | Version inventory, pre-release evaluation, approval gate, rollback plan | Change records, benchmark comparison, rollback exercise | Critical |
| G-06 | Incident response | No AI-specific incident classification, pause action, or ownership is described | R-10 | Harm may not be contained or investigated promptly | AI incident playbook, kill/pause path, tabletop exercise, review process | Approved playbook, tabletop output, escalation roster | Critical |
| G-07 | Fairness and UX | No representative scenario set or transparency training is described | R-06, R-07 | Uneven experience or improper reliance may go unnoticed | Test diverse scenarios, explain limitations, train agents to override and escalate | Test rubric, results, notice text, training evidence | High |
| G-08 | Auditability | No minimum event schema, retention rule, or reader authorization is described | R-08 | Investigations may lack reliable records or over-collect data | Define minimal logs, retention, access restrictions, and periodic review | Logging design, retention approval, access review | High |

## Gate recommendation

A hypothetical pilot should not proceed until G-01 through G-06 have documented design evidence and acceptance results. This is a risk-based recommendation, not a statement about legal or regulatory requirements.
