username = input('what is your username : ')
password = input('give me your password : ')

print(f'Hey {username}, your password {password} is  {len(password)} letters long')

#or

password_length = len(password)
hidden_password = "*"*password_length

print(f'Hey {username}, your password {hidden_password} is  {password_length} letters long')
