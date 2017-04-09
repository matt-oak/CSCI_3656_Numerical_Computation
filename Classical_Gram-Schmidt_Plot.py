#Plotting results of running Classical Gram-Schmidt on US census data
#Matt Oakley

from __future__ import division
import matplotlib.pyplot as plt

def model(x):
	return 2179282*x - 4086203111

def linear_interpolation(p1, p2, year):
	return p1[1] + (p2[1] - p1[1]) * ((year - p1[0]) / (p2[0] - p1[0]))

def plot():
	years = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
	pops = [92228496, 106021537, 122775046, 132164569, 150697361, 179323175, 
			203302031, 226545805, 248709873, 281421906]
	data_from_model = []
	for i in range(0, len(years)):
		data_from_model.append(model(years[i]))
	plt.plot(years, pops, 'o')
	regression, = plt.plot(years, data_from_model)
	plt.axis([1905, 2005, 85000000, 310000000])
	plt.ylabel('Population in 100s of Millions')
	plt.xlabel('Decade')
	plt.legend([regression], ['Linear Fit'])
	plt.title('Decadal US Census Data')
	plt.show()

print model(1995)
print linear_interpolation((1990, 248709873), (2000, 281421906), 1995)