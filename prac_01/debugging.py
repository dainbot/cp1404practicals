score = float(input("Enter score: "))
if score < 0 and score > 100:
    print("Invalid score")
else: #score is between 0 and 100
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")