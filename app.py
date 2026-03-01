from fastapi import FastAPI
from pydantic import BaseModel
from pdf_loader import load_and_split
from vector_store import create_vector_store, search
from ollama_client import ask_ollama
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
OLLAMA_URL = os.getenv("OLLAMA_URL")
TOP_K = int(os.getenv("TOP_K"))
app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

chunks = load_and_split("data/cv_oumansour_abdellatif.pdf")
index, stored_chunks = create_vector_store(chunks)

@app.post("/ask")
def ask_question(request: QuestionRequest):
    retrieved = search(request.question, index, stored_chunks, TOP_K)
    context = "\n".join(retrieved)

    answer = ask_ollama(context, request.question)
    print(f"Question: {request.question}")
    print(f"Context: {context}")
    print(f"Answer: {answer}")
    return {"answer": answer}