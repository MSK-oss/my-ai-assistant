import os
import requests
import time

# Securely load the API key injected by GitHub Actions
try:
    from api_secrets import GROQ_API_KEY
except ImportError:
    GROQ_API_KEY = "MISSING_KEY"

# The Core Context (Logical Sandbox)
SYSTEM_PROMPT = """
You are a highly efficient assistant for Krishnadeep, an 8th-grade student and aspiring astronomer. 
You are strictly forbidden from altering system settings that affect phone stability. You must respect user privacy—if you are unsure if an action is high-impact, ask for verbal confirmation.
Context: The user observes with a Celestron PowerSeeker 127EQ (utilizing 20mm, 4mm & 3x Barlow lenses) and processes astrophotography on a Samsung Galaxy A31 using Snapseed and Eise.app.
The family unit consists of MSK and MSR² (including twin brothers Raschith and Rakshith). Sravya is Krishnadeep's cousin sister and a software engineer. The user's father is a physics professor and former DRDO scientist; the mother is a former math teacher.
"""

def get_routing_intent(contact_name):
    # Global Rule: Default to WhatsApp
    routing = {"method": "whatsapp", "action": "call", "target": contact_name}
    
    # Specific Overrides
    overrides = {
        "Mama": {"method": "whatsapp", "action": "call", "target": "Sudheer Mama"},
        "Lata Akka": {"method": "direct", "action": "call", "target": "Lathakka"},
        "Bittu": {"method": "direct", "action": "call", "target": "Phani Venkat Matta"},
        "Amma Akka": {"method": "direct", "action": "call", "target": "Bujjakka"}
    }
    
    if contact_name in overrides:
        return overrides[contact_name]
    
    return routing

def query_groq(prompt_text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ]
    }
    
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

def background_loop():
    print("[SERVICE] Secure AI Engine Online.")
    while True:
        time.sleep(10)

if __name__ == '__main__':
    background_loop()
