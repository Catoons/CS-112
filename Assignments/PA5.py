#takes two arguments, one of them optional (*args)
def update_user_info(users, *args):
    inf = users.items()
#lists the items in the dictionary to be iterated over  

#checks to see if the optional argument was given (if so, the length of
#args will be greater than zero. Since args returns a tuple, I create a
#new variable 'upd' that stores the lists in args outside of a tuple.
    
    if len(args)>0:
        upd = args[0]
        
#iterates over the keys and values of users, and the updates given to them.
#if the first item in the update list (the name) matches the key, the key
#is updated with the integers and lists of the original and that in upd
#added together. 
        
        for key, value in inf:
            for d in upd:
                if d[0] == key:
                    users[key] = [d[1]+value[0], value[1]+d[2]]
                    
#after updates have taken place, I iterate over upd again and if
#a name isn't in the users dictionary, I update it with the name as
#the key and the integer and book list as the value.
                    
        for y in upd:
            if y[0] not in users:
                users[y[0]] = [y[1], y[2]]
    
    return users






def update_progress(usersbooks, *args):
#creates an empy list than args will be put in, so they can be
#used with the last function
    
    temp_list =[]
    inf = usersbooks.items()
    
#iterates over the dictionary usersbooks and adds a placeholder
#number '0' so it fits the same format as past function
    
    for key, value in inf:
        usersbooks[key] = [0, value]
            
#now, it iterates over users books again, but sets the 'score'
#(aka progress) based off the number of books
        
    for key, value in inf:
        score = len(value[1]) * 10
        usersbooks[key] = [score, value[1]]
        

        
#if there are books to be added, this code takes args outside of
#it's tuple as just the dictionary
    
    if len(args) > 0:
        
         
        args_dict = args[0]
    
        arif = args_dict.items()
    
#adds a placeholder number to args just like usersbooks
        
        for key, value in arif:
            args_dict[key] = [0, value]
        
#also gives progress like usersbooks, but this time, creates a list
#using the dictionary values, to fit the format of the second argument
#used in update_user_info
            
        for key, value in arif:
            score = len(value[1]) * 10
            temp_list.append([key, score, value[1]])  

            
#runs update_user_info using the dictionary and list I created    
        
    new_thing = update_user_info(usersbooks, temp_list)
        
        
    return  new_thing





#takes three arguments, last of which is optional

def users(names, books, *args):
    
    new_dict = {}
    i=0
    
#if args exists, newbooks is assigned the list inside the args tuple
    
    if len(args) > 0:
        
        newbooks = args[0]

#iterates over names, books and newbooks using i, and places the
#corresponding values in the lists into 'new_dict' to fit the format
#update_progress
        
        while i<len(names):
            new_dict[names[i]] = books[i]+newbooks[i]
            i+=1
            
#if args does not exist, the same thing happens but only one list
#of books is added
            
    else:
        
        while i<len(names):
            new_dict[names[i]] = books[i]
            i+=1
    
#passes new_dict into update_progress and returns the result    
    
    return update_progress(new_dict)


           

def string_difference(s, t):

#checks if s is empty, if so, ends the recursion by returning an empty list
    
    
    if len(s) == 0:
        return []
    
    
#if s is not empty, and the first letter is in the string 't', calls
#the function again without the first letter of s
    else:
        if s[0] in t:
            return string_difference(s[1:], t)
        
#if the first letter of s is in t, it returns a list containing the
#first letter of s in addition to the function without the first letter of s
        if s[0] not in t:
            return [s[0]] + string_difference(s[1:], t)
    


def count_consecutive_chars(some_str):
    # Put your function body here
    
    result = [0]    # Use recursion to obtain your own result
    
    return result

