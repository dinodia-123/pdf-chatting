
import streamlit as st
import openai
import pdfplumber
from sentence_transformers import SentenceTransformer

# Set your OpenAI API key
openai.api_key = "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"

# Initialize the embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to extract text from PDF
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to split text into manageable chunks
def split_text(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to get answers using OpenAI API
def get_answer(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # gpt-3.5-turbo-instruct is not available, gpt-3.5-turbo is valid
            temperature=0,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Chat with Your PDF", layout="wide")
st.title("📄 Chat with Your PDF")

# Sidebar for PDF upload
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    # Display extracted content
    st.subheader("Extracted Content")
    st.text_area("Content from PDF:", text, height=300)

    # Split text into manageable chunks
    chunks = split_text(text)
    st.write(f"🔹 **PDF split into {len(chunks)} chunks for efficient processing.**")

    # Ask a question
    st.subheader("Ask a Question")
    question = st.text_input("Type your question here:")

    if question:
        # Use the first chunk as context for simplicity
        context = chunks[0]
        with st.spinner("Generating answer..."):
            answer = get_answer(question, context)
        st.success("Answer:")
        st.write(answer)

    # Optional: Display all chunks (debugging or transparency)
    with st.expander("Show all chunks (for debugging purposes)"):
        for i, chunk in enumerate(chunks):
            st.write(f"**Chunk {i+1}:** {chunk}")

else:
    st.info("Please upload a PDF file to get started.")
