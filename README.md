# AIRAS - AI-based Resume Analysis System

AIRAS is an intelligent tool designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). Using Google's Gemini 1.5 Flash AI model, it provides comprehensive analysis and feedback on resumes.

## Features

- Resume parsing (PDF and DOCX formats)
- ATS compatibility analysis
- Skills gap analysis
- Formatting suggestions
- Experience and education evaluation
- Downloadable detailed reports
- Support for multiple job roles

## Prerequisites

- Python 3.8+
- Google AI API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AIRAS.git
cd AIRAS
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google AI API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

Run the application using Streamlit:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Project Structure

- `app.py`: Main Streamlit web application
- `resume_analyzer.py`: Core resume analysis functionality
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Supported Job Roles

- Software Engineer
- Full Stack Developer
- Machine Learning Engineer
- Cloud Engineer
- Data Scientist
- Product Manager
- DevOps Engineer
- UX Designer
- Marketing Manager
- Business Analyst
- And many more...

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 