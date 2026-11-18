# 📄 AI Resume Screening Tool

An interactive web application built with **Streamlit** and **Natural Language Processing (NLP)** that evaluates how well a candidate's resume matches a target job description. It calculates an overall compatibility score and provides a side-by-side **Skills Gap Analysis**.

---

## ✨ Features

* **PDF Text Extraction:** Automatically extracts text from uploaded PDF resumes.
* **NLP Match Scoring:** Uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate an accurate percentage match between the resume and the job description.
* **Visual Match Feedback:** Categorizes candidates into *Excellent Match* (70%+), *Partial Match* (40%–69%), or *Low Match* (<40%) with instant visual alerts.
* **Key Skills Gap Analysis:** Compares keywords from the job description against the resume to highlight both **Matched Keywords** and **Missing Critical Keywords**.

---

## 🛠️ Tech Stack

* **Frontend / UI:** [Streamlit](https://streamlit.io)
* **PDF Parsing:** [PyPDF2](https://pypi.org)
* **Machine Learning / NLP:** [Scikit-Learn](https://scikit-learn.org) (`TfidfVectorizer`, `cosine_similarity`)
* **Text Processing:** Python `re` (Regular Expressions)

---

## 📂 Project Structure

```text
ai-resume-screener/
│
├── app.py               # Main Streamlit application script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 2. Installation
Clone the repository (or navigate to your project folder) and install the required dependencies:

```bash
pip install streamlit PyPDF2 scikit-learn
```

*(Optional)* You can also create a `requirements.txt` file with the following content:
```text
streamlit
PyPDF2
scikit-learn
```
And install via:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit server by running:

```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`.

---

## 📖 How to Use

1. **Paste the Job Description:** Copy the target job requirements and paste them into the text area.
2. **Upload Resume:** Upload a candidate's resume in `.pdf` format (must contain selectable text, not a scanned image).
3. **Analyze:** Click the **"Analyze & Score Resume"** button.
4. **Review Results:** Check the overall match percentage and review the matched vs. missing keywords under the **Key Skills Gap Analysis** section.

---

## 🔮 Future Enhancements

* Support for **`.docx`** and **`.txt`** resume formats.
* **Multi-word phrase matching** (e.g., `"supply chain"`, `"project management"`) using N-grams.
* **Batch Screening** to upload and rank multiple resumes at once.
* **OCR Support** for scanned PDF resumes.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

