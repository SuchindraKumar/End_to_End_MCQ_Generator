# 📝 MCQ Generator Application (LangChain + OpenAI + Streamlit)

An **end-to-end MCQ Generator** that creates Multiple Choice Questions from **PDF, TXT, or DOCX files** using **LangChain** and **OpenAI**, with a clean **Streamlit UI**.

---

## 🚀 Features

* 📄 Reads **PDF, TXT, or DOCX files** and extracts text automatically
* 🧠 Generates high-quality MCQs using OpenAI via LangChain
* 🎯 Customizable:

  * Number of MCQs
  * Subject
  * Difficulty / Tone
* 📊 Displays MCQs in a clean table
* 📝 Provides quiz complexity review
* 💰 Shows token usage and cost
* 🔐 Secure API key handling via `.env`
* 📦 Proper Python package structure

---

## 🗂️ Project Structure

```
End_to_End_MCQ_Generator/
│
├── StreamlitAPP.py
├── Response.json
├── setup.py
├── README.md
├── .env
├── env/                     # Conda virtual environment
│
└── src/
    └── mcqgenerator/
        ├── __init__.py
        ├── MCQGenerator.py
        ├── utils.py
        └── logger.py
```

---

## ⚙️ Prerequisites

* Python **3.10**
* An **OpenAI API Key**
* Conda (recommended)

---

## 🧪 Environment Setup (Recommended Way)

### 1️⃣ Create virtual environment inside project

```bash
conda create -p env python=3.10 -y
```

### 2️⃣ Activate environment

```bash
conda activate ./env
```

---

## 📦 Install Dependencies

### Option 1: Install from `setup.py`

```bash
pip install -e .
```

### Option 2: Manual install (if needed)

```bash
pip install \
langchain-core \
langchain-openai \
langchain-community \
streamlit \
pandas \
python-dotenv \
PyPDF2 \
python-docx \
openai
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ **Never commit `.env` to GitHub**

---

## ▶️ Run the Application

```bash
streamlit run StreamlitAPP.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📥 Supported File Formats

| Format | Supported |
| ------ | --------- |
| PDF    | ✅         |
| TXT    | ✅         |
| DOCX   | ✅         |

> Reads PDF, TXT, or DOCX files and returns extracted text.

---

## 🧠 How It Works

1. Upload a document
2. Text is extracted
3. LangChain prompt generates MCQs in JSON format
4. Output is parsed and displayed
5. Quiz is reviewed for difficulty and clarity

---

## 📄 Sample Input

* AI Notes
* Study Material
* Lecture Content
* Research Text
* Exam Preparation Notes

---

## ❗ Common Issues & Fixes

### ❌ `ModuleNotFoundError: No module named 'docx'`

```bash
pip install python-docx
```

---

### ❌ Conda env not found

```bash
conda info --envs
conda activate ./env
```

---

### ❌ Dependency conflict (OpenAI & LangChain)

✔️ Use these **tested compatible versions**:

```
langchain-core>=0.2
langchain-openai>=0.1
openai>=1.6
```

---

## 👨‍💻 Author

**Suchindra Kumar**
Data Scientist | ML | GenAI 

---

## ⭐ If you like this project

* Star ⭐ the repo
* Fork 🍴 it
* Use it in your portfolio 🚀
---

## 🖼 Screenshots
> ℹ️ The following screenshots show the **same page**, captured in two parts for readability.


## 🖼 Screenshots

![MCQ Creator Full Page Part 1](assets/screenshot-part-1.png)

![MCQ Creator Full Page Part 2](assets/screenshot-part-2.png)



---
