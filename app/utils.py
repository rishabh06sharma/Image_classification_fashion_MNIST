from numpy.core.fromnumeric import resize
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, ConcatDataset
from torch import nn
import torch.nn.functional as F
from PIL import Image
from torchvision.transforms.transforms import Grayscale, Resize
import io

## load the model
class net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
        nn.LayerNorm(normalized_shape=([1, 28, 28])),
        nn.Conv2d(1, 10, kernel_size=3),
        nn.ReLU(),
        nn.Conv2d(10, 12, kernel_size=3),
        nn.ReLU(),
        nn.Conv2d(12, 18, kernel_size=3),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(18*22*22, 120),
        nn.ReLU(),
        nn.Linear(120, 60),
        nn.ReLU(),
        nn.Linear(60, 10))
    def forward(self,t):
        return self.layers(t)

model=net()
PATH="models/model-fold-9.pth" # model directory
model.load_state_dict(torch.load(PATH,map_location='cpu'))

def image_transform(image):
    transform=transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                transforms.Resize((28,28)), transforms.ToTensor()])
    image=Image.open(io.BytesIO(image))
    return transform(image).unsqueeze(0) #one sample

def predict_it(image):
    # inputs, targets = inputs.to(device), targets.to(device)
    output=model(image)
    _, predicted = torch.max(output.data, 1)
    return predicted
