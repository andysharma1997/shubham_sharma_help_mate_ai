import chromadb
from chromadb.config import Settings
from app.services.models.embedding_model import EmbeddModel
from app.utilities import shubham_logger
from app.utilities.constants import Constants
from app.utilities.singleton_factory import Singleton
from typing import List
from functools import lru_cache

logger = shubham_logger.ShubhamLogger(shubham_logger.get_logger(__name__),{"helpmate":"v1"})


class ChromaDBHandler(metaclass=Singleton):
    """
    Class to handle all the vector DB operations
    author: Shubham Sharma
    """
    def __init__(self, embed_model: EmbeddModel):
        """
        Constructor to initalize the vector Db
        author: Shubham Sharma

        Args:
            embed_model (EmbeddModel): _description_
        """
        
        self.client = chromadb.PersistentClient(path= Constants.fetch_constant("vector_store_settings")["persist_directory"])
        self.collection_name = Constants.fetch_constant("vector_store_settings")["collection_name"]
        self.collection = self.client.get_or_create_collection(self.collection_name)
        self.model = embed_model

    def add_documents(self, chunks: List[str], source="insurance_policy"):
        """
        This method will be used to add the documents and there embeddings to the vector store
        author: Shubham Sharma

        Args:
            chunks (List[str]): _description_
            source (str, optional): _description_. Defaults to "insurance_policy".
        """
        logger.info(f"Starting to add the {len(chunks)} to collection={self.collection_name}")
        embeddings = self.model.embedd(chunks)
        metadatas=[]
        ids = []
        for i,_chunk in enumerate(chunks):
            ids.append(f"{source}_chunk_{i}")
            metadatas.append({"source": source, "chunk_id": i})
        self.collection.add(documents=chunks,embeddings=embeddings,metadatas=metadatas,ids=ids)

    @lru_cache(maxsize=32)
    def query(self, query_text: str, top_k: int=Constants.fetch_constant("vector_store_settings")["top_k"]):
        """
        This method is used to retrive the top_k closest documents for a given query 
        author: Shubham Sharma

        Args:
            query_text (str): _description_
            top_k (int, optional): _description_. Defaults to Constants.fetch_constant("vector_store_settings")["top_k"].

        Returns:
            _type_: _description_
        """
        logger.info(f"feteching {top_k} results for query={query_text}")
        query_embedding = self.model.embedd([query_text])[0]
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results["documents"][0], results["ids"][0]

    def reset_collection(self):
        """
        This method is used to reset the collection.
        """
        logger.warning(f"Resetting the collection={self.collection_name}")
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(self.collection.name)
