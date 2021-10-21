import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk.
rw = RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.tick_params(axis='both', which='major', labelsize='12')
ax.set_title("Random Walk with 1000 Steps", fontsize = 22)

x_coordinates = rw.x_values
y_coordinates = rw.y_values

x_y_coordinates = zip(rw.x_values, rw.y_values)

# (0,0) will be black, (-x,-y) will be red, (+x,+y) will be green, (x,y) such that not both x and y have the same, and such that x!=y!=0, sign will be blue.
for x,y in x_y_coordinates:
    print(x,y)
    if x == 0 and y == 0:
        ax.scatter(x, y, color='black', s=25, marker=11)
        rw.x_values.remove(x)
        rw.y_values.remove(y)
    elif x < 0 and y < 0:
        ax.scatter(x, y, color='red', s=25, marker=11)
        rw.x_values.remove(x)
        rw.y_values.remove(y)
    elif x > 0 and y > 0:    
        ax.scatter(x, y, color ='green', s=25, marker=6)
        rw.x_values.remove(x)
        rw.y_values.remove(y)
    else:
        ax.scatter(x, y, color ='blue', s=25, marker ='d')


plt.show()
    





