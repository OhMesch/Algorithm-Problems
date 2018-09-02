class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sortedA = sorted(A)
        reversedA = sorted(A, reverse = True)
        monotonic = sortedA == A or reversedA == A
        return(monotonic)


driver = Solution()

print("1")
print(driver.isMonotonic([1,2,2,3]))
print("True")

print("\n2")
print(driver.isMonotonic([6,5,4,4]))
print("True")

print("\n3")
print(driver.isMonotonic([1,3,2]))
print("False")

print("\n4")
print(driver.isMonotonic([1,2,4,5]))
print("True")

print("\n5")
print(driver.isMonotonic([1,1,1]))
print("True")