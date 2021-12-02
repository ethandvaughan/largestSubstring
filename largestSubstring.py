import sys

# Instantiate globals
firstString = sys.argv[1]
secondString = sys.argv[2]
substring = ""
substrings = []
sep = 0

# Looks through the strings and adds the largest substring to list substrings
# i: index for firstString
# j: index for secondString
def findSubstring(i, j):
	global substring 
	global firstString
	global secondString
	global sep
	
	# Catches index out of range if the last letter of a string matches
	try:
		if firstString[i] == secondString[j]:
			substring = substring + firstString[i]
			return(findSubstring(i+1, j+1))
		else:
			substrings.append(substring + " " + str(sep))
			substring = ""
			return 
	except:
		substrings.append(substring + " " + str(sep))
		substring = ""
		return
	
# Starter method that finds the first matching letters
def start():
	global firstString
	global secondString
	global substrings
	global sep
	for i in range(len(firstString)):
		for j in range(len(secondString)):
			if firstString[i] == secondString[j]:
				sep = abs(i - j)
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

main()
