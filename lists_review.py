desserts = ["ice cream", "cookies"]
desserts.sort()
print desserts
print desserts.index("ice cream")
food = []
food.extend(desserts)
print food
food.extend(["broccoli", "turnips"])
print desserts, food
food.remove("cookies")
print food[0:1]
breakfast = ("cookies, cookies, cookies").split(", ")
print breakfast


# Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument
#and then outputs only the numbers from the list that fall between 1 and 20
#(inclusive)

def number(list):
    for n in range (0, len(list)): 
        if list[n] >= 1 and list[n] <= 20:
            print list[n]

list = [2, 4, 8, 16, 32, 64]
number(list)
