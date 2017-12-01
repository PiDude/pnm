
import math
import numpy as np
import matplotlib.pyplot as plt



Fs = 2048
Ts = 1.0/Fs
t = np.arange(0,1,Ts)
f1 = 5
f2 = 30

sig1 = np.sin(2 * np.pi * f1 * t)
sig2 = 0.2 * np.sin(2 * np.pi * f2 * t)

sig3 = sig1 + sig2

noise = np.random.normal(0, 1, 2048)



nsig3 = sig3 + noise

plt.subplot(2,1,1)
plt.plot(nsig3)
plt.xlabel('time')
plt.ylabel('amplitude')



plt.subplot(2,1,2)
n = len(nsig3)    # length of signal

print ('n = ', n)

k = np.arange(0, n, 1)


T = n/Fs

print ('T = ', T)

frq = k/T        # one side of frequency range

#print(frq)

freq = frq[range(n//2)]

#print (freq)



Y = np.fft.fft(nsig3)/n

print (Y)

Y = Y[range(n//2)]

print (abs(Y))

plt.plot(freq, abs(Y), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel(' abs value freq')




plt.show()




