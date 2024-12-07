with open("data/Day1.txt") as file:
    text = file.read()

file_strip = text.strip()
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

totals = []
for number, list_2_value in zip(sorted_list_1, sorted_list_2):
    distance = int(list_2_value) - int(number)
    totals.append(abs(distance))
    print(totals)

answer = sum(totals)
print(answer)
