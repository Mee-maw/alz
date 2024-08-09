import streamlit as st

# Set the configuration for the main page
st.set_page_config(page_title="Alzheimer's Detection App", layout="wide")

# Define the navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload and Predict", "Model Info", "About"])

if page == "Home":
    import pages.Home as home
    home.main()

elif page == "Upload and Predict":
    import pages.Predict as upload_and_predict
    upload_and_predict.main()

elif page == "Model Info":
    import pages.Info as model_info
    model_info.main()

elif page == "About":
    import pages.About as about
    about.main()
