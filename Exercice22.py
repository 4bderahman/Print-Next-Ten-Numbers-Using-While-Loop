# asking the user t inter the starting number
Depart = int(input("Enter a starting number: "))

i = 1

# Using a while loop to calculate the next ten numbers
while i <= 10:
    Total = Depart + i
    i += 1

i = 1

print("The next ten numbers are:")

# then we are Using a loop to print the next ten numbers
while i <= 10:
    print(Depart + i)
    i += 1
