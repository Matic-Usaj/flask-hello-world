from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

lessons = [
    {"id": 1, "name": "Python programming", "credits": 5},
    {"id": 2, "name": "Java programming", "credits": 5},
    {"id": 3, "name": "History", "credits": 5},
    {"id": 4, "name": "English", "credits": 5},
]

@app.route('/')
def hello_world():
    return 'Hello, World! now my app is running locally'

@app.route('/lessons')
def get_lessons():
    return jsonify(lessons)

@app.route('/create-lesson')
def create_lesson():
    name = request.args["name"]
    credits = request.args["credits"]
    lesson_id = len(lessons) + 1
    new_lesson = {"id": lesson_id, "name": name, "credits": credits}
    lessons.append(new_lesson)
    return jsonify(lessons)

@app.route('/delete/<lesson_id>', methods=["GET"])
def delete_lesson(lesson_id):
    for lesson in lessons:
        if lesson["id"] == int(lesson_id):
            lessons.remove(lesson)
    return render_template("delete-success.html", lesson_id = lesson_id)


if __name__ == "__main__":
    app.run()
