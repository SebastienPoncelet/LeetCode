# LINKED LIST SOLUTION --> NOT MOST EFFICIENT

# Runtime: 6036 ms, faster than 5.00% of Python3 online submissions for Min Stack.
# Memory Usage: 19.2 MB, less than 7.15% of Python3 online submissions for Min Stack.

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        

    def push(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
        else:
            current_list = self.head
            self.head = Node(val)
            self.head.next = current_list
        

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.data
        

    def getMin(self) -> int:
        list = self.head
        lower_val = list.data
        list = list.next

        while list:
            if lower_val > list.data:
                lower_val = list.data
            list = list.next
        return lower_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# LIST SOLUTION

# Runtime: 60 ms, faster than 74.60% of Python3 online submissions for Min Stack.
# Memory Usage: 18.2 MB, less than 57.68% of Python3 online submissions for Min Stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

