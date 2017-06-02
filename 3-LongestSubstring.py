class Solution(object):
	def lengthOfLongestSubstring(self, s):

		longest = 0
		index = 0
		tracker = {}
		flag = 0

		while index < len(s):
			if s[index] not in tracker:
				tracker[s[index]]=index
				index += 1
			else:
				if len(tracker) > longest:
					longest = len(tracker)
				index = tracker[s[index]] + 1
				tracker.clear()
				flag = 88

		if flag == 0:
			longest = len(tracker)

		if len(tracker) > longest:
					longest = len(tracker)

		return(int(longest))


		# for index, element in enumerate(s):
		# 	# print(index,element)
		# 	if element not in tracker:
		# 		temp.append(element)
		# 		tracker.append(element)
		# 	else:
		# 		tracker = []
		# 		# print('else', temp) 
				
		# 		if len(temp) > len(longest):
		# 			longest = temp
		# 			# print('it happened', longest)
		# 		temp = []





# t1 = 'abcabcbb'  # abc       3
# t2 = 'bbbbb'     # b         1
# t3 = 'pwwkew'    # wke       3
# t4 = 'pwetywuiw' # etywui    6
# t5 = 'abcdef'	 # abcdef    6
# t6 = 'aabc'		 # abc       3

# lengthObj = Solution()
# print(lengthObj.lengthOfLongestSubstring(t1))
# print(lengthObj.lengthOfLongestSubstring(t2))
# print(lengthObj.lengthOfLongestSubstring(t3))
# print(lengthObj.lengthOfLongestSubstring(t4))
# print(lengthObj.lengthOfLongestSubstring(t5))
# print(lengthObj.lengthOfLongestSubstring(t6))

