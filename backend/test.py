import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# True output
t = 5

# Generate some random data for illustration
np.random.seed(42)
x = np.random.rand(100)
o = 2 * x + 1 + 0.1 * np.random.randn(100)  # Simple linear relation with noise

# Define the error function
def error(w0, w1):
    return np.mean((t - (w0 + w1 * x))**3)

# Generate a meshgrid of w0 and w1 values
w0_values = np.linspace(0, 5, 100)
w1_values = np.linspace(1, 3, 100)
w0_mesh, w1_mesh = np.meshgrid(w0_values, w1_values)
error_mesh = np.zeros_like(w0_mesh)

# Calculate the error for each combination of w0 and w1
for i in range(len(w0_values)):
    for j in range(len(w1_values)):
        error_mesh[i, j] = error(w0_values[i], w1_values[j])

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w0_mesh, w1_mesh, error_mesh, cmap='viridis', alpha=0.8)
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('Error')

plt.title('Linear Error in 3D Space')
plt.show()