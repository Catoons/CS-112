#######################################
# Task 1: Making full names
#######################################

def make_full_names(name_list):
    x=0
    new_names = []
    
    length = len(name_list)
    
    while length >= 3:
        first = name_list[x]
        middle = name_list[x+1]
        last = name_list[x+2]
        
        new_names.append(f'{first} {middle} {last}')
        x += 3
        length -= 3
        
    return new_names

#######################################
# Task 2: Who's enrolled? 
#######################################

def is_enrolled(students, name, crs_name='CS112'):
    
    if crs_name in (students[name]):
        return True
    else:
        return False
    
#######################################
# Task 3: Birth Years 
#######################################

def birth_years(f_name):
    
    better = []
    
    file = open(f_name, 'r')
    thelines = file.readlines()
    
    for x in thelines:
        year = x[-5:-1]
        if int(year) not in better:
            better.append(int(year))
            
    better.sort()
    
    return better
