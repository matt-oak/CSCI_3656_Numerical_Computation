#Script to compute the integral of a function using the trapezoidal rule
#Matthew Oakley, #101697544

#Function to integrate via trapezoidal rule
def trap(x, fx, lbound, ubound, h):
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

	print x_final
	print fx_final

	#Trapezoid rule summation
	total = 0.0
	for i in range(0, len(fx_final) - 1):
		total += fx_final[i] + fx_final[i+1]

	return total

#Given x, f(x), lower/upper bound, and step size		
x = [0.9000, 0.9500, 1.0000, 1.0500, 1.1000, 1.1500, 1.2000, 1.2500, 1.3000, 1.3500,
 	1.4000, 1.4500, 1.5000, 1.5500, 1.6000, 1.6500, 1.7000, 1.7500, 1.8000, 1.8500, 1.9000]
fx = [2.9596, 3.0857, 3.2183, 3.3577, 3.5042, 3.6582, 3.8201, 3.9903, 4.1693, 4.3547,
	4.5552, 4.7631, 4.9817, 5.2115, 5.4530, 5.7070, 5.9739, 6.2546, 6.5496, 6.8598, 7.1859]
lbound = 1.0
ubound = 1.8
h = 0.2

answer = trap(x, fx, lbound, ubound, h)

print "x: {}".format(x)
print "f(x): {}".format(fx)
print "Lower bound: {}".format(lbound)
print "Upper bound: {}".format(ubound)
print "Step size: {}".format(h)
print "\n"
print "Answer: {}".format(answer)