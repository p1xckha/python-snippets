# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Tuple

'''
simple example of gausian mixture model (d=1)
make an animaton of the convergence.
'''


#########################################
# Define the Gaussian Mixture Model
#=======================================

def GMM(X: np.array, weights: np.array, mu: np.array, sigma: np.array, 
        n_iterations: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray] :
    '''
    Computes the Gaussian Mixture Model (GMM) given the data and initial parameters.
    '''
    n_samples = len(X)
    n_gaussians = len(weights)

    # Define the post probability matrix
    post_prob = np.zeros((n_samples, n_gaussians))
    
    weights_history = [weights.copy()]
    mu_history = [mu.copy()]
    sigma_history = [sigma.copy()]

    # Iterate
    for _ in range(n_iterations):
        # E-step: Update the post probability matrix
        for i in range(n_samples):
            for j in range(n_gaussians):
                post_prob[i, j] = weights[j] * norm.pdf(X[i], mu[j], sigma[j])
            post_prob[i]= post_prob[i] / post_prob[i].sum(axis=0)
    
        # M-step: Update the parameters
        for j in range(n_gaussians):
            weights[j] = post_prob[:, j].mean()
            mu[j] = np.sum(post_prob[:, j] * X) / post_prob[:, j].sum()
            sigma[j] = np.sqrt(np.sum(post_prob[:, j] * (X - mu[j])**2) / post_prob[:, j].sum())
        
        # Save the history
        weights_history.append(weights.copy())
        mu_history.append(mu.copy())
        sigma_history.append(sigma.copy())

    return np.array(weights_history), np.array(mu_history), np.array(sigma_history)

# Create the initialization function
def init():
    return (dots, mixture_line, gaussian1_line, gaussian2_line)

# Create the animation function
def update(frame: int):
    weights = weights_history[frame]
    mu = mu_history[frame]
    sigma = sigma_history[frame]

    mixture_y = norm.pdf(x, mu[0], sigma[0]) * weights[0] + norm.pdf(x, mu[1], sigma[1]) * weights[1]
    gaussian1_y =  norm.pdf(x, mu[0], sigma[0])* weights[0]
    gaussian2_y =  norm.pdf(x, mu[1], sigma[1]) * weights[1]

    mixture_line.set_ydata(mixture_y)
    gaussian1_line.set_ydata(gaussian1_y)
    gaussian2_line.set_ydata(gaussian2_y)
    
    # set the title to indicate the current iteration number
    ax.set_title(f"Gaussian Mixture Model (Iteration {frame})") 
    
    return (mixture_line, gaussian1_line, gaussian2_line)


###################################################
# generate random points by gaussian1 and gaussian2
#==================================================

# np.random.seed(42) # fixed

# Define the number of points in each gaussian
n_points = 50

# gaussian1
mu1 = 0.0
sigma1 = 1.0
points1 = np.random.normal(mu1, sigma1, n_points)

# gaussian2
mu2 = 6.0
sigma2 = 0.5
points2 = np.random.normal(mu2, sigma2, n_points)

# Combine the points into a single array
X = np.concatenate([points1, points2]) # observed points

# or use simple observed points X
X = np.array([-1.0, 0.0, 4.0, 5.0, 6.0])

# initialize parameter of GMM
weights = np.array([0.5, 0.5]) 
mu = np.array([6.0, 7.0])
sigma = np.array([1.0, 2.0])


########################
# Run the GMM algorithm
#========================
weights_history, mu_history, sigma_history = GMM(X, weights, mu, sigma, n_iterations=10)

# find out that parameters are converged
print("weights_history:\n", weights_history)
print("mu_history: \n", mu_history)
print("sigma_history:\n", sigma_history) 


#############################################################
# make an animation with histories of weights, mu, sigma
#============================================================

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim([-5, 15])
ax.set_ylim([-0.1, 0.7])
ax.set_xlabel('X')
ax.set_ylabel('PDF (Probability Density Function)')
ax.set_title('Gaussian Mixture Model (d=1)')

# plot 1d observed points on the x axis
dots = ax.scatter(X, [0]*len(X))

# Create the line plot
x = np.linspace(-5, 15, 100)
mixture_line, = ax.plot(x, norm.pdf(x, mu[0], sigma[0]) * weights[0] + norm.pdf(x, mu[1], sigma[1]) * weights[1], label='Mixture') # lines.Line2D
gaussian1_line, = ax.plot(x, norm.pdf(x, mu[0], sigma[0])* weights[0], label='gaussian1')
gaussian2_line, = ax.plot(x, norm.pdf(x, mu[1], sigma[1]) * weights[1], label='gaussian2')
ax.legend()

# Create the animation
animation = FuncAnimation(fig, update, init_func=init, frames=len(weights_history), interval=500, blit=True)
animation.save('gaussian_mixture_animation.gif')

# Show the animation
plt.show()

