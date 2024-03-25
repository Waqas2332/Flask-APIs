for value in range(1,5):
    print(value)
    
# Making list of numbers using range function

nums = list(range(1,6))
print(nums)

# giving range function both starting range, ending range and step between each value
even_numbers = list(range(2,11,2))
print(even_numbers)

# functions on list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))