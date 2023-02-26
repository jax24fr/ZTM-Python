#Dictionnary Exercise 

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
  'age': 41,
  'username': 'Giovanni',
  'weapons': 1,
  'is_active': 'yes',
  'clan':'jax24fr'
}
#2 iterate and print all the keys in the above user.
print(user)
#3 Add a new weapon to your user
user.update({'weapons': 2})
print(user)
#4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})
print(user)
#5 Ban the user by setting the previous key to True
user.update({'is_banned': True})
print(user)
#6 create a new user2 my copying the previous user and update the age value and username value. 
user2 = user.copy()
user2.update({'age':43,'username':'Cecile'})
print(user2)