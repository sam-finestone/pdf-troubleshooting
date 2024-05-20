from pydantic import BaseModel, validator


class UploadSchema(BaseModel):
    filename: str

    @validator("filename")
    def check_filename(cls, value: str) -> str:
        """Ensure the filename ends with .pdf"""
        if not value.endswith(".pdf"):
            raise ValueError("Unsupported file type. Only PDF files are accepted.")
        return value
