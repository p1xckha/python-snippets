# -*- coding: utf-8 -*-
'''
draw a plane and a normal vector onto it
'''
import matplotlib.pyplot as plt
import numpy as np

class PlotPlane():
    def __init__(self, a0:float, a1:float, a2:float, a3:float):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        
        # The normal vector theta of the plane is defined by the coefficients a1, a2, and a3. 
        self.theta = np.array([a1,a2,a3]) 
        # unit vector of theta
        self.unit_theta = self.theta / np.linalg.norm(self.theta) 
        
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
    
    def linear(self, x, y) -> float:
        return (-self.a0 - self.a1*x - self.a2*y)/self.a3
    
    @property
    def fig(self):
        return self._fig
    
    @fig.setter
    def fig(self, fig):
        self._fig = fig
    
    @property
    def ax(self):
        return self._ax
    
    @ax.setter
    def ax(self, ax):
        self._ax = ax
    
    def plot(self, xmin=-10, xmax=10, ymin=-10, ymax=10):
        x = np.arange(xmin, xmax, 0.1)
        y = np.arange(ymin, ymax, 0.1)
        X, Y = np.meshgrid(x, y)
        Z = self.linear(X, Y)
        title = self.__str__()
        self.ax.plot_surface(X, Y, Z)
        self.ax.set_xlabel('x-axis')
        self.ax.set_ylabel('y-axis')
        self.ax.set_zlabel('z-axis')
        self.fig.suptitle(title)
    
    def plot_point(self, x, y, z, label=""):
        self.ax.scatter(x, y, z, color='red', label=label)
    
    def distance_from_point(self, x: float, y:float, z:float)-> float:
        '''
        return the signed distance, that is, negative number is possible 
        '''
        theta = np.array([self.a1, self.a2, self.a3])
        point = np.array([x, y, z])
        theta0 = self.a0
        norm_theta = np.linalg.norm(theta)
        distance = (np.inner(theta, point) + theta0)/norm_theta
        
        return distance
    
    def get_projection(self, x:float, y:float, z:float) -> np.ndarray:
        point = np.array([x, y, z])
        result = point - self.distance_from_point(x, y, z) * self.unit_theta
        return result
    
    def draw_line(self,point1, point2, label=""):
        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]
        z_values = [point1[2], point2[2]]
        self.ax.plot(x_values, y_values, z_values, label=label)
        
    def draw_normal_vector_from_point(self, x, y, z):
        projection = self.get_projection(x, y, z)
        self.draw_line(point, projection, "normal vector onto the plane")
        self.plot_point(*projection)
    
    def savefig(self, filename):
        self.fig.savefig(filename)
        
    def __str__(self):
        result = f"Plane:{self.a0}+{self.a1}x+{self.a2}y+{self.a3}z=0\n"
        return result


pp = PlotPlane(100, 1, 2, 5)
pp.plot(-100,100,-100,100)
point = (50,0,100)
pp.plot_point(*point)
pp.draw_normal_vector_from_point(*point)

plt.legend()
plt.show()
pp.savefig('myplane.svg')



