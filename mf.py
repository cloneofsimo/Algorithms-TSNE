import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data.dataloader import DataLoader
from torch.utils.data import Dataset
import torch.optim as optim
from model import mf_model


epochs = 1500
lr = 2e-1
device = "gpu"

model = mf_model()

optimizer = torch.optim.AdamW(model.parameters(), lr = lr, weight_decay = 1e-7)

for epoch in range(epochs):
    epoch_loss = 0

    model.zero_grad()
    #idxs = idxs.to(device)
    x = torch.zeros(1,1)
    loss = model(x)
    #print(model.usr(torch.tensor([0])))
    #print(loss)
    loss.backward()
    optimizer.step()
    epoch_loss += loss.item()
    print(epoch_loss)
    #$print(model.b[12])

torch.save(model,"model.dat")
model.eval()
im = torch.load("distribution_tensor.dat")

n_usr = im.shape[0]
n_item = im.shape[1]
print(n_usr)
pre = model.predict(torch.zeros(n_item))
print(pre)