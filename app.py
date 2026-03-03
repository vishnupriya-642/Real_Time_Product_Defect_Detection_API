import streamlit as st
import requests

st.title("Real-Time Product Defect Detection")

st.write("Upload an image to check whether the product is Defective or OK.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):

        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://localhost:8000/predict",
            files={"file": uploaded_file}
        )

        if response.status_code == 200:
            result = response.json()["prediction"]
            st.success(f"Prediction: {result}")
        else:
            st.error("Error in prediction")