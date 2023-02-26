#Dictionnary

user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

print('basket' in user)
print('size' in user)

print('greet' in user.keys())
print('greet' in user.values())
print('hello' in user.values())
print(user.items())



print(user.update({'age':55}))
print(user)
