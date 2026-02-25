from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "fake_news_project"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    title = request.form['news_title']
    content = request.form['news_content']

    # Demo logic (replace later with ML model)
    if len(content) > 150:
        result_text = "Real News"
        result_type = "real"
        confidence = 85
    else:
        result_text = "Fake News"
        result_type = "fake"
        confidence = 65

    # Prediction history
    if "history" not in session:
        session["history"] = []

    session["history"].append({
        "title": title,
        "result": result_text,
        "confidence": confidence
    })

    session["history"] = session["history"][-5:]

    return render_template(
        "index.html",
        prediction_text=result_text,
        prediction_type=result_type,
        confidence=confidence,
        history=session["history"]
    )


if __name__ == "__main__":
    app.run(debug=True)