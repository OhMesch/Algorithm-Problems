'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 
'''

class Solution():
	def rotate(self,arr):
		n=len(arr)
		for j in range(n//2):
			for i in range(j,n-1-j):
				a1 = arr[j][i]
				a2 = arr[i][n-j-1]
				a3 = arr[n-j-1][n-i-1]
				a4 = arr[n-i-1][j]
				arr[j][i],arr[i][n-j-1],arr[n-j-1][n-i-1],arr[n-i-1][j] = a4,a1,a2,a3

driver = Solution()
print('\n')

print('1')
print('**',driver.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print('-- [[7, 4, 1], [8, 5, 2], [9, 6, 3]]')

print('2')
print('**',driver.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print('-- [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]')

print('3 ')
print('**',driver.rotate([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]))
print('-- ')