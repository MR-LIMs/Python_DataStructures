class Node:
  def __init__(self, key=None):
    self.key = key
    self.next = self
    self.prev = self

class doublyLinkedList:
  def __init__(self):
    self.head = Node()  # dummy_node
    self.size = 0

  def __len__(self):
    return self.size

  # def __iter__():
  # def __str__():
  # def __repr__():

  # -> ap -> a -> ...(headnode는 없다) -> b -> bn -> / x -> xn 
  # a부터 b를 떼어내 x 다음에 붙인다.
  # a와 b가 이어져있는가?
  # 중간에 headnode가 있는가?
  def splice(self, a_node, b_node, x_node):
    node = a_node
    while (node != b_node):
      if(a_node.next == self.head):
        print('a와 b가 분리돼있거나, head node가 끼어있어 splice가 불가능합니다.')
        return None
      node = a_node.next

    # ap <--> bn / move, insert, push에서는 같은 것 끼리 연산.
    a_node.prev.next = b_node.next
    b_node.next.prev = a_node.prev

    # x <--> a
    x_node.next = a_node
    a_node.prev = x_node

    # b <--> xn
    b_node.next = x.next
    x_node.next.prev = b_node

# 삽입, 삭제, 탐색에 사용되는 splice 
# 이동 연산
  def moveAfter(a_node, x_node):
    splice(a_node, a_node, x_node)
  
  def moveBefore(a_node, x_node):
    splice(a_node, a_node, x_node.prev)

# 삽입 연산
  def insertAfter(x_node, key):
    moveAfter(Node(key), x_node)

  def insertBefore(x_node, key):
    moveBefore(Node(key), x_node)

  def pushFront(self, key):
    insertAfter(self.head, key)
  
  def pushBack(self, key):
    insertBefore(self.head, key)

head = doublyLinkedList()
head.pushFront(3)

print(len(L0))