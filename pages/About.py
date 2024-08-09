import streamlit as st

def main():
    st.title("About")
    st.write("""
    This application was developed to help detect different stages of Alzheimer's Disease using deep learning techniques.
    It uses a ResNet-50 model pre-trained on ImageNet and fine-tuned on a custom dataset.
    For more information, please refer to the [GitHub repository](https://github.com/your-repo).
    """)

    st.subheader("Developers")
    st.write("""
    - **Md. Abdur Rahman**: ✨New Dataset: Alzheimer MRI Disease Classification 🧠
    - **Mohamed Gobara**: Augmented Alzheimer MRI Dataset with 93.5%
    - **uraninjo**: Pytorch Ensemble Learning | Alzheimer Dataset
    """)

    st.subheader("Acknowledgements")
    st.write("""
    We would like to thank the contributors of the Alzheimer's Disease dataset and the community for their support in developing this application.
    """)

if __name__ == "__main__":
    main()
