from copy import deepcopy 

user = {
  'a' : 'b',
  'b' : 'a'
}

user2 = user

print(user2 is user)