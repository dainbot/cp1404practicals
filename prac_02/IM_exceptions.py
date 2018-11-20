finished = False
result = 0
while not finished:
    try:
        enterNum = int(input("Please enter a number: "))
        print(enterNum)
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)