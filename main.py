from linked_class import MyList, ListNode

lst = MyList()

nd = ListNode(1)
lst.enqueue(nd)
nd = ListNode(2)
lst.enqueue(nd)
nd = ListNode(3)
lst.enqueue(nd)
lst.dequeue(2)
#lst.remove(1)

for data in lst:
   print(data)
