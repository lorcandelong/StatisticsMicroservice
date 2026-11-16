
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/statistics', methods=['POST'])

def calculate_statistics():

    data = request.get_json()

    tasks = data["tasks"]

    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks if task["completed"] == True
    )

    incomplete_tasks = total_tasks - completed_tasks

    return jsonify({
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "incomplete_tasks": incomplete_tasks,
        }) 

@app.route('/password-statistics', methods=['POST'])
def calculate_password_statistics():

    data = request.get_json()

    passwords = data["passwords"]

    total_passwords = len(passwords)

    weak_passwords = sum(
        1 for password in passwords
        if password["score"] == "Weak"
    )

    medium_passwords = sum(
        1 for password in passwords
        if password["score"] == "Medium"
    )

    strong_passwords = sum(
        1 for password in passwords
        if password["score"] == "Strong"
    )

    return jsonify({
        "total_passwords": total_passwords,
        "weak_passwords": weak_passwords,
        "medium_passwords": medium_passwords,
        "strong_passwords": strong_passwords
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)