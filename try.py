import streamlit as st
import pandas as pd
import json
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App
st.title("Unified Search System: CSV & JSON Knowledge Base")
st.markdown("""
Upload both CSV and JSON files as your knowledge base, and query across them to find the top 5 most relevant URLs.
""")

# Check if OpenAI API key is available
if not openai_api_key:
    st.error("OpenAI API key not found. Please ensure it's set in the .env file.")
else:
    # File uploaders for CSV and JSON files
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    json_file = st.file_uploader("Upload a JSON file", type=["json"])

    # List to hold all documents
    documents = []

    # Process the CSV file
    if csv_file is not None:
        try:
            # Read CSV
            csv_data = pd.read_csv(csv_file)
            st.success("CSV file uploaded successfully!")

            # Convert each row into a Document object
            for index, row in csv_data.iterrows():
                documents.append(
                    Document(
                        page_content=row["question"] + " " + row["answer"],
                        metadata={"url": row["url"], "source": "CSV"}
                    )
                )
        except Exception as e:
            st.error(f"Error processing the CSV file: {e}")

    # Process the JSON file
    if json_file is not None:
        try:
            # Read JSON
            json_data = json.load(json_file)
            st.success("JSON file uploaded successfully!")

            # Convert each key-value pair into a Document object
            for key, value in json_data.items():
                documents.append(
                    Document(
                        page_content=value["text"],
                        metadata={"url": key, "title": value.get("title", "No Title"), "source": "JSON"}
                    )
                )
        except Exception as e:
            st.error(f"Error processing the JSON file: {e}")

    # Proceed if documents are available
    if documents:
        try:
            # Initialize embeddings and vector store
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            vectorstore = FAISS.from_documents(documents, embeddings)
            st.success("Knowledge base indexed successfully!")

            # Query input
            query = st.text_input("Ask a question", placeholder="E.g., How do I integrate ClearFeed with MS Teams?")

            if query:
                with st.spinner("Searching for the most relevant URLs..."):
                    try:
                        # Perform similarity search for top 5 results
                        results = vectorstore.similarity_search(query, k=5)
                        st.success("Search completed!")

                        # Display results
                        st.markdown("### Top 5 Relevant URLs:")
                        for i, result in enumerate(results, 1):
                            url = result.metadata.get("url", "No URL")
                            title = result.metadata.get("title", "No Title")
                            snippet = result.page_content[:200]  # Display first 200 characters
                            if url != "No URL":
                                st.markdown(f"**{i}. [{title}]({url})**")
                                st.write(f"Snippet: {snippet}...\n")
                            else:
                                st.write(f"**{i}. No URL Available**")
                                st.write(f"Snippet: {snippet}...\n")
                    except Exception as e:
                        st.error(f"Error processing the query: {e}")
        except Exception as e:
            st.error(f"Error initializing the knowledge base: {e}")
    else:
        st.warning("Please upload at least one file to begin.")

# Footer
st.markdown("---")
st.caption("Powered by OpenAI & LangChain")
