#Program for Gaussian Elimination (without pivoting)
#Matt Oakley, #101697544

from __future__ import division

matrix = [
			[9, 1, -1],
			[28, 4, -2],
			[-18, -2, 2]
		]

b_vec = [-1, 5, 6]

#Augment the matrix to assist with Gaussian Elimination
def augment(matrix, b):
	aug_matrix = []

	#Add b to the end of each row of the matrix
	for i in range(len(b)):
		row = matrix[i]
		row.append(b[i])
		aug_matrix.append(row)

	return aug_matrix

#Print out the current matrix
def print_matrix(matrix, comp_string):
	if comp_string != "":
		print "Computation: {}".format(comp_string)
		print "\n"
	for i in range(len(matrix)):
		row = matrix[i]
		for j in range(len(row)):
			print "{:.2f}\t".format(row[j]),
		print "\n"

#Perform either forward elimination or back substitution
def sub_elim(matrix, hammer_row, row, flag):
	temp_row = []

	#Find the "hammer" and index of it
	for i in range(len(hammer_row)):
		if abs(hammer_row[i]) < 0.00000000001:
			continue
		else:
			hammer = hammer_row[i]
			hammer_index = i
			break

	#If forward elimination, append leading zeroes
	if flag == "forward_elim":
		for i in range(hammer_index):
			temp_row.append(0.0)

	#If back substitution, append pre-hammer list
	elif flag == "back_sub":
		for i in range(hammer_index):
			temp_row.append(row[i])
	else:
		print "Check flag"

	#Compute the rest of the new row and return it
	factor = row[hammer_index]/hammer
	for i in range(hammer_index, len(hammer_row)):
		new_val = row[i] - (factor * hammer_row[i])
		temp_row.append(new_val)
	computation = "R{} <-- R{} - {:.2f}*R{}".format(matrix.index(row), matrix.index(row), factor, matrix.index(hammer_row))

	return temp_row, computation

#Solve and print for x1, x2, ..., xn
def get_answers(matrix):
	print "--------------------"
	print "\n"
	for i in range(len(matrix)):
		row = matrix[i]
		numerator = row[-1]
		denominator = row[i]
		print "x{} = {}".format(i+1, numerator/denominator)

#Perform Gaussian Elimination on a given matrix and b-vector
def gaussian_elim(matrix, b):
	matrix_size = len(matrix)

	#Augment the matrix
	aug_matrix = augment(matrix, b)
	print_matrix(aug_matrix, "")

	#Forward Substitution
	i = 0
	while True:
		for j in range(i + 1, matrix_size):
			new_row, comp_string = sub_elim(aug_matrix, aug_matrix[i], aug_matrix[j], "forward_elim")
			row_to_remove = aug_matrix[j]
			aug_matrix.insert(j, new_row)
			aug_matrix.remove(row_to_remove)
			print_matrix(aug_matrix, comp_string)
		i += 1
		if i == matrix_size - 1:
			break

	#Back Substitution
	i = len(aug_matrix) - 1
	while True:
		for j in range(i - 1, -1, -1):
			new_row, comp_string = sub_elim(aug_matrix, aug_matrix[i], aug_matrix[j], "back_sub")
			row_to_remove = aug_matrix[j]
			aug_matrix.insert(j, new_row)
			aug_matrix.remove(row_to_remove)
			print_matrix(aug_matrix, comp_string)
		i -= 1
		if i == 0:
			break

	#Print answers to system of equations
	get_answers(aug_matrix)

#Perform Gaussian Elimination on given matrix and b-vector
gaussian_elim(matrix, b_vec)