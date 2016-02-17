#!/usr/bin/python3

##
# It compares 2 files line by line. Counts the same lines and write out the different lines too.
# The first ot param is the 2 file.  
##

import sys

def getFileNameFromArgument(index):
	""" Returns the file name based on the first argument. 
		Exit from script if something goes wrong. """
	try:
		fileName = sys.argv[index]
	except IndexError:
		print("Please give 2 file as arguments!")
		exit()
	else:
		return fileName

def getFile(fileName):
	""" Returns the file based on the fileName param. 
		Exit from script if something goes wrong. """
	try:
		file = open(fileName, "r")
	except IOError:
		print("Unable to open the file: " + fileName)
		exit()
	else:
		return file
		
first = getFile(getFileNameFromArgument(1))
second = getFile(getFileNameFromArgument(2))

index = 1
sum = 0
for firstRow in first:
	secondRow = second.readline()
	if firstRow == secondRow:
		sum += 1
	else:
		print("Wrong line (row index, first, second): " + str(index) + ", " + firstRow + ", " + secondRow)

print("Sum: " + str(sum))	
