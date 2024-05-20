# PDF Troubleshooting Information Extractor
This Python Flask application extracts troubleshooting information from uploaded PDF files using Optical Character Recognition (OCR) and the OpenAI GPT model to process and analyze the text. 

## Approach

- PDF File Upload: Users can upload PDF documents to extract troubleshooting information.
- OCR Processing: Converts images in PDFs to text for analysis.
- OpenAI Integration: Utilizes OpenAI's powerful GPT models to analyze text and extract structured troubleshooting information.
- Flask Web Server: Provides a web interface for interacting with the application.

# Getting Started

## Prerequisites

- Python 3.8+
- Flask
- OpenAI API Key

Libraries: openai, flask, pytesseract, pdf2image, python-dotenv

## Installation
Clone the repository
```bash
git clone <https://github.com/sam-finestone/pdf-troubleshooting.git>
cd pdf-troubleshooting
```

Install dependencies

```bash
pip install -r requirements.txt
```

Set up environment variables

Create a .env file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY='your_openai_api_key_here'
```

## Running the Application
To start the application locally:

```bash
python run.py
```

The application will be available at <http://localhost:5000>.

## Testing
To ensure reliability and maintainability, tests are written using pytest. To run the tests:

```bash
pytest
```

Ensure you have test configurations set in your Flask application or set up a separate test instance with mock data for testing purposes.

### How to Run Tests
The application includes unit tests for API routes, OCR functionality, and integration with the OpenAI API:

Unit Tests: Test individual functions and components.
Integration Tests: Test the integration between the components and external APIs.

```bash
pytest tests/
```

## Deployment
For deployment, ensure that you configure production-grade environment settings. Do not run the application in debug mode in production.

## Acknowledgments
Powered by OpenAI's GPT models.