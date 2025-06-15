from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    fact = get_random_fact()
    return render_template("index.html", fact=fact)

def get_random_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        return response.json().get("text", "Couldn't fetch a fact right now.")
    except:
        return "Something went wrong. Try again!"

if __name__ == "__main__":
    app.run(debug=True)