f= open("day15/input.txt").read().splitlines()

def hash_word(word):
    current = 0
    for char in word:
        current += ord(char)
        current *= 17
        current %= 256
    return current

lists = f[0].split(",")

boxes = [dict() for _ in range(256)]

for line in lists:
    if "-" in line:
        lab = line[:-1]
        boxNum = hash_word(lab)
        if lab in boxes[boxNum]:
            del boxes[boxNum][lab]
    else:
        lab, num = line.split("=")
        boxNum = hash_word(lab)
        boxes[boxNum][lab] = int(num)

total = 0
for lists in range(len(boxes)):
    for line, lab in enumerate(boxes[lists]):
        total += (lists+1) * (line+1) * boxes[lists][lab]

print(total)