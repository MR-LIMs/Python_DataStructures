# Hash Table이란? => less collsion + fast computation
#===================================================================
# dictionary와 같은 객체를 삽입, 삭제, 탐색 하는데에 key와 value 쌍을 스택으로 쌓기에는 비효율적.

# 해쉬테이블 (Hash Table) : 매우 빠른 평균 삽입, 삭제, 탐색
# Hash Table = Table(List) + Hash function + Collision resolution method

# 해쉬함수 : function(key) = key % m(slot의 갯수)
# f(key1) = 7 / f(key2) = 7 처럼 겹친다면, 충돌 발생 
# => collision resolution method 필요.

# 해쉬함수의 형태는 위와 같이 나머지를 취하는 것 외에 복잡한 형식이 있다.
#===================================================================

# Hash function (검색 필요)
#===================================================================
# Perfect Hash Function : 충돌없이 key 1개에 slot 1개 
# => 이상적이나 불가능

# Universal Hash Function
# Percentage(f(x) == f(y)) = 1/m : 충돌이 일어날 확률이 1/m

# C-Universal Hash Function
# Percentage(f(x) == f(y)) = c/m : 충돌이 일어날 확률이 c/m

# Division Hash Function
# f(key) = (k % p) % m  // [p:소수 m:slot의 갯수]
# => 충돌이 많이 일어남
#===================================================================
# Addictive Hash Function
# f(key) = SumOf(key[i]) % m
# key가 string일 때, 많이 사용한다.

# Rotating Hash Function
# h = initial value
# for i in range(len(key)):
#   h = (h << 4)^(h >> 28)^key[i]
# return (h % p) % m

# Universal Hash Function => C++ STL, Java에 사용한다.
# h = initial value
# for i in range(len(key)):
#   h = ((h * 4) + key[i]) % p
# return h % m

# 그 외 : Multiplication, Folding, Mid-squares, Extraction...
#===================================================================

# 충돌회피방법
#===================================================================
# open addressing : 충돌이 일어났을 때, 주변의 공간을 찾아 저장하는 방법
# 1) linear probing : 한칸씩 밑으로 내려가면서 빈 칸을 찾는다.
#    - cluster : 군집한 지역 => 피해야한다.
#    - set, 삽입 
#      key가 있으면 value를 업데이트, 없으면 key와 value를 insert
#    - remove, 삭제
#    - search, 탐색
# 2) quadratic probing
# 3) double hashing
#===================================================================

def findSlot(key):  # key가 있으면 slot번호 return / 없으면 key값이 삽입될 slot번호 return
  i = f(key)
  stack = i
  while(H[i] == )