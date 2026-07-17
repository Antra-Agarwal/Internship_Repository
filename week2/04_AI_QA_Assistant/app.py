import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


def create_chain():
    """
    Creates and returns the LangChain pipeline.
    """

    # Load environment variables from .env
    load_dotenv()

    # Create Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3,
    )

    # Create Prompt Template
    prompt = PromptTemplate.from_template(
        """
You are an intelligent AI Question Answering Assistant.

Instructions:
- Answer accurately.
- Use simple and easy-to-understand language.
- Keep the answer concise (around 150-200 words unless the user asks for more).
- Use bullet points whenever appropriate.
- Give one real-world example if it helps explain the concept.
- If you are unsure about something, honestly say that you don't know instead of making up information.

Question:
{question}
"""
    )

    # Convert model response to plain string
    parser = StrOutputParser()

    # Create LangChain pipeline
    chain = prompt | llm | parser

    return chain


def main():
    """
    Runs the AI Question Answering Assistant.
    """

    chain = create_chain()

    print("=" * 70)
    print("🤖 AI Question Answering Assistant")
    print("Powered by LangChain + Google Gemini")
    print("Type 'exit', 'quit', or 'bye' to close the application.")
    print("=" * 70)

    while True:

        # Take user input
        question = input("\nAsk your question: ").strip()

        # Ignore empty input
        if not question:
            print("⚠️ Please enter a valid question.")
            continue

        # Exit condition
        if question.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Thank you for using the AI Question Answering Assistant!")
            break

        print("\nGenerating answer...\n")

        try:
            # Get AI response
            response = chain.invoke(
                {
                    "question": question
                }
            )

            print("-" * 70)
            print("Answer:\n")
            print(response)
            print("-" * 70)

        except Exception as e:

            error_message = str(e)

            # Handle API quota errors
            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print("❌ API quota exceeded or rate limit reached.")
                print("Please wait a minute and try again.")

            # Handle API key issues
            elif "API_KEY" in error_message.upper():
                print("❌ Invalid or missing Google API Key.")
                print("Please check your .env file.")

            # Any other error
            else:
                print("❌ An unexpected error occurred.")
                print(error_message)


if __name__ == "__main__":
    main()