import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initialize the circle (the object that will be animated)
circle = plt.Circle((1, 5), 0.5, fc='blue')

# Function to initialize the plot
def init():
    ax.add_patch(circle)
    return circle,

# Function to update the plot for each frame of the animation
def update(frame):
    x, y = circle.center
    x = x + 0.1  # Move the circle horizontally
    circle.center = (x, y)
    return circle,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100),
                              init_func=init, blit=True)

# Show the plot
plt.title('Simple Animation with Matplotlib')
plt.show()
