import streamlit as st
import PyPDF2
from docx import Document
import io
import google.generativeai as genai
from typing import Dict, Any, List, Tuple
import os
from dotenv import load_dotenv
import re
from datetime import datetime
import json

# Load API key from .env file
load_dotenv()

# Get API key and validate it
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Please set your GOOGLE_API_KEY in the .env file")
    st.stop()

if not GOOGLE_API_KEY.startswith("AI"):
    st.error("Invalid API key format. Please make sure you're using a valid Google AI API key.")
    st.stop()

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error(f"Error configuring Gemini API: {str(e)}")
    st.stop()

class AIRAS:
    def __init__(self):
        # Dictionary containing required skills for different job roles
        # This helps in matching resume content with job requirements
        self.common_keywords = {
            "software_engineer": {
                "technical_skills": [
                    "Python", "Java", "JavaScript", "React", "Node.js", "SQL",
                    "REST API", "Microservices", "Docker", "AWS", "CI/CD",
                    "System Design", "Algorithms", "Data Structures", "Git"
                ],
                "soft_skills": [
                    "Problem Solving", "Team Collaboration", "Communication",
                    "Time Management", "Code Review", "Documentation"
                ]
            },
            "full_stack_developer": {
                "technical_skills": [
                    "JavaScript", "TypeScript", "React", "Node.js", "Express",
                    "SQL", "MongoDB", "REST API", "GraphQL", "HTML5", "CSS3",
                    "AWS", "CI/CD", "Git", "Docker"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Time Management",
                    "Code Review", "Documentation", "Agile Development"
                ]
            },
            "machine_learning_engineer": {
                "technical_skills": [
                    "Python", "TensorFlow", "PyTorch", "Scikit-learn",
                    "Deep Learning", "Computer Vision", "NLP", "MLOps",
                    "AWS SageMaker", "Statistical Analysis", "Big Data",
                    "Docker", "Git"
                ],
                "soft_skills": [
                    "Research", "Problem Solving", "Analytical Thinking",
                    "Communication", "Documentation", "Team Collaboration"
                ]
            },
            "cloud_engineer": {
                "technical_skills": [
                    "AWS", "Azure", "GCP", "Terraform", "Docker", "Kubernetes",
                    "CI/CD", "Linux", "Networking", "Security", "Serverless",
                    "Infrastructure as Code", "Git"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Team Collaboration",
                    "Documentation", "Time Management", "Security Mindset"
                ]
            },
            "data_scientist": {
                "technical_skills": [
                    "Python", "SQL", "Machine Learning", "Data Analysis",
                    "Statistics", "Pandas", "NumPy", "Scikit-learn",
                    "Data Visualization", "Big Data", "Deep Learning",
                    "A/B Testing", "ETL", "Git"
                ],
                "soft_skills": [
                    "Problem Solving", "Data Storytelling", "Business Acumen",
                    "Communication", "Critical Thinking", "Analytical Thinking"
                ]
            },
            "product_manager": {
                "technical_skills": [
                    "Agile", "Scrum", "Product Strategy", "Market Research",
                    "User Stories", "Analytics", "A/B Testing", "SQL",
                    "JIRA", "Data Analysis", "User Experience"
                ],
                "soft_skills": [
                    "Leadership", "Communication", "Strategic Thinking",
                    "Problem Solving", "User Empathy", "Decision Making"
                ]
            },
            "devops_engineer": {
                "technical_skills": [
                    "Docker", "Kubernetes", "CI/CD", "Jenkins", "AWS",
                    "Azure", "GCP", "Terraform", "Linux", "Shell Scripting",
                    "Monitoring", "Git", "Security"
                ],
                "soft_skills": [
                    "Problem Solving", "Automation Mindset", "Communication",
                    "Team Collaboration", "Documentation", "Continuous Improvement"
                ]
            },
            "ux_designer": {
                "technical_skills": [
                    "Figma", "Adobe XD", "User Research", "Wireframing",
                    "Prototyping", "UI Design", "Design Systems", "Accessibility",
                    "User Testing", "Information Architecture", "HTML/CSS"
                ],
                "soft_skills": [
                    "User Empathy", "Communication", "Problem Solving",
                    "Presentation Skills", "Attention to Detail", "Collaboration"
                ]
            },
            "marketing_manager": {
                "technical_skills": [
                    "Digital Marketing", "SEO", "SEM", "Social Media Marketing",
                    "Content Marketing", "Email Marketing", "Analytics", "CRM",
                    "Google Analytics", "Market Research", "Campaign Management"
                ],
                "soft_skills": [
                    "Strategic Thinking", "Communication", "Leadership",
                    "Project Management", "Analytical Thinking", "Creativity"
                ]
            },
            "business_analyst": {
                "technical_skills": [
                    "SQL", "Data Analysis", "Requirements Gathering",
                    "Agile", "JIRA", "Excel", "Power BI", "Tableau",
                    "Documentation", "System Analysis"
                ],
                "soft_skills": [
                    "Analytical Thinking", "Communication", "Problem Solving",
                    "Stakeholder Management", "Business Acumen", "Documentation"
                ]
            },
            "cybersecurity_analyst": {
                "technical_skills": [
                    "Network Security", "SIEM", "Firewall", "IDS/IPS",
                    "Vulnerability Assessment", "Penetration Testing", "Security Tools",
                    "Incident Response", "Threat Intelligence", "Cloud Security",
                    "Linux", "Python", "Git"
                ],
                "soft_skills": [
                    "Analytical Thinking", "Problem Solving", "Attention to Detail",
                    "Communication", "Documentation", "Security Mindset"
                ]
            },
            "mobile_developer": {
                "technical_skills": [
                    "Swift", "Kotlin", "Java", "iOS Development",
                    "Android Development", "React Native", "REST API",
                    "Mobile UI/UX", "Git", "CI/CD", "Testing"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Time Management",
                    "Code Review", "Documentation", "User Experience"
                ]
            },
            "blockchain_developer": {
                "technical_skills": [
                    "Solidity", "Web3.js", "Ethereum", "Smart Contracts",
                    "Blockchain Architecture", "Cryptography", "Node.js",
                    "Python", "JavaScript", "Git", "Security"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Time Management",
                    "Documentation", "Research", "Security Mindset"
                ]
            },
            "ai_engineer": {
                "technical_skills": [
                    "Python", "TensorFlow", "PyTorch", "Deep Learning",
                    "Machine Learning", "NLP", "Computer Vision",
                    "AI Model Development", "MLOps", "Docker", "Git",
                    "Cloud AI Services"
                ],
                "soft_skills": [
                    "Research", "Problem Solving", "Analytical Thinking",
                    "Communication", "Documentation", "Innovation"
                ]
            },
            "frontend_developer": {
                "technical_skills": [
                    "JavaScript", "TypeScript", "React", "Vue.js", "Angular",
                    "HTML5", "CSS3", "Redux", "Next.js", "Responsive Design",
                    "Web Accessibility", "Git", "CI/CD", "REST API"
                ],
                "soft_skills": [
                    "Problem Solving", "Attention to Detail", "Communication",
                    "Time Management", "Code Review", "User Experience Focus"
                ]
            },
            "backend_developer": {
                "technical_skills": [
                    "Python", "Java", "Node.js", "REST API", "GraphQL",
                    "Microservices", "Docker", "SQL", "MongoDB", "Redis",
                    "AWS", "CI/CD", "Git", "System Design"
                ],
                "soft_skills": [
                    "Problem Solving", "System Architecture", "Communication",
                    "Time Management", "Code Review", "Documentation"
                ]
            },
            "mobile_app_developer": {
                "technical_skills": [
                    "Swift", "Kotlin", "Java", "iOS Development",
                    "Android Development", "React Native", "Flutter",
                    "Mobile UI/UX", "REST API", "Git", "CI/CD",
                    "Mobile Testing"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Time Management",
                    "Code Review", "Documentation", "User Experience"
                ]
            },
            "hybrid_application_developer": {
                "technical_skills": [
                    "JavaScript", "TypeScript", "React Native", "Flutter",
                    "HTML5", "CSS3", "Responsive Design", "REST API",
                    "Git", "CI/CD", "Mobile Testing", "App Store",
                    "Play Store"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Time Management",
                    "Code Review", "Documentation", "User Experience"
                ]
            },
            "qa_engineer": {
                "technical_skills": [
                    "Test Automation", "Selenium", "Cypress", "Jest",
                    "Python", "Java", "JavaScript", "API Testing",
                    "Performance Testing", "CI/CD", "Git", "Agile",
                    "Test Planning"
                ],
                "soft_skills": [
                    "Attention to Detail", "Analytical Thinking", "Communication",
                    "Problem Solving", "Documentation", "Quality Focus"
                ]
            },
            "data_analyst": {
                "technical_skills": [
                    "SQL", "Python", "Excel", "Power BI", "Tableau",
                    "Data Visualization", "Statistical Analysis", "Data Cleaning",
                    "ETL", "Business Intelligence", "A/B Testing", "Git"
                ],
                "soft_skills": [
                    "Analytical Thinking", "Problem Solving", "Communication",
                    "Business Acumen", "Data Storytelling", "Attention to Detail"
                ]
            },
            "deep_learning_engineer": {
                "technical_skills": [
                    "Python", "TensorFlow", "PyTorch", "Keras",
                    "Neural Networks", "CNN", "RNN", "LSTM", "GAN",
                    "Computer Vision", "NLP", "MLOps", "AWS SageMaker",
                    "Docker", "Git"
                ],
                "soft_skills": [
                    "Research", "Problem Solving", "Analytical Thinking",
                    "Communication", "Documentation", "Innovation"
                ]
            },
            "mlops_engineer": {
                "technical_skills": [
                    "Python", "Docker", "Kubernetes", "CI/CD", "Jenkins",
                    "MLflow", "TensorFlow", "PyTorch", "AWS SageMaker",
                    "Azure ML", "Model Deployment", "Monitoring", "Git",
                    "Security"
                ],
                "soft_skills": [
                    "Problem Solving", "Communication", "Team Collaboration",
                    "Documentation", "Time Management", "DevOps Mindset"
                ]
            },
            "data_engineer": {
                "technical_skills": [
                    "Python", "SQL", "ETL", "Data Warehousing", "Big Data",
                    "Apache Spark", "Hadoop", "Kafka", "Airflow", "AWS",
                    "Data Modeling", "Data Pipeline", "Git", "CI/CD"
                ],
                "soft_skills": [
                    "Problem Solving", "Technical Documentation", "Collaboration",
                    "Attention to Detail", "Time Management", "System Architecture"
                ]
            },
            "project_manager": {
                "technical_skills": [
                    "Agile", "Scrum", "Kanban", "JIRA", "Project Planning",
                    "Risk Management", "Resource Management", "Budget Management",
                    "Stakeholder Management", "Data Analysis", "Reporting"
                ],
                "soft_skills": [
                    "Leadership", "Communication", "Strategic Thinking",
                    "Problem Solving", "Time Management", "Decision Making"
                ]
            },
            "hr_executive": {
                "technical_skills": [
                    "HRIS", "ATS", "Payroll Systems", "Recruitment",
                    "Talent Management", "Performance Management", "HR Analytics",
                    "Compliance", "Benefits Administration", "Data Analysis"
                ],
                "soft_skills": [
                    "Communication", "Interpersonal Skills", "Problem Solving",
                    "Conflict Resolution", "Time Management", "Leadership"
                ]
            },
            "graphic_designer": {
                "technical_skills": [
                    "Adobe Creative Suite", "Photoshop", "Illustrator", "InDesign",
                    "UI/UX Design", "Typography", "Color Theory", "Layout Design",
                    "Digital Design", "Figma", "Sketch", "HTML/CSS"
                ],
                "soft_skills": [
                    "Creativity", "Communication", "Problem Solving",
                    "Time Management", "Attention to Detail", "Client Management"
                ]
            }
        }
        # Initialize the latest Gemini model for resume analysis
        try:
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            st.write("Successfully initialized Gemini model")
        except Exception as e:
            st.error(f"Error initializing Gemini model: {str(e)}")
            st.stop()

    def parse_resume(self, file_content: bytes, file_type: str) -> str:
        """Extract text content from uploaded resume file"""
        try:
            if file_type.lower() in ["pdf", "application/pdf"]:
                return self._parse_pdf(file_content)
            elif file_type.lower() in ["docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                return self._parse_docx(file_content)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
        except Exception as e:
            st.error(f"Error parsing resume: {str(e)}")
            return ""

    def _parse_pdf(self, file_content: bytes) -> str:
        """Extract text from PDF files"""
        try:
            pdf_file = io.BytesIO(file_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text.strip()
        except Exception as e:
            st.error(f"Error parsing PDF: {str(e)}")
            return ""

    def _parse_docx(self, file_content: bytes) -> str:
        """Extract text from DOCX files"""
        try:
            docx_file = io.BytesIO(file_content)
            doc = Document(docx_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            st.error(f"Error parsing DOCX: {str(e)}")
            return ""

    def analyze_resume(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Analyze resume content using Gemini AI and return structured feedback"""
        try:
            # Get required skills for the selected job role
            job_keywords = self.common_keywords.get(job_title.lower(), {})
            
            # Create prompt for Gemini AI with specific analysis requirements
            prompt = f"""
            Analyze this resume for a {job_title} position. Provide a detailed analysis in the following JSON format:

            {{
                "ats_score": float,  # Score between 0-100, based on keyword matching, formatting, and content relevance
                "missing_technical_skills": [string],  # List of missing technical skills
                "missing_soft_skills": [string],  # List of missing soft skills
                "formatting_issues": [string],  # List of formatting issues
                "content_structure": [string],  # List of content structure observations
                "experience_analysis": [string],  # List of experience-related observations
                "education_analysis": [string],  # List of education-related observations
                "skills_analysis": [string],  # List of skills-related observations
                "suggestions": [string]  # List of improvement suggestions
            }}

            Focus on:
            1. ATS compatibility and keyword optimization
            2. Technical and soft skills alignment with the role
            3. Experience relevance and impact
            4. Education and certifications
            5. Overall structure and formatting
            6. Specific, actionable improvement suggestions

            Resume:
            {resume_text}

            Important keywords for this role:
            Technical Skills: {', '.join(job_keywords.get('technical_skills', []))}
            Soft Skills: {', '.join(job_keywords.get('soft_skills', []))}

            IMPORTANT: Respond ONLY with the JSON object, no additional text or explanation.
            """

            # Get analysis from Gemini AI
            try:
                response = self.model.generate_content(prompt)
                if not response or not response.text:
                    st.error("Empty response from Gemini API. Please try again.")
                    return {}
                
                # Extract JSON from the response
                response_text = response.text
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    analysis = json.loads(json_match.group())
                    return analysis
                else:
                    st.error("Could not find valid JSON in the response. Please try again.")
                    return {}
            except Exception as e:
                st.error(f"Error calling Gemini API: {str(e)}")
                return {}

        except Exception as e:
            st.error(f"Error in analysis: {str(e)}")
            return {}

def main():
    # Set up the Streamlit page configuration
    st.set_page_config(
        page_title="AIRAS",
        page_icon=None,
        layout="wide"
    )

    st.title("AI based Resume Analysing System")
    
    st.markdown("""
    AIRAS (AI-based Resume Analysis System) is an intelligent tool designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). 
    By leveraging advanced AI technology, it analyzes your resume against industry-specific job roles and provides detailed feedback on ATS compatibility, 
    missing skills, formatting issues, and actionable improvement suggestions. Whether you're a fresh graduate or an experienced professional, 
    AIRAS helps you craft a resume that stands out in the competitive job market.
    """)
    
    st.write("Upload your resume and get comprehensive feedback to improve your ATS score! This tool is developed by a human for human users.")

    # Create analyzer instance
    analyzer = AIRAS()

    # File upload widget
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    
    # Job role selection dropdown
    job_title = st.selectbox(
        "Select your target job role",
        [
            # Original Roles
            "Software Engineer",
            "Full Stack Developer",
            "Machine Learning Engineer",
            "Cloud Engineer",
            "Data Scientist",
            "Product Manager",
            "DevOps Engineer",
            "UX Designer",
            "Marketing Manager",
            "Business Analyst",
            "Cybersecurity Analyst",
            "Mobile Developer",
            "Blockchain Developer",
            "AI Engineer",
            # New Specialized Roles
            "Frontend Developer",
            "Backend Developer",
            "Mobile App Developer",
            "Hybrid Application Developer",
            "QA Engineer",
            "Data Analyst",
            "Deep Learning Engineer",
            "MLOps Engineer",
            "Data Engineer",
            "Project Manager",
            "HR Executive",
            "Graphic Designer"
        ]
    )

    if uploaded_file and job_title:
        # Extract text from uploaded resume
        resume_text = analyzer.parse_resume(uploaded_file.getvalue(), uploaded_file.type)
        
        if resume_text:
            # Show loading spinner while analyzing
            with st.spinner("Analyzing your resume..."):
                # Get resume analysis
                analysis = analyzer.analyze_resume(resume_text, job_title)

                if analysis:
                    # Create tabs for different sections of analysis
                    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Detailed Analysis", "Suggestions", "Skills Analysis"])

                    # Overview tab - ATS score and missing skills
                    with tab1:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("ATS Score")
                            st.metric("Score", f"{analysis.get('ats_score', 0)}/100")
                            
                            st.subheader("Missing Technical Skills")
                            for skill in analysis.get('missing_technical_skills', []):
                                st.write(f"- {skill}")

                        with col2:
                            st.subheader("Missing Soft Skills")
                            for skill in analysis.get('missing_soft_skills', []):
                                st.write(f"- {skill}")

                    # Detailed Analysis tab - Formatting and content issues
                    with tab2:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("Formatting Issues")
                            for issue in analysis.get('formatting_issues', []):
                                st.write(f"- {issue}")

                            st.subheader("Content Structure")
                            for point in analysis.get('content_structure', []):
                                st.write(f"- {point}")

                        with col2:
                            st.subheader("Experience Analysis")
                            for point in analysis.get('experience_analysis', []):
                                st.write(f"- {point}")

                            st.subheader("Education Analysis")
                            for point in analysis.get('education_analysis', []):
                                st.write(f"- {point}")

                    # Suggestions tab - Improvement recommendations
                    with tab3:
                        st.subheader("Improvement Suggestions")
                        for i, suggestion in enumerate(analysis.get('suggestions', []), 1):
                            st.write(f"{i}. {suggestion}")

                    # Skills Analysis tab - Detailed skills assessment
                    with tab4:
                        st.subheader("Skills Analysis")
                        for point in analysis.get('skills_analysis', []):
                            st.write(f"- {point}")

                    # Add download button for the analysis report
                    st.download_button(
                        label="Download Analysis Report",
                        data=f"Resume Analysis Report\n\n" + 
                             f"Job Title: {job_title}\n" +
                             f"ATS Score: {analysis.get('ats_score', 0)}/100\n\n" +
                             f"Missing Technical Skills:\n" + "\n".join(f"- {skill}" for skill in analysis.get('missing_technical_skills', [])) + "\n\n" +
                             f"Missing Soft Skills:\n" + "\n".join(f"- {skill}" for skill in analysis.get('missing_soft_skills', [])) + "\n\n" +
                             f"Improvement Suggestions:\n" + "\n".join(f"{i+1}. {suggestion}" for i, suggestion in enumerate(analysis.get('suggestions', []))),
                        file_name=f"resume_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

if __name__ == "__main__":
    main() 