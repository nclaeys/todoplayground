from flask import request, json, jsonify
from app import app
from app.models import Todo


@app.route("/todos", methods=['GET'])
def todos():
    all = Todo.get_all()
    print(all)
    return jsonify(all)


@app.route("/todos", methods=["POST"])
def add_todo():
    content = request.get_json()
    print(content)
    try:
        new_todo = Todo(content['day'], content['title'])
        new_todo.insert()
        return jsonify(new_todo.json())
    except ValueError:
        return jsonify({"message": "failed to parse date"})


@app.route("/todos/by_day/<string:day>")
def get_todo_day(day):
    todos_for_day = Todo.query_by_day(day)
    return jsonify({"todos": todos_for_day})
