
#python lists
fruits = ["apple", "orange", "blueberry", 1]
print(fruits[2])
print(fruits[-1]) #last 
print(fruits[1:4]) 
print(fruits[:3])
fruits[3] = "peach"
print(fruits)
fruits.insert(3, "melon")
fruits.append("cherry")
print(fruits)

fruits2 = ["cucumber", "strawberry"]
fruits.extend(fruits2)
print(fruits)
fruits.remove("strawberry")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#list comprehension
fruits3 = [f for f in fruits if f != "apple"]
print(fruits3)


#boolean
print(bool(0))
#comparison
print(10<9)
print(9==9)
print(9!=9)
#logical operations
print(11>10 and 10>9)
print(11>10 or 6>9)
print(not(4<5))

#nunbers
#exponent in Python
number2 = 2
print(number2**2)

number1 = 10
number1 += 5
print(number1)