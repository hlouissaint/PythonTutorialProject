def remove_duplicate_v1(mylist):
    return list(set(mylist))

def remove_duplicate_v2(l):
    y = []
    for i in l:
        if i not in y:
            y.append(i)
    return y

alist = [1,2,3,4,3,2,1]

print (list(remove_duplicate_v1(alist)))
print (list(remove_duplicate_v2(alist)))