from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Krishna", "email": "krishna@example.com"},
    {"id": 2, "name": "John", "email": "john@example.com"},
    {"id": 3, "name": "Alice", "email": "alice@example.com"},
]


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP",
            "service": "user-service"
        }
    )


@app.route("/users")
def get_users():
    return jsonify(users)


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        return jsonify(user)

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
