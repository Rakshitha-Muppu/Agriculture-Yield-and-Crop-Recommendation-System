from flask import Blueprint, request, jsonify

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    return jsonify(
        {
            "recommended_crop": "Rice",
            "predicted_yield": 4.5
        }
    )