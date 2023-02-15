import pandas as pd
import matplotlib.pyplot as plt

# read Spice output file into a pandas dataframe
data = pd.read_csv('test/data.correct', delim_whitespace=True, header=None)

# select the columns with the time and current data for each current
time = data[0]
i1 = data[1]
i2 = data[2]
i3 = data[3]

# plot the three currents vs time
plt.plot(time, i1, label='I1')
plt.plot(time, i2, label='I2')
plt.plot(time, i3, label='I3')

# add axis labels and a title to the plot
plt.xlabel('time (sec)')
plt.ylabel('current (mA)')
plt.title('Spice Output')

# add a legend to the plot
plt.legend()

# show the plot
plt.show()
