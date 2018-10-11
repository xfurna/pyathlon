for i in range(100, 900):
    for j in range(i, 900):
        for k in range(j, 900):
            if i+j+k == 1000 and i*i+j*j == k*k:
                print(i*j*k)
                break

