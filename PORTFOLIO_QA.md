# Portfolio QA

## Release decision

**Lab status: COMPLETE AND READY FOR KEENAN TO PUBLISH.**  
**Overall portfolio status: READY FOR KEENAN TO PUBLISH.**

This decision means the local fictional lab artifacts, deterministic verification, evidence images, and copy-ready publishing materials are present. It does **not** mean the item is live on GitHub or Upwork. Keenan must personally publish it and confirm both listings are live before the overall portfolio task can be reported fully complete.

## Verification record

| Check | Result | Evidence |
|---|---|---|
| Required artifacts | Pass | README, six assessment documents, CSV risk register, publishing kit, and this QA file are present |
| Risk-register integrity | Pass | 10 records, required schema, and 10/10 likelihood × impact calculations validated |
| Status integrity | Pass | All 10 risks remain `Open`, consistent with proposed rather than implemented controls |
| Screenshot evidence | Pass | Four PNG evidence captures are present and linked in README |
| Claim boundary | Pass | Documents label the organization and system fictional, scope the lab to synthetic assumptions, and avoid implemented-control, client, certification, production, or results claims |
| Publishing boundary | Pass | Publishing kit is copy-ready only. No GitHub or Upwork upload, push, submission, credential request, or account action was performed |

## Exact verification command

```bash
python scripts/verify_assessment.py
```

Expected completed-run output:

```text
VERIFICATION PASSED: 4/4 required screenshot files; 10 risk records; 10/10 rating calculations valid.
Scope check: fictional-only lab; all risk statuses remain Open; no implemented-control status asserted.
```

## Evidence review

| File | Review result | Supported claim |
|---|---|---|
| `evidence/01_executive_summary.png` | Reviewed | Fictional decision context, conditional posture, and 7/2/1/10 risk profile |
| `evidence/02_risk_register.png` | Reviewed | Example register rows show ratings, owners, and Open status |
| `evidence/03_rmf_gap_remediation.png` | Reviewed | NIST AI RMF function alignment and critical remediation sequence |
| `evidence/04_verification_results.png` | Reviewed | Deterministic local QA scope and passed result statement |

## Claim-to-artifact traceability

| Public claim | Supporting local artifact |
|---|---|
| Fictional internal support assistant assessed | `01_SYSTEM_SCOPE.md` |
| 10 risks with likelihood, impact, controls, remediation, owner, and status | `02_RISK_REGISTER.csv` |
| NIST AI RMF Govern, Map, Measure, Manage alignment | `03_NIST_AI_RMF_MAPPING.md` |
| Eight documented control gaps and evidence needed | `04_CONTROL_GAP_ANALYSIS.md` |
| Sequenced remediation and decision gates | `05_REMEDIATION_PLAN.md` |
| Conditional, not pilot-ready fictional posture | `06_EXECUTIVE_SUMMARY.md` |
| Copy-ready publishing content | `PUBLISHING_KIT.md` |

## Authorization and isolation boundary

- This is a local, desk-based portfolio assessment of a fictional system.
- No client systems, user accounts, real datasets, credentials, network targets, or production services were accessed.
- The static evidence captures present repository content only.
- Recommendations remain proposed until independently evidenced in a real authorized environment.

## GitHub and marketplace readiness

- **GitHub-ready:** Yes. Repository README, assessment artifacts, verification script, evidence captures, and publishing metadata are locally prepared.
- **Upwork-ready:** Yes. The provided title, description, skills, and screenshot order stay within demonstrated fictional-lab scope.
- **Live status:** Not published or submitted by Hermes. Keenan personally performs all publishing actions.

## Optional improvement

Add a PDF export only if a target marketplace or recruiter specifically requests a single-file attachment. It is not required for repository or Upwork publishing.
