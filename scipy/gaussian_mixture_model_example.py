# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
simple example of gausian mixture model (d=1)

make an animaton of the convergence.
'''

###################################################
# generate random points by cluster1 and cluster2
#==================================================

# np.random.seed(42) # fixed

# Define the number of points in each cluster
n_points = 50

# cluster1
mu1 = 0.0
sigma1 = 1.0
points1 = np.random.normal(mu1, sigma1, n_points)

# cluster2
mu2 = 6.0
sigma2 = 0.5
points2 = np.random.normal(mu2, sigma2, n_points)

# Combine the points into a single array
X = np.concatenate([points1, points2]) # observed points

# initialize parameter of GMM
weights = np.array([0.5, 0.5])
mu = np.array([4.0, 6.0])
sigma = np.array([1.0, 8.0])


#########################################
# Define the Gaussian Mixture Model
#=======================================

def GMM(X, weights, mu, sigma, n_iterations):
    '''
    Computes the Gaussian Mixture Model (GMM) given the data and initial parameters.

    Parameters:
    X (numpy.ndarray): Array of shape (n_samples,) containing the input data
    weights (numpy.ndarray): Array of shape (n_clusters,) containing the initial weights for each cluster
    mu (numpy.ndarray): Array of shape (n_clusters,) containing the initial means for each cluster
    sigma (numpy.ndarray): Array of shape (n_clusters,) containing the initial standard deviations for each cluster
    n_iterations (int): Number of iterations to run the algorithm

    Returns:
    weights_history (numpy.ndarray): Array of shape (n_iterations, n_clusters) containing the weights for each cluster at each iteration
    mu_history (numpy.ndarray): Array of shape (n_iterations, n_clusters) containing the means for each cluster at each iteration
    sigma_history (numpy.ndarray): Array of shape (n_iterations, n_clusters) containing the standard deviations for each cluster at each iteration
    '''
    n_samples = len(X)
    n_clusters = len(weights)

    # Define the responsibility matrix
    R = np.zeros((n_samples, n_clusters))
    weights_history = [weights.copy()]
    mu_history = [mu.copy()]
    sigma_history = [sigma.copy()]

    # Iterate
    for _ in range(n_iterations):
        for i in range(n_samples):
            # E-step: Update the responsibility matrix
            for j in range(n_clusters):
                R[i, j] = weights[j] * norm.pdf(X[i], mu[j], sigma[j])
            R[i]= R[i] / R[i].sum(axis=0)
    
        # M-step: Update the parameters
        for j in range(n_clusters):
            weights[j] = R[:, j].mean()
            mu[j] = np.sum(R[:, j] * X) / R[:, j].sum()
            sigma[j] = np.sqrt(np.sum(R[:, j] * (X - mu[j])**2) / R[:, j].sum())
        
        # Save the history
        weights_history.append(weights.copy())
        mu_history.append(mu.copy())
        sigma_history.append(sigma.copy())

    return np.array(weights_history), np.array(mu_history), np.array(sigma_history)

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
ax.scatter(X, [0]*len(X))

# Create the line plot
x = np.linspace(-5, 15, 100)
line, = ax.plot(x, norm.pdf(x, mu[0], sigma[0]) * weights[0] + norm.pdf(x, mu[1], sigma[1]) * weights[1], label='Mixture') # lines.Line2D
line1, = ax.plot(x, norm.pdf(x, mu[0], sigma[0])* weights[0], label='Cluster1')
line2, = ax.plot(x, norm.pdf(x, mu[1], sigma[1]) * weights[1], label='Cluster2')
ax.legend()

# Create the initialization function
def init():
    line.set_ydata([0] * len(x))
    return (line, line1, line2)

# Create the animation function
def update(frame):
    weights = weights_history[frame]
    mu = mu_history[frame]
    sigma = sigma_history[frame]
    y = norm.pdf(x, mu[0], sigma[0]) * weights[0] + norm.pdf(x, mu[1], sigma[1]) * weights[1]
    y1 =  norm.pdf(x, mu[0], sigma[0])* weights[0]
    y2 =  norm.pdf(x, mu[1], sigma[1]) * weights[1]
    line.set_ydata(y)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    
    return (line, line1, line2)

# Create the animation
animation = FuncAnimation(fig, update, init_func=init, frames=len(weights_history), interval=2000, blit=True)
animation.save('gaussian_mixture_animation.gif')

# Show the animation
plt.show()



