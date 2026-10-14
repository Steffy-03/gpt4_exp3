import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_emails():
    file_path = "data/emails.csv"

    try:
        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        print("Error loading CSV file:", e)
        return None


def retrieve_similar_email(customer_email, df):
    # Convert customer emails into TF-IDF vectors
    vectorizer = TfidfVectorizer()

    email_vectors = vectorizer.fit_transform(
        df["Customer_Email"].fillna("")
    )

    # Convert new customer email into a vector
    query_vector = vectorizer.transform([customer_email])

    # Calculate cosine similarity
    similarities = cosine_similarity(
        query_vector,
        email_vectors
    )[0]

    # Find the most similar email
    best_index = similarities.argmax()

    previous_email = df.iloc[best_index]["Customer_Email"]
    previous_reply = df.iloc[best_index]["Previous_Reply"]

    print("\n===== Most Similar Previous Email =====")
    print("\nPrevious Email:")
    print(previous_email)

    print("\nPrevious Reply:")
    print(previous_reply)

    print("\nSimilarity Score:")
    print(round(similarities[best_index], 2))

    return previous_email, previous_reply


if __name__ == "__main__":
    df = load_emails()

    if df is not None:
        customer_email = input("Enter Customer Email: ")
        retrieve_similar_email(customer_email, df)