def h(n,source,target,help):
    if n ==1:
        print(source,"-->",target)
    else:
        h(n-1,source,help,target)
        print(source,"-->",target)
        h(n-1,help,target,source)