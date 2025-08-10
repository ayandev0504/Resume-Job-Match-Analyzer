# Resume-Job-Match-Analyzer
A Streamlit web application that analyzes how well a resume matches a given job description using OpenAI’s LLM API. The app extracts text from uploaded PDF resumes, compares them with job descriptions, and provides a match score along with improvement suggestions.

Features
Upload Resume (PDF) – Extracts text using PyMuPDF for accurate parsing.

Paste Job Description – Allows you to input the target job description.

AI-Powered Matching – Uses OpenAI LLM to compare resume and job requirements.

Match Score – Gives a percentage score for compatibility.

Improvement Suggestions – Detailed feedback to enhance resume relevance.

Clean UI – Built with Streamlit for a fast and interactive experience

📂 Project Structure
resume-job-match-analyzer/
│── venv/                  
│── app.py                 
│── utils/
│   ├── __init__.py
│   ├── pdf_parser.py      
│   ├── llm_analysis.py    
│── requirements.txt       

⚙️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/ayandev0504/Resume-Job-Match-Analyzer/tree/main
cd resume-job-match-analyzer
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
3️⃣ Activate Virtual Environment
Windows (PowerShell)

bash
Copy
Edit
venv\Scripts\Activate
Mac/Linux

bash
Copy
Edit
source venv/bin/activate
4️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5️⃣ Set Your OpenAI API Key
In PowerShell:

bash
Copy
Edit
$env:OPENAI_API_KEY="your_api_key_here"
In Linux/Mac:

bash
Copy
Edit
export OPENAI_API_KEY="your_api_key_here"
6️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
