import sys

# Instantiate globals
firstString = sys.argv[1].lower()
secondString = sys.argv[2].lower()
substring = ""
substrings = []


# Looks through the strings and adds the largest substring to list substrings
# i: index for firstString
# j: index for secondString
def findSubstring(i, j):
	global substring 
	global firstString
	global secondString
	
	# Catches index out of range if the last letter of a string matches
	try:
		if firstString[i] == secondString[j]:
			substring = substring + firstString[i]
			return(findSubstring(i+1, j+1))
		else:
			substrings.append(substring)
			substring = ""
			return 
	except:
		substrings.append(substring)
		substring = ""
		return


# Calculates the phylogenetic distance if the strings are of equal length
def getDistance():
	global firstString
	global secondString
	if len(firstString) != len(secondString):
		return("Strings are not of the same length")

	same = 0
	for i in range(len(firstString)):
		if (firstString[i] == secondString[i]):
			same += 1
	return(len(firstString) - same)	

	
# Starter method that finds the first matching letters
def start():
	global firstString
	global secondString
	global substrings
	for i in range(len(firstString)):
		for j in range(len(secondString)):
			if firstString[i] == secondString[j]:
				findSubstring(i, j)


# Returns the largest element of the list of substrings
def largest():
	global substrings
	return max(substrings, key=len)

def main():
	global firstString
	global secondString
	start()

	# Reverse the first string and compare
	firstString = firstString[::-1]
	start()

	# Reverse the second string and compare
	firstString = firstString[::-1]
	secondString = secondString[::-1]
	start()

	print(largest())

	# Calculate distance
	secondString = secondString[::-1]
	print("Phylogenetic Distance: ", getDistance())

main()
