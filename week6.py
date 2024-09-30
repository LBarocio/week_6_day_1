# dictionary = a collection of {key:values} pairs ordered and changeable. No duplicates. 

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# "dir" shows attributes of dictionary 
# print(dir(capitals))
# "Help" gives you back documentation 
# print(help(capitals))

print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else: 
#     print("That capital doesn't exist")


# # how to add values 
# capitals.update({"Germany": "Berlin"})
# capitals.update({"Illinois": "Springfield"})
# capitals.update({"USA": "Detroit"})

# # Remove values
# capitals.pop("China")
# capitals.popitem()

# # how to clear dictionary
# capitals.clear()



# print(capitals)


# # to get all keys without the values 
# keys = capitals.keys()
# print(keys)

# # to get all values without the keys
# values = capitals.values
# print(values)

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values
# for value in capitals. values()
# print(values)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")