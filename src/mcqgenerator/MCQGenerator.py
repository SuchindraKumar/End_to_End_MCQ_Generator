import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_community.callbacks import get_openai_callback

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4.1-nano", openai_api_key=key, temperature=0.7)

# Quiz Generation Prompt
quiz_template = """
Text: {text}
You are an expert MCQ maker. Given the above text, create {number} multiple choice questions for {subject} students in {tone} tone.
Format your response like RESPONSE_JSON below.
### RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt = ChatPromptTemplate.from_template(quiz_template + "\n{format_instructions}")
quiz_parser = JsonOutputParser()
quiz_chain = quiz_generation_prompt | llm | quiz_parser

# Quiz Evaluation Prompt
review_template = """
You are an expert English grammarian and writer. Evaluate the complexity of the quiz for {subject} students.
If questions are not appropriate, update them to match cognitive abilities. Use max 50 words for analysis.

Quiz_MCQs:
{quiz}
"""
quiz_evaluation_prompt = ChatPromptTemplate.from_template(review_template)
review_chain = quiz_evaluation_prompt | llm | StrOutputParser()

# Overall Chain
generate_evaluate_chain = (
    RunnablePassthrough.assign(
        quiz=quiz_chain
    )
    | RunnableParallel(
        quiz=lambda x: x["quiz"],
        review=review_chain
    )
)
