#Program for Jacobi method
#Matt Oakley, #101697544

from __future__ import division

#Initial guess vector
#Structured [x1, x2, x3]
initial_guess = [0, 0, 0]

#Equation 1 rearranged solved for x1
def eq1(x2, x3):
	return (-2/3) + (1/3)*x2 - (1/3)*x3

#Equation 2 rearranged solved for x2
def eq2(x1, x3):
	return (-1/8) + (1/8)*x1 - (1/4)*x3

#Equation 3 rearranged solved for x3
def eq3(x1, x2):
	return (4/5) - (1/5)*x1 - (1/5)*x2

# def eq1(x2, x3):
# 	return 1 + 8*x2 + 2*x3

# def eq2(x1, x3):
# 	return 4 - x1 - 5*x3

# def eq3(x1, x2):
# 	return -2 - 3*x1 + x2

#Function to run Jacobi method given equations and initial guess
def jacobi(initial_guess, num_iterations):
	print "Jacobi Method"
	for i in range(0, num_iterations):
		#Print out the current guesses vector
		print initial_guess, "\n"

		#Compute new x1, x2, and x3 values
		new_x1 = eq1(initial_guess[1], initial_guess[2])
		new_x2 = eq2(initial_guess[0], initial_guess[2])
		new_x3 = eq3(initial_guess[0], initial_guess[1])

		#Reset guess vector
		initial_guess[0] = new_x1
		initial_guess[1] = new_x2
		initial_guess[2] = new_x3

#Function to run Gauss-Seidel method given equations and initial guess
def gauss_seidel(initial_guess, num_iterations):
	print "Gauss-Seidel Method"
	for i in range(0, num_iterations):
		#Print out the current guesses vector
		print initial_guess, "\n"

		#Solve for new xn using most up-to-date information
		new_x1 = eq1(initial_guess[1], initial_guess[2])
		initial_guess[0] = new_x1
		new_x2 = eq2(initial_guess[0], initial_guess[2])
		initial_guess[1] = new_x2
		new_x3 = eq3(initial_guess[0], initial_guess[1])
		initial_guess[2] = new_x3

#jacobi(initial_guess, 8)
gauss_seidel(initial_guess, 8)