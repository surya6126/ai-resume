import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Function to extract core keywords/skills from text
def extract_keywords(text):
    # Standardize text to lowercase and extract words longer than 2 characters
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    # A list of common words to filter out
    stop_words = set([
        'the', 'and', 'your', 'that', 'have', 'with', 'this', 'for', 'from', 'with',
        'company', 'role', 'job', 'work', 'team', 'experience', 'skills', 'ability',
        'required', 'preferred', 'qualification', 'management', 'position', 'candidate'
    ])
    return set([w for w in words if w not in stop_words])

# --- Streamlit Web UI Layout ---
st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="centered")

st.title("📄 AI Resume Screening Tool")
st.subheader("Evaluate how well a resume matches a job description using NLP")
st.write("---")

# Input 1: Job Description
st.write("### 1. Paste the Job Description")
job_description = st.text_area("Paste the target job requirements here:", height=200, 
                               placeholder="e.g., Looking for a Production Manager with experience in supply chain, operations, and quality control...")

# Input 2: Resume Upload
st.write("### 2. Upload the Resume")
uploaded_file = st.file_uploader("Upload candidate resume (PDF format only):", type=["pdf"])

# --- Processing & Matching Logic ---
if st.button("Analyze & Score Resume"):
    if not job_description:
        st.error("Please paste a job description first!")
    elif not uploaded_file:
        st.error("Please upload a resume PDF file!")
    else:
        with st.spinner("Analyzing text and calculating match profile..."):
            try:
                # 1. Extract text from the uploaded resume
                resume_text = extract_text_from_pdf(uploaded_file)
                
                if not resume_text.strip():
                    st.error("Could not extract text from the PDF. It might be scanned or blank.")
                else:
                    # 2. Combine texts for vectorization
                    text_corpus = [resume_text, job_description]
                    
                    # 3. Vectorize text using TF-IDF
                    vectorizer = TfidfVectorizer(stop_words='english')
                    tfidf_matrix = vectorizer.fit_transform(text_corpus)
                    
                    # 4. Calculate Cosine Similarity
                    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
                    match_percentage = round(similarity_matrix[0][0] * 100, 2)
                    
                    # 5. Display the final results
                    st.success("Analysis Complete!")
                    st.metric(label="Overall Resume Match Score", value=f"{match_percentage}%")
                    
                    # Score Feedback Visuals
                    if match_percentage >= 70:
                        st.balloons()
                        st.success("🔥 Excellent Match! This candidate is highly qualified for this role.")
                    elif 40 <= match_percentage < 70:
                        st.warning("⚠️ Partial Match. The candidate has some relevant skills but misses core requirements.")
                    else:
                        st.error("❌ Low Match. This candidate does not meet the specified job criteria.")
                    
                    # --- NEW FEATURE: Skills Gap Analysis ---
                    st.write("---")
                    st.write("### 📊 Key Skills Gap Analysis")
                    
                    job_keywords = extract_keywords(job_description)
                    resume_keywords = extract_keywords(resume_text)
                    
                    # Find words present in Job Description but missing in Resume
                    missing_keywords = job_keywords.difference(resume_keywords)
                    # Find words present in both
                    matched_keywords = job_keywords.intersection(resume_keywords)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write("#### ✅ Matched Keywords Found:")
                        if matched_keywords:
                            st.write(", ".join(list(matched_keywords)[:15]) + "...")
                        else:
                            st.write("*None identified*")
                            
                    with col2:
                        st.write("#### ❌ Missing Critical Keywords:")
                        if missing_keywords:
                            # Displaying top 15 missing words as a quick summary
                            st.write(", ".join(list(missing_keywords)[:15]) + "...")
                        else:
                            st.write("*No major gaps found!*")
                            
            except Exception as e:
                st.error(f"An error occurred during processing: {e}")