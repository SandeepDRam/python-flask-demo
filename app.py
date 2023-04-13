"""
A simple Flask web application.
"""

import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the home page of the web application.
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Renders the about page of the web application.
    """
    return render_template("about.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
