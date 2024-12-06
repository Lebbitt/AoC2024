file = open("data/Day1.txt").read()
file_strip = file.strip()
file_list = file_strip.split("\n")

list_1 = []
list_2 = []

for f in file_list:
    line = f.split("   ", 1)
    print(line)
    list_1.append(line[0])
    list_2.append(line[1])

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

id = 0
totals = []
for number in sorted_list_1:
    list_2_value = sorted_list_2[id]
    distance = int(list_2_value) - int(number)
    totals.append(abs(distance))
    id += 1
    print(totals)

answer = sum(totals)
print(answer)
