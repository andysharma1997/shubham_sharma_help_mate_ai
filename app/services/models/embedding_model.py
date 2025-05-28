import torch
from sentence_transformers import SentenceTransformer
from app.utilities.chunk_utils import batch_iterable
from app.utilities import shubham_logger
from app.utilities.constants import Constants
from app.utilities.singleton_factory import Singleton
from typing import List
from tqdm import tqdm

logger = shubham_logger.ShubhamLogger(shubham_logger.get_logger(__name__),{"helpmate":"v1"})


class EmbeddModel(metaclass=Singleton):
    """
    Model implementation for text embeddings
    author: Shubham Sharma
    Args:
        metaclass (_type_, optional): _description_. Defaults to Singleton.
    """
    def __init__(self):
        self.model_name = Constants.fetch_constant("models")["embedding_model"]["name"]
        self.batch_size = Constants.fetch_constant("models")["embedding_model"]["batch_size"]
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model =  SentenceTransformer(self.model_name, device=self.device)
    
    def embedd(self,texts: List[str]):
        """
        This method will convert the raw text to the vector embeddings.
        author: Shubham Sharma

        Args:
            texts (List[str]): _description_
        """
        embeddings = []
        logger.info(f"Starting embedding {len(texts)} texts")
        for batch in tqdm(batch_iterable(iterable=texts,batch_size=self.batch_size),total=len(texts)//self.batch_size):
            embeddings.extend(self.model.encode(batch))
        return embeddings