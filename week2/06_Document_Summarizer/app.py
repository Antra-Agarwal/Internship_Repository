import os

from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


SUMMARY_LENGTHS = {
    "1": "Short",
    "2": "Medium",
    "3": "Detailed",
}


def create_chain():
    """
    Creates and returns the LangChain pipeline.
    """

    load_dotenv()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3,
    )

    prompt = PromptTemplate.from_template(
        """
You are an expert document summarizer.

Summarize the following document.

Summary Length:
{summary_length}

Instructions:
- Preserve the main ideas.
- Use simple language.
- Use bullet points whenever appropriate.
- Do not include unnecessary details.

Document:

{text}
"""
    )

    parser = StrOutputParser()

    return prompt | llm | parser


def read_text_file(file_path):
    """
    Reads a text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf_file(file_path):
    """
    Reads a PDF file.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text(file_path):
    """
    Detects the file type and extracts text.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        return read_text_file(file_path)

    elif extension == ".pdf":
        return read_pdf_file(file_path)

    else:
        raise ValueError("Unsupported file type. Please provide a .txt or .pdf file.")


def get_summary_length():

    print("\nChoose Summary Length\n")

    for key, value in SUMMARY_LENGTHS.items():
        print(f"{key}. {value}")

    while True:

        choice = input("\nEnter choice: ").strip()

        if choice.lower() == "exit":
            return "exit"

        if choice in SUMMARY_LENGTHS:
            return SUMMARY_LENGTHS[choice]

        print("Invalid choice. Please try again.")


def save_summary(summary):

    choice = input("\nSave summary as a text file? (y/n): ").strip().lower()

    if choice != "y":
        return

    filename = input("Enter filename (without .txt): ").strip()

    if not filename:
        filename = "summary"

    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print(f"\n✅ Summary saved as '{filename}.txt'")


def main():

    chain = create_chain()

    print("=" * 75)
    print("📄 AI Document Summarizer")
    print("Powered by LangChain + Google Gemini")
    print("Supports .txt and .pdf files")
    print("Type 'exit' anytime to quit.")
    print("=" * 75)

    while True:

        file_path = input("\nEnter document path: ").strip()

        if file_path.lower() == "exit":
            break

        if not os.path.exists(file_path):
            print("❌ File not found.")
            continue

        summary_length = get_summary_length()

        if summary_length == "exit":
            break

        try:

            print("\nReading document...\n")

            document_text = extract_text(file_path)

            if not document_text.strip():
                print("❌ The document is empty.")
                continue

            print("Generating summary...\n")

            summary = chain.invoke(
                {
                    "summary_length": summary_length,
                    "text": document_text,
                }
            )

            print("-" * 75)
            print(summary)
            print("-" * 75)

            save_summary(summary)

        except Exception as e:

            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print("❌ API quota exceeded.")
                print("Please wait a minute and try again.")

            elif "API_KEY" in error_message.upper():
                print("❌ Invalid or missing Google API Key.")

            else:
                print("❌ Error:")
                print(error_message)

    print("\n👋 Thank you for using the AI Document Summarizer!")


if __name__ == "__main__":
    main()