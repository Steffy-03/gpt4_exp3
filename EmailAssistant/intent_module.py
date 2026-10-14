import requests


def detect_intent(customer_email):
    prompt = f"""
Classify the following customer email into exactly one of these intents:

- Delivery Issue
- Refund Request
- Product Complaint
- Technical Support
- Order Cancellation
- General Inquiry

Customer Email:
{customer_email}

Return only the intent name. Do not provide any explanation.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:latest",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        intent = result["response"].strip()

        print("\n===== Detected Intent =====")
        print(intent)

        return intent

    except Exception as e:
        print("Error connecting to Ollama:", e)
        return None


if __name__ == "__main__":
    customer_email = input("Enter Customer Email: ")
    detect_intent(customer_email)