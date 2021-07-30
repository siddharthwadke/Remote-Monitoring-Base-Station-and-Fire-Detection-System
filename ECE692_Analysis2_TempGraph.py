import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is used to Animate the graph
def animate(i, xs, ys):

    # Read temperature from Sensor
    temp_f = np.random.randint(60, 75, 1)

    # for appending x and y to the list
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_f)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Plot Formatting
    plt.xticks(rotation=50, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature vs Time graph')
    plt.ylabel('Temperature (deg F)')

# Call Animate() function.
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
