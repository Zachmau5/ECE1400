import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#signal.transferfunction requires inputs of coeff of num/denom
s = signal.TransferFunction([5, 25, 15, 5], [1, 23, 162, 360])

# Bode plot
w, mag, phase = signal.bode(s, np.logspace(10e-3, 10, num=500))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w, mag)
ax1.set_ylabel('Magnitude (dB)')
ax2.semilogx(w, phase)
ax2.set_ylabel('Phase (deg)')
ax2.set_xlabel('Frequency (Hz)')
plt.suptitle('Bode Plot of H(s)')

# Pole-zero plot
zeros = s.zeros
poles = s.poles
fig, ax = plt.subplots()
ax.scatter(zeros.real, zeros.imag, marker='o', color='xkcd:vomit green', label='Zeros')
ax.scatter(poles.real, poles.imag, marker='x', color='xkcd:eggplant purple', label='Poles')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_aspect('equal', 'box')
plt.legend()
plt.title('Pole-Zero Plot of H(s)')

# Show the plots
plt.show()
