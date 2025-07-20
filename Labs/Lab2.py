def calculate_grades(scores):
    grades = []
    bigboy = 0
    
    for x in scores:
        bigboy += x
    howmany = len(scores)
   
    avg = bigboy/howmany
    scores.append(avg)
    
    for x in scores:
        
        if x >= 95:
            letter = 'A+'
            grades.append(letter)
            
        elif 95 > x >= 91:
            letter = 'A'
            grades.append(letter)
                
        elif 90 >= x >= 80:
            letter = 'B+'
            grades.append(letter)
                
        elif x < 80:
            letter = 'F'
            grades.append(letter)
            
                
    return grades

