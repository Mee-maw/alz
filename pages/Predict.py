import streamlit as st
from PIL import Image
import torch
print(torch.__version__)
import torch
from torchvision import transforms, models
import torch.nn as nn

class CustomResNetModel(nn.Module):
    def __init__(self, num_classes):
        super(CustomResNetModel, self).__init__()
        self.resnet = models.resnet50(pretrained=False)
        num_features = self.resnet.fc.in_features
        self.resnet.fc = nn.Linear(num_features, num_classes)
                
    def forward(self, x):
        return self.resnet(x)

def load_model(model_path, num_classes):
    model = CustomResNetModel(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def main():
    st.title("Alzheimer's Disease Stage Prediction")
    st.write("Upload an MRI image to predict the stage of Alzheimer's Disease.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Define transformations
            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])
            
            image = transform(image)
            image = image.unsqueeze(0)

            # Load the model
            num_classes = 4
            model = load_model('custom_resnet_model.pth', num_classes)
            
            # Perform prediction
            with torch.no_grad():
                outputs = model(image)
                _, preds = torch.max(outputs, 1)
                class_names = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
                prediction = class_names[preds[0]]
            
            st.write(f"Prediction: **{prediction}**")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
