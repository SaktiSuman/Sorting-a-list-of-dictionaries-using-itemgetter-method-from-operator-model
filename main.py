from operator import itemgetter
lis = [
    { "name" : "Nandini", "age" : 20},
    { "name" : "Manjeet", "age" : 20 },
    { "name" : "Nikhil" , "age" : 19 }
]
print("The list printed by sorting age: ")
print(sorted(lis, key = itemgetter("age")))
print("\r")
print("The list printed by sorting age and name: ")
print(sorted(lis, key = itemgetter("age", "name")))
print("\r")