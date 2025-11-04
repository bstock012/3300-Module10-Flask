# module 10 - Flask Application
# Blaine Stockman 11/3/2025

from flask import Flask

app = Flask(__name__)

@app.route("/") # root route or home route
def hello():
    return "Hello World!!"

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)