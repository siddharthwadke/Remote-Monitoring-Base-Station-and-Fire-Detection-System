import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Randomly Generated Sequence- Code will updated here for Input from DHT11
    humidity_c = np.random.randint(40, 50, 1)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(humidity_c)

    # Limit x and y lists to 20 items
    xs = xs[-10:]
    ys = ys[-10:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Plot Formatting
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Humidity graph')
    plt.ylabel('Humidity %')

# Call Animate() function.
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
