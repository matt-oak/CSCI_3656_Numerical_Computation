#Forward Euler
#Matthew Oakley, #101697544

from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#First-order functions of system
def x_func(x, y):
	return 16 * (y - x)

def y_func(x, y, z):
	return (45 * x) - y - (x * z)

def z_func(x, y, z):
	return (x * y) - (4 * z)

#Compute new x/y/z values using Forward Euler
def forward_euler(x_points, y_points, z_points, t_points, h, i):
	x = x_points[i]
	y = y_points[i]
	z = z_points[i]

	x_val = x + (h * x_func(x, y))
	y_val = y + (h * y_func(x, y, z))
	z_val = z + (h * z_func(x, y, z))

	x_points.append(x_val)
	y_points.append(y_val)
	z_points.append(z_val)
	t_points.append(t_points[i] + h)

#Plot points
def plot(x, t):
	# fig = plt.figure()
	# ax = fig.add_subplot(111, projection='3d')
	# ax.scatter(x, y, z)
	plt.plot(x, t, 'bo')
	plt.show()

#Given values
initial_condition = [1.0, 1.0, 1.0]
h = 0.0001
num_steps = int(1 / h)

x_points = []
y_points = []
z_points = []
t_points = [0]
x_points.append(initial_condition[0])
y_points.append(initial_condition[1])
z_points.append(initial_condition[2])

#Generate num_steps amount of points
for i in range(0, num_steps):
	forward_euler(x_points, y_points, z_points, t_points, h, i)

#XvsT plot
plot(x_points[:], t_points[:])

#XvsYvsZ plot, must change plot function
#plot(x_points[:], y_points[:], z_points[:])