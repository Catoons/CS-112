def first_ingredient(f_name, recipe):
    
#opens the csv file for reading and creates two empty lists to be used

    thefile = open(f_name, 'r')
    thelines = thefile.readlines()
    test_list = []
    test_list_prime = []
    
#iterates over the lines of the file, splits them at commas and places
#each line in a list to be more easily indexed and iterated over
#then, if the first string of the list matches the recipie name, the string
#following it is returned 
 
    for x in thelines:
        better = x.split(',')
        test_list.append(better)
        if better[0] == recipe:
            return(better[1])
        
#iterates over all the strings in test_list and creates a new list
#containing only strings instead of lists of strings
        
    for y in test_list:
        for u in y:
            test_list_prime.append(u)
            
#checks to see if the recipe variable matches any strings in test_list_prime
#and if there is no match, 'NOT FOUND' is returned 
            
    if recipe not in test_list_prime:
        return('NOT FOUND')

def uses_this(inventory_file, recipe_file):

#creates some empty lists and dictionaries to be used later
    
    invlist = []
    reclist = []
    mydict = {}
    tempdict = {}
    all_ys = []
    
#opens the two files for reading
    
    infile = open(inventory_file, 'r')
    recfile = open(recipe_file, 'r')
    
    inlines = infile.readlines()
    reclines = recfile.readlines()
    
#creates a list from the contents of the inventory file    
    
    for x in inlines:
       
        better = x.split(',')
        invlist.append(better)
        
#same thing for the recipe file
        
    for y in reclines:
        
        better = y.split(',')
        reclist.append(better)

#iterates through each item in each list, making sure to remove '\n'
#if the item in not already in the 'all_ys' list, it will be added to then end
#this is so I can easily check whether an item in inventory is used at all,
#because if it isn't, it won't be in this list        

    for y in reclist:
        for yy in y:
            yyy = yy.strip('\n')
            if yyy not in all_ys:
                all_ys.append(yyy)
    
#iterates through the items and items only in the inventory lists        
    
    for x in invlist:
        item = x[0]
        
#if the item is in the recipe list, it is either added as a new key to the
#dictionary, or, if it already exists there, the recipie name is added
#to the already existing value list 
        
        for y in reclist:
            if item in y:
                if item in mydict:
                    mydict[item].append(y[0])
                else:
                    mydict[item] = [y[0]]
                    
#if, however, the item is not used in any recipes, it is added to the
#dictionary but with a blank list as value 
                    
            if item not in all_ys:
                mydict[item] = []
            
    return mydict









def in_stock(inventory_file, recipe_file, recipe_name):
    
    inventory_list = []
    recipe_list = []
    temp_list = []
    final_list = []
    
    invfile = open(inventory_file, 'r')
    recfile = open(recipe_file, 'r')
    
    invlines = invfile.readlines()
    reclines = recfile.readlines()
    
#iterates through the inventory, creating a list of lists for ingredients
#and strips them of '\n'
    
    for x in invlines:
        better = x.split(',')
        for y in better:
            xy = y.strip('\n')
            temp_list.append(xy)

#the temporary list is added to the iventory list and then cleared
#so it can be used again 

        inventory_list.append(temp_list)
        temp_list = []
        
#same thing is done for the recipes         
        
    for x in reclines:
        better = x.split(',')
        for y in better:
            xy = y.strip('\n')
            temp_list.append(xy)
            
        recipe_list.append(temp_list)
        temp_list = []
        
#iterates through the list of recipes until it finds the requested recipe       
    
    for x in recipe_list:
        thing2make = x[0]
        if thing2make == recipe_name:
            
#iterates through the inventory list, and if the item is in the recipe's
#ingredients, it adds all of it's data, including name, to final_list
#the name is also added to temp_list to be checked against in next section
            
            for y in inventory_list:
        
                if y[0] in x:
                    final_list.append(f'{y[0]}->{y[1]} {y[2]}')
                    temp_list.append(y[0])

#iterates through the recipe's ingredients, and if the item was never found
#in the inventory, it is appended to final_list with the notice
#it also checks to make sure it is not looking at the name of the recipe
#itself, since that is also stored with the list of its ingredients

            for b in x:
                if b not in temp_list and b != recipe_name:
                    final_list.append(f'{b}->NEED THIS')
                
                    
#if nothing was ever added to final_list, meaning the requested recipe was
#not in the recipe file, it adds the string 'NOT FOUND' to final_list
        
    if len(final_list) == 0:
        final_list = ['NOT FOUND']   
        
    
    return final_list


def check_units(f_name, units = ['oz','each']):

#creating two empty lists to be used later

    inventory_list = []
    temp_list = []

#tries to open the file by the name given, if no file with the name is found,
#return the string 'inventory name incorrect'

    try: 
        invfile = open(f_name, 'r')
        invlines = invfile.readlines()
    
    except FileNotFoundError:
        return 'inventory name incorrect'
        

#same thing that's been going on in past functions - the file's lines are read,    
#stripped of any '\n' and added to the inventory list as one list per line

    for x in invlines:
        better = x.split(',')
        for y in better:
            xy = y.strip('\n')
            temp_list.append(xy)
            
        inventory_list.append(temp_list)
        temp_list = []

#iterates through each line's list, and if the last value is not present in
#the units variable, a ValueError is raised.  

    try:
        
        for x in inventory_list:
            if x[-1] not in units:
                raise ValueError

#if a ValueError is raised, it checks to see if the units variable is using the
#default values or if something new was entered. If something was entered,
#the string 'incorrect units' is returned. Else, it returns 'missing units'.

    except ValueError:
        
        if units != ['oz', 'each']:
            return 'incorrect units'
        if units == ['oz', 'each']:
            return 'missing units'
            
#if no errors were ever raised, 'all fine' is returned.             
    
    return 'all fine' 
    


def first_five_ingr(f_name, recipe):

#creates empty lists to use later
    
    ing_list = []
    temp_list = []
    rec_list = []
    
#opens the ingredients file for reading, and reads the lines
    
    ingfile = open(f_name, 'r')
    inglines = ingfile.readlines()
    

#once again, strips the lines of '\n' and places them in a list in another list

    for x in inglines:
        better = x.split(',')
        for y in better:
            xy = y.strip('\n')
            temp_list.append(xy)
            
        ing_list.append(temp_list)
        temp_list = []
 
 
#iterates through the ingredient list to find the recipe names, and puts them
#in a list to compare the value of the recipe variable to 
 
    for x in ing_list:
        rec_list.append(x[0])

#if the recipe variable is not in the list of recipe names, it returns
#'recipe not found'. If it is in there, the function moves on

    try:
        if recipe not in rec_list:
            raise ValueError
    
    except ValueError:
        return 'recipe not found'
    
#iterates through the ingredient list until it finds the list that corresponds
#to the entered recipe. Once it does, it tries returning the first five
#ingredients of the recipe (they are in the list after its name)
    
    for x in ing_list:
        if x[0] == recipe:
            try:
                return (x[1], x[2], x[3], x[4], x[5])

#if an indexerror arises due to at least one of the five ingredients not
#existing, it instead returns the string 'not enough ingredients'

            except IndexError:
                return 'not enough ingredients'       
            
                      
