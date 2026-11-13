
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "jobs.csv")

def get_jobs():
    return pd.read_csv(DATA_FILE).to_dict(orient="records")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html", jobs=get_jobs())

@app.route("/salary")
def salary():
    return render_template("salary.html", jobs=get_jobs())

@app.route("/skills")
def skills():
    return render_template("skills.html", jobs=get_jobs())

@app.route("/charts")
def charts():
    return render_template("charts.html")

if __name__ == "__main__":
    app.run(debug=True)
