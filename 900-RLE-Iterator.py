class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.Arr = A
        self.currIndex = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n:
            if self.currIndex >= len(self.Arr):
                    val = -1
                    break
            if self.Arr[self.currIndex] == 0:
                self.currIndex += 2
            else:
                self.Arr[self.currIndex] -= 1
                val = self.Arr[self.currIndex + 1]
                n -= 1
        return(val)