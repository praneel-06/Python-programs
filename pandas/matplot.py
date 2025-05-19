import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 400)  # Avoid singularity
a = 1  # Adjust as needed
r = a * (1/np.cos(theta) + np.cos(theta))

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, label=r'$r = a(\sec\theta + \cos\theta)$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Polar Plot of r = a(secθ + cosθ)")
plt.show()