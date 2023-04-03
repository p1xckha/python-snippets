# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


class NonLinearPerceptron():
    def __init__(self, x:np.array, y:np.array, transform):
        self.x = x # (n, d) array
        self.y = y # (n, ) array
        
        self.transform = transform # x -> phi(x)
        self.x_transformed = np.apply_along_axis(transform, axis=1, arr=x)
        self.theta = self.transform((0,0)) 
        self.theta0 = 0
        self.mistakes = np.zeros(x.shape[0]) # (n, ) array

    def update(self, i):
        distance = self.theta @ self.x_transformed[i] + self.theta0
        if self.y[i] * distance <=0:
            self.mistakes[i] += 1
            self.theta += self.x_transformed[i] * self.y[i]
            self.theta0 += self.y[i]
    
    def accuracy(self):
        d = self.y * (self.x_transformed @ self.theta + self.theta0)
        acc = d > 0
        return acc.mean()
    
    def fit(self, epochs=1, shuffle=False):
        for epoch in range(epochs):
            if shuffle:
                perm = np.random.permutation(len(self))
                self.x_transformed = self.x_transformed[perm]
                self.y = self.y[perm]
            for i in range(len(self)):
                self.update(i)
    
    def __str__(self):
        return f"{self.theta}@phi(x) + {self.theta0} = 0"
    
    def __len__(self):
        return len(self.x)


def non_linear_perceptron_2d_example():
    # generate random 2D dataset
    n_features = 2
    n_samples = 100
    np.random.seed(42)
    x = np.random.randn(n_samples, n_features)
    y = np.sign(-6 * x[:,0]**2 - 3* x[:,1]**2 +10) # placeholder
    
    # polynomial feature vector p=2
    def transform(x):
        return np.array([x[0]**2, x[1]**2, np.sqrt(2)*x[0]*x[1], np.sqrt(2)*x[0], np.sqrt(2) *x[1], 1])

    p = NonLinearPerceptron(x, y, transform)
    p.fit(10)
    print(p)
    print(p.accuracy())
    
    # plot data points
    colors = np.where(y > 0, 'b', 'r')
    plt.scatter(x[:,0], x[:,1], c=colors)
    
    # Define a grid of x and y values
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    
    a,b,c,d,e,f = p.theta
    g = p.theta0

    # Calculate the value of the ellipse equation for each point in the grid
    F = a * X ** 2 + b * Y**2 + c * np.sqrt(2) *X*Y + d*np.sqrt(2)*X + e* np.sqrt(2)*Y + f + g

    # draw the decision boundary
    plt.contour(X, Y, F, levels=[0], colors='black')
    plt.gca().set_aspect('equal')
    plt.show()


if __name__ == '__main__':
    non_linear_perceptron_2d_example()
