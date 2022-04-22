#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:11:19 2022

@author: garimasharma
This file gives an idea how to use pyplots and plotly for data visualization
"""

#%% Chapter - 15 - Data visualization 

# prob 15. 1

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y=[]
for num in x:
    cube = num**3
    y.append(cube)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

z=[]
x1 = list(range(1,5001,1))
for num in range(1, 5001,1):
    cube1= num**3
    z.append(cube1)

fig,ax = plt.subplots()
ax.plot(x1,z)
plt.title('Cube of nums', fontsize=14)
plt.xlabel('NUms', fontsize=14)
plt.ylabel('cubes', fontsize=14)
ax.tick_params(axis='both', labelsize=14)    
plt.show()    
#%%
# we can change the look of the plot by using build in style functions

plt.style.available  # run this on kernal to check the available styles 


        
z=[]
x1 = list(range(1,5001,1))
for num in range(1, 5001,1):
    cube1= num**3
    z.append(cube1)

# fivethirtyeight, seaborn-ticks, tabeleau-colorblind10 are nice ones to use 
plt.style.use('classic')
fig,ax = plt.subplots()
ax.plot(x1,z)
plt.title('Cube of nums', fontsize=14)
plt.xlabel('NUms', fontsize=14)
plt.ylabel('cubes', fontsize=14)
ax.tick_params(axis='both', labelsize=14)    
plt.show()            
    
    
#%% We can use scatter plot rather than a line plot 

        
z=[]
x1 = list(range(1,5001,1))
for num in range(1, 5001,1):
    cube1= num**3
    z.append(cube1)

# fivethirtyeight, seaborn-ticks, tabeleau-colorblind10 are nice ones to use 
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x1,z, s=3)     # use scatter instead of plot 

ax.axis([1,5000,1, z[-1]+1000])   # set axis limits of x-y-axis

plt.title('Cube of nums', fontsize=14)
plt.xlabel('NUms', fontsize=14)
plt.ylabel('cubes', fontsize=14)
ax.tick_params(axis='both', which ='major', labelsize=14)    
plt.show()  


#%% we can customize the colors of the graphs as below


z=[]
x1 = list(range(1,5001,1))
for num in range(1, 5001,1):
    cube1= num**3
    z.append(cube1)

# fivethirtyeight, seaborn-ticks, tabeleau-colorblind10 are nice ones to use 
plt.style.use('seaborn')
fig,ax = plt.subplots()
#ax.scatter(x1,z, c='red', s=5)     # use scatter instead of plot 
# or 

#ax.scatter(x1,z, c =(0,0.8,0),s=5)

# or you can use colormap 

ax.scatter(x1,z, c=z, cmap = plt.cm.Blues, s=5)


ax.axis([1,5000,1, z[-1]+1000])   # set axis limits of x-y-axis

plt.title('Cube of nums', fontsize=14)
plt.xlabel('NUms', fontsize=14)
plt.ylabel('cubes', fontsize=14)
ax.tick_params(axis='both', which ='major', labelsize=14)    
plt.show()           

#%% we can save our plots by using ply.savefig() instead of plt.show()

z=[]
x1 = list(range(1,5001,1))
for num in range(1, 5001,1):
    cube1= num**3
    z.append(cube1)

# fivethirtyeight, seaborn-ticks, tabeleau-colorblind10 are nice ones to use 
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x1,z, c='red', s=5)     # use scatter instead of plot 
# or 

#ax.scatter(x1,z, c =(0,0.8,0),s=5)

# or you can use colormap 

#ax.scatter(x1,z, c=z, cmap = plt.cm.Blues, s=5)


ax.axis([1,5000,1, z[-1]+1000])   # set axis limits of x-y-axis

plt.title('Cube of nums', fontsize=14)
plt.xlabel('NUms', fontsize=14)
plt.ylabel('cubes', fontsize=14)
ax.tick_params(axis='both', which ='major', labelsize=14)    

plt.savefig('cubes.png', bbox_inches='tight')

#%% random walk plot

from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        """ Initialize the attributes of the walk"""
        self.num_points = num_points
        # all walk starts at 0,0
        self.x_values =[0]
        self.y_values = [0]
        
    def fill_walk(self):
        """ calculate all points in the walk"""
        # Keep taking steps until we reach max num_points
        while len(self.x_values) < self.num_points:
            x_direction = choice([1])
            x_distance = choice([1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4,5,6,7,8])
            y_step = y_direction * y_distance
            
            #Reject moves that go nowhere
            if x_step==0 and y_step==0:
                continue
            else:
                # calculate the new position
                x = self.x_values[-1] + x_step
                y = self.y_values[-1] + y_step
                
                self.x_values.append(x)
                self.y_values.append(y)
                

# plot the random walk
Rw = RandomWalk()
Rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(Rw.x_values, Rw.y_values, s=10)
plt.title('Random walk', fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()

#%% generate multiple random walks

while True:
    rw=RandomWalk()
    rw.fill_walk()
    
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()
    
    keep_running = input("make another walk (y/n)?")
    if keep_running=='n':
        break
    
#%% coloring the walk points 

while True:
    rw=RandomWalk()
    rw.fill_walk()
    
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("make another walk (y/n)?")
    if keep_running=='n':
        break
    
#%% plotting the starting and end points

    
while True:
    rw=RandomWalk()
    rw.fill_walk()
    
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=15)
    
    # emphasise on first and last point
    ax.scatter(0,0,c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolor='none', s=100)

    plt.show()
    
    keep_running = input("Do you want more random walks (y/n)?")
    if keep_running == 'n':
        break

#%% turn off the axis in this plot

    
while True:
    rw=RandomWalk()
    rw.fill_walk()
    
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=15)
    
    # emphasise on first and last point
    ax.scatter(0,0,c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolor='none', s=100)
    
    # axis off
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want more walks (y/n)?")
    if keep_running =='n':
        break
        
#%% Add more points (adding plot points)

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor='none', s=10)
    plt.show()
    
    keep_running = input("Do you want more walks (y/n)?")
    if keep_running =='n':
        break

#%% altering the size of the image to fill the screen

while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.style.use('seaborn')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor='none', s=10)
    plt.show()
    
    keep_running = input("Do you want more walks (y/n)?")
    if keep_running =='n':
        break
    
#%% Prob 15.3 

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values)
    plt.show()    
    
    keep_running = input("do yu want more random walks (y/n)?")
    if keep_running=='n':
        break
    
#%% Rolling a dice an dplot histogram using plotly


from random import randint

class Die():
    
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)
    
#%%     

from plotly.graph_objects import Bar, Layout
from plotly import offline

die = Die()
# make some rolls and store the result in list
result=[]
for roll in range(100):
    results = die.roll()
    result.append(results)
    
print(result)    

# Analyze the results
frequency=[]
for value in range(1, die.num_sides + 1):
    frequencys = result.count(value)
    frequency.append(frequencys)
    
# Visulalize the results 

x_value = list(range(1,die.num_sides+1))

data = [Bar(x = x_value, y = frequency)]


x_axis_config = {'title': 'Result'}
y_axis_config = {'title':'frequencies'}

my_layout = Layout(title = 'Hist of rollong dice 100 times', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='hist_d6.html')   
# by defauult it opnes the interactive plot in web browser as a HTML file, we can save that file
#in our working dir by using "filename='name.html'

#%% Roll 2 dice, D6  

die1 = Die()
die2 = Die()

result=[]

for roll in range(100):
    results = die1.roll() + die2.roll()
    result.append(results)
    
print(result)

# analyze frequencies 
frequency = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    f = result.count(value)
    frequency.append(f)

# Visulaize 

x_value = list(range(2, max_result+1))
data = [ Bar(x = x_value, y = frequency )  ]

x_axis_config = {'title': 'result', 'dtick':1}
y_axis_config = {'title': 'Frequency of results'}

my_layout = Layout(title='Hist of rolling 2 dice', xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='twodice.html')

#%% Roll 2 dice : D6 and D10

die1 = Die()
die2=Die(10)

result=[]
for roll in range(100):
    results = die1.roll() + die2.roll()
    result.append(results)
    
print(result)

frequency = []

max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    f = result.count(value)
    frequency.append(f)
   
    
x_value = list(range(2,max_result + 1))

data = [Bar(x = x_value, y = frequency)]


x_axis_config = {'title': 'Result'}
y_axis_config = {'title':'frequencies'}

my_layout = Layout(title = 'Hist of rollong dice 100 times', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='hist_d10.html')     


    


    