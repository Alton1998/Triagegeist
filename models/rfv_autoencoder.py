from typing import List

from torch import nn


class RFVEncoder(nn.Module):
    def __init__(self, input_dim:int=38, hidden_dim=None, output_dim:int=8):
        super(RFVEncoder, self).__init__()
        if hidden_dim is None:
            hidden_dim = [64, 32, 16]
        layers_list = list()
        n_in = input_dim
        for i in hidden_dim:
            layers_list.append(nn.Linear(n_in,i))
            layers_list.append(nn.ReLU())
            n_in = i

        layers_list.append(nn.Linear(hidden_dim[-1],output_dim))
        self.encoder = nn.Sequential(*layers_list)

    def forward(self, x):
        return self.encoder(x)


class RFVDecoder(nn.Module):
    def __init__(self, input_dim:int=8, hidden_dim=None, output_dim:int=38):
        super(RFVDecoder, self).__init__()
        if hidden_dim is None:
            hidden_dim = [16,32,64]
        n_in = input_dim
        layers_list = list()
        for i in hidden_dim:
            layers_list.append(nn.Linear(n_in,i))
            layers_list.append(nn.ReLU())
            n_in = i
        layers_list.append(nn.Linear(hidden_dim[-1],output_dim))
        self.decoder = nn.Sequential(*layers_list)


    def forward(self, x):
        return self.decoder(x)


class RFVAutoEncoder(nn.Module):
    def __init__(self, encoder:nn.Module=RFVEncoder(), decoder:nn.Module=RFVDecoder()):
        super(RFVAutoEncoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        x = self.encoder(x)
        return self.decoder(x)
