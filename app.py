import json
from flask import Flask, request

with open("tests/courses_data.json", "r") as file:
    courses_data = json.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, World!"

@app.get("/courses")
def courses():
    return courses_data

@app.post("/courses")
def update_courses():
    new_course = request.json
    courses_data["courses"].append(new_course)
    return courses_data


if __name__ == "__main__":
    app.run(debug=True)
