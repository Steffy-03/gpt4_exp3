def get_customer_input():
    print("\n===== Intelligent Email Assistant =====")

    customer_name = input("Enter Customer Name: ")
    subject = input("Enter Email Subject: ")
    customer_email = input("Enter Customer Email: ")

    print("\n===== Entered Details =====")
    print("Customer Name :", customer_name)
    print("Subject       :", subject)
    print("Customer Email:", customer_email)

    return customer_name, subject, customer_email


if __name__ == "__main__":
    get_customer_input()