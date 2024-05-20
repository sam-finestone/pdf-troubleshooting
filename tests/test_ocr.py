from unittest.mock import patch, MagicMock
from werkzeug.datastructures import FileStorage
from io import BytesIO
import pytest

# Assuming these functions are defined in a module called `ocr` within the `services` package.
from app.ocr import extract_text_from_pdf


def create_file_storage(content=b"dummy PDF content", filename="test.pdf"):
    return FileStorage(
        stream=BytesIO(content), filename=filename, content_type="application/pdf"
    )


@pytest.fixture
def valid_pdf():
    """Fixture to create a mock PDF file with valid content."""
    return create_file_storage()


@pytest.fixture
def empty_pdf():
    """Fixture to create a mock empty PDF file."""
    return create_file_storage(content=b"")


@pytest.mark.usefixtures("valid_pdf", "empty_pdf")
class TestOCR:
    """
    Test suite for the OCR functionality within the 'ocr' module.

    Covers various scenarios to ensure robustness of the text extraction from PDF files:
    - `test_extract_text_from_valid_pdf`: Tests the function's ability to correctly extract text from a standard PDF with readable content. Ensures that text extraction returns the expected output when everything functions as it should.
    - `test_extract_text_from_empty_pdf`: Tests the function's handling of an empty PDF file. Verifies that the function returns an empty string, indicating no text was extracted, which is the expected behavior for empty documents.
    - `test_extract_text_from_non_english_pdf`: Tests OCR capabilities on a PDF containing non-English (Japanese in this case) characters. This checks the function's ability to handle and accurately extract text from PDFs with various character sets.
    """

    @patch("app.ocr.convert_from_path")
    @patch(
        "app.ocr.pytesseract.image_to_string", return_value="Extracted text"
    )
    def test_extract_text_from_valid_pdf(
        self, mock_image_to_string, mock_convert_from_path, valid_pdf
    ):
        """
        Validates that text is extracted correctly from a typical PDF file containing standard text.
        The test ensures that both the convert_from_path and image_to_string functions are called and return the expected output.
        """
        image_mock = MagicMock()
        mock_convert_from_path.return_value = [image_mock]
        assert extract_text_from_pdf(valid_pdf) == "Extracted text"

    @patch("app.ocr.convert_from_path", return_value=[])
    def test_extract_text_from_empty_pdf(self, mock_convert_from_path, empty_pdf):
        """
        Ensures that the function handles empty PDF files gracefully.
        Tests that no images are processed and verifies the function returns an empty string as no text is present to extract.
        """
        assert extract_text_from_pdf(empty_pdf) == ""

    @patch("app.ocr.convert_from_path")
    @patch("app.ocr.pytesseract.image_to_string", return_value="テスト")
    def test_extract_text_from_non_english_pdf(
        self, mock_image_to_string, mock_convert_from_path, valid_pdf
    ):
        """
        Checks the OCR function's ability to extract non-English text (Japanese in this example) from a PDF.
        This test is crucial for applications requiring internationalization support, ensuring that text extraction is not limited to ASCII characters.
        """
        image_mock = MagicMock()
        mock_convert_from_path.return_value = [image_mock]
        assert extract_text_from_pdf(valid_pdf) == "テスト"
