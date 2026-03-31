# tools.py

import re
import json
# ==============================
# MASTER OPS SYSTEM PROMPT
# ==============================

SYSTEM_PROMPT = """
You are GMDECOR Project Operations Controller (Master Ops Agent).

Objective:
Maintain absolute control over Progress, Cost, Quality, and Coordination.

Operational Style:
- High-pressure execution
- No explanations
- No theory
- No conversational filler

Analysis Logic:
1. Compare Current Progress vs Timeline
2. Cross-check Daily Reports with Issues to detect hidden delays
3. Generate a strict 3-day recovery micro-schedule

Output Rules (STRICT FORMAT):

STATUS:
<short execution status>

TOP RISKS:
- Risk 1
- Risk 2
- Risk 3

ACTION PLAN:
DAY 1:
DAY 2:
DAY 3:

ASSIGNMENT:
- Site:
- Procurement:
- Finance:

ALERT:
<critical warning>

All output must be in English.
"""

# ==============================
# ANALYST FUNCTION
# ==============================

def analyst(input_text: str) -> dict:
    """
    Extract structured data from raw input
    """

    data = {
        "project": "",
        "timeline": "",
        "progress": "",
        "issues": "",
        "reports": ""
    }

    # simple parsing (extendable)
    project_match = re.search(r"Project:\s*(.*)", input_text)
    timeline_match = re.search(r"Timeline:\s*(.*)", input_text)
    progress_match = re.search(r"Progress:\s*(.*)", input_text)
    issues_match = re.search(r"Issues:\s*(.*)", input_text)
    reports_match = re.search(r"Reports:\s*(.*)", input_text)

    if project_match:
        data["project"] = project_match.group(1)

    if timeline_match:
        data["timeline"] = timeline_match.group(1)

    if progress_match:
        data["progress"] = progress_match.group(1)

    if issues_match:
        data["issues"] = issues_match.group(1)

    if reports_match:
        data["reports"] = reports_match.group(1)

    return data


# ==============================
# ROUTER FUNCTION
# ==============================

def router(data: dict) -> str:
    """
    Decide analysis type
    """

    progress = data.get("progress", "")
    issues = data.get("issues", "")

    if issues and "delay" in issues.lower():
        return "RECOVERY_PLAN"

    if "risk" in issues.lower():
        return "RISK_ASSESSMENT"

    if progress:
        return "PROGRESS_UPDATE"

    return "GENERAL_ANALYSIS"