class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,val):
        self.head = ListNode(val)
        self.tail = self.head
        self.length = 1
    
    def add(self, val):
        node = ListNode(val)

        self.tail.next = node
        self.tail = self.tail.next
        self.length+=1

    def dequeue(self):
        temp = self.head.val
        self.head = self.head.next
        self.length-=1
        return temp


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        for i in range(n):
            if i == 0:
                l = LinkedList(students[i])
            else:
                l.add(students[i])

        i = 0
        while True:
            temp = l.length
            while temp != 0:
                if l.head.val == sandwiches[i]:
                    l.dequeue()
                    i+=1
                    break
                else:
                    temp-=1
                    x = l.dequeue()
                    l.add(x)

            
            if temp ==0:
                break
        return l.length



        