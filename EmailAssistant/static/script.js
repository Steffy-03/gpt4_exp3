async function generateResponse() {

    const customerName =
        document.getElementById("customer_name").value.trim();

    const subject =
        document.getElementById("subject").value.trim();

    const customerEmail =
        document.getElementById("customer_email").value.trim();

    const tone =
        document.getElementById("tone").value;


    if (!customerName || !subject || !customerEmail) {

        alert("Please enter Customer Name, Subject and Customer Email.");

        return;
    }


    const button =
        document.getElementById("generateBtn");


    button.disabled = true;

    button.innerHTML = "⏳ Processing with Ollama...";


    document.getElementById("intent").innerText =
        "Processing...";

    document.getElementById("intent").className =
        "badge waiting";


    document.getElementById("previous_email").innerText =
        "Searching previous interactions...";


    document.getElementById("previous_reply").innerText =
        "Retrieving previous reply...";


    document.getElementById("generated_reply").innerText =
        "Generating AI response...";

    document.getElementById("generated_reply")
        .classList.remove("placeholder");


    document.getElementById("improved_reply").innerText =
        "Improving tone...";

    document.getElementById("improved_reply")
        .classList.remove("placeholder");


    document.getElementById("summary").innerText =
        "Generating summary...";

    document.getElementById("summary")
        .classList.remove("placeholder");


    document.getElementById("selected_tone").innerText =
        tone;


    try {

        const response = await fetch("/generate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                customer_name: customerName,
                subject: subject,
                customer_email: customerEmail,
                tone: tone

            })

        });


        const result = await response.json();


        if (!result.success) {

            alert("Error: " + result.error);

            resetButton();

            return;
        }


        /* Intent */

        document.getElementById("intent").innerText =
            result.intent;

        document.getElementById("intent").className =
            "badge success";


        /* Previous Email */

        document.getElementById("previous_email").innerText =
            result.previous_email;


        /* Previous Reply */

        document.getElementById("previous_reply").innerText =
            result.previous_reply;


        /* AI Reply */

        document.getElementById("generated_reply").innerText =
            result.generated_reply;


        /* Improved Reply */

        document.getElementById("improved_reply").innerText =
            result.improved_reply;


        /* Summary */

        document.getElementById("summary").innerText =
            result.summary;


        /* Word Count */

        const words =
            result.summary.trim().split(/\s+/).length;


        document.getElementById("word_count").innerText =
            words + " words";


        /* Button */

        button.disabled = false;

        button.innerHTML =
            "✓ Response Generated";


        setTimeout(() => {

            button.innerHTML =
                "✨ Generate AI Response";

        }, 2500);


    } catch (error) {

        console.error(error);

        alert(
            "Unable to connect to the Flask server."
        );

        resetButton();

    }

}


function resetButton() {

    const button =
        document.getElementById("generateBtn");

    button.disabled = false;

    button.innerHTML =
        "✨ Generate AI Response";

}


function copyText(elementId) {

    const text =
        document.getElementById(elementId).innerText;


    if (
        !text ||
        text.includes("Your AI-generated reply")
    ) {

        alert("There is no generated reply to copy.");

        return;
    }


    navigator.clipboard.writeText(text)
        .then(() => {

            alert("Reply copied to clipboard!");

        })
        .catch(() => {

            alert("Unable to copy the reply.");

        });

}