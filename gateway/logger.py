import json
from datetime import datetime

LOG_FILE = "logs/threat_audit.json"

def log_incident(prompt, analysis):
    """Saves every security event for forensic analysis."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user_prompt": prompt,
        "risk_score": analysis.risk_score,
        "reasoning": analysis.reasoning,
        "decision": "BLOCKED" if analysis.is_blocked else "ALLOWED"
    }
    
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"Logging Error: {e}")
