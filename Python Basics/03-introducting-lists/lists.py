motorcycles = []

# append() is used to add element at the end of the list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# insert() is used to add element at the specified index in the list, shift all the values to the right from the index 

motorcycles.insert(0, 'ducati')
print(motorcycles)

# del keyword deletes the element at the specified index

del motorcycles[0]
print(motorcycles)

# pop() removes element at the specified index and return that element as well. if index is not specified, it pop out last element from the list

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# remove() takes value and remove that value from the list. it is used when value is known but index is not known. if one only occurs more than once, rmeove() removes only first occurence of it

motorcycles.remove("yamaha")
print(motorcycles)