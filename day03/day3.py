import re

with open("input.txt", "r") as rfile:
    data = rfile.readlines()
data = "".join([row.rstrip() for row in data])

# 1

regex = r"mul\(\d{1,3},\d{1,3}\)"
muls = re.findall(regex, data)

total = sum([int(x.split("(")[1].split(",")[0])*int(x.split("(")[1].split(",")[1].rstrip(")")) for x in muls])
print("Total:", total)

# 2

regex2 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

total = 0
enabled = True
for match in re.finditer(regex2, data):
    if match[0].startswith("don"):
        enabled = False
        continue
    if match[0].startswith("do"):
        enabled = True
        continue
    if enabled:
        total += int(match[0].split("(")[1].split(",")[0])*int(match[0].split("(")[1].split(",")[1].rstrip(")"))

print("Total:", total)