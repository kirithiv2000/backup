class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.
        self.prev = None
        


def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count

def average(head):
    summ=0
    c=count_nodes(head)
    for i in range(c):
        summ+=head.data
        print(head.data)
        head=head.next
        
    return summ/c
        

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

nodeE.prev = nodeD
nodeD.prev = nodeC
nodeC.prev = nodeB
nodeB.prev = nodeA


print("This linked list's length is: (should print 5)")
print(count_nodes(nodeA))


print(nodeA.data)
print(nodeA.next.data)
print(nodeA.next.next.data)
print(nodeA.next.next.next.data)
print(nodeA.next.next.next.next.data)

print(average(nodeA))
