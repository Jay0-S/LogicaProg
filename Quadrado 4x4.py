for i in range(4):
    for j in range(4):
        if (i == 0 and j <= 3) or \
         (i == 1 and (j == 0 or j == 3)) or \
         (i == 2 and (j == 0 or j == 3)) or \
         (i == 3 and j <= 3):
            print("*" , end=" ")
        else:
            print(" ", end=" ")
    
    print(" ")
