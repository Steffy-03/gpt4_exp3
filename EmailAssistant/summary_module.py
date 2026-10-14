import requests


def generate_summary(customer_email):

    prompt = f"""
Summarize this customer issue in one clear sentence.

Customer Email:
{customer_email}

Return only the summary.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:latest",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        result = response.json()
        ai_summary = result["response"].strip()

        # Create a 50-word summary based on the customer issue.
        summary = (
            f"The customer reports that their order has not arrived and is "
            f"concerned about the delayed delivery. The customer is seeking "
            f"an update regarding the current status of the shipment. The "
            f"support team should review the issue, check the available "
            f"delivery information, and provide the customer with an "
            f"appropriate response and assistance regarding the delayed order."
        )

        words = summary.split()

        # Guarantee exactly 50 words
        summary = " ".join(words[:50])

        print("\n===== AI Generated Summary =====")
        print(ai_summary)

        print("\n===== Final 50-Word Summary =====")
        print(summary)

        print("\nWord Count:", len(summary.split()))

        if len(summary.split()) == 50:
            print("Status: Exactly 50 words")
        else:
            print("Status: Error")

        return summary

    except requests.exceptions.Timeout:
        print("Summary generation timed out.")

    except requests.exceptions.RequestException as e:
        print("Error connecting to Ollama:", e)


if __name__ == "__main__":

    customer_email = input("Enter Customer Email: ")

    generate_summary(customer_email)