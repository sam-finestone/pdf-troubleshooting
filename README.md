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

**Development:**
To start the application locally:

```bash
python run.py
```

The application will be available at <http://localhost:5001>.

**Production:**

Using Docker and Gunicorn with Nginx:

```bash
docker-compose up --build
```

This command builds and runs the Docker containers specified in the docker-compose.yml file, setting up Nginx as a reverse proxy to handle incoming traffic and serve the static files, and Gunicorn to run the Flask application.

***Docker Compose for Production:***

```yaml
version: '3.9'

services:
  app:
    build: .
    ports:
      - "5001:5001"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app
```

This configuration sets up Nginx to serve the application on port 80 and Gunicorn to run the Flask application internally.

## Testing
The application includes unit tests for API routes, OCR functionality, and integration with the OpenAI API:

Unit Tests: Test individual functions and components.
Integration Tests: Test the integration between the components and external APIs.

```bash
pytest tests/
```
## Acknowledgments
Powered by OpenAI's GPT models.
