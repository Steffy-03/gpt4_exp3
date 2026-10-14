import requests


def generate_reply(customer_email, previous_reply):
    prompt = f"""
You are a professional customer support assistant.

Generate a professional email reply to the customer.

Customer Email:
{customer_email}

Previous Reply:
{previous_reply}

Requirements:
- Be polite and professional.
- Directly address the customer's issue.
- Use the previous reply as context.
- Do not copy the previous reply exactly.
- Keep the response concise.
- Include a greeting and a closing.
- Sign off as "Support Team".

Return only the email reply.
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
        generated_reply = result["response"].strip()

        print("\n===== AI Generated Reply =====")
        print(generated_reply)

        return generated_reply

    except Exception as e:
        print("Error connecting to Ollama:", e)
        return None


if __name__ == "__main__":
    customer_email = input("Enter Customer Email: ")

    previous_reply = input("Enter Previous Reply: ")

    generate_reply(customer_email, previous_reply)