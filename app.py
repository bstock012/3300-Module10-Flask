# module 10 - Flask Application
# Blaine Stockman 11/3/2025

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
     return"This is Blaine's about page."

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)