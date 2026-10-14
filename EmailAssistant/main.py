from input_module import get_customer_input
from intent_module import detect_intent
from retrieval_module import load_emails, retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


def complete_email_assistant():

    print("\n" + "=" * 50)
    print("       INTELLIGENT EMAIL ASSISTANT")
    print("=" * 50)

    # Q1 - User Input
    customer_name, subject, customer_email = get_customer_input()

    # Q3 - Intent Detection
    print("\nProcessing customer intent...")
    intent = detect_intent(customer_email)

    # Q4 & Q5 - Load CSV and Retrieve Similar Email
    print("\nSearching previous customer interactions...")

    df = load_emails()

    previous_email, previous_reply = retrieve_similar_email(
        customer_email,
        df
    )

    # Q6 - AI Reply Generation
    print("\nGenerating professional reply...")

    generated_reply = generate_reply(
        customer_email,
        previous_reply
    )

    # Q7 - Tone Improvement
    print("\n===== Tone Improvement =====")
    print("1. Friendly")
    print("2. Formal")
    print("3. Empathetic")

    tone_choice = input("Choose a tone: ")

    if tone_choice == "1":
        selected_tone = "Friendly"

    elif tone_choice == "2":
        selected_tone = "Formal"

    elif tone_choice == "3":
        selected_tone = "Empathetic"

    else:
        print("Invalid choice. Using Formal tone.")
        selected_tone = "Formal"

    improved_reply = improve_tone(
        generated_reply,
        selected_tone
    )

    # Q8 - Conversation Summary
    print("\nGenerating conversation summary...")

    summary = generate_summary(customer_email)

    # Q9 - Save Reply
    print("\nSaving reply...")

    save_reply(
        customer_email,
        improved_reply,
        intent
    )

    # Final Output
    print("\n" + "=" * 50)
    print("       EMAIL ASSISTANT COMPLETED")
    print("=" * 50)

    print("\nCustomer Name :", customer_name)
    print("Subject       :", subject)
    print("Intent        :", intent)

    print("\n===== Final Reply =====")
    print(improved_reply)

    print("\n===== Conversation Summary =====")
    print(summary)

    print("\nReply saved successfully.")


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("       INTELLIGENT EMAIL ASSISTANT")
        print("=" * 50)

        print("1. Run Complete Email Assistant")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            complete_email_assistant()

        elif choice == "2":
            print("\nThank you for using Intelligent Email Assistant.")
            break

        else:
            print("\nInvalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()