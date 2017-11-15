'''
Problem:
You are given a string representing an attendance record for a student. The record only contains the following three characters:

    'A' : Absent.
    'L' : Late.
    'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = False
        late_counter = 0
        
        for day in s:
            if day == 'L':
                late_counter += 1
                if late_counter >= 3:
                    return(False)

            else:
                if day == 'A':
                    if absent:
                        return(False)
                    absent = True
                late_counter = 0
        return(True)