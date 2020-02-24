from solutions import *

fin_name = "b_read_on.txt"
fin = open(fin_name, "r")

b, l, d = map(int, fin.readline().split())
# b - Number of books
# l - Number of Libraries
# d - Number of given days

scores = list(map(int, fin.readline().split()))
print("Input")
print("B L D:", b, l ,d)
print("Items:", scores)
print()

lib = {i: [scores[i], []] for i in range(b)}

libs = []
for i in range(l):
    _, t, m = map(int, fin.readline().split())
    # t - days for registration
    # m - processing rate
    
    libs += [[0, t, m, [], i]]
    for j in list(map(int, fin.readline().split())):
        libs[-1][3] += [(scores[j], j)]
    
    libs[-1][3].sort(reverse = True)
    
    #print("T M:", t, m)
    #print("Books:", libs[-1][-1])    
    #print()
    
    pr =  m * (d-t) / 5.0
    cur = 0
    sc = 0
    for i in libs[-1][3]:
        sc += i[0]
        cur += 1
        if cur >= pr:
            break
    
    libs[-1][0] = sc
    
libs.sort(reverse=True)
    
for i in libs:
    for (_, j) in i[3]:
        lib[j][1] += [i[4]]

print("=========")

total, ans, v = solve(b, l, d, libs, lib, scores)

# ===============
# Output
# ===============

print(v)
print(total)
print(len(ans))

#for i in ans:
#    print(i[0], len(i[1]))
#    print(' '.join(map(str, i[1])))

fout = open(fin_name.strip("txt") + "out", "w")
fout.write(str(len(ans)) + "\n")
for i in ans:
    fout.write("{} {}\n".format(i[0], len(i[1])))
    fout.write(' '.join(map(str, i[1])) + "\n")
fout.close()
