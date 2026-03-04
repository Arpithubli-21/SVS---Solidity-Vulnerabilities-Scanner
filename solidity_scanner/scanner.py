"""
scanner.py
Core scanning engine for the Solidity vulnerability scanner.
Reads a Solidity source file, applies every rule from vulnerability_rules.py,
and returns a structured list of findings.
"""

from vulnerability_rules import VULNERABILITY_RULES


def scan_solidity(source_code: str) -> dict:
    """
    Scan *source_code* (a Solidity file as a string) for known vulnerabilities.

    Returns
    -------
    dict with keys:
        findings   : list[dict]  – one entry per matched vulnerability occurrence
        summary    : dict        – counts grouped by severity
        total      : int         – total number of findings
        safe       : bool        – True when no findings were found
    """
    findings = []

    lines = source_code.splitlines()

    for rule in VULNERABILITY_RULES:
        matched_lines = []

        for line_no, line in enumerate(lines, start=1):
            # Skip comment lines (// …)
            stripped = line.strip()
            if stripped.startswith("//") or stripped.startswith("*"):
                continue

            if rule["pattern"].search(line):
                matched_lines.append({"line": line_no, "content": line.strip()})

        if matched_lines:
            findings.append(
                {
                    "id": rule["id"],
                    "name": rule["name"],
                    "description": rule["description"],
                    "severity": rule["severity"],
                    "recommendation": rule["recommendation"],
                    "occurrences": matched_lines,
                }
            )

    # Build summary counters
    summary = {"High": 0, "Medium": 0, "Low": 0}
    for finding in findings:
        sev = finding["severity"]
        if sev in summary:
            summary[sev] += 1

    # Sort findings: High → Medium → Low
    severity_order = {"High": 0, "Medium": 1, "Low": 2}
    findings.sort(key=lambda f: severity_order.get(f["severity"], 9))

    return {
        "findings": findings,
        "summary": summary,
        "total": len(findings),
        "safe": len(findings) == 0,
    }


def get_severity_badge_class(severity: str) -> str:
    """Return a CSS class name matching the severity level."""
    mapping = {
        "High": "badge-high",
        "Medium": "badge-medium",
        "Low": "badge-low",
    }
    return mapping.get(severity, "badge-low")
