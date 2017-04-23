#Script to compute the integral of a function using Simpson's 1/3 rule
#Matthew Oakley, #101697544

from __future__ import division

#Function to integrate via trapezoidal rule
def get_points(x, fx, lbound, ubound, h):
	#Remove x/fx entries that are out of the given bounds
	lindex = 0
	uindex = 0
	for i in range(0, len(x)):
		if x[i] < lbound:
			lindex += 1
		elif x[i] > ubound:
			uindex = i
			break
	x = x[lindex:uindex]
	fx = fx[lindex:uindex]

	#Get rid of values not in respect of h
	x_final = []
	x_final.append(x[0])
	fx_final = []
	fx_final.append(fx[0])
	step = x[0]
	for i in range(0, len(x)):
		step += h
		rstep = round(step, 2)
		try:
			index = x.index(rstep)
			x_final.append(x[index])
			fx_final.append(fx[index])
		except ValueError:
			break

	return x_final, fx_final

#Composite version of Simpson's 1/3 rule
def simpson(fx, h):
	#Assign coefficients
	for i in range(0, len(fx)):
		if i == 0 or i == len(fx) - 1:
			fx[i] *= 1
		elif i%2 != 0:
			fx[i] *= 4
		else:
			fx[i] *= 2

	#Summation
	total = 0
	for i in range(0, len(fx)):
		total += fx[i]

	total *= h/3
	return total

#Given x, f(x), lower/upper bound, and step size		
x = [0.9000, 0.9500, 1.0000, 1.0500, 1.1000, 1.1500, 1.2000, 1.2500, 1.3000, 1.3500,
 	1.4000, 1.4500, 1.5000, 1.5500, 1.6000, 1.6500, 1.7000, 1.7500, 1.8000, 1.8500, 1.9000]
fx = [2.9596, 3.0857, 3.2183, 3.3577, 3.5042, 3.6582, 3.8201, 3.9903, 4.1693, 4.3547,
	4.5552, 4.7631, 4.9817, 5.2115, 5.4530, 5.7070, 5.9739, 6.2546, 6.5496, 6.8598, 7.1859]
lbound = 1.0
ubound = 1.8
h = 0.05

x_final, fx_final = get_points(x, fx, lbound, ubound, h)
ans = simpson(fx_final, h)
print "Answer: {}".format(ans)