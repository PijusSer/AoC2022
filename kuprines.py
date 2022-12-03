import string

backpacks = open(r'C:\Users\Pijus\Desktop\ipython\1203\input.txt', 'r')

shared = ''
point_sum = 0

num_list = [*range(1, 53)]
point_values = dict(zip(string.ascii_letters, num_list))

#for line in backpacks:
#    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
#    shared = ''.join(set(firstpart).intersection(secondpart))
#    point_sum += point_values[shared]
#    shared = ''
#
#print (point_sum)

lines = []
for line in backpacks:
    lines.append(line)
    if len(lines) >= 3:
        lines2 = [x.replace('\n', '') for x in lines]
        shared = ''.join(set.intersection(*map(set,lines2)))
        point_sum += point_values[shared]
        shared = ''
        lines = []

print (point_sum)
