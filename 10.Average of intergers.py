last_integer = int(input("Enter a last integer(N) to get the average of all(N>1): "))
number = 0
average = 0

if last_integer <= 1:
    print("Please type again an integer greater than 1")
else:
    for i in range(1, last_integer + 1):
        number += i
        average = number / last_integer
    print(f"The average of integers from 1 to {last_integer} is {average}")
