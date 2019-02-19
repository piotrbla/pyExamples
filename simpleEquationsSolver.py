def printint(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    print(int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(x7), int(x8), int(x9), int(x10))


for r1 in [1, 2, 3]:
    for r2 in [1, 2, 3]:
        for r3 in [1, 2, 3]:
            for r4 in [1, 2, 3]:
                for r5 in [1, 2, 3]:
                    for r6 in [1, 2, 3]:
                        x1 = -(2 * r6 + 2 * r5 + 3 * r4 + r3 + r1 - 34) / 3
                        x10 = r5
                        x11 = r1
                        x12 = -(- r6 - r5 - 3 * r4 - 2 * r3 + r1 + 11) / 3
                        x13 = -(r6 + 4 * r5 + 6 * r4 + 2 * r3 + 3 * r2 + 2 * r1 - 62) / 3
                        x14 = -(-4 * r6 + 2 * r5 + r3 + r1 - 7) / 3
                        x15 = (- r6 + 2 * r5 + r3 + r1 - 1) / 3
                        x16 = (r6 + r5 - r3 + 2 * r1 + 1) / 3
                        x17 = -(2 * r6 + 2 * r5 + 6 * r4 + r3 + r1 - 43) / 3
                        x18 = 4 - r3
                        x19 = r3
                        x2 = 4 - r4
                        x20 = (- r6 - r5 - 3 * r4 - 2 * r3 + r1 + 23) / 3
                        x3 = r4
                        x4 = r6
                        x5 = (-4 * r6 + 2 * r5 - 3 * r4 + r3 + r1 + 14) / 3
                        x6 = -(- r6 + 2 * r5 - 3 * r4 + r3 + r1 - 4) / 3
                        x7 = -(r6 + r5 + 3 * r4 - r3 + 2 * r1 - 26) / 3
                        x8 = (r6 + r5 + 3 * r4 - r3 + 2 * r1 - 14) / 3
                        x9 = r2
                        if int(x1) != x1 or int(x8) != x8:
                            continue
                        if x8 < 1 or x1 > 3:
                            continue
                        if x13 > 3:
                            continue

                        printint(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
                        printint(x11, x12, x13, x14, x15, x16, x17, x18, x19, x20)
                        print(x3+x7+4+x16)