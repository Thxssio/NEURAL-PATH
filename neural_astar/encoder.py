import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, input_channels, output_channels):
        super(CNN, self).__init__()
        self.conv = nn.Conv2d(input_channels, output_channels, kernel_size=3, padding=1)

    def forward(self, x):
        return self.conv(x)

class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        # Aqui entraria a implementação do UNet
        self.dummy_layer = nn.Identity()

    def forward(self, x):
        return self.dummy_layer(x)
