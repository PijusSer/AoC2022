space = open(r'C:\Users\Pijus\Desktop\ipython\1204\input.txt', 'r')


pairs = []
s_l = []
overlap_count = 0

for line in space:
    line = line.strip()
    pairs = line.split(',')
    for sections in pairs:
        s_l += sections.split('-')
    if s_l[2] <= s_l[0] and s_l[3] >= s_l[1]:
        overlap_count += 1
    else:
        if s_l[0] <= s_l[2] and s_l[1] >= s_l[3]:
            overlap_count += 1
    # if set((range(int(s_l[0]), int(s_l[1])))).issubset(range(int(s_l[2]), int(s_l[3]))) or set((range(int(s_l[2]), int(s_l[3])))).issubset(range(int(s_l[0]), int(s_l[1]))):
        # overlap_count += 1
    s_l = []
print (overlap_count)