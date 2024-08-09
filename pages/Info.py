import streamlit as st

def main():
    st.title("Model Information")
    st.write("""
    This section contains information about the deep learning model used in this application.
    The model is a custom ResNet-50 trained on the Alzheimer's MRI dataset.
    - **Model Architecture**: ResNet-50
    - **Training Data**: Custom dataset with four classes: MildDemented, ModerateDemented, NonDemented, VeryMildDemented
    - **Training Method**: Transfer learning with frozen ResNet layers and a custom final layer.
    """)

    st.subheader("Model Architecture")
    st.write("""
    The model used in this application is based on the ResNet-50 architecture. ResNet, short for Residual Networks, is a classic neural network used as a backbone for many computer vision tasks.
    """)
    
    st.code("""
    class CustomResNetModel(nn.Module):
        def __init__(self, num_classes):
            super(CustomResNetModel, self).__init__()
            self.resnet = models.resnet50(pretrained=False)
            num_features = self.resnet.fc.in_features
            self.resnet.fc = nn.Linear(num_features, num_classes)
            
        def forward(self, x):
            return self.resnet(x)
    """, language='python')

if __name__ == "__main__":
    main()
