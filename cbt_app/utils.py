import pdfplumber
import re  # Add this import for regex

def extract_questions_from_pdf(pdf_path):
    questions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            parsed_questions = parse_questions(text)
            questions.extend(parsed_questions)

    return questions

def parse_questions(text):
    """
    Parses the raw text from the PDF into a list of dictionaries,
    where each dictionary represents a question and its answer options.
    """
    questions = []
    current_question = None

    # Simple regex patterns to capture questions and options
    question_pattern = re.compile(r"^\d+\.")  # Question number pattern
    option_pattern = re.compile(r"^[A-E]\.")  # Answer options pattern

    lines = text.split("\n")

    for line in lines:
        if question_pattern.match(line):  # Detect a new question
            if current_question:
                questions.append(current_question)  # Save the previous question
            current_question = {
                "question_main": line.strip(),
                "a": "",
                "b": "",
                "c": "",
                "d": "",
                "e": ""  # Option E is optional
            }
        elif option_pattern.match(line) and current_question:
            option_key = line[0].lower()  # 'A.' becomes 'a', 'B.' becomes 'b', etc.
            current_question[option_key] = line[2:].strip()  # Remove the option letter and period

    if current_question:  # Save the last question
        questions.append(current_question)

    return questions
