import torch
import torch.nn as nn
from sentence_transformers import CrossEncoder
from app.utilities.chunk_utils import batch_iterable
from app.utilities import shubham_logger
from app.utilities.constants import Constants
from app.utilities.singleton_factory import Singleton
from typing import List
from tqdm import tqdm

logger = shubham_logger.ShubhamLogger(shubham_logger.get_logger(__name__),{"helpmate":"v1"})


class ReRankModel(metaclass=Singleton):
    """
    Model implementation for text embeddings
    author: Shubham Sharma
    Args:
        metaclass (_type_, optional): _description_. Defaults to Singleton.
    """
    def __init__(self):
        self.model_name = Constants.fetch_constant("models")["re-ranker"]["name"]
        self.batch_size = Constants.fetch_constant("models")["re-ranker"]["batch_size"]
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model =  CrossEncoder(self.model_name, activation_fn=nn.Sigmoid(),device=self.device)
    
    def re_rank(self,query: str, chunks: List[str],ids:List[str]):
        """
        This method will convert the raw text to the vector embeddings.s
        author: Shubham Sharma

        Args:
            texts (List[str]): _description_
        """
        pairs = [(query, chunk) for chunk in chunks]
        logger.info(f"Starting re-ranking of query={query} texts")
        scores = self.model.predict(pairs)
        sorted_pairs = sorted(zip(chunks, scores, ids), key=lambda x: x[1], reverse=True)
        return sorted_pairs

