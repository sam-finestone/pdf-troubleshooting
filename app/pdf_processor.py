from typing import Dict
import openai

def extract_troubleshooting_info(full_text: str, client: openai.OpenAI) -> dict:
    """
    Analyze the extracted text and summarize troubleshooting information by sections,
    including the locations within the document.

    Args:
        full_text (str): The full text from the OCR process.
        client (openai.OpenAI): The OpenAI client configured with an API key.

    Returns:
        dict: A dictionary containing structured troubleshooting information, with details
              and locations.
    """
    # prompt = (
    #     "You are reviewing a technical manual. Please extract all troubleshooting information, "
    #     "organize it by sections as presented in the manual, and specify the page numbers or "
    #     "section titles where each piece of troubleshooting information is located. Summarize "
    #     "the troubleshooting steps or tips for each section. Provide the output in a structured "
    #     "format that includes both the content and its location within the document."
    # )
    prompt = (
        "Locate the 'Troubleshoot' section in the document provided below. Extract and summarize "
        "all the troubleshooting information from this section. Include a detailed structure of the "
        "troubleshooting steps or tips mentioned. For each piece of information, specify the exact "
        "location within the document, such as page number or section titles, so that a front-end "
        "application can display references or citations to these sources. Provide this information "
        "in a structured format that clearly delineates content and its corresponding location."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt + "\n\n" + full_text}],
            max_tokens=1024,  # Adjust token limit based on needs and model capacity
        )
        troubleshooting_info = response.choices[0].message.content.strip()
        return {"troubleshooting_info": troubleshooting_info}
    except Exception as e:
        return {"error": str(e)}