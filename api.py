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
    
    
@api_bp.route('/tasks', methods=['POST'])
def api_create_task():
    """CREATE: Adds a new task using JSON input data"""
    if not request.is_json:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()
    name = data.get('name')
    due_date = data.get('due_date', '')
    priority = data.get('priority', 1)

    if not name:
        return jsonify({"status": "error", "message": "Task 'name' is required"}), 400

    try:
        db = connect_db()
        db.execute(
            'insert into ftasks (name, due_date, priority, status) values (?, ?, ?, 1)',
            [name, due_date, priority]
        )
        db.commit()
        db.close()
        return jsonify({"status": "success", "message": "Task created successfully"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    """UPDATE: Modifies an existing task by its ID"""
    if not request.is_json:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()
    name = data.get('name')
    due_date = data.get('due_date')
    priority = data.get('priority')

    try:
        db = connect_db()
        cur = db.execute('select task_id from ftasks where task_id = ?', [task_id])
        if not cur.fetchone():
            db.close()
            return jsonify({"status": "error", "message": "Task not found"}), 404

        db.execute(
            'update ftasks set name = ?, due_date = ?, priority = ? where task_id = ?',
            [name, due_date, priority, task_id]
        )
        db.commit()
        db.close()
        return jsonify({"status": "success", "message": "Task updated successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
    
@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    """DELETE: Erases a task by its ID from the system"""
    try:
        db = connect_db()
        cur = db.execute('select task_id from ftasks where task_id = ?', [task_id])
        if not cur.fetchone():
            db.close()
            return jsonify({"status": "error", "message": "Task not found"}), 404

        db.execute('delete from ftasks where task_id = ?', [task_id])
        db.commit()
        db.close()
        return jsonify({"status": "success", "message": "Task deleted successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    