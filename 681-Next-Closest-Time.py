# Problem: Given a time in the format "HH:MM"
# Return: The next closest time using the current digits

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        all_min = []
        all_hour = []
        all_time = []
        unq_time = {}

        availible_digits = [x for x in time if x != ':']

        for first_digit in availible_digits:
        	for second_digit in availible_digits:
        		temp = first_digit+second_digit
        		if int(temp) < 60:
        			all_min.append(temp)
        			if int(temp) < 24:
        				all_hour.append(temp)

        for hour in all_hour:
        	for minute in all_min:
        		comb_time = hour+':'+minute
        		if comb_time not in unq_time:
        			all_time.append(comb_time)
        			unq_time[comb_time] = 1

        sorted_time = sorted(all_time, key=lambda x: (int(x[:2]),int(x[3:])))

        if sorted_time[-1] == time:
        	return(sorted_time[0])
        else:
        	for index in range(len(sorted_time)):
        		if sorted_time[index] == time:
        			return(sorted_time[index+1])


driver = Solution()
print('\n')

print('**',driver.nextClosestTime('19:34'))
print('-- 19:39\n')

print('**',driver.nextClosestTime('23:59'))
print('-- 22:22\n')

print('**',driver.nextClosestTime('03:59'))
print('-- 05:00\n')

print('**',driver.nextClosestTime('02:42'))
print('-- 02:44\n')