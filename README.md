# AIRAS - AI-based Resume Analysis System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

AIRAS is a sophisticated AI-powered resume analysis tool that leverages Google's Gemini 1.5 Flash AI model to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). It provides comprehensive analysis and actionable feedback to improve resume effectiveness.

## 📸 Demo & Screenshots

### Video Demo
[Watch the Demo Video](link-to-your-demo-video)

### Screenshots
<details>
<summary>Click to expand</summary>

#### Main Interface
![Main Interface](assets/images/main-interface.png)

#### Analysis Results
![Analysis Results](assets/images/analysis-results.png)

#### Skills Assessment
![Skills Assessment](assets/images/skills-assessment.png)
</details>

## ✨ Key Features

- **AI-Powered Analysis**
  - ATS compatibility scoring
  - Role-specific skill gap analysis
  - Formatting and structure evaluation
  - Experience relevance assessment

- **Smart Resume Parsing**
  - PDF and DOCX support
  - Intelligent text extraction
  - Format integrity preservation

- **Comprehensive Feedback**
  - Technical & soft skills assessment
  - Content structure recommendations
  - Actionable improvement suggestions

## 🛠️ Tech Stack

- Frontend: Streamlit
- AI/ML: Google Gemini 1.5 Flash
- Document Processing: PyPDF2, python-docx
- Environment: python-dotenv

## 📋 Prerequisites

- Python 3.8+
- Google AI API Key (Gemini)
- Git

## 🚀 Quick Start

1. **Clone & Setup**
   ```bash
   git clone https://github.com/rohanmushan/AIRAS-AI-based-Resume-Analysis-System.git
   cd AIRAS-AI-based-Resume-Analysis-System
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Install & Configure**
   ```bash
   pip install -r requirements.txt
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

3. **Run Application**
   ```bash
   streamlit run code/app.py
   ```

## 📂 Project Structure

```
AIRAS/
├── code/                # Source code
│   ├── app.py          # Streamlit application
│   └── resume_analyzer.py  # Analysis engine
├── assets/             # Media resources
│   ├── images/         # Screenshots
│   └── videos/         # Demo videos
├── requirements.txt    # Dependencies
├── .env               # Configuration
└── README.md         # Documentation
```

## 🎯 Supported Roles

### Technical
- Software Engineer
- Full Stack Developer
- Data Scientist
- ML Engineer
- DevOps Engineer

### Management
- Product Manager
- Project Manager
- Business Analyst


## 🔒 Privacy & Security

- In-memory processing only
- No data storage
- Secure API handling
- Environment-based configuration

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

⭐️ If you find this project helpful, please consider giving it a star! 
