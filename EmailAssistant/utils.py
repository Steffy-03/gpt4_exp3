from datetime import datetime


def save_reply(customer_email, generated_reply, intent):
    file_path = "outputs/generated_reply.txt"

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("===== Intelligent Email Assistant =====\n\n")

        file.write("Date: " + current_date + "\n\n")

        file.write("Customer Email:\n")
        file.write(customer_email + "\n\n")

        file.write("Intent:\n")
        file.write(intent + "\n\n")

        file.write("Generated Reply:\n")
        file.write(generated_reply + "\n")

    print("\n===== Reply Saved Successfully =====")
    print("Saved to:", file_path)


if __name__ == "__main__":

    customer_email = "My order has not arrived."

    generated_reply = """Dear Customer,

We sincerely apologize for the inconvenience caused by the delay in your order.
Our logistics team is currently tracking your shipment and will provide an update
within the next 24 hours.

Regards,
Support Team"""

    intent = "Delivery Issue"

    save_reply(
        customer_email,
        generated_reply,
        intent
    )