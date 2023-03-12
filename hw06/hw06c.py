#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

# read Spice output file into a pandas dataframe
data = pd.read_csv("../test/data.correct")
data.plot(x="time",ylabel="current (mA)",xlabel="time (sec)",title="Spice Output")
plt.show()
