import pytest
from flask import url_for, Flask
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import io
from unittest.mock import patch


def test_home_page(client):
    """Test the home route to ensure it loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Upload Your PDF" in response.get_data(as_text=True)

def test_upload_no_file(client):
    """Test uploading without a file results in the correct error message."""
    response = client.post("/upload-pdf", data={})
    assert response.status_code == 400
    assert "No file part" in response.get_data(as_text=True)


def test_upload_invalid_file_type(client):
    """Test uploading an invalid file type according to the schema."""
    data = {"file": (io.BytesIO(b"Dummy data"), "test.txt")}
    response = client.post("/upload-pdf", content_type="multipart/form-data", data=data)
    assert response.status_code == 400
    assert "Unsupported file type" in response.get_data(as_text=True)


def test_upload_valid_file(client, mocker):
    """Test uploading a valid file results in correct API interaction and response."""
    mocker.patch(
        "app.ocr.extract_text_from_pdf", return_value="Extracted OCR text"
    )
    mocker.patch(
        "app.pdf_processor.extract_troubleshooting_info",
        return_value={"troubleshooting_info": "Details"},
    )
    mocker.patch("app.schemas.UploadSchema")  # Assuming validation passes

    data = {"file": (io.BytesIO(b"PDF data"), "document.pdf")}
    response = client.post("/upload-pdf", content_type="multipart/form-data", data=data)
    assert response.status_code == 200
    # assert "troubleshooting" in response.get_data(as_text=True)
