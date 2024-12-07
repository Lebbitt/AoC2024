#get each row, get each number, for each number: the difference between two and the sign of difference, if diff val is 1-3 and diff vals are same, then safe
def is_safe(report):
    return correct_size(report) and same_sign(report)

def correct_size(report):
    if report[1:]!='':
        for n1, n2 in zip(report, report[1:]):
            difference = abs(int(n1)-int(n2))
            if difference<1 or difference>3:
                return False
        return True

def same_sign(report):
    all_positive = []
    all_negative = []
    if report[1:]!='':
        for n1, n2 in zip(report, report[1:]):
            difference = int(n1)-int(n2)
            print(difference)
            if difference>0:
                all_positive.append("+")
            elif difference<0:
                all_negative.append("-")
    if len(all_positive)==len(report)-1:
        print("positive", all_positive)
        return True
    elif len(all_negative)==len(report)-1:
        print("negative", all_negative)
        return True
    else:
        return False

file = open("data/Day2.input").read()
file_strip = file.strip()
file_list = file_strip.split("\n")

safe_count = 0

for report in file_list:
    level = report.split(" ")
    print("level", level)
    
    output = is_safe(level)
    if output==True:
        safe_count +=1
        print(safe_count)

print("Safe count = ", safe_count)

