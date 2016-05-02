N = int(input())
for i in range(N):
    command = input()
    values = command.split()
    if values[0] == "insert":
        L.insert(int(values[1]), int(values[2]))
    if values[0] == "print":
        print(L)
    if values[0] == "remove":
        L.remove(int(values[1]))
    if values[0] == "append":
        L.append(int(values[1]))
    if values[0] == "sort":
        L = sorted(L)
    if values[0] == "reverse":
          L.reverse()

    if values[0] == "pop":
        L.pop()
