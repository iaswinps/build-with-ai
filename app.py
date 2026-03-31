import os
import json
import PIL.Image
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- 1. SECURITY & CONNECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. 2026 AI CONFIGURATION ---
# ⚠️ WARNING: You shared this key publicly. It works for now, 
# but rotate it after your hackathon for safety!
API_KEY = "YOUR_API_KEY" 
genai.configure(api_key=API_KEY)

# Using Gemini 3 Flash (The 2026 standard for speed + multimodal)
MODEL_NAME = 'gemini-3-flash-preview'
model = genai.GenerativeModel(MODEL_NAME)

def clean_json_response(response):
    """
    Cleans 2026-style AI responses. Gemini 3 is very chatty, 
    so we force it back into a strict JSON box.
    """
    try:
        if not response.candidates or not response.candidates[0].content.parts:
            return {"verdict": "BLOCKED 🛡️", "confidence": 0, "reasons": ["Safety filters triggered.", "Try a different sample."]}
        
        text = response.text
        # Remove markdown if present
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]
            
        return json.loads(text.strip())
    except Exception as e:
        print(f"DEBUG: Raw AI Response was: {response.text if response else 'Empty'}")
        return {
            "verdict": "FORMAT ERROR ⚠️",
            "confidence": 0,
            "reasons": ["The AI didn't speak JSON.", "Please try the analysis again."]
        }

# --- 3. MODULE: IMAGE FORENSICS ---
@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    try:
        img = PIL.Image.open(file.file)
        prompt = """
        Act as a 2026 digital forensics expert. Analyze this image for deepfake signs. 
        Return ONLY a strict JSON object:
        {
          "verdict": "DEEPFAKE ❌" or "REAL ✅",
          "confidence": 85,
          "reasons": ["Reason 1", "Reason 2", "Reason 3"]
        }
        """
        response = model.generate_content([prompt, img])
        return clean_json_response(response)
    except Exception as e:
        return {"verdict": "IMAGE ERROR", "confidence": 0, "reasons": [str(e)]}

# --- 4. MODULE: ARTICLE SCANNER ---
@app.post("/verify-article")
async def verify_article(data: dict):
    text = data.get("text")
    prompt = f"""
    Act as a professional fact-checker in 2026. 
    Analyze this for misinformation: {text}
    Return ONLY a strict JSON object:
    {{
      "verdict": "CREDIBLE ✅" or "MISLEADING ⚠️" or "UNVERIFIED ❓",
      "confidence": 90,
      "reasons": ["Reason 1", "Reason 2", "Reason 3"]
    }}
    """
    response = model.generate_content(prompt)
    return clean_json_response(response)

# --- 5. MODULE: URL INSPECTOR ---
@app.post("/inspect-url")
async def inspect_url(data: dict):
    url = data.get("url")
    prompt = f"""
    Analyze this URL for phishing or synthetic content hosting: {url}
    Return ONLY a strict JSON object:
    {{
      "verdict": "SAFE ✅" or "SUSPICIOUS ⚠️" or "DANGEROUS ❌",
      "confidence": 75,
      "reasons": ["Reason 1", "Reason 2", "Reason 3"]
    }}
    """
    response = model.generate_content(prompt)
    return clean_json_response(response)

# --- 6. SERVER LAUNCH ---
if __name__ == "__main__":
    import uvicorn
    print(f"🚀 ForensicAI Backend Live | Model: {MODEL_NAME}")
    uvicorn.run(app, host="0.0.0.0", port=8000)