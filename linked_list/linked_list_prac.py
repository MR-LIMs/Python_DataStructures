class Node:
  def __init__(self, key=None):
    self.key = key
    self.next = None
  
  def __str__(self):
    return str(self.key)  # __str__함수를 사용할 때는 return할 value를 str()로 감싸줘야 한다.
                          # 감싸지 않을 경우, TypeError: __str__ returned non-string (type int)
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def __len__(self):
    return self.size

  # insert methods (pushHead / pushTail)
  def pushHead(self, key):
    newNode = Node(key)
    newNode.next = self.head
    self.head = newNode
    self.size += 1

  def pushTail(self, key):
    newNode = Node(key)
    if len(self) == 0:
      self.head = newNode
    else:
      tailNode = self.head
      while (tailNode != None):
        tailNode = tailNode.next
      tailNode.next = newNode
    self.size += 1

  # delete methods (popHead / popTail)
  def popHead(self):
    if (len(self) != 0):
      popNode = self.head
      popKey = popNode.key
      self.head = popNode.next
      del popNode
      self.size -= 1
      return popKey
    else:
      return None

  def popTail(self):
    if (len(self) != 0):
      tailNode, popNode = None, self.head
      while (popNode.next != None):
        tailNode = popNode
        popNode = popNode.next
      if len(self) == 1:
        self.head = None
      else:
        tailNode.next = None # or tail.next
      popkey = popNode.key
      del popNode
      self.size -= 1
      return popKey
    else:
      return None
  # search method
  def search(self, key):
    preNode = self.head
    while (preNode != None):
      if (preNode.key == key):
        return preNode
      preNode = preNode.next
    return None # or return preNode

  # 제네레이터
  def __iterator__(self):
    preNode = self.head
    while (preNode != None):
      yield preNode
      preNode.next
    # while loop가 끝나면 stopIterator Error Message를 return 해주고,
    # Error Message를 보고, for문을 끝낸다. 

# 오답
# self.head를 head.next로
# size 빼먹음
# def popTail 틀림 => tailNode = None / len0, else -> len1, else
