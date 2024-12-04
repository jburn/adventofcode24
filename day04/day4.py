with open("input.txt", "r") as rfile:
    data = rfile.readlines()
data = [d.rstrip("\n") for d in data]

# 1
dirs = [
    # x, y
    [(0, -1), (0, -2), (0, -3)], # N
    [(1, -1), (2, -2), (3, -3)], # NE
    [(1, 1), (2, 2), (3, 3)], # SE
    [(0, 1), (0, 2), (0, 3)], # S
    [(-1, 1), (-2, 2), (-3, 3)], # SW 
    [(-1, -1), (-2, -2), (-3, -3)], # NW
]

total = 0
for y, row in enumerate(data):
    total += row.count("XMAS")
    total += row.count("SAMX")
    for x, letter in enumerate(row):
        if letter == 'X':
            for dir in dirs:
                try:
                    for i, c in enumerate(dir):  
                        if y+c[1] < 0 or x+c[0] < 0:
                            break                  
                        if data[y+c[1]][x+c[0]] != "MAS"[i]:
                            break
                    else:
                        total += 1
                except IndexError:
                    continue

print("XMASes:", total)

# 2

matches = ["SAM", "MAS"]

total2 = 0
for y, row in enumerate(data):
    for x, letter in enumerate(row):
        if letter == "A":
            try:
                if (f"{data[y-1][x-1]}A{data[y+1][x+1]}" in matches) and (f"{data[y+1][x-1]}A{data[y-1][x+1]}" in matches):
                    if y-1 < 0 or x-1 < 0:
                        continue
                    total2 += 1
            except:
                pass

print("Total 2:", total2)