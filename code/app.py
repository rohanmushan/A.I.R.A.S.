import streamlit as st
from datetime import datetime
from resume_analyzer import AIRAS

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