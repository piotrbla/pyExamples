#!/usr/bin/py
# Head ends here
def findStrings(a,query):
    all=set()
    for s in a:
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                all.add(s[i:j])
                if (len(all)>2908):
                    print(i)
                    print(j)
    setS= sorted(list(all))
    for q in query:
        if (q>len(setS)):
            print("INVALID")
        else:
            print(setS[q-1])
