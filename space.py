

space = open(r'C:\Users\Pijus\Desktop\ipython\1204\input.txt', 'r')


pairs = []
s_l = []
overlap_count = 0

for line in space:
    line = line.strip()
    pairs = line.split(',')
    for sections in pairs:
        s_l += sections.split('-')
    if set((range(int(s_l[0]), int(s_l[1])))).issubset(range(int(s_l[2]), int(s_l[3]))) or set((range(int(s_l[2]), int(s_l[3])))).issubset(range(int(s_l[0]), int(s_l[1]))):
        overlap_count += 1
    s_l = []
print (overlap_count)