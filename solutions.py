def solve(b, l, d, libs, lib, scores):
    def f():
        order = []
        for i in sorted(lib, key=lib.get, reverse=True):
            choices = []
            for j in lib[i][1]:
                if j in order:
                    break
                choices += [(len(libs[j][3]) / float(libs[j][2]), libs[j][1], j)]
            else:
                if len(choices) == 0:
                    continue
                choices.sort(reverse=True)
                order += [choices[0][2]]
                #print("Choices: ",choices)
        
        total, ans = score(order) 
        return total, ans, 0
    
    def f1():
        order = []
        scanned = set()
        days = d
        for i in sorted(lib, key=lib.get, reverse=True):
            if i in scanned:
                continue
            
            if len(lib[i][1]) > 0 and lib[i][1][0] not in order:
                choices = []
                for j in lib[i][1]:
                    if j in order:
                        continue
                    sc = 0
                    max_books = (days-libs[j][1]) * libs[j][2]
                    cur = 0
                    for k in libs[j][3]:
                        if k[1] in scanned: 
                            continue
                        sc += k[0]
                        cur += 1
                        if cur >= max_books:
                            break  
                        
                    choices += [(5 * sc + len(libs[j][3]) / float(libs[j][2]) / libs[j][1], j)]
                
                if len(choices) == 0:
                    continue
                choices.sort(reverse=True)            
            
                
                order += [choices[0][1]]
                k = order[-1]
                days -= libs[k][1]
                max_books = days * libs[k][2]
                cur = 0
                for j in libs[k][3]:
                    scanned.add(j[1]) 
                    cur += 1
                    if cur >= max_books:
                        break
                
                #print("Choices: ",choices)
        
        
        total, ans = score(order) 
        return total, ans, 1
    
    def f2():
        order = []
        for i in sorted(lib, key=lib.get, reverse=True):
            choices = []
            for j in lib[i][1]:
                if j in order:
                    break
                choices += [(libs[j][0] / float(d) + len(libs[j][2]) / float(libs[j][1]) / b, j)]
            else:
                if len(choices) == 0:
                    continue
                choices.sort(reverse=True)
                order += [choices[0][1]]
                #print("Choices: ",choices)
        
        total, ans = score(order) 
        return total, ans, 2
    
    max_total = 0
    ans = []
    
    def score(order):
        total = 0
        days = d
        scanned = set()
        to_scan = []
        libs_f = []
        
        for i in order:
            if i in libs_f:
                continue
            days -= libs[i][1]
            libs_f += [i]
            if days <= 0:
                break
            to_scan += [[i, []]]
            max_books = days * libs[i][2]
            for j in libs[i][3]:
                if j[1] in scanned:
                    continue
                scanned.add(j[1])
                total += j[0]
                to_scan[-1][1] += [j[1]]
                max_books -= 1
                if max_books <= 0:
                    break
        return total, to_scan    

    total, ans, v = f()
    
    for i in [f1]:  #, f2, f3, f4]:
        print(i.__name__)
        a1, a2, a3 = i()
        if a1 > total:
            total = a1
            ans = a2
            v = a3

    return total, ans, v