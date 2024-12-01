with open("input.txt", "r") as rfile:
    data = rfile.readlines()

lines = [row.rstrip("\n").split("   ") for row in data]
list1 = sorted([int(line[0]) for line in lines])
list2 = sorted([int(line[1]) for line in lines])

print("Distance:", sum([abs(list1[i] - list2[i]) for i in range(len(lines))]))
