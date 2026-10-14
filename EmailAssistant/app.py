from flask import Flask, render_template, request, jsonify

from intent_module import detect_intent
from retrieval_module import load_emails, retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    try:
        data = request.get_json()

        customer_name = data.get("customer_name", "")
        subject = data.get("subject", "")
        customer_email = data.get("customer_email", "")
        tone = data.get("tone", "Formal")

        # 1. Intent Detection
        intent = detect_intent(customer_email)

        # 2. Load historical emails
        df = load_emails()

        # 3. Retrieve similar email
        previous_email, previous_reply = retrieve_similar_email(
            customer_email,
            df
        )

        # 4. Generate AI reply
        generated_reply = generate_reply(
            customer_email,
            previous_reply
        )

        # 5. Improve tone
        improved_reply = improve_tone(
            generated_reply,
            tone
        )

        # 6. Generate summary
        summary = generate_summary(customer_email)

        # 7. Save reply
        save_reply(
            customer_email,
            improved_reply,
            intent
        )

        return jsonify({
            "success": True,
            "customer_name": customer_name,
            "subject": subject,
            "intent": intent,
            "previous_email": previous_email,
            "previous_reply": previous_reply,
            "generated_reply": generated_reply,
            "improved_reply": improved_reply,
            "summary": summary
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)