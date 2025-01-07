import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
import openai

# Set your OpenAI API key directly (use secret management in production)
openai.api_key = "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"

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Generate embeddings
def generate_embeddings(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text, show_progress_bar=True)

# Get answer using ChatCompletion
def get_answer(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ],
        max_tokens=150,
        temperature=0.5
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app UI
st.title("PDF Question-Answering App")
st.write("Upload a PDF, extract text, and get answers to your questions.")

uploaded_files = st.file_uploader("Upload PDF(s)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    all_texts = []
    for uploaded_file in uploaded_files:
        file_path = f"./temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf(file_path)
        all_texts.append(text)
    
    context = " ".join(all_texts)
    st.write("Extracted Text Preview:")
    st.text(context[:1000])  # Show first 1000 characters of extracted text
    
    question = st.text_input("Ask a question based on the PDF content:")
    
    if question:
        answer = get_answer(question, context)
        st.write("Answer:")
        st.write(answer)


