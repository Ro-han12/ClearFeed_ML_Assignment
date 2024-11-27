# Unified Search System: CSV & JSON Knowledge Base

This is a **Streamlit application** designed to create a unified search system that allows you to upload CSV and JSON files as a knowledge base. Users can query across these files to find the **top 5 most relevant URLs**.

---

## Features

- **File Upload**:
  - Upload **CSV** files containing questions, answers, and URLs.
  - Upload **JSON** files with textual data mapped to URLs and optional titles.

- **Knowledge Base Creation**:
  - Indexes the uploaded data using **FAISS** (a vector search library).
  - Embeds documents using **OpenAI embeddings**.

- **Query and Retrieve**:
  - Accepts user queries.
  - Returns the **top 5 most relevant URLs** with snippets of the corresponding content.

- **Error Handling**:
  - Validates file uploads and API key configurations.
  - Graceful error messages for issues in processing files or queries.

---

## Requirements

### Python Libraries
- **Streamlit**: For building the web application.
- **Pandas**: To handle CSV files.
- **LangChain**: For document handling and embedding.
- **FAISS**: For efficient similarity search.
- **dotenv**: To manage environment variables.
- **OpenAI API**: To generate embeddings.

Install dependencies using:
```bash
pip install streamlit pandas langchain faiss-cpu python-dotenv openai
```

---

## Usage

### 1. Setup
- Create a `.env` file in the project root directory with your OpenAI API key:
  ```env
  OPENAI_API_KEY=your_openai_api_key_here
  ```

### 2. Run the Application
Run the Streamlit app locally:
```bash
streamlit run app.py
```

### 3. Upload Files
- Upload a **CSV** file with the following columns:
  - `question`
  - `answer`
  - `url`
  
- Upload a **JSON** file with a structure like:
  ```json
  {
      "url_1": {
          "text": "Some content for this URL.",
          "title": "Optional Title"
      },
      "url_2": {
          "text": "Another content block."
      }
  }
  ```

### 4. Query the Knowledge Base
- Type your question in the text box (e.g., *"How do I integrate ClearFeed with MS Teams?"*).
- The app retrieves the **top 5 URLs** and displays their titles, snippets, and links.

---

## Example Workflow

1. **File Upload**:
    - CSV: *Uploaded successfully.*
    - JSON: *Uploaded successfully.*
    
2. **Query Input**:
    ```
    How do I integrate ClearFeed with MS Teams?
    ```

3. **Results**:
    ```
    1. [Integration Guide](https://example.com/clearfeed-teams-integration)
       Snippet: ClearFeed can be integrated with Microsoft Teams by...

    2. [Getting Started](https://example.com/getting-started)
       Snippet: To start with ClearFeed on MS Teams...
    ```

---

## Troubleshooting

### Missing API Key
If the OpenAI API key is not configured:
```plaintext
OpenAI API key not found. Please ensure it's set in the .env file.
```

### File Format Errors
- Ensure CSV files contain the columns: `question`, `answer`, `url`.
- Ensure JSON files are properly formatted key-value pairs.

---

## Acknowledgments
- **OpenAI**: For embedding generation.
- **LangChain**: For document processing and vector store integration.
- **FAISS**: For efficient similarity search.
- **Streamlit**: For rapid web app development. 

---

**Powered by OpenAI & LangChain**  
For feedback or contributions, contact: `rohannair2939@gmail.com`
