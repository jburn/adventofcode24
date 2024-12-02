with open("input.txt", "r") as rfile:
    data = rfile.readlines()

lines = [[int(num) for num in row.rstrip("\n").split()] for row in data]

# 1
def check_line(line):
    length = len(line)
    if length != len(set(line)):
        return False
    if line[0] > line[1]: line.reverse()
    for i in range(1, length):
        if(0 >= line[i] - line[i-1]) or (line[i] - line[i-1] >= 4):
            return False
    return True
    
print("Safe lines:", len([line for line in lines if check_line(line)]))

# 2
def check_line2(line):
    valid_inc_dec = (line==sorted(line) or line==sorted(line, reverse=True))
    if not valid_inc_dec: return False
    length = len(line)
    for i in range(1, length):
        if not (1 <= abs(line[i] - line[i-1]) <= 3):
            return False
    return True

def check_tolerance(line):
    for i in range(len(line)):
        curr = line[:i] + line[i+1:]
        if check_line2(curr):
            return True
    return False

count = 0
for line in lines:
    if check_line2(line):
        count += 1
    elif check_tolerance(line):
        count += 1

print("Safe lines 2:", count)
