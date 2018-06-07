# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

class Solution:
    def __init__(self):
        self.counter = dict()
        self.sol = []

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        for fullDomain in cpdomains:
            [numStr,domain] = self.splitNumberAndDomain(fullDomain)
            domainPerm = self.permutateDomain(domain)
            self.addPermutationsToCounter(numStr,domainPerm)
        self.formatSolution()

        return(self.sol)

    def splitNumberAndDomain(self, fullString):
        return(fullString.split())

    def permutateDomain(self, domain):
        domainPermutations = [domain]

        for i in range(len(domain)):
            if domain[i] == '.':
                domainPermutations.append(domain[i+1:])

        return(domainPermutations)

    def addPermutationsToCounter(self, number,domainPerms):
        for domain in domainPerms:
            self.counter[domain] = self.counter.get(domain,0) + int(number)

    def formatSolution(self):
        for k,v in self.counter.items():
            self.sol.append(str(v) + " " + k)

        
driver = Solution()
print("1:\n", driver.subdomainVisits(["9001 discuss.leetcode.com"]))
print(' ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]')

driver = Solution()
print("\n2:\n", driver.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
print(' ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]')