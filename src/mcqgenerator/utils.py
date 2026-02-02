import json
import PyPDF2
import traceback
from io import BytesIO
from docx import Document


def read_file(file):
    """
    Reads PDF, TXT, or DOCX file and returns extracted text
    """
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        try:
            text = ""
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except Exception as e:
            raise RuntimeError("Error reading PDF file") from e

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif filename.endswith(".docx"):
        try:
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            raise RuntimeError("Error reading DOCX file") from e

    else:
        raise ValueError("Unsupported file format. Only PDF, TXT, and DOCX are supported.")


def get_table_data(quiz, show_correct=True):
    """
    Converts quiz dict to table data for display
    """
    try:
        # If quiz is string → parse JSON
        if isinstance(quiz, str):
            quiz_dict = json.loads(quiz)
        elif isinstance(quiz, dict):
            quiz_dict = quiz
        else:
            raise TypeError("Quiz must be a dict or JSON string")

        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(f"{k} -> {v}" for k, v in value["options"].items())
            correct = value["correct"] if show_correct else "Hidden"

            quiz_table_data.append({
                "MCQ": mcq,
                "Choices": options,
                "Correct": correct
            })

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return None



