from flask import Blueprint, request, jsonify
from services.prediction_service import (
    create_prediction,
    get_user_predictions
)

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    recommended_crop = "Rice"
    predicted_yield = 4.5

    create_prediction(
        data["user_id"],
        data["soil_type"],
        data["location"],
        data["state"],
        data["district"],
        data["season"],
        data["crop_input"],
        data["temperature"],
        data["rainfall"],
        data["humidity"],
        data["land_acres"],
        data["land_type"],
        recommended_crop,
        predicted_yield
    )

    return jsonify(
        {
            "recommended_crop": recommended_crop,
            "predicted_yield": predicted_yield
        }
    )

@predict_bp.route("/history/<int:user_id>", methods=["GET"])
def history(user_id):

    predictions = get_user_predictions(user_id)

    return jsonify(predictions)