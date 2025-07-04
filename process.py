from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
import sys

csv_path = "restaurant_reviews.csv"

if not os.path.exists(csv_path):
    print(f"❌ CSV file not found: {csv_path}")
    sys.exit(1)

df = pd.read_csv(csv_path)

# Check required columns
required_columns = {"Title", "Review", "Rating", "Date"}
if not required_columns.issubset(df.columns):
    print(f"❌ CSV must contain these columns: {required_columns}")
    sys.exit(1)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        content = f"{row['Title']} {row['Review']}"
        doc = Document(
            page_content=content,
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(doc)

    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

    vector_store.add_documents(documents=documents, ids=ids)
else:
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
