#!/usr/bin/py
# Head ends here
givenStrings = []


class Element(object):
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __repr__(self):
        global givenStrings
        return givenStrings[self.k][self.i:self.j]

    def __cmp__(self, other):
        global givenStrings
        return givenStrings[self.k][self.i:self.j].__cmp__(givenStrings[other.k][other.i:other.j])

    def __lt__(self, other):
        return givenStrings[self.k][self.i:self.j] < (givenStrings[other.k][other.i:other.j])


def findStrings(a, query):
    global givenStrings
    givenStrings = a
    allElements = []
    k = 0
    for s in a:
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                allElements.append(Element(i, j, k))
        k += 1

    setS = sorted(allElements)
    uniqueSet = []
    if len(setS)>1:
        for i in range(len(setS)-1):
            x = setS[i]
            y = setS[i + 1]
            if givenStrings[x.k][x.i:x.j]!=(givenStrings[y.k][y.i:y.j]):
                uniqueSet.append(setS[i])
    if setS[len(setS)-2] != setS[len(setS)-1]:
        uniqueSet.append(setS[len(setS)-1])
    print(uniqueSet)
    for q in query:
        if q > len(uniqueSet):
            print("INVALID")
        else:
            print(uniqueSet[q - 1])


# Tail starts here

if __name__ == '__main__':
    #n = int(input())
    n=2
    string = []
    # for i in range(0, n):
    #     string.append(input().strip())
    string.append("aab")
    string.append("aac")
    # q = int(input())
    query = []
    # for i in range(0, q):
    #     t1 = int(input())
    #     query.append(t1)
    query.append(3)
    query.append(8)
    query.append(23)
    findStrings(string, query)
# 2
# aab
# aac
# 3  = {"a", "aa", "aab", "aac", "ab", "ac", "b", "c"}. T
# 3
# 8
# 23
