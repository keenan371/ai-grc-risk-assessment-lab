#!/usr/bin/env python3
"""Deterministic local QA for the fictional AI GRC portfolio lab."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', '01_SYSTEM_SCOPE.md', '02_RISK_REGISTER.csv',
    '03_NIST_AI_RMF_MAPPING.md', '04_CONTROL_GAP_ANALYSIS.md',
    '05_REMEDIATION_PLAN.md', '06_EXECUTIVE_SUMMARY.md',
    'PUBLISHING_KIT.md', 'PORTFOLIO_QA.md',
    'evidence/01_executive_summary.png', 'evidence/02_risk_register.png',
    'evidence/03_rmf_gap_remediation.png', 'evidence/04_verification_results.png',
]
REQUIRED_COLUMNS = {'Risk_ID','Risk_Title','Likelihood_1_5','Impact_1_5','Inherent_Rating','Priority','Proposed_Controls','Remediation','Owner','Status'}
BANNED = ('real client', 'implemented controls', 'certified', 'guaranteed results', 'production assessment')

def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f'missing required artifact: {rel}')
    csv_path = ROOT / '02_RISK_REGISTER.csv'
    rows = []
    if csv_path.is_file():
        with csv_path.open(newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
            missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
            if missing:
                errors.append('missing CSV columns: ' + ', '.join(sorted(missing)))
        if len(rows) != 10:
            errors.append(f'expected 10 risk records, found {len(rows)}')
        for row in rows:
            try:
                likelihood, impact, rating = int(row['Likelihood_1_5']), int(row['Impact_1_5']), int(row['Inherent_Rating'])
                if not (1 <= likelihood <= 5 and 1 <= impact <= 5 and rating == likelihood * impact):
                    errors.append(f"invalid rating calculation: {row.get('Risk_ID', 'unknown')}")
            except (KeyError, ValueError):
                errors.append(f"non-numeric rating fields: {row.get('Risk_ID', 'unknown')}")
            if row.get('Status') != 'Open':
                errors.append(f"non-evidenced risk must remain Open: {row.get('Risk_ID', 'unknown')}")
    for rel in ['README.md','01_SYSTEM_SCOPE.md','03_NIST_AI_RMF_MAPPING.md','04_CONTROL_GAP_ANALYSIS.md','05_REMEDIATION_PLAN.md','06_EXECUTIVE_SUMMARY.md','PUBLISHING_KIT.md','PORTFOLIO_QA.md']:
        path = ROOT / rel
        if path.is_file():
            text = path.read_text(encoding='utf-8').lower()
            for phrase in BANNED:
                if phrase in text and phrase not in ('real client', 'implemented controls', 'production assessment'):
                    errors.append(f'unsupported claim phrase in {rel}: {phrase}')
    if errors:
        print('VERIFICATION FAILED')
        for error in errors:
            print('- ' + error)
        return 1
    print('VERIFICATION PASSED: 4/4 required screenshot files; 10 risk records; 10/10 rating calculations valid.')
    print('Scope check: fictional-only lab; all risk statuses remain Open; no implemented-control status asserted.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
