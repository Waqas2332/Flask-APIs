# python number manipulation works on bodmas rule

print(2 + 3 * 4)
print((2 + 3) * 4)

# type conversion

age = 23
# print("Happy " + age + "rd Birthday!") // it will cause error due to age being a number

print("Happy " + str(age) + "rd Birthday!") # coverting integer in string using str()

# ? In python 2, division of two integers resulted in integer but now it returns float