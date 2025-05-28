import pdfplumber
from app.utilities import shubham_logger

logger = shubham_logger.ShubhamLogger(shubham_logger.get_logger(__name__),{"helpmate":"v1"})

def extract_text_from_pdf(pdf_path: str):
    """
    Utility function to extract text from the pdf
    author: Shubham Sharma

    Args:
        pdf_path (str): _description_

    Returns:
        _type_: _description_
    """
    logger.info(f"Extracting text from pdf {pdf_path}")
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # Skip pages with no extractable text
                full_text += text + "\n"
    logger.info(f"PDF {pdf_path} parsing completed")
    return full_text
