def trace(matrix):
    i = 0
    
    if len(matrix[0]) == len(matrix):
        
        for x in range(len(matrix)):
           i += matrix[x][x]
        
        return i
       

    else:
        return('Trace is only defined for square matrices')
    

aa = trace([[2,4], [5, 6]])
print(aa)

    



    