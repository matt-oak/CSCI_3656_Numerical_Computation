#Program for Linear Interpolation
#Matt Oakley, #101697544
#I collaborated with Daniel Thompson 

from __future__ import division
import matplotlib.pyplot as plt

#2 closest points and x value you want to approximate
point1 = (2000, 281421906)
point2 = (2010, 308745538)
x_star = 2050

#Function to run interpolation given 2 points and x value
def linear_interpolation(point1, point2, x_star):
	return point1[1] + (point2[1] - point1[1]) * ((x_star - point1[0]) / (point2[0] - point1[0]))

#Function to plot census data per decade using pyplot
def plot_census_data():
	years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
	pops = [76212168, 92228496, 106021537, 122775046, 132164569,
			150697361, 179323175, 203302031, 226545805, 248709873,
			281421906, 308745538]

	plt.plot(years, pops)
	plt.axis([1895, 2015, 70000000, 320000000])
	plt.ylabel('Population in 100s of Millions')
	plt.xlabel('Decade')
	plt.show()
	

#plot_census_data()
val = linear_interpolation(point1, point2, x_star)
print val