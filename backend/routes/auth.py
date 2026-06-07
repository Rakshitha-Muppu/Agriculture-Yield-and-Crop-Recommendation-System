from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    return jsonify(
        {
            "message": "Register Route Working"
        }
    )


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    return jsonify(
        {
            "message": "Login Route Working"
        }
    )