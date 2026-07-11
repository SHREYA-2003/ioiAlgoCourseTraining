# Take input
a = int(input("Enter Largest number : "))
b = int(input("Enter Smallest number : "))

# Find LCM
max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        lcm = max_num
        break
    max_num += 1

# Print result
print("LCM is :", lcm)
