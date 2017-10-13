class BinSearch():
	def search_any(self,nums,target):
		l = 0
		r = len(nums)-1
		while True:
			mid = (l+r)//2
			if r < l:
				return(-1)
			elif nums[mid] < target:
				l = mid+1
			elif nums[mid] > target:
				r = mid-1
			else:
				return(mid)

	def search_first(self,nums,target):
		l,r = 0,len(nums)
		seen = False
		while l<r:
			mid = (l+r)//2
			if nums[mid] > target:
				r = mid
			elif nums[mid] == target:
				r = mid
				seen = True
			else:
				l = mid+1
		if seen:
			return(l)
		else:
			return(-1)

	def search_all(self,nums,target):
		l = self.search_first(nums,target)
		if l < 0:
			return(None)
		r = l
		h = len(nums)
		while r<h:
			mid = (r+h)//2
			if nums[mid] > target:
				h = mid
			else:
				r = mid+1
		if r-1 != l:
			return(tuple([l,r-1]))
		else:
			return(tuple([l]))


driver = BinSearch()
print('\n')

print('1')
print('**',driver.search_any([1,2,3,4,5,6,7,8,9,10],4))
print('-- 3')

print('2')
print('**',driver.search_any([1,2,3,4,5,7,8,9,10],6))
print('-- -1')

print('3')
print('**',driver.search_all([1,2,3,3,3,3,3,3,4,6,7,8,8,8],3))
print('-- (2, 7)')

print('4')
print('**',driver.search_all([1,2,3,3,3,3,3,3,4,6,7,8,8,8],5))
print('-- None')

print('5')
print('**',driver.search_first([0,0,0,0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],0))
print('-- 0')

print('6')
print('**',driver.search_first([0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],5))
print('-- 7')

print('7')
print('**',driver.search_first([0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],30))
print('-- -1')

print('8')
print('**',driver.search_all([0,0,0,0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],0))
print('-- (0, 3)')

print('9')
print('**',driver.search_all([0,0,0,0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],5))
print('-- (10, 12)')

print('10')
print('**',driver.search_all([0,1,2,2,3,3,4,5,5,5,6,6,11,15,24],0))
print('-- (0,)')

print('11')
print('**',driver.search_all([1,1],1))
print('-- (0, 1)')

print('12')
print('**',driver.search_all([1],1))
print('-- (0,)')