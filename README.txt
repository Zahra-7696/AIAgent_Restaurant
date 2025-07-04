
🍕 AI-Powered Pizza Restaurant Chatbot
--------------------------------------

🔍 Aim:
This project is designed to build a conversational agent that can intelligently answer user queries about a pizza restaurant using customer review data. It leverages Generative AI to extract meaningful insights from restaurant reviews using Large Language Models (LLMs) and a vector database for semantic search.

📦 Tech Stack:
--------------
- LangChain: For chaining prompts and managing retrieval-based QA.
- Ollama: For running local large language models.
- LLMs Used:
  - `llama3.2` (for answering questions)
  - `mxbai-embed-large` (for generating embeddings)
- Vector Database: `ChromaDB` is used to store and retrieve semantically relevant reviews.

📁 Files:
---------
- `main.py`: Entry point of the chatbot. It initializes the LLM and handles user input/output.
- `process.py`: Handles loading, embedding, and storing restaurant reviews using ChromaDB.
- `restaurant_reviews.csv`: The dataset containing restaurant review data with columns: `Title`, `Review`, `Rating`, `Date`.

⚙️ How It Works:
----------------
1. When the app starts, it checks if a ChromaDB vector store already exists.
2. If not, it reads from `restaurant_reviews.csv`, creates embeddings using `mxbai-embed-large`, and stores them in ChromaDB.
3. The chatbot interface in `main.py` lets users ask questions.
4. The top-k most relevant reviews are retrieved semantically using vector similarity.
5. The retrieved reviews and the question are sent to `llama3.2` LLM to generate a contextual answer.

▶️ How to Run:
--------------
1. Make sure you have Python 3.10+ and Ollama installed and running.
2. Install required packages in a virtual environment:

   pip install langchain langchain_community langchain_ollama langchain_chroma pandas

3. Download and run the required models in Ollama:

   ollama run llama3
   ollama run mxbai-embed-large

4. Place your `restaurant_reviews.csv` in the same directory.
5. Run the chatbot:

   python main.py

6. Ask a question like:

   What is the best pizza in town?

7. To exit, type `q`.

📝 Notes:
---------
- Make sure the CSV file contains the required columns: `Title`, `Review`, `Rating`, `Date`.
- If you change the LLM or embedding model, update the `model=` argument in both `main.py` and `process.py`.

📧 Contact:
-----------
Maintainer: ZahraS. Torabi  
For feedback or issues, please raise an issue in the GitHub repo or contact via gmail: z.torabi.university@gmil.com
