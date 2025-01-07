import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
import openai

# Set your OpenAI API key
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
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = openai.completions.create(
        model = "gpt-3.5-turbo-instruct",
       temperature = 0,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Sidebar
st.sidebar.title("PDF Chat Assistant")
st.sidebar.write("Upload PDFs and ask questions based on their content.")

uploaded_files = st.sidebar.file_uploader("Upload PDF(s)", type="pdf", accept_multiple_files=True)

st.sidebar.write("---")
st.sidebar.write("Built with 💙 using Streamlit, SentenceTransformers, and OpenAI.")

# Main app layout
st.title("📄 PDF Chat Assistant")
st.write(
    "Upload one or more PDFs, extract their content, and ask questions based on the extracted text."
)

if uploaded_files:
    all_texts = []
    for uploaded_file in uploaded_files:
        file_path = f"./temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf(file_path)
        all_texts.append(text)
    
    context = " ".join(all_texts)
    
    # Display extracted text
    with st.expander("📜 Extracted Text Preview", expanded=False):
        st.text_area("Preview", context[:3000], height=200)
    
    # User question input
    question = st.text_input("💬 Ask a question based on the PDF content:")
    
    if question:
        with st.spinner("Generating answer..."):
            answer = get_answer(question, context)
        
        st.success("Answer:")
        st.write(answer)
else:
    st.info("Please upload at least one PDF to start.")




