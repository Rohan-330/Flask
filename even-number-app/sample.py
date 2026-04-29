def even(n):
    result = "Even Numbers:<br>"
    for i in range(2, 2*n + 1, 2):
        print(" i = " + str(i))
        result += str(i) + " "
        print(" result = " + result)
    return result

n = int(input("Enter a number: "))
print(even(n))
