#print(type(2 + 4))
#print(2 - 4)
#print(2 * 4)
#print(type(2 / 4))

#print(2**3)
#print(5 // 4)
#print(6 % 5)


print(round(3.9))
print(abs(-20))

#Escape Sequence

weather = "It's kind of sunny \nhope you have a good day!"
print(weather)

#formatted strings
name = "johnny"
age = 55

print ("hi " + name + " you are " + str(age) + " years old")
print (f"hi {name} you are {age} years old")
print("hi {} you are {} years old".format(name, age))
print("hi {1} you are {0} years old".format(name, age))




#builtin method
greed= "to be or not to be"
print(greed[0:len(greed)])
print(greed.upper())
print(greed.find('be'))
print(greed.replace('be','me'))
print(greed)

#Booleans
print(bool(1))


#exercise :
birth_year = input("what year were you born ?")
print(type(birth_year))

age=2023-int(birth_year)
print(f'you age is : {age} ')
