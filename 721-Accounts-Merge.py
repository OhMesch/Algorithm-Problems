class GraphNode():
    def __init__(self,email,owner):
        self.email = email
        self.owner = owner
        self.group = None
        self.children = []

    def get_children(self):
        return(self.children)

    def get_email(self):
        return(self.email)

    def get_owner(self):
        return(self.owner)

    def get_group(self):
        return(self.group)

    def add_child(self, new_child):
        self.children.append(new_child)

    def set_group(self,group):
        self.group = group


class Solution:
    def __init__(self):
        self.visited = set()

    def DFS_group(self,node,group):
        if node not in self.visited:
            self.visited.add(node)
            node.set_group(group)
            for child in node.get_children():
                self.DFS_group(child,group)

    def create_edge(self,node1,node2):
        node1.add_child(node2)
        node2.add_child(node1)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        node_key = {}
        for personal_info in accounts:
            own = personal_info[0]
            my_emails = personal_info[1:]

            for i in range(len(my_emails)):
                email = my_emails[i]
                if email not in node_key:
                    node_key[email] = GraphNode(email,own)
                # else:
                #     pass

                # for j in range(i+1,len(my_emails)):
                    # self.create_edge(my_emails[i],my_emails[j])

            for connection in my_emails[1:]:
                #connect everything
                self.create_edge(node_key[my_emails[0]],node_key[connection])

        i = 0
        groups = []
        for node in node_key.values():
            print(node.get_email())
            if node not in self.visited:
                self.DFS_group(node,i)
                groups.append([node.get_owner()])
                i += 1
            groups[node.get_group()].append(node.get_email())

        return([[x[0]] + sorted(x[1:]) for  x in groups])

driver = Solution()
print(driver.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
