from flask import Flask, request, jsonify

app = Flask(__name__)


users_db = [
    {"id": 1, "name": "Олексій", "role": "admin"},
    {"id": 2, "name": "Марія", "role": "user"}
]
next_id = 3  

def make_response(status, data=None, message="", code=200):
    """Формує красиву JSON-відповідь"""
    response = {
        "status": status,
        "data": data,
        "message": message
    }
    return jsonify(response), code
@app.route('/users', methods=['GET'])
def get_users():
    return make_response("success", users_db, "Список користувачів отримано")

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    req_data = request.json 

    if not req_data or 'name' not in req_data:
        return make_response("error", None, "Поле 'name' є обов'язковим!", 400)

    new_user = {
        "id": next_id,
        "name": req_data['name'],
        "role": req_data.get('role', 'user')  
    }
    
    users_db.append(new_user)
    next_id += 1
    
    return make_response("success", new_user, "Користувача успішно створено", 201)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if user:
        return make_response("success", user, "Користувача знайдено")
    return make_response("error", None, "Користувача з таким ID не знайдено", 404)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if not user:
        return make_response("error", None, "Користувача не знайдено", 404)
    
    req_data = request.json
    user['name'] = req_data.get('name', user['name'])
    user['role'] = req_data.get('role', user['role'])
    
    return make_response("success", user, "Дані оновлено")

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users_db
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if user:
        users_db.remove(user) 
        return make_response("success", None, f"Користувача ID {user_id} видалено")
    
    return make_response("error", None, "Користувача не знайдено", 404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)