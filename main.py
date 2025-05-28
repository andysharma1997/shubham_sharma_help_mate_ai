import streamlit as st
import tempfile
import pandas as pd
from dotenv import load_dotenv
from app.services.vector_store import ChromaDBHandler
from app.services.models.embedding_model import EmbeddModel
from app.services.models.re_ranker_model import ReRankModel
from app.services.generate_answer import generate_prompt, get_answer_from_openai
from app.utilities.pdf_utils import extract_text_from_pdf
from app.utilities.chunk_utils import chunk_text


load_dotenv()

embedd_model = EmbeddModel()
re_ranker_model = ReRankModel()

if 'db' not in st.session_state:
    st.session_state.db = ChromaDBHandler(embedd_model)

st.title("📄 Mr.HelpMate AI")


st.header("📤 Upload PDF and Create Vector Store")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.success("PDF uploaded successfully.")
    st.info("Extracting text and chunking...")
    
    text = extract_text_from_pdf(tmp_path)
    chunks = chunk_text(text)

    st.info(f"Embedding {len(chunks)} chunks into ChromaDB...")
    st.session_state.db.reset_collection()
    st.session_state.db.add_documents(chunks)
    st.success("Vector store created successfully!")

# Section 2: Query the system
st.header("🔍 Query the System")
query = st.text_input("Enter your question about the policy:")
query_button = st.button("Search")

if query and query_button:
    st.info("Searching ...")
    top_docs, top_ids = st.session_state.db.query(query)

    if top_docs:
        # Re-rank documents (assume function exists)
        st.info("Re-ranking retrieved documents...")
        reranked = re_ranker_model.re_rank(query, top_docs,top_ids)

        # Section 3: Generated Output
        st.header("🧠 Generated Output")
        prompt = generate_prompt(query,[doc[0] for doc in reranked[:5]])

        top_answer =  get_answer_from_openai(prompt) # Simplified, can plug into LLM later
        st.write(top_answer)
        
        st.header("📑 Retrieved Documents")
        data = [{"DocumentID": idx,"Text": doc} for idx,doc in zip(top_ids,top_docs)]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.header("📑 Top-5 Re-ranked Documents Used for Generation with Scores")
        data = [{"DocumentID": doc[2], "Score": round(doc[1], 4), "Text": doc[0]} for doc in reranked[:5]]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.header("📑 Retrieved Documents")
        st.write("No Documents found, please upload the documents to create the DB")