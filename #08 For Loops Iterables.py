#08 

#Iterable -> List , Dictionary, tuple, set, string
#Iterated -> one by one check each item in the collection


user = {
  'name' : 'Golem',
  'age':5006,
  'can_swim':False
}

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
      print(item)



for i,char in enumerate('Heeellloooo'):
  print(i, char)

for i,char in enumerate(list(range(100))):
  if char ==50:
    print(f'index of 50 is: {i}')