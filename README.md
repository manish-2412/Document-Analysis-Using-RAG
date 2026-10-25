# Document Analysis Using RAG

A Retrieval-Augmented Generation (RAG) chatbot that enables users to upload PDF documents, query their contents, and receive accurate, document-grounded responses. The system integrates language processing for embeddings, vector storage for similarity retrieval, and an intuitive web interface.

---

## Features

- **PDF Processing**: Extracts text from uploaded PDF documents and splits it into manageable chunks for embedding and storage.
- **Embedding and Retrieval**: Uses Cohere's embeddings for encoding document chunks and Pinecone for scalable vector similarity search.
- **Question Answering**: Leverages Cohere's language models to generate accurate responses by retrieving and analyzing relevant document chunks.
- **Interactive Interface**: Provides a simple and intuitive interface using Streamlit for uploading documents, entering queries, and viewing results.

---

## Getting Started

Follow the steps below to run and interact with the project:

### 1. Clone the Repository

Clone the repository to your local system using the following command:

```bash
git clone https://github.com/manish-2412/Document-Analysis-Using-RAG.git
cd Document-Analysis-Using-RAG
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment and activate it to isolate project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python libraries using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

### 4. Obtain API Keys

Get your API keys for:

- Cohere: Sign up at Cohere to obtain an API key.
- Pinecone: Sign up at Pinecone to obtain an API key.
  These keys will be entered via the Streamlit interface when running the app.

### 5. Run the Application

Launch the Streamlit application:

```bash
cd src
streamlit run app.py
```

### 6. Access the Application

Once the application is running, open your browser and navigate to the URL provided by Streamlit, typically http://localhost:8501.

### 7. Upload a Document

Use the interface to upload a PDF file containing the content you want to query.

### 8. Ask Questions

- Enter your question in the query box. The chatbot will:

- Retrieve relevant chunks of text from the uploaded document.
- Generate a precise and context-aware response.

# Project Structure

```bash
├── app.py                # Main application file with Streamlit interface
├── vectorstore.py        # Handles PDF processing, embedding, and retrieval
├── chatbot.py            # Handles user interaction and response generation
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
```
