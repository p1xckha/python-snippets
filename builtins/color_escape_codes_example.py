# -*- coding: utf-8 -*-

# modify text color
def red(s):
    return '\033[1;31m%s\033[m' % s

def green(s):
    return '\033[1;32m%s\033[m' % s 

def yellow(s):
    return '\033[1;33m%s\033[m' % s 
    
def blue(s):
    return '\033[1;34m%s\033[m' % s

def magenta(s):
    return '\033[1;35m%s\033[m' % s 

def cyan(s):
    return '\033[1;36m%s\033[m' % s 

def white(s):
    return '\033[1;37m%s\033[m' % s 

def rgb_text(s, rgb=(0,255,0)):
    color_rgb = ';'.join(str(c) for c in rgb)
    text = '\033[38;2;%sm%s\033[m' % (color_rgb, s)
    return text

# modify background color
def white_bg(s): # looks like light gray
    return '\033[47m%s\033[m' % s 

def rgb_bg(s, rgb=(0,255,0)):
    color_rgb = ';'.join(str(c) for c in rgb)
    text = '\033[48;2;%sm%s\033[m' % (color_rgb, s)
    return text

text = "Hello Color Escape Codes"
color_functions = [red, green,yellow,blue,magenta,cyan,white]
for color_function in color_functions:
    print(color_function(text))

print(rgb_text("green text"))
print(white_bg("white background"))
print(rgb_bg("green background"))

