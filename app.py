import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bookDetails", methods=['POST'])
def bookDetails():
    base_url = "https://openlibrary.org/subjects/"
    subject = request.form['subject']

    url = f"{base_url}{subject}.json"
    response = requests.get(url)

    if response.status_code == 200:
        book_details = response.json()

        if book_details:
            return render_template("book_details.html", book_details=book_details)
        else:
            return "Error: Empty response"
    else:
        return f"Error: Unable to fetch data. Status code: {response.status_code}"

if __name__ == "__main__":
    application.run(debug=True)
