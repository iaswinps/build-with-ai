<div align="center">

# 🔍 ForensicAI
### Truth Detection Suite

**Detect What's Real. Expose What's Not.**

![Open Source](https://img.shields.io/badge/Open%20Source-MIT%20License-00B0C8?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/Powered%20by-Gemini%20Flash-orange?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## 📌 Overview

**ForensicAI** is a fully open-source deepfake and misinformation detection 
platform that provides real-time forensic analysis across three detection 
vectors — images, article text, and URLs — powered by **Google Gemini Flash**.

Built for a hackathon. Open to the world.

> Anyone can fork this repository, swap in their own Gemini API key in 
> `app.py`, and run a fully functional instance on their local machine 
> — completely free.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖼️ **Image Forensics** | Detects GAN/Diffusion artifacts, facial warping, lighting inconsistencies |
| 📰 **Article Scanner** | Flags sensationalism, unverified claims, and source bias in news text |
| 🔗 **URL Inspector** | Checks domain reputation, SSL validity, and misinformation host matching |
| 📊 **Confidence Scoring** | Every verdict includes a % score and 3-point AI explanation |
| 🌑 **Dark Forensic UI** | Professional dark-mode interface, fully responsive |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, Tailwind CSS, Lucide Icons (CDN) |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **AI Engine** | Google Gemini Flash (Multimodal) |
| **Deployment** | Local / Any Python-capable host |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A **free** Gemini API key → [Get one at Google AI Studio](https://aistudio.google.com/)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/ForensicAI.git
cd ForensicAI
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Open `app.py` and find the `API_KEY` variable:
```python
# app.py
API_KEY = "YOUR_AIza_KEY_HERE"  # ← Replace with your Gemini API key
```

> 🔒 Your key is only used locally to authenticate Gemini requests.  
> It is never stored or transmitted anywhere else.

**4. Launch the platform**
```bash
python app.py
```
Then open `index.html` in your browser, or navigate to `http://localhost:8000`

---

## ⚙️ How It Works
```
User submits content
        ↓
 ┌──────────────────────────────────┐
 │  Image → Deepfake Detection      │
 │  Text  → Misinformation Scanner  │
 │  URL   → Domain Risk Inspector   │
 └──────────────────────────────────┘
        ↓
  Gemini Flash analyzes input
        ↓
  Verdict + Confidence % + Reasons
```

| Input | Verdict Options | Signals Analyzed |
|---|---|---|
| 🖼️ Image | `REAL` / `DEEPFAKE` | Pixel artifacts, face geometry, metadata |
| 📰 Article | `CREDIBLE` / `MISLEADING` / `UNVERIFIED` | Bias, tone, factual consistency |
| 🔗 URL | `SAFE` / `SUSPICIOUS` / `DANGEROUS` | Domain age, SSL, reputation score |

---

## 🤝 Contributing

ForensicAI is open to contributions from everyone.  
Found a bug? Want to add a feature? Open a PR.
```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

### 💡 Ideas for Contributions
- 🎥 Video upload support for deepfake detection
- 🌍 Multilingual article analysis
- 🔌 Alternative AI providers (OpenAI, Claude, etc.)
- 🧩 Browser extension for URL inspection
- 📈 Improved confidence score calibration

---

## ⚠️ Disclaimer

ForensicAI is built for demonstration purposes. While Gemini Flash delivers 
state-of-the-art analysis, no AI achieves 100% accuracy. Always corroborate 
results with additional sources and human judgment.

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, 
modify, and distribute this software. See [LICENSE](LICENSE) for details.

---

<div align="center">

Built with purpose. Open to the world.

**ForensicAI — 2026**

</div>