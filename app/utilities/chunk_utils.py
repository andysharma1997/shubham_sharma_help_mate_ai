from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.utilities.constants import Constants
from typing import Iterable, List, Generator, TypeVar

T = TypeVar('T')



def chunk_text(text: str):
    """
    Utility to chunk the large text into small size with overlapping of text.
    author: Shubham Sharma
    Args:
        text (str): _description_
        chunk_size (int, optional): _description_. Defaults to 500.
        chunk_overlap (int, optional): _description_. Defaults to 50.

    Returns:
        _type_: _description_
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Constants.fetch_constant("chunk_settings")["chunk_size"],
        chunk_overlap=Constants.fetch_constant("chunk_settings")["chunk_overlap"],
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)




def batch_iterable(iterable: Iterable[T], batch_size: int) -> Generator[List[T], None, None]:
    """
    Splits an iterable into batches of a given size.

    Args:
        iterable (Iterable): Any iterable (list, generator, etc.)
        batch_size (int): Number of elements per batch.

    Yields:
        Generator[List]: A generator of batches (lists) of elements.
    """
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
