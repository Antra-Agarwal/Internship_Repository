import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


EMAIL_TYPES = {
    "1": "Leave Application",
    "2": "Resignation",
    "3": "Thank You",
    "4": "Apology",
    "5": "Meeting Request",
    "6": "Job Application",
    "7": "Follow-up",
}

TONES = {
    "1": "Professional",
    "2": "Formal",
    "3": "Friendly",
}


def create_chain():
    """Creates and returns the LangChain pipeline."""

    load_dotenv()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.5,
    )

    prompt = PromptTemplate.from_template(
        """
You are an expert email writer.

Generate a well-structured email using the information below.

Email Type:
{email_type}

Recipient:
{recipient}

Tone:
{tone}

Purpose:
{purpose}

Sender Name:
{sender}

Instructions:
- Generate a suitable subject line.
- Begin with an appropriate greeting.
- Keep the tone consistent.
- Write a clear and concise email.
- End with a polite closing.
- If the sender name is provided, include it in the signature.
- If the sender name is not provided, end politely without adding a name.
- Do not use placeholders like [Your Name].
"""
    )

    parser = StrOutputParser()

    return prompt | llm | parser


def display_email_menu():

    print("\nChoose Email Type\n")

    for key, value in EMAIL_TYPES.items():
        print(f"{key}. {value}")

    print("\nOr type your own email type.")


def get_email_type():

    while True:

        display_email_menu()

        choice = input("\nEnter choice or custom email type: ").strip()

        if choice.lower() == "exit":
            return "exit"

        if choice in EMAIL_TYPES:
            return EMAIL_TYPES[choice]

        if choice:
            return choice

        print("⚠️ Please enter a valid email type.")


def display_tone_menu():

    print("\nChoose Tone\n")

    for key, value in TONES.items():
        print(f"{key}. {value}")


def get_tone():

    while True:

        display_tone_menu()

        choice = input("\nEnter choice: ").strip()

        if choice.lower() == "exit":
            return "exit"

        if choice in TONES:
            return TONES[choice]

        print("⚠️ Invalid choice. Please try again.")


def save_email(email):

    choice = input("\nSave this email as a text file? (y/n): ").strip().lower()

    if choice != "y":
        return

    filename = input("Enter filename (without .txt): ").strip()

    if not filename:
        filename = "generated_email"

    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        file.write(email)

    print(f"\n✅ Email saved as '{filename}.txt'")


def generate_email(chain, email_type, recipient, tone, purpose, sender):

    return chain.invoke(
        {
            "email_type": email_type,
            "recipient": recipient,
            "tone": tone,
            "purpose": purpose,
            "sender": sender if sender else "",
        }
    )


def main():

    chain = create_chain()

    print("=" * 75)
    print("📧 AI Email Generator")
    print("Powered by LangChain + Google Gemini")
    print("Type 'exit' at any prompt to quit.")
    print("=" * 75)

    while True:

        email_type = get_email_type()

        if email_type == "exit":
            break

        recipient = input("\nRecipient: ").strip()

        if recipient.lower() == "exit":
            break

        if not recipient:
            print("⚠️ Recipient cannot be empty.")
            continue

        tone = get_tone()

        if tone == "exit":
            break

        purpose = input("\nPurpose of the Email: ").strip()

        if purpose.lower() == "exit":
            break

        if not purpose:
            print("⚠️ Purpose cannot be empty.")
            continue

        sender = input("\nSender Name (Optional): ").strip()

        if sender.lower() == "exit":
            break

        print("\nGenerating email...\n")

        try:

            response = generate_email(
                chain,
                email_type,
                recipient,
                tone,
                purpose,
                sender,
            )

            print("-" * 75)
            print(response)
            print("-" * 75)

            save_email(response)

            while True:

                regenerate = input(
                    "\nGenerate another version of the same email? (y/n): "
                ).strip().lower()

                if regenerate == "n":
                    break

                if regenerate != "y":
                    print("Please enter 'y' or 'n'.")
                    continue

                print("\nGenerating another version...\n")

                response = generate_email(
                    chain,
                    email_type,
                    recipient,
                    tone,
                    purpose,
                    sender,
                )

                print("-" * 75)
                print(response)
                print("-" * 75)

                save_email(response)

        except Exception as e:

            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print("\n❌ API quota exceeded.")
                print("Please wait a minute and try again.")

            elif "API_KEY" in error_message.upper():
                print("\n❌ Invalid or missing Google API Key.")
                print("Please check your .env file.")

            else:
                print("\n❌ An unexpected error occurred.")
                print(error_message)

    print("\n👋 Thank you for using the AI Email Generator!")


if __name__ == "__main__":
    main()