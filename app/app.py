import streamlit as st
from utils import predict_price_range

st.set_page_config(
    page_title="Beverage Price Prediction",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center;'>
        Beverage Price Prediction
    </h1>

    <br>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=25
    )

    income_levels = st.selectbox(
        "Income Level",
        [
            "<10L",
            "10L - 15L",
            "16L - 25L",
            "26L - 35L",
            "> 35L",
            "Not Reported"
        ]
    )

    awareness = st.selectbox(
        "Awareness Of Other Brands",
        [
            "0 to 1",
            "2 to 4",
            "above 4"
        ]
    )

    packaging = st.selectbox(
        "Packaging Preference",
        [
            "Simple",
            "Premium",
            "Eco-Friendly"
        ]
    )

with col2:

    gender = st.selectbox(
        "Gender",
        ["M", "F"]
    )

    consume_frequency = st.selectbox(
        "Consumption Frequency",
        [
            "0-2 times",
            "3-4 times",
            "5-7 times"
        ]
    )

    reason = st.selectbox(
        "Reason For Choosing Brand",
        [
            "Price",
            "Quality",
            "Availability",
            "Brand Reputation"
        ]
    )

    health = st.selectbox(
        "Health Concerns",
        [
            "Low (Not very concerned)",
            "Medium (Moderately health-conscious)",
            "High (Very health-conscious)"
        ]
    )

with col3:

    zone = st.selectbox(
        "Zone",
        [
            "Rural",
            "Semi-Urban",
            "Urban",
            "Metro"
        ]
    )

    current_brand = st.selectbox(
        "Current Brand",
        [
            "Established",
            "Newcomer"
        ]
    )

    flavor = st.selectbox(
        "Flavor Preference",
        [
            "Traditional",
            "Exotic"
        ]
    )

    situation = st.selectbox(
        "Consumption Situation",
        [
            "Active (eg. Sports, gym)",
            "Casual (eg. At home)",
            "Social (eg. Parties)"
        ]
    )

with col4:

    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Working Professional",
            "Entrepreneur",
            "Retired"
        ]
    )

    preferable_size = st.selectbox(
        "Preferred Size",
        [
            "Small (250 ml)",
            "Medium (500 ml)",
            "Large (1 L)"
        ]
    )

    purchase_channel = st.selectbox(
        "Purchase Channel",
        [
            "Online",
            "Retail Store"
        ]
    )

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2,1,2])

with c2:

    predict_button = st.button(
    "Calculate Price Range",
    use_container_width=True
)
    
if predict_button:

    user_input = {

        'age': age,
        'gender': gender,
        'zone': zone,
        'occupation': occupation,
        'income_levels': income_levels,
        'consume_frequency(weekly)': consume_frequency,
        'current_brand': current_brand,
        'preferable_consumption_size': preferable_size,
        'awareness_of_other_brands': awareness,
        'reasons_for_choosing_brands': reason,
        'flavor_preference': flavor,
        'purchase_channel': purchase_channel,
        'packaging_preference': packaging,
        'health_concerns': health,
        'typical_consumption_situations': situation
    }

    prediction = predict_price_range(
        user_input
    )

    st.markdown("""
<style>

.stButton > button {

    background-color: #1565C0;
    color: white;

    border-radius: 12px;

    height: 3em;

    font-size: 18px;

    font-weight: bold;

    border: none;

    cursor: pointer !important;
}

.stButton > button:hover {

    background-color: #0D47A1;

    color: white;

    cursor: pointer !important;
}

</style>
""",
unsafe_allow_html=True)

    st.success(
        f"Predicted Price Range: {prediction} INR"
    )

st.markdown(
    """
    <style>

    .footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        color: gray;
        font-size: 12px;
        z-index: 999;
    }

    </style>

    <div class="footer">
        © 2026 Siba Narayana Parida™
    </div>
    """,
    unsafe_allow_html=True
)