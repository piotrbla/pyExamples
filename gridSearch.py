#!/bin/python3

import sys

# t = int(input().strip())
# for a0 in range(t):
# G = [
#     "7283455864",
#     "6731158619",
#     "8988242643",
#     "3830589324",
#     "2229505813",
#     "5633845374",
#     "6473530293",
#     "7053106601",
#     "0834282956",
#     "4607924137"
# ]
# P = ["9505", "3845", "3530"]
G = [
        "123412",
        "561212",
        "123634",
        "781288"
    ]
P = ["12","34"]
def myfind(s, toFind):
    found = []
    pos = s.find(toFind, 0)
    while(pos>-1):
        found.append(pos)
        if pos+1>len(s):
            break
        pos = s.find(toFind, pos+1)
    return found
if True:
    # print(G)
    # print(P)
    if P:
        found = False
        s = P[0]
        gCount = 0
        for gs in G:
            if s in gs:
                positions = myfind(gs, s)
                gInnerCount = gCount - 1
                if len(G) - gCount < len(P):
                    found = False
                    continue
                found = True
                for ps in P:
                    gInnerCount += 1
                    if ps in G[gInnerCount]:
                        positions = list(set(positions).intersection(myfind(G[gInnerCount], ps)))
                        if positions:
                            continue
                    found = False
                    break
                if found:
                    break;
            gCount += 1
        if found:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
