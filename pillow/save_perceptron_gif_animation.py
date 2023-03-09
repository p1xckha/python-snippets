# -*- coding: utf-8 -*-

import numpy as np 
from PIL import Image, ImageDraw

class DrawGifGraph():
    def __init__(self, width=250, height=250):
        self.width = width
        self.height = height
        self.offsetx = int(self.width/2)
        self.offsety = int(self.height/2)
        self.im = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
        self.frames = [] # list of im
        self._times = 1
    
    @property
    def times(self):
        return self._times
    
    @times.setter
    def times(self, value):
        if value <= 0:
            raise ValueError("Times must be a positive integer.")
        self._times = value
    
    def clear_im(self):
        self.im = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
        
    def draw_point(self, x, y, r=0.5, fill=(0,0,255)):
        draw = ImageDraw.Draw(self.im)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=fill)
    
    def draw_line(self, x1, y1, x2, y2, fill=(0,0,0)):
        draw = ImageDraw.Draw(self.im)
        draw.line([(x1,y1),(x2,y2)], fill=fill)
        
    def draw_axis(self):
        self.draw_line(self.offsetx,0, self.offsetx, self.width)
        self.draw_line(0,self.offsety, self.width, self.offsety)
    
    def xy2wd(self, x, y, times=None):
        '''
        convert a point (x,y) into a point (width, height)
        '''
        if times:
            self.times = times
        w = x * self.times + self.offsetx
        h = -y * self.times + self.offsety
        return w, h
    
    def add_frame(self, frame: Image.Image):
        self.frames.append(frame)
    
    def save_im(self, filename):
        self.im.save(filename)
    
    def save_gif_animation(self, filename):
        self.frames[0].save(filename, save_all=True, append_images=self.frames[1:], duration=500, loop=3)

def perceptron(X, Y, start=0, through_origin=True):
    w = np.zeros(2) # weight
    b = 0 # bias
    w_list = [] # list for weights
    b_list = [] # list for bias
    i = start
    cnt = 0
    while not all(Y*(X@w+b)>0):
        x,y = X[i], Y[i]
        if y*(w@x+b)<=0:
          cnt += 1
          w += y*x
          if not through_origin:
              b += y
          w_list.append(w.copy())
          b_list.append(b)
        i = (i+1) % len(X)
    return w_list, b_list


def line(w:list[float],b:float): # annnotation is correct?
    assert w[1] != 0, "we assume w[1]!=0"
    return lambda x,w0=w[0],w1=w[1]: (-w0*x -b)/w1 

##################################


X = np.array([
[-1,-1],
[1,0],
[-1,10]
])

Y = np.array([
    1,
    -1,
    1
])

w_list, b_list = perceptron(X, Y, 0, True)
print(w_list)
print(b_list) 

gifgraph = DrawGifGraph()

gifgraph.times = 10
xmin = -15
xmax = 15
ymin = -15
ymax = 15
# Loop through a range of values to create the animation frames
for i in range(len(w_list)):
    h = line(w_list[i], b_list[i]) 
    x1, y1 = gifgraph.xy2wd(xmin, h(xmin))
    x2, y2 = gifgraph.xy2wd(xmax, h(xmax))
    gifgraph.draw_line(x1, y1, x2, y2)
    gifgraph.draw_axis()

    # Draw the points and color them based on their classification
    for j, point in enumerate(X):
        color = (255, 0, 0) if Y[j] == 1 else (0, 0, 255)
        x, y = gifgraph.xy2wd(point[0], point[1])
        gifgraph.draw_point(x, y, fill=color)
    gifgraph.add_frame(gifgraph.im)
    gifgraph.clear_im()
    
# Save the sequence as an animated GIF
gifgraph.save_gif_animation('percep.gif')
