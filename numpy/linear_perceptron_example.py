# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self, x:np.array, y:np.array):
        self.x = x # (n, d) matrix
        self.y = y # (n, ) array
        self.theta = np.zeros(x.shape[1:]) # (d, ) array
        self.theta0 = 0
        self.mistakes = np.zeros(x.shape[0]) # (n, ) array
    
    def update(self, i):
        distance = self.y[i] * (self.x[i] @ self.theta + self.theta0)
        if distance <= 0:
            self.theta += self.y[i] * self.x[i]
            self.theta0 += self.y[i]
            self.mistakes[i] += 1
    
    def fit(self, epochs=1, shuffle=False):
        for epoch in range(epochs):
            if shuffle:
                perm = np.random.permutation(len(self))
                self.x = self.x[perm]
                self.y = self.y[perm]
            for i in range(len(self)):
                self.update(i)
    
    def accuracy(self):
        distances = self.y * (self.x @ self.theta + self.theta0)
        acc = distances > 0
        return acc.mean()
    
    def predict(self, x):
        return np.sign(x @ self.theta + self.theta0)
    
    def __len__(self):
        return len(self.x)
    
    def __str__(self):
        return f"<{self.theta},x> + {self.theta0} = 0"

#####################


    
def perceptron_1d_example():
    # dim = 1
    x = np.array([[-1], [0], [1], [2],[3],[4]])
    y = np.array([-1, -1, -1, 1, 1, 1])
    p = Perceptron(x, y)
    p.fit(5)
    print(p)
    print("accuracy:",p.accuracy())

def perceptron_2d_example():
    # generate random 2D dataset
    n_features = 2
    n_samples = 100
    np.random.seed(42)
    x = np.random.randn(n_samples, n_features)
    y = np.sign(x[:,0] + x[:,1])
    
    # train perceptron
    p = Perceptron(x, y)
    p.fit(epochs=5, shuffle=True)
    print(p)
    print("accuracy:",p.accuracy())
    
    colors = np.where(y > 0, 'b', 'r')
    plt.scatter(x[:,0], x[:,1], c=colors)
    
    # draw the decision boundary
    w = -p.theta[0] / p.theta[1]
    b = -p.theta0 / p.theta[1]
    x_line = np.linspace(-3, 3)
    y_line = w * x_line + b
    plt.plot(x_line, y_line, 'g--')
    
    plt.show()

def perceptron_3d_example():
    # generate random 3D dataset
    n_features = 3
    n_samples = 100
    np.random.seed(42)
    x = np.random.randn(n_samples, n_features)
    y = np.sign(x[:,0] + x[:,1] + x[:,2])
    
    # train perceptron
    p = Perceptron(x, y)
    p.fit(epochs=4, shuffle=True)
    print(p)
    print("accuracy:",p.accuracy())
    
    # plot the points and decision plane
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    colors = np.where(y > 0, 'b', 'r')
    ax.scatter(x[:,0], x[:,1], x[:,2], c=colors)
    
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 10), np.linspace(y_min, y_max, 10))
    zz = (-p.theta[0]*xx - p.theta[1]*yy - p.theta0) / p.theta[2]
    ax.plot_surface(xx, yy, zz, alpha=0.2)
    
    # set the viewpoint based on the input angle
    angle_degrees = 260
    ax.view_init(elev=30, azim=angle_degrees, roll=0)
    
    plt.show()


perceptron_1d_example()
perceptron_2d_example()
perceptron_3d_example()

