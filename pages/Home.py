import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://example.com/alz3.jpeg");
            background-size: cover;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to the Alzheimer's Detection App")
    st.write("""
    This application uses a deep learning model to detect different stages of Alzheimer's Disease 
    from MRI images. Use the navigation menu to upload images, see model information, and learn more about the project.
    """)
    
    st.subheader("Facts about Alzheimer's Disease")
    st.write("""
    - **Alzheimer's Disease** is a progressive neurological disorder that causes the brain to shrink (atrophy) and brain cells to die.
    - It is the most common cause of dementia, accounting for 60-80% of dementia cases.
    - Symptoms typically develop slowly and worsen over time, becoming severe enough to interfere with daily tasks.
    - Common early symptoms include memory loss, confusion, and difficulty completing familiar tasks.
    - The exact cause of Alzheimer's is not yet known, but it involves a combination of genetic, environmental, and lifestyle factors.
    - Risk factors include age, family history, and certain genetic mutations, with age being the greatest risk factor.
    - There is currently no cure for Alzheimer's, but treatments can help manage symptoms and improve quality of life.
    - Research is ongoing to better understand the disease and develop new treatments.
    """)

if __name__ == "__main__":
    main()
