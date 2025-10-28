from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Hello World Agent")

@app.get("/")
def root():
    return {"message": "Hello World! This is your Python Agent."}

# Optional: Agent Network-compatible card endpoint
@app.get("/card")
def get_card():
    card = {
        "schemaVersion": "1.0.0",
        "name": "hello-world-agent",
        "displayName": "Hello World Agent",
        "description": "A simple demo agent that says Hello World",
        "invoke": {
            "method": "POST",
            "url": "https://YOUR_DOMAIN_OR_LOCALHOST/invoke",
            "headers": [{"name": "Content-Type", "value": "application/json"}]
        }
    }
    return JSONResponse(content=card)

# Optional: a /invoke endpoint to mimic agent invocation
@app.post("/invoke")
async def invoke(request: Request):
    data = await request.json()
    user_message = data.get("input", {}).get("messages", [{}])[0].get("content", "No message")
    reply = f"Hello! You said: '{user_message}'. I'm your Hello World Agent."
    return {
        "output": {
            "messages": [{"role": "assistant", "content": reply}],
            "sessionId": "demo-session-1"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
