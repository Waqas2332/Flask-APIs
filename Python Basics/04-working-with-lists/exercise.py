for value in range(1,21):
    print(value)
    
    
million = list(range(1,1000001))
# print(million)

print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1,20,2))
for num in odd_numbers:
    print(num)
    
multiple_3 = list(range(3,31,3))
for num in multiple_3:
    print(num)
    
cubes = []
for value in range(1,11):
    cubes.append(value**3)
    
print(cubes)

cubes_comprehension = list(value**3 for value in range(1,11))
print(cubes_comprehension)