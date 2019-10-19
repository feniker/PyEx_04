from scipy.fftpack import *
import numpy as np
from math import *
import matplotlib.pyplot as plt
dt = 0.01
Time = 10
t = np.arange(-Time, Time, dt)
pure_sign = [100*sin(2*pi*i) + 30*sin(2*pi*2*i) + 0*sin(2*pi*3*i) for i in t]
noise = np.random.uniform(-100, 100, len(t))
sign = pure_sign + noise
#plt.plot(t, noise, 'g')
#plt.plot(t, pure_sign, 'r')
plt.plot(t, sign)
plt.xlabel('Time, c')
plt.ylabel('Voltage, V')
plt.grid(True)
plt.title('Sign')
plt.savefig("image1.png")
plt.show()
spectrum = rfft(sign)
plt.plot(rfftfreq(len(t), d = dt), np.abs(spectrum)/len(t))
plt.xlabel('Frequence, Hz')
plt.ylabel('Voltage, V')
plt.title('Spectrum')
plt.grid(True)
plt.savefig("image2.png")
plt.show()
#New spectrum
new_spectrum = []
for i in range(len(spectrum)):
    if np.abs(spectrum[i])*10>max(np.abs(spectrum)):
        spectrum[i] = spectrum[i]
    else:
        spectrum [i] = 0
plt.plot(rfftfreq(len(t), d = dt), np.abs(spectrum)/len(t))
plt.xlabel('Frequence, Hz')
plt.ylabel('Voltage, V')
plt.title('New spectrum')
plt.grid(True)
plt.savefig("image3.png")
plt.show()
#New signal
new_sign = irfft(spectrum)
print(type(new_sign), "- type new_sign")
plt.plot(t[:len(t)//10],pure_sign[:len(t)//10], label = 'Pure sognal')
plt.plot(t[:len(t)//10],new_sign[:len(t)//10], label = 'New signal')
plt.plot(t[:len(t)//10],sign[:len(t)//10], label = 'Old signal')
plt.legend()
plt.title('New signal')
plt.savefig("image4.png")
plt.show()