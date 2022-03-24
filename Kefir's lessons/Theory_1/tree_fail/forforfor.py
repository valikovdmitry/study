


lst = [1,2,3,4,5,6,7,8,9]

count = 0
for v1 in lst:
    for v2 in lst:
        for v3 in lst:
            for v4 in lst:
                for v5 in lst:
                    for v6 in lst:
                        for v7 in lst:
                            for v8 in lst:
                                for v9 in lst:
                                    s1 = v1 + v2
                                    s2 = v2 + v3
                                    s3 = v3 + v4
                                    s4 = v4 + v5
                                    s5 = v5 + v6
                                    s6 = v6 + v7
                                    s7 = v7 + v8
                                    s8 = v8 + v9
                                    if s1 % 3 != 0 and s1 % 5 != 0 and s1 % 7 != 0 and s2 % 3 != 0 and s2 % 5 != 0 and s2 % 7 != 0 and s3 % 3 != 0 and s3 % 5 != 0 and s3 % 7 != 0 and s4 % 3 != 0 and s4 % 5 != 0 and s4 % 7 != 0 and s5 % 3 != 0 and s5 % 5 != 0 and s5 % 7 != 0 and s6 % 3 != 0 and s6 % 5 != 0 and s6 % 7 != 0 and s7 % 3 != 0 and s7 % 5 != 0 and s7 % 7 != 0 and s8 % 3 != 0 and s8 % 5 != 0 and s8 % 7 != 0 and v1 != v2 and v2 != v3 and v3 != v4 and v4 != v5 and v5 != v6 and v6 != v7 and v7 != v8 and v8 != v9:
                                        print(v1, v2, v3, v4, v5, v6, v7, v8, v9)

