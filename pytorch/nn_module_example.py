import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt


class Model(nn.Module):
    def __init__(self, in_features:int=1, out_features:int=1):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.criterion = nn.MSELoss()
   
    def forward(self, x:torch.Tensor):
        return self.linear(x)
    
    def regularization(self, lambda_reg):
        l2_regularization = torch.norm(model.state_dict()['linear.weight'], p=2)**2
        return lambda_reg * l2_regularization


class Data(Dataset):
    def __init__(self, x: torch.Tensor, y: torch.Tensor):
        self.x = x
        self.y = y
        self.len = len(x)
    
    def __getitem__(self, index:int):
        return self.x[index], self.y[index]
    
    def __len__(self):
        return self.len



def train_model(x: torch.Tensor, y:torch.Tensor, model, n_epochs:int, lambda_reg:float, lr=0.01, momentum=0.9, batch_size=25):
    data = Data(x, y)
    dataloader = DataLoader(data, batch_size=batch_size, shuffle=True)
    optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=momentum)

    for epoch in range(n_epochs):
        for x_batch, y_batch in dataloader:
            optimizer.zero_grad()
            y_hat = model(x_batch)
            loss = model.criterion(y_hat, y_batch) + model.regularization(lambda_reg)
            loss.backward()
            optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, loss {loss.item():.4f}")

    # save the model checkpoint
    torch.save(model.state_dict(), "model_checkpoint.pth")


# data
N = 100
n_features = 1
noise = torch.randn(N, n_features) * 0.5 # Nx1 tensor
x = torch.randn(N, n_features) # Nx1 tensor
a, b = 2, 3
y = a*x + b + noise

# training 
model = Model()
n_epochs = 30
lambda_reg = 0.05 # regularization parameter
lr = 0.01
train_model(x, y, model, n_epochs, lambda_reg, lr=lr)

# result
a = model.state_dict()['linear.weight'].item()
b = model.state_dict()['linear.bias'].item()
print(f"predicted: y={a:.4}*x + {b:.4}")

# predict
yhat = model(x) # Nx1

# plot
fig, ax = plt.subplots()
ax.plot(x, yhat.detach().numpy(), label='Predicted')
ax.scatter(x, y, label='Acutual Values')
ax.set_title('Linear Regression with L2 regularization')
ax.set_xlabel('Input')
ax.set_ylabel('Output')
ax.legend()

plt.show()






