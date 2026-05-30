import joblib
import pandas as pd

from config import (
    MODEL_PATH,
    SCALER_PATH,
    TARGET_ENCODER_PATH,
    COLUMNS_PATH,
    ENCODER_PATH
)

model = joblib.load(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

target_encoder = joblib.load(
    TARGET_ENCODER_PATH
)

model_columns = joblib.load(
    COLUMNS_PATH
)

feature_label_encoders = joblib.load(
    ENCODER_PATH
)

def get_age_group(age):

    if age <= 25:
        return "18-25"

    elif age <= 35:
        return "26-35"

    elif age <= 45:
        return "36-45"

    elif age <= 55:
        return "46-55"

    elif age <= 70:
        return "56-70"

    else:
        return "70+"
    
frequency_map = {
    "0-2 times": 1,
    "3-4 times": 2,
    "5-7 times": 3
}

awareness_map = {
    '0 to 1': 1,
    '2 to 4': 2,
    'above 4': 3
}

def calculate_cf_ab_score(
    frequency,
    awareness
):

    freq_score = frequency_map[frequency]

    awareness_score = awareness_map[awareness]

    return round(
        freq_score /
        (
            freq_score +
            awareness_score
        ),
        2
    )

zone_map = {
    "Rural": 1,
    "Semi-Urban": 2,
    "Urban": 3,
    "Metro": 4
}

income_map = {
    '<10L': 1,
    '10L - 15L': 2,
    '16L - 25L': 3,
    '26L - 35L': 4,
    '> 35L': 5,
    'Not Reported': 0
}

def calculate_zas_score(
    zone,
    income
):

    zone_score = zone_map[zone]

    income_score = income_map[income]

    return zone_score * income_score

def calculate_bsi(
    brand,
    reason
):

    if (
        brand != "Established"
        and reason in [
            "Price",
            "Quality"
        ]
    ):
        return 1

    return 0

def predict_price_range(user_input):

    # --------------------------
    # Feature Engineering
    # --------------------------

    user_input['age_group'] = get_age_group(
        user_input['age']
    )

    user_input['cf_ab_score'] = calculate_cf_ab_score(
        user_input['consume_frequency(weekly)'],
        user_input['awareness_of_other_brands']
    )

    user_input['zas_score'] = calculate_zas_score(
        user_input['zone'],
        user_input['income_levels']
    )

    user_input['bsi'] = calculate_bsi(
        user_input['current_brand'],
        user_input['reasons_for_choosing_brands']
    )

    # remove raw age
    user_input.pop('age')

    # --------------------------
    # Create DataFrame
    # --------------------------

    input_df = pd.DataFrame([user_input])

    # --------------------------
    # Label Encoding
    # --------------------------

    label_encode_cols = [
        'age_group',
        'income_levels',
        'health_concerns',
        'consume_frequency(weekly)',
        'preferable_consumption_size'
    ]

    for col in label_encode_cols:

        input_df[col] = (
            feature_label_encoders[col]
            .transform(input_df[col])
        )

    # --------------------------
    # One Hot Encoding
    # --------------------------

    input_df = pd.get_dummies(
        input_df
    )

    # --------------------------
    # Align Columns
    # --------------------------

    for col in model_columns:

        if col not in input_df.columns:

            input_df[col] = 0

    input_df = input_df[
        model_columns
    ]

    # --------------------------
    # Prediction
    # --------------------------

    prediction = model.predict(
        input_df
    )

    predicted_price = (
        target_encoder
        .inverse_transform(prediction)
    )[0]

    return predicted_price