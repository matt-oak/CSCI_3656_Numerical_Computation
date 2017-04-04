from __future__ import division
import math
import sys

#Function to compute the Bezier curve between 4 points
def bez(spline, x, y, z):
    #Comput 100 points on the curve
    for i in range(0, 101):
        t = i / 100
        x_val = ((1-t)**3*spline[0][0]) + (3*(1-t)**2*t*spline[1][0]) + (3*(1-t)*t**2*spline[2][0]) + (t**3*spline[3][0])
        y_val = ((1-t)**3*spline[0][1]) + (3*(1-t)**2*t*spline[1][1]) + (3*(1-t)*t**2*spline[2][1]) + (t**3*spline[3][1])
        z_val = ((1-t)**3*spline[0][2]) + (3*(1-t)**2*t*spline[1][2]) + (3*(1-t)*t**2*spline[2][2]) + (t**3*spline[3][2])

        #Add points to original x/y/z lists
        x.append(x_val)
        y.append(y_val)
        z.append(z_val)

#Given data points
#Top Surface
x = [33.44, 8.81, 15.62, 40.16, 61.45, 58.81, 36.97, 64.71, 89.11, 67.24, 65.90, 76.55]
y = [87.93, 84.07, 34.83, 38.71, 67.07, 91.44, 63.29, 42.38, 46.49, 18.32, 31.93, 44.51]
z = [105.88, 103.11, 105.98, 108.13, 108.12, 107.72, 107.14, 109.07, 109.93, 109.99, 109.51, 109.91]

#Bottom Surface
# x = [15.59, 38.57, 61.10, 58.97, 36.98, 64.45, 89.18, 66.87, 65.90, 76.55]
# y = [35.07, 37.17, 67.15, 92.05, 63.24, 42.66, 46.85, 18.48, 31.93, 44.51]
# z = [12.88, 13.33, 17.31, 19.09, 16.51, 20.01, 27.71, 14.24, 21.0, 22.0]

#Data points in tuples
p0 = [x[0], y[0], z[0]]
p1 = [x[1], y[1], z[1]]
p2 = [x[2], y[2], z[2]]
p3 = [x[3], y[3], z[3]]
p4 = [x[4], y[4], z[4]]
p5 = [x[5], y[5], z[5]]
p6 = [x[6], y[6], z[6]]
p7 = [x[7], y[7], z[7]]
p8 = [x[8], y[8], z[8]]
p9 = [x[9], y[9], z[9]]
p10 = [x[10], y[10], z[10]]
p11 = [x[11], y[11], z[11]]

#Sets of points to create splines
#Top Surface splines
spline0 = [p5, p0, p1, p2]
spline1 = [p5, p0, p6, p2]
spline2 = [p2, p3, p6, p4]
spline3 = [p5, p0, p6, p4]
spline4 = [p1, p6, p3, p2]
spline5 = [p9, p10, p11, p8]
spline6 = [p3, p7, p8, p11]
spline7 = [p3, p7, p9, p10]
spline8 = [p2, p3, p6, p10]
spline9 = [p2, p3, p4, p8]
spline10 = [p2, p4, p5, p8]
spline11 = [p1, p2, p9, p8]
spline12 = [p8, p0, p3, p11]

#Bottom Surface splines
# spline0 = [p6, p3, p4, p0]
# spline1 = [p3, p4, p2, p9]
# spline2 = [p6, p9, p5, p1]
# spline3 = [p6, p9, p5, p4]
# spline4 = [p6, p9, p8, p7]
# spline5 = [p0, p1, p8, p7]
# spline6 = [p8, p5, p4, p1]
# spline7 = [p4, p1, p7, p6]

bez(spline0, x, y, z)
bez(spline1, x, y, z)
bez(spline2, x, y, z)
bez(spline3, x, y, z)
bez(spline4, x, y, z)
bez(spline5, x, y, z)
bez(spline6, x, y, z)
bez(spline7, x, y, z)
bez(spline8, x, y, z)
bez(spline9, x, y, z)
bez(spline10, x, y, z)
bez(spline11, x, y, z)
bez(spline12, x, y, z)

#Output x/y/z points to file in order to copy/paste to Matlab to plot
file = open("out.txt", "w")
for val in x:
    file.write(str(val) + ", ")
file.close()