# Problem Statement:
# Write the code that will take a string and convert 
# it into a zigzag problem using a given a number of rows:

class Solution(object):
	def convert(self, s, numRows):
		if numRows == 1:
			return(s)
		array = []
		y = 0
		output = []
		for elm in range(numRows):
			array.append([])

		for character in s:

			if y == numRows-1:
				up = True

			if y == 0:
				up = False

			if up:
				array[y].append(character)
				if y > 0 and y < (numRows -1):
					for rows in array:
						rows.append(' ')
					del array[y][-1]

				y -= 1
			else:
				array[y].append(character)
				y += 1
		for rowArr in array:
			if len(rowArr) == 0:
				del rowArr
			else:
				while rowArr[-1] == ' ':
					del rowArr[-1]
			# print(rowArr)
			# ^ This line displays the text in the zigzag pattern
				for char in rowArr:
					output.append(char)

		output = ''.join(output)
		output = output.replace(' ','')
		output = output.rstrip()

		return(output)


# the last line on down adds spaces to everything



driver = Solution()

s1 = 'PAYPALISHIRING'
r1 = 3

s2 = '123456789'
r2 = 4

s3 = 'A'
r3 = 2

print(driver.convert(s1,r1))
print(driver.convert(s2,r2))
print(driver.convert(s3,r3))

# array = [[1,2,3],[4,5,6],[7,8,9]]
# print(array)
# array.pop()
# print(array)
# del array[1][-1]
# print(array)