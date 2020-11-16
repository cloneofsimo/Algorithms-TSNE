import torch
import torch.nn as nn
import torch.nn.functional as F

class mf_model(nn.Module):
    def __init__(self):
        super().__init__()
        self.im = torch.load("distribution_tensor.dat")
        n_usr = self.im.shape[0]
        n_item = self.im.shape[1]
        n_dim = 16
        
        self.item = nn.Embedding(n_item, n_dim)
        self.usr = nn.Embedding(n_usr, n_dim)
        self.bias = nn.Embedding(1, n_item)
        self.im = torch.load("distribution_tensor.dat")
        self.n_usr = n_usr
        self.n_item = n_item

    def forward(self, x):
        U = self.item(torch.arange(0, self.n_item)).t()
        V = self.usr(torch.arange(0, self.n_usr))
        im_p = V@U + self.bias(torch.tensor([0])).repeat(self.n_usr, 1)
        loss = ((im_p - self.im)*(im_p - self.im)).sum()
        return loss
    
    def predict(self, x):
        y = self.item(torch.arange(0, self.n_item)).t() @ (x)
        lh = self.usr(torch.arange(0, self.n_usr)) @ y
        return torch.argmax(lh)
    
    def predict_kth(self, x, k):
        y = self.item(torch.arange(0, self.n_item)).t() @ (x)
        lh = self.usr(torch.arange(0, self.n_usr)) @ y
        _, ind = torch.topk(lh, k = k)
        return ind[k-1]

#Autograd

