# ⚖️ ForensicAI: Truth Detection Suite

**Detect What's Real. Expose What's Not.**

ForensicAI is a high-performance, dark-themed web application designed to combat deepfakes and digital misinformation. Built in 2026 for the [Hackathon Name], it leverages the **Gemini 3 Flash** multimodal engine to provide real-time forensic analysis of images, text, and URLs.



---

## 🛠️ Features

- **📸 Image Forensics:** Detects GAN/Diffusion artifacts, lighting inconsistencies, and facial warping in deepfakes.
- **📰 Article Scanner:** Semantically analyzes news text for sensationalism, bias, and factual discrepancies.
- **🔗 URL Inspector:** Heuristic analysis of domains to identify phishing risks and known misinformation hosts.
- **📱 Responsive UI:** Professional, minimal dark-mode interface optimized for desktop and mobile.

---

## 🚀 Getting Started

Follow these steps to run ForensicAI on your local machine.

### 1. Prerequisites
- **Python 3.10+**
- A **Gemini API Key** (Get one for free at [Google AI Studio](https://aistudio.google.com/))

### 2. Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/ForensicAI.git](https://github.com/yourusername/ForensicAI.git)
   
   cd ForensicAI
2.
    Install the backend dependencies:

    Bash
    pip install -r requirements.txt

3.
    Setup Your API Key
    Open app.py.

    Locate the variable API_KEY.

    Replace the placeholder string with your own Gemini API key:

    Python
    API_KEY = "YOUR_AIza_KEY_HERE"

4.
    Launch the Platform
    Start the Backend:

    Bash
    python app.py
    Open the Frontend:
    Simply double-click index.html or open it in any modern browser.

🏗️ Tech Stack
Frontend: HTML5, Tailwind CSS, Lucide Icons (CDN-driven SPA)

Backend: Python, FastAPI, Uvicorn

AI Intelligence: Google Gemini 3 Flash (Multimodal)

⚖️ Disclaimer
This tool is built for hackathon demonstration purposes. While Gemini 3 provides state-of-the-art detection, no AI is 100% accurate. Always use multiple sources for verification.

