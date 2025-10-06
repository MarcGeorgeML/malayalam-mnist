from letter_architecture import ConvNet
from PIL import Image
import torch
from torchvision import transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def predict(image): 
    test_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor()
    ])

    # Load and transform the image
    transformed_image = test_transform(image).unsqueeze(0).to(device)  
    
    # load the model
    model = ConvNet().to(device)
    model.load_state_dict(torch.load('mal_model.pth', map_location=device))
    model.eval() 

    # Pass the input through the model
    with torch.no_grad():
        output = model(transformed_image)
        _, predicted = torch.max(output, 1)
    
    return predicted.item()