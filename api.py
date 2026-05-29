from flask import Blueprint, jsonify, request
from routes import connect_db 

api_bp = Blueprint('api', __name__)

@api_bp.route('/tasks', methods=['GET'])
def api_get_tasks():

    try:
        db = connect_db()
        cur = db.execute('select name, due_date, priority, task_id from ftasks')
        tasks = [
            dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) 
            for row in cur.fetchall()
        ]
        db.close()
        return jsonify({"status": "success", "tasks": tasks}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500