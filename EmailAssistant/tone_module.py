import requests


def improve_tone(reply, tone):
    prompt = f"""
You are a professional customer support email editor.

Rewrite the following email in a {tone} tone.

Original Email:
{reply}

Rules:
- Keep the same meaning and facts.
- Do not invent new information.
- Do not add placeholders.
- Do not change shipment status or delivery information.
- Only change the tone and wording.
- Keep it professional.
- Return only the rewritten email.
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
        improved_reply = result["response"].strip()

        print(f"\n===== {tone} Tone =====")
        print(improved_reply)

        return improved_reply

    except requests.exceptions.Timeout:
        print(f"\n{tone} tone generation timed out.")
        print("Please try again.")

    except requests.exceptions.RequestException as e:
        print(f"\nError generating {tone} tone:", e)


if __name__ == "__main__":

    print("===== Tone Improver =====")

    print("\nEnter the complete reply.")
    print("Type END on a new line after entering the reply.\n")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    reply = "\n".join(lines)

    print("\nChoose a tone:")
    print("1. Friendly")
    print("2. Formal")
    print("3. Empathetic")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        improve_tone(reply, "Friendly")

    elif choice == "2":
        improve_tone(reply, "Formal")

    elif choice == "3":
        improve_tone(reply, "Empathetic")

    else:
        print("Invalid choice.")