# from flask import Flask
# from dotenv import load_dotenv
# import os

# def create_app():
#     """
#     Create a Flask application instance.
#     """
#     load_dotenv()
#     app = Flask(__name__, template_folder="../templates")  # Ensure this path is correct based on your structure
#     app.config["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#     from .api import main
#     app.register_blueprint(main)

#     return app
# Load .env file explicitly
# load_dotenv()

# # Now you can use os.getenv to access your environment variables
# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError("No API Key found. Check your .env file.")
from flask import Flask
from dotenv import load_dotenv
import os
from pathlib import Path

def create_app():
    # Explicitly specify the path to the .env file
    dotenv_path = os.path.join(Path(os.path.dirname(__file__)).parent, ".env")
    load_dotenv(dotenv_path)

    app = Flask(__name__, template_folder="../templates")
    app.config["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    if not app.config["OPENAI_API_KEY"]:
        raise Exception("API key not loaded from .env")

    from .api import main

    app.register_blueprint(main)

    return app
