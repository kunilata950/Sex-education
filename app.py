from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/consent")
def consent():
    return render_template("consent.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/relationships")
def relationships():
    return render_template("relationships.html")

if __name__ == "__main__":
    app.run(debug=True)