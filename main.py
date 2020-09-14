class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
  def printList(self):
    temp=self.head
    while temp:
      print(temp.data)
      temp=temp.next

if __name__ =='__main__':
  llist=LinkedList()
  llist.head=Node(1)
  second=Node(12)
  third=Node(35)
  fourty=Node(54)
  fivety=Node(98)
  sexty=Node(23)
  #here we linked node with another node
  llist.head.next=second
  second.next=third
  third.next=fourty
  fourty.next=fivety
  fivety.next=sexty

  llist.printList()