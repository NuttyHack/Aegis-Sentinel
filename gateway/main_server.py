from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
# This imports the analyze_prompt function from your firewall.py file
from firewall import analyze_prompt 

app = FastAPI(title="Aegis-Sentinel API Gateway")

class PromptRequest(BaseModel):
    user_input: str

@app.post("/check-security")
async def security_gateway(request: PromptRequest):
    """
    This endpoint intercepts the user input and runs it 
    through the firewall before it goes anywhere else.
    """
    print(f"--- 🛡️ Incoming Prompt Check ---")
    print(f"Content: {request.user_input[:50]}...")
    
    # Send it to your bouncer
    analysis = analyze_prompt(request.user_input)
    
    # Check the score (> 7 means block)
    if analysis.is_blocked:
        print(f"🚫 BLOCKED | Score: {analysis.risk_score} | Reason: {analysis.reasoning}")
        raise HTTPException(
            status_code=403, 
            detail={
                "message": "SECURITY ALERT: Prompt blocked for malicious intent.",
                "analysis": analysis.model_dump()
            }
        )
    
    print(f"✅ ALLOWED | Score: {analysis.risk_score}")
    return {
        "status": "Safe",
        "risk_score": analysis.risk_score,
        "message": "The prompt is safe to process."
    }

if __name__ == "__main__":
    # This runs the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
