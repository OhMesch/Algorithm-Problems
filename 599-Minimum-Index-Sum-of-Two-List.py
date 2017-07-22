# Problem: Given two lists representing favorite resturants in order of preference
# Return: The resturant choice that will make the two people most happy 

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = dict()
        s1,s2 = set(list1),set(list2)
        l1,l2 = len(list1),len(list2)
        common = s1.intersection(s2)
        
        if len(common) == 1:
            return(list(common))

        for i in range(min(l1,l2)):
            print('i',i)
            if list1[i] in common:
                if list1[i] not in d:
                    print('zero',list1[i],i)
                    d[list1[i]] = i
                else:
                    d[list1[i]] += i
                    print('first',list1[i],d[list1[i]])
            if list2[i] in common:
                if list2[i] not in d:
                    print('Test',list2[i])
                    d[list2[i]] = i
                else:
                    d[list2[i]] += i
                    print('second',list1[i],d[list1[i]])
        print(d)
        if l1 != l2:
            if l1<l2:
                for j in range (l1,l2):
                    print('j',j)
                    if list2[j] in common:
                        if list2[j] not in d:
                            print('Inital',list2[j],j)
                            d[list2[j]] = j
                        else:
                            print('down here',list2[j],d[list2[j]],j)
                            d[list2[j]] += j

            else:
                for j in range (l2,l1):
                    print('j',j)
                    if list1[j] in common:
                        if list1[j] not in d:
                            print('Inital',list2[j],j)
                            d[list1[j]] = j
                        else:
                            print('all down',d[list2[j]])
                            d[list1[j]] += j
        print(d)
        mostLiked = min([v for v in d.values()])
        return([k for k,v in d.items() if v == mostLiked])


driver = Solution()
t1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
t2=["Piatti", "The Grill at Torrey Pines",'KFC', "Hungry Hunter Steakhouse", "Shogun","Burger King"]
t3 = ["Shogun","Tapioca Express","Burger King","KFC"]
t4 = ["KFC","Burger King","Tapioca Express","Shogun"]
t5 = ["Shogun","Tapioca Express","Burger King","KFC"]
t6 =["KNN","KFC","Burger King","Tapioca Express","Shogun"]

print('\n')
print('T1 and T2\n',driver.findRestaurant(t1,t2),'["Shogun"]\n')
print('T3 and T4\n',driver.findRestaurant(t3,t4),'\n ["KFC","Burger King","Tapioca Express","Shogun"]\n')
print('T5 and T6\n',driver.findRestaurant(t5,t6),'\n ["KFC","Burger King","Tapioca Express","Shogun"]\n')