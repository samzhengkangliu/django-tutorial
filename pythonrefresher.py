# Variables, Strings, Ints and Print
age = 25
name = "Sam"
print(f'Hello my name is {name} and I am {age} years old')

# If statement
if age > 18:
    print("You are an adult.")
else:
    print("You are younger than 18")

# Function
def hello(str):
    print("Hello World!" + str)

hello(" Sam")

def hi(name, age):
    return "Hello {} you are {} years old".format(name, age)

sentence = hi("Sam", 18)
print(sentence)

def tripleprint(word):
    print(word*3)

# Lists
catNames = ["Java", "Javascript", "Python", "C"]
# add item
catNames.insert(0, "Jane")
print(catNames)
# get item
print(catNames[1])
# delete item
del(catNames[0])
print(catNames)
# length
print(len(catNames))
# replace
catNames[3] = "C++"
print(catNames)

# Loops
for name in catNames:
    print(name)

for x in range(5,10):
    print(x)

year = 1995
while year < 2000:
    print(year)
    year +=1

# Dictionaries
cats = {"Java": 4, "Javascript": 3, "Sean": 5}
print(cats)
# Access item value
print(cats["Sean"])
# Delete item
del(cats["Sean"])
print(cats)
# Add an item
cats["Sam"] = 7
print(cats)

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range(len(words)):
    cooldictionary[words[i]] = definitions[i]
print(cooldictionary)

# Classes
class Dog:

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("BARK!" + str)

myDog = Dog("Fido", 13, "Brown")
myDog.bark("WOWO")
print(myDog.name)

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2020 - self.year

myCar = Car(2020, "BMW", "M4")
print(myCar.age())
