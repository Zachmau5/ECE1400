#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import control as ctl
from scipy import signal



import control as ctl
def main():
    s=ctl.TransferFunction.s
    h=5*(s+5)*(s+3)*(s+1)/((s+6)*(s+12)*(s+5))
    ctl.bode_plot(h, Hz=True, omega_limits=(0.01,10))
    plt.show()
    ctl.pzmap(h)
    plt.show()
if __name__ == "__main__":
    main()
