class Solution():
	def groupAnagrams(self, strs):
		d = {}
		grouped = []
		i = 0
		for word in strs:
			k = ''.join(sorted(word))
			if k in d:
				grouped[d[k]].append(word)
			else:
				grouped.append([])
				grouped[i].append(word)
				d[k] = i
				i+=1
		return(grouped)

driver = Solution()
print('\n')

print('1')
print('**',driver.group(['eat','tea','tan','ate','nat','bat']))
print('-- [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]')