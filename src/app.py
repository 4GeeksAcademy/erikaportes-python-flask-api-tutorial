from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        'label': 'My first task',
        'done': True
    },
]

# POST - Crear tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    # Validar que venga JSON
    if not request_body:
        return jsonify({"error": "Request body vacío"}), 400

    # Validar estructura
    if 'label' not in request_body or 'done' not in request_body:
        return jsonify({"error": "Faltan campos 'label' o 'done'"}), 400

    print("Incoming request:", request_body)

    todos.append(request_body)

    return jsonify({
        "message": "Tarea agregada correctamente",
        "todos": todos
    }), 201


# GET - Obtener tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    if len(todos) == 0:
        return jsonify({"message": "No hay tareas"}), 400

    return jsonify(todos), 200


# DELETE - Eliminar tarea
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    # Validar índice negativo
    if position < 0:
        return jsonify({"error": "Posición inválida"}), 400

    # Validar que exista la tarea
    if position >= len(todos):
        return jsonify({"error": "La tarea no existe"}), 404

    deleted = todos[position]
    del todos[position]

    return jsonify({
        "message": "Tarea eliminada correctamente",
        "deleted": deleted,
        "todos": todos
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)






# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#    request_body = request.json
#    print("Incoming request with the following body: ", request_body)
#    todos.append(request_body)
#    return jsonify(todos)

# @app.route('/todos', methods=['GET'])
# def get_todos():
#     return jsonify(todos), 200

# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     if position < len(todos):
#         del todos[position]
#     return jsonify(todos)

# todos = [
#     {
#         'label': 'My first task',
#         'done': True
#     },
# ]


# if __name__ == '__main__':
#  app.run(host='0.0.0.0', port=3245, debug=True)