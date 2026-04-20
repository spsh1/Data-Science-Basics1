import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to create the initial plot
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# Function to update the plot for each frame of the animation
def animate(frame):
    line.set_ydata(np.sin(x + 0.1 * frame))
    return line,

# Create a figure and axis
fig, ax = plt.subplots()

# Generate initial data
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
line, = ax.plot(x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, interval=50, blit=True)

# Uncomment the next line to save the animation as a gif file
# ani.save('my_animation.gif', writer='imagemagick')

# Show the plot
plt.show()
