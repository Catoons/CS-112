def getBMI(inputPath, outputPath):
    myfile = open(inputPath, 'r')
    thelines = myfile.readlines()
    
    newfile = open(outputPath, 'w')
    
    for x in thelines[1:]:
        better = x.split(',')
        aa = float(better[2])
        b = better[3].strip()
        bb = float(b)
        BMI = bb/(aa**2)
        BMI = round(BMI,2)
        newfile.write(f'{better[0]}: {BMI}\n')
        
        
    

    
    
    