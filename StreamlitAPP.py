import json
import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from langchain_community.callbacks import get_openai_callback

from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain, quiz_parser

# Load environment variables
load_dotenv()

# ====== PAGE CONFIG ======
st.set_page_config(
    page_title="MCQ Creator App",
    page_icon="📝",  # Page tab icon
    layout="wide"
)

# ====== TITLE ======
st.markdown("## 📝 MCQ Creator Application with LangChain & OpenAI")

# ====== SIDEBAR ======
st.sidebar.header("⚙️ MCQ Generation Settings")

# Difficulty/Tone
difficulty_choice = st.sidebar.selectbox(
    "🎯 Select Difficulty Level",
    options=["Simple", "Intermediate", "Advanced"],
    index=0,
)

# Number of MCQs
mcq_count_sidebar = st.sidebar.slider(
    "🔢 Number of MCQs", min_value=3, max_value=50, value=5
)

# Show correct answers toggle
show_correct_sidebar = st.sidebar.checkbox("✅ Show Correct Answers", value=True)

# ====== MAIN FORM ======
with st.form("user_inputs"):
    uploaded_file = st.file_uploader("📄 Upload a PDF or TXT file")
    subject = st.text_input("📚 Insert Subject", max_chars=30)
    submit = st.form_submit_button("🚀 Create MCQs")

if submit and uploaded_file and subject:
    with st.spinner("⏳ Generating MCQs..."):
        try:
            text = read_file(uploaded_file)

            # Invoke the chain
            with get_openai_callback() as cb:
                response = generate_evaluate_chain.invoke(
                    {
                        "text": text,
                        "number": mcq_count_sidebar,
                        "subject": subject,
                        "tone": difficulty_choice,
                        "response_json": json.dumps(
                            {
                                str(i): {
                                    "mcq": "question",
                                    "options": {
                                        "a": "choice",
                                        "b": "choice",
                                        "c": "choice",
                                        "d": "choice",
                                    },
                                    "correct": "answer",
                                }
                                for i in range(1, mcq_count_sidebar + 1)
                            }
                        ),
                        "format_instructions": quiz_parser.get_format_instructions(),
                    }
                )

            st.success("✅ MCQs Generated Successfully!")
            st.info(
                f"**Total Tokens:** {cb.total_tokens} | "
                f"**Prompt Tokens:** {cb.prompt_tokens} | "
                f"**Completion Tokens:** {cb.completion_tokens} | "
                f"**Total Cost (USD):** ${cb.total_cost:.6f}"
            )

            quiz = response["quiz"]
            review = response["review"]

            table_data = get_table_data(quiz)
            df = pd.DataFrame(table_data)
            df.index += 1

            st.subheader("📋 Generated MCQs")
            if not show_correct_sidebar:
                df = df.drop(columns=["Correct"])
            st.table(df)

            st.subheader("📝 Quiz Review")
            st.text_area("Review", review, height=200)

            # Download CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download MCQs as CSV",
                data=csv,
                file_name=f"{subject}_MCQs.csv",
                mime="text/csv",
            )

        except Exception as e:
            st.error("❌ An error occurred while generating MCQs")
            st.exception(e)
