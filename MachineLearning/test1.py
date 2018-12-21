file='dataset.csv'
lines = open(file).read().splitlines()
print(lines)
for line in lines:
    print(line)
    for c in range(len(line)):
        print(line[c])