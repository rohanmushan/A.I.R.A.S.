# AIRAS - AI-based Resume Analysis System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

AIRAS is a sophisticated AI-powered resume analysis tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). Leveraging Google's Gemini 1.5 Flash AI model, it provides comprehensive analysis and actionable feedback to improve resume effectiveness.

## 🌟 Key Features

- **Smart Resume Parsing**
  - Supports PDF and DOCX formats
  - Intelligent text extraction and processing
  - Maintains formatting integrity

- **AI-Powered Analysis**
  - ATS compatibility scoring
  - Role-specific skill gap analysis
  - Formatting and structure evaluation
  - Experience relevance assessment

- **Comprehensive Feedback**
  - Technical skills assessment
  - Soft skills evaluation
  - Content structure recommendations
  - Formatting improvement suggestions

- **Multiple Job Role Support**
  - 20+ pre-configured job profiles
  - Customized skill requirements
  - Industry-standard keyword matching

- **User-Friendly Interface**
  - Clean, intuitive design
  - Real-time analysis
  - Downloadable detailed reports
  - Interactive results visualization

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **AI/ML:** Google Gemini 1.5 Flash
- **Document Processing:** PyPDF2, python-docx
- **Environment Management:** python-dotenv
- **Version Control:** Git

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API Key (Gemini)
- Git (for version control)
- pip (Python package manager)

## 🚀 Installation Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rohanmushan/AIRAS-AI-based-Resume-Analysis-System.git
   cd AIRAS-AI-based-Resume-Analysis-System
   ```

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```
   Replace `your_api_key_here` with your actual Google Gemini API key.

## 📂 Project Structure

```
AIRAS/
├── code/                # Source code directory
│   ├── app.py          # Main Streamlit application
│   └── resume_analyzer.py  # Core analysis engine
├── assets/             # Project assets and resources
├── airas/              # Virtual environment directory
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this)
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT License
└── README.md        # Project documentation
```

## 🎯 Supported Job Roles

1. **Engineering & Development**
   - Software Engineer
   - Full Stack Developer
   - Frontend Developer
   - Backend Developer
   - DevOps Engineer
   - Mobile Developer

2. **Data & AI**
   - Data Scientist
   - Machine Learning Engineer
   - AI Engineer
   - Data Analyst
   - Deep Learning Engineer
   - MLOps Engineer

3. **Management & Design**
   - Product Manager
   - Project Manager
   - UX Designer
   - Business Analyst
   - Marketing Manager
   - HR Executive

## 🚀 Usage

1. **Start the Application**
   ```bash
   streamlit run code/app.py
   ```

2. **Access the Web Interface**
   - Open your browser
   - Navigate to `http://localhost:8501`

3. **Analyze Your Resume**
   - Upload your resume (PDF/DOCX)
   - Select target job role
   - View comprehensive analysis
   - Download detailed report

## 💡 Best Practices

- Keep your resume in PDF or DOCX format
- Ensure clear section headings
- Use standard fonts
- Avoid complex formatting
- Include relevant keywords
- Quantify achievements where possible

## 🔒 Security & Privacy

- Resumes are processed in-memory only
- No data is stored permanently
- Secure API key handling
- Environment variables for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powerful language processing
- Streamlit for the amazing web framework
- Open source community for various dependencies

## 📧 Contact

Rohan Mushan - [GitHub Profile](https://github.com/rohanmushan)

Project Link: [https://github.com/rohanmushan/AIRAS-AI-based-Resume-Analysis-System](https://github.com/rohanmushan/AIRAS-AI-based-Resume-Analysis-System)

---

⭐️ Star this repository if you find it helpful! 