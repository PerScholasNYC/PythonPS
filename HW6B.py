from collections import defaultdict

dicto = defaultdict(int)
with open('yourfile.txt') as f:
    for line in f:
        s_line = line.rstrip().split(',') #assuming ',' is the delimiter
        for ele in s_line:
            dicto[ele] += 1

 #dicto contians words as keys, word counts as values
for input() in dicto.iteritems():
     print input()
