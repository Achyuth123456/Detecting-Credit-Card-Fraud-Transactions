import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import base64

# Load the model
model_path = r"C:\\Users\\achyu\\Downloads\\fraud_detection_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load background image
background_image_path = r"C:\\Users\\achyu\\Downloads\\background_image.jpg"

def apply_custom_css():
    # Streamlit CSS for a custom background
    css = f"""
    <style>
    body {{
        background-image: url("data:image/jpg;base64,{encode_image(background_image_path)}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .stApp {{
        background: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
        max-width: 700px;
        margin: auto;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
    }}
    footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 1rem;
        font-size: 0.9em;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_footer():
    footer_html = """
    <footer>
        <p>Created by Achyuth Kumar Miryala</p>
        <p>Contact: <a href="mailto:Achyuthkumarmiryala@my.unt.edu" style="color: #ffcc00;">Achyuthkumarmiryala@my.unt.edu</a> | 
        <a href="https://www.linkedin.com/in/achyuthkumarmiryala" style="color: #ffcc00;">LinkedIn</a></p>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def main():
    st.title("Fraud Detection System")
    st.sidebar.header("Input Transaction Details")

    # Collect input parameters
    time = st.sidebar.number_input("Time", min_value=0, max_value=172792, step=1)
    amount = st.sidebar.number_input("Amount", min_value=0.0, max_value=100000.0, step=1.0)
    V1 = st.sidebar.number_input("V1", min_value=-50.0, max_value=50.0)
    V2 = st.sidebar.number_input("V2", min_value=-50.0, max_value=50.0)
    V3 = st.sidebar.number_input("V3", min_value=-50.0, max_value=50.0)
    V4 = st.sidebar.number_input("V4", min_value=-50.0, max_value=50.0)
    V5 = st.sidebar.number_input("V5", min_value=-50.0, max_value=50.0)
    V6 = st.sidebar.number_input("V6", min_value=-50.0, max_value=50.0)
    V7 = st.sidebar.number_input("V7", min_value=-50.0, max_value=50.0)
    V8 = st.sidebar.number_input("V8", min_value=-50.0, max_value=50.0)
    V9 = st.sidebar.number_input("V9", min_value=-50.0, max_value=50.0)
    V10 = st.sidebar.number_input("V10", min_value=-50.0, max_value=50.0)

    # Create a DataFrame with the inputs
    input_data = {
        'Time': [time],
        'Amount': [amount],
        'V1': [V1],
        'V2': [V2],
        'V3': [V3],
        'V4': [V4],
        'V5': [V5],
        'V6': [V6],
        'V7': [V7],
        'V8': [V8],
        'V9': [V9],
        'V10': [V10]
    }
    input_df = pd.DataFrame(input_data)

    # Match the input_df to model features
    input_df = input_df.iloc[:, :model.n_features_in_]

    # Prediction
    try:
        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.write("### 🚨 Alert: This transaction is likely fraudulent.")
        else:
            st.write("### ✅ This transaction is not fraudulent.")
    except ValueError as e:
        st.error(f"An error occurred: {e}")

apply_custom_css()
main()
display_footer()
