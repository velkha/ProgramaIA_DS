import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 100, 1000)

d_r = 1*t 
d_s = 4*(t-30)

fig, ax = plt.subplots()
plt.title('help')
plt.xlabel('Time')
plt.ylabel('Variable')
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='brown')
plt.axvline(x=30, color='purple', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')

plt.show()