import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to initialize the plot
def init():
    ax.clear()
    return ax,

# Function to update the plot for each frame of the animation
def animate(frame):
    ax.clear()
    ax.set_title(f'Frame {frame}')
    ax.plot_wireframe(X, Y, Z + 0.1 * frame, color='b')
    return ax,

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, interval=50, blit=True)

# Uncomment the next line to save the animation as a gif file
# ani.save('3d_wireframe_animation.gif', writer='imagemagick')

# Show the plot
plt.show()
