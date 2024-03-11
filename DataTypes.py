x = "Hello World"
x = 50
x = 60.5
x = 3j
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")
x = range(10)
x = {"name": "Suraj", "age": 24}
x = {"geeks", "for", "geeks"}
x = frozenset ({"geeks", "for", "geeks"})
x = True
x = b"Geeks"
x = bytearray(4)
x = memoryview(bytes(6))
x = None

# Create a list
my_list = [1,2,3,4,5, "String"]
my_list.insert(1, 0)
print(my_list)

# append
my_list.append(5)
my_list.append(8)
print(my_list)

my_list.remove(2)   # remove the content list
print(my_list)

my_list.remove(my_list[0])  # to remove from the index
print(my_list)

my_list.pop()     # use to remove the last element
print(my_list)

my_list.pop()
print("list after pop",my_list)
varpop = my_list.pop()
print("list remians unchanged", my_list)

