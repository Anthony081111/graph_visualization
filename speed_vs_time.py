"""Draw graphs of speed vs time"""

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

# GRAPH ONE
# Define speed and time values for data points
speed = [10, 10, 10, 10, 10, 10]
time = [0, 1, 2, 3, 4, 5]

# Plot speed vs time
plt.plot(time, speed, color="black")
plt.fill_between(time, speed, color="orange", alpha=0.5)   # fill the area below the curve
plt.title("Graph 01 -- Constant Speed")
plt.xlabel("Time (hours)")
plt.ylabel("Speed (miles/hour)")

# Show the unit grid on the graph
plt.grid(True)
plt.yticks(range(0, max(speed)+1, 1))
plt.xticks(range(min(time), max(time)+1, 1))

# Display the graph
plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# GRAPH TWO
# Define speed and time values for data points
speed = [0, 2, 4, 6, 8, 10]
time = [0, 1, 2, 3, 4, 5]

# Plot speed vs time
plt.plot(time, speed, color="black")
plt.fill_between(time, speed, color="orange", alpha=0.5)   # fill the area below the curve
plt.title("Graph 02 -- Increasing Speed")
plt.xlabel("Time (hours)")
plt.ylabel("Speed (miles/hour)")

# Show the unit grid on the graph
plt.grid(True)
plt.yticks(range(0, max(speed)+1, 1))
plt.xticks(range(min(time), max(time)+1, 1))

# Display the graph
plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# GRAPH THREE
# Define speed and time values for data points
fig, a1 = plt.subplots()
speed = [0, 2, 4, 6, 8, 10]
time = [0, 1, 2, 3, 4, 5]

# Plot speed vs time
plt.plot(time, speed, color="black")
plt.fill_between(time, speed, color="orange", alpha=0.5)   # fill the area below the curve
plt.title("Graph 03 -- Increasing Speed")
plt.xlabel("Time (hours)")
plt.ylabel("Speed (miles/hour)")

# Set major ticks every one unit of time
a1.xaxis.set_major_locator(MultipleLocator(1))

# Set minor ticks every 0.5 units
a1.xaxis.set_minor_locator(AutoMinorLocator(2))
a1.yaxis.set_minor_locator(AutoMinorLocator(2))

# Show the unit grid on the graph
a1.grid(which="both")
plt.grid(True)
plt.yticks(range(0, max(speed)+1, 1))
plt.xticks(range(min(time), max(time)+1, 1))

# Display the graph
plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# GRAPH FOUR
# Define speed and time values for data points
fig, a2 = plt.subplots()
speed = [0, 2, 4, 6, 8, 10]
time = [0, 1, 2, 3, 4, 5]

# Plot speed vs time
plt.plot(time, speed, color="black")
plt.fill_between(time, speed, color="orange", alpha=0.5)   # fill the area below the curve
plt.title("Graph 04 -- Increasing Speed")
plt.xlabel("Time (hours)")
plt.ylabel("Speed (miles/hour)")

# Set major ticks every one unit of time
a2.xaxis.set_major_locator(MultipleLocator(1))

# Set minor ticks every 0.5 units
a2.xaxis.set_minor_locator(AutoMinorLocator(2))
a2.yaxis.set_minor_locator(AutoMinorLocator(2))

# Show the unit grid on the graph
a2.grid(which="both")
plt.grid(True)
plt.yticks(range(0, max(speed)+1, 1))
plt.xticks(range(min(time), max(time)+1, 1))

# Display the graph
plt.show()
