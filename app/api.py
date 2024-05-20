from flask import Blueprint, request, jsonify, render_template, current_app
from openai import OpenAI
from .ocr import extract_text_from_pdf
from .pdf_processor import extract_troubleshooting_info
from .schemas.upload_schema import UploadSchema
from pydantic import ValidationError

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/upload-pdf", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    try:
        UploadSchema(filename=file.filename)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    full_text = extract_text_from_pdf(file)  
    api_key = current_app.config["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
    result = extract_troubleshooting_info(
        full_text, client
    )  
    return jsonify(result)
