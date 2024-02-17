fruits=["mango", "banana", "grape"]

print("Enter a fruit name")
done = True

while done:
    entry = input()
    if entry == " ":
        done = False
    elif entry not in fruits:
        fruits.append(entry)
    else:
        index = entry in fruits
        print(index)
        
