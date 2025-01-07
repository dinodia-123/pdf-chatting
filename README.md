# PDF Chatting Application
This application allows you to upload PDF files and interact with them by asking questions. The app uses a powerful combination of OpenAI's GPT models and sentence embeddings to extract relevant information from the PDFs, highlight the relevant sections, and generate answers to your questions.

You can upload PDFs, and the system will process them to give intelligent responses based on the contents.

# Live Demo (Working)
Check out the live version of the app here:
https://pdf-chatting-rk9x8yun7wuszdmzrdevq2.streamlit.app/


# Features
Upload PDF files: Allows you to upload PDFs for processing.
Extract and process text: Extracts text from the uploaded PDFs and splits them into chunks for better performance.
Ask questions: You can ask questions, and the app will generate an answer based on the content of the uploaded PDFs.
Highlight relevant sections: The app highlights sections in the PDF that are relevant to the question asked.
# Prerequisites
Before you start, you need to have the following installed:

Python 3.7 or later
pip
You will also need a OpenAI API Key. You can obtain your API key from OpenAI's official website by creating an account: OpenAI.

Setup Instructions
1. Clone the Repository
Clone the repository to your local machine (or your cloud setup):

bash
Copy code
git clone https://github.com/yourusername/pdf-chatting.git
2. Install the Required Dependencies
Navigate to the project directory and install the required packages using pip:

bash
Copy code
cd pdf-chatting
pip install -r requirements.txt
3. Set Your OpenAI API Key
In the app.py file, replace the openai.api_key with your actual OpenAI API key:

python
Copy code
openai.api_key = "your-openai-api-key"
Alternatively, you can set the key using environment variables for better security (recommended for production):

bash
Copy code
export OPENAI_API_KEY="your-openai-api-key"
In your code, you can access the key using:

python
Copy code
openai.api_key = os.getenv("OPENAI_API_KEY")
4. Run the App Locally
After setting everything up, you can start the app locally using Streamlit:

bash
Copy code
streamlit run app.py
This will open the app in your default browser at http://localhost:8501.

# Usage Instructions
Upload PDFs: On the sidebar, you will see an option to upload one or more PDF files. You can select multiple PDFs and upload them for processing.

Ask a Question: Once the PDFs are uploaded, you can enter a question in the input box at the center of the app. The app will process the PDF content and display an answer based on the extracted text.

View Answer: After submitting a question, the app will display an answer based on the context from the uploaded PDFs. It will use OpenAI's GPT model to generate an intelligent response.

See Relevant Text: If relevant chunks from the PDF content were found, they will be highlighted and displayed.

Cross-Document Queries: If you upload multiple PDFs, the system will allow you to query across all uploaded documents and return answers based on the combined content.

# Deployment
You can deploy this application using Streamlit Cloud, Hugging Face Spaces, or your own cloud provider.

For Streamlit Cloud deployment:

Create an account at Streamlit Cloud.
Link your GitHub repository or upload your files.
Follow the steps to deploy the app online.
For Hugging Face Spaces deployment:

Create an account at Hugging Face.
Create a new space.
Upload your project and deploy the app.
# Files Overview
app.py: Main Streamlit application file, contains the logic for PDF extraction, question-answering, and user interface.
requirements.txt: Contains all the necessary Python libraries and dependencies required to run the app.
# Libraries Used
openai: To interface with the OpenAI GPT models for question answering.
streamlit: To create the interactive web interface.
PyPDF2: For PDF file reading and extracting text.
sentence-transformers: For generating sentence embeddings from PDF content.
pdfplumber: To extract text and data from PDFs, especially if the PDFs are scanned or contain non-standard text encoding.
