
size = int(input("Enter the size of the pattern: "))

while True:
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")


row = 0
while row < size:
    
    for col in range(size):
        print("*", end="")
    print() 
    row += 1