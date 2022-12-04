space = open(r'C:\Users\Pijus\Desktop\ipython\1204\input.txt', 'r')

pairs = []
s_l = []
contain_count = 0
overlap_count = 0

for line in space:
    line = line.strip()
    pairs = line.split(',')
    for sections in pairs:
        s_l += sections.split('-')
    a = int(s_l[0])
    b = int(s_l[1])
    c = int(s_l[2])
    d = int(s_l[3])
    if set(range(a, b+1)).issubset(range(c, d+1)) or set(range(c, d+1)).issubset(range(a, b+1)):
        contain_count += 1
    if not set(range(a, b+1)).isdisjoint(set(range(c, d+1))):
        overlap_count += 1
    s_l = []
print (contain_count)
print (overlap_count)