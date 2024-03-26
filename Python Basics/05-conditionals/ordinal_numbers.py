numbers = list(range(1,10))

for number in numbers:
    suffix = ""
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(str(number) + suffix)