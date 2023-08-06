import numpy as np
from tqdm import tqdm
from .functions import Linear

class LinearRegression():
    def __init__(self, train_inputs, train_targets):
        self.inputs = train_inputs
        self.targets = train_targets
        self.prediction = None
        self.loss = None
        self.linear = Linear(train_inputs.shape[1], train_targets.shape[1])
            
    def forward(self,X,y): 
        self.linear.inputs = self.inputs = X
        self.linear.targets = self.targets = y
        self.outputs = self.linear.forward()
        return self.outputs
      
    def backward(self, lr = 1e-3):
        self.linear.backward(lr)

        
    def fit(self, epochs):
        for epoch in tqdm(range(epochs)):
            self.forward(self.inputs, self.targets)
            self.backward()
