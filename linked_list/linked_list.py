# del 객체 : 선언된 객체를 삭제해준다.

class Node:
  def __init__(self, key=None):
    self.key = key    # key
    self.next = None  # link
  def __str__(self):
    return str(self.key) 
    """
    print(Node)를 하면 string함수가 정의돼있는지 
    확인 후 정의돼있다면 print(Node.key) 
    """

# a1(hn) -> a2 -> a3(tn) -> None
a1 = Node(3)
a2 = Node(9)
a3 = Node(-1)

a1.next = a2
a2.next = a3

# head node만 안다면?
# size:3 / head node의 주소 -> a1(hn) -> a2 -> a3(tn) -> None
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  # Node length(갯수)
  def __len__(self):
    return self.size

  # Node 삽입 method
  def pushFront(self, key):
    new_node= Node(key)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
  
  def pushBack(self, key):
    new_node = Node(key)
    if len(self) == 0:
      self.head = new_node
    else:
      tail_node = self.head
      while(tail_node.next != None):
        tail_node = tail_node.next
      tail_node.next = new_node
    self.size += 1

  # Node 삭제 method
  def popFront(self):
    if len(self) == 0:
      return None
    else:
      head_node = self.head
      pop_key = head_node.key
      self.head = head_node.next
      self.size -= 1
      del head_node # 객체 자체를 없애준다.
      return pop_key

  def popBack(self):
    if len(self) == 0:
      return None
    else:
      prev_node, tail_node = None, self.head
      while (tail_node.next != None):
        prev_node = tail_node
        tail_node = tail_node.next   
      if len(self) == 1:
        self.head = None
      else:   
        prev_node.next = None # or tail.next
      pop_key = tail_node.key
      del tail_node
      self.size -= 1
      return pop_key

  # 탐색 method
  def search(self, key):
    pre_node = self.head
    while (pre_node != None):
      if (pre_node.key == key):
        return pre_node
      pre_node = pre_node.next
    return None # or return pre_node

  # 제네레이터 (리스트의 for문과 흡사함 / for i in list:)
  # for x in linkedList:
  #   print(x)
  def __iter__(self):
    pre_node = self.head
    while pre_node != None:
      yield pre_node  # 제네레이터의 특징 yield : return과 비슷하다.
      pre_node = pre_node.next
    # while loop가 끝나면 stopIterator Error Message를 return 해주고,
    # Error Message를 보고, for문을 끝낸다. 

# 3 -> 9 -> -1
"""
L.pushFront(-1)
L.pushFront(9)
L.pushFront(3)
L.pushFront(5)
"""

"""
  def popBack:
    if len(self) == 0:
      return None
    else:
      tail_node = self.head
      prev_node = self.head
      count = 1
      
      while (tail_node.next != None):
        count += 1
        tail_node = tail_node.next

      for i in (count-1):
        prev_node = tail_node.next
      
      pop_key = tail_node.key
      del tail_node
      prev_node = None # or tail.next
"""