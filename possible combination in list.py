a=[1,3,6,4]
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if(i!=j and j!=k and k!=l and i!=l):
                    print(a[i],a[j],a[k],a[l])