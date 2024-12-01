with open("input.txt", "r") as rfile:
    data = rfile.readlines()

lines = [row.rstrip("\n").split("   ") for row in data]
list1 = sorted([int(line[0]) for line in lines])
list2 = sorted([int(line[1]) for line in lines])

print("Similiarity score:", sum([val*list2.count(val) for val in list1]))