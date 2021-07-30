from flask import request, json, Flask
from app.utils import to_date
from app import app

db = [
    {
        'day': to_date('10-07-2021'),
        'title': 'My first todo'
    }
]


@app.route("/todos", methods=['GET'])
def todos():
    all_todos = {'todos': db}
    return json.dumps(all_todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    content = request.get_json()
    print(content)
    try:
        date = to_date(content["day"])
    except ValueError:
        return json.dumps({"message": "failed to parse date"})

    new_todo = {"title": content['title'], "day": date}
    db.append(new_todo)
    return json.dumps(new_todo)


@app.route("/todos/by_day/<string:day>")
def get_todo_day(day):
    todos_for_day = [todo for todo in db if todo["day"].toordinal() == to_date(day).toordinal()]
    return json.dumps({"todos": todos_for_day})
