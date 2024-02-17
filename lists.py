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
        for fruit in fruits:
            if fruit == entry:
                print('{0} is already in the list'.format(fruit))        
print(fruits)


