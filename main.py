from pdfminer.high_level import extract_text
from json_helper import InputData as input
import time

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

start_time = time.time()
text = extract_text_from_pdf(r'C:\Users\Ankush Agnihotri\Documents\AnkushResume.pdf')
print(f"Text extraction time: {time.time() - start_time} seconds")

llm = input.llm()

try:
    start_time = time.time()
    data = llm.invoke(input.input_data(text))
    print(f"Ollama processing time: {time.time() - start_time} seconds")
    print(data)
except Exception as e:
    print(f"Error during LLM invocation: {e}")