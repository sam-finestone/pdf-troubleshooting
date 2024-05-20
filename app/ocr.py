from typing import List
from pdf2image import convert_from_path
import pytesseract
import tempfile

# def extract_text_from_pdf(pdf_path: str) -> str:
#     """
#     Convert a PDF file to images and extract text using OCR.

#     Args:
#     pdf_path (str): The file path to the PDF document.

#     Returns:
#     str: The concatenated text extracted from the PDF.
#     """
#     images = convert_from_path(pdf_path)
#     full_text = "\n".join(pytesseract.image_to_string(image) for image in images)
#     return full_text

# def extract_text_from_pdf(file: str) -> str:
#     # Save the file temporarily and convert to images
#     with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_pdf:
#         file.save(temp_pdf.name)
#         images = convert_from_path(temp_pdf.name)

#     # Concatenate text from all images
#     full_text = ""
#     for image in images:
#         full_text += pytesseract.image_to_string(image) + "\n"
#     return full_text
import pytesseract
from pdf2image import convert_from_path
import tempfile


def extract_text_from_pdf(file_storage) -> str:
    """
    Extracts text from a PDF file using OCR.

    Args:
    file_storage (FileStorage): A Flask FileStorage object containing the uploaded PDF file.

    Returns:
    str: The concatenated text extracted from all pages of the PDF.
    """
    # Save the file temporarily and convert to images
    try:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            file_storage.save(temp_pdf.name)
            images = convert_from_path(temp_pdf.name)
    except Exception as e:
        # Log error and return an error message or raise a custom exception
        print(f"Error processing PDF file: {str(e)}")
        return "Failed to process PDF file."

    # Concatenate text from all images
    full_text = ""
    try:
        for image in images:
            full_text += pytesseract.image_to_string(image) + "\n"
    except Exception as e:
        print(f"Error during OCR process: {str(e)}")
        return "Failed during OCR process."

    return full_text.strip()
