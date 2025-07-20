def sum_evens(n):
#'i' is the current number that is being checked, finalnum will be the total
#of all even numbers added together
    i = 1
    finalnum = 0

#checks if i is divisible by 2. If so, it is added to finalnum
    while i <= n:
        if i % 2 == 0:
            finalnum += i
        i += 1
        
    return finalnum


def is_deficit(n):
#'i' is the number we will be dividing n by to see if it is a factor 
    mylist = []
    i = n - 1
    determine = 0
 
#Tests all numbers between n and 0 (excluding n and 0) to see if i is
#a factor of n. If it is, the current value of i is added to 'mylist'.
#then, i is subtracted by 1 so the next number can be tested.
    
    while i >= 1:        
        if n % i == 0:
            mylist.append(i)
        i -= 1
        
#iterates over the list of factors, and adds them together
# in the variable 'determine' 
    for x in mylist:
        determine += x

#returns True or false based on if determine is less or greater than/equal
#to the original number.

    if determine < n:
        return True
    elif determine >= n:
        return False 


def list_deficits(bottom, top):
    
#sets i equal to bottom and creates a blank list 'deflist'
    
    i = bottom
    deflist = []
 
#creates a loop that iterates through all numbers in the given range
#and adds their deficits to deflist. 

    while i <= top:
        
        if is_deficit(i) == True:
            deflist.append(i)
            
        i += 1
        
    return deflist


def hail_steps(n):
    i = 0

#creates a loop that will multiply n by 3 and add 1 if it is odd, or
#divide n by 2 if it is even, until n is equal to 1.

    while n != 1:
        
        if n % 2 != 0:
            n = (n*3) + 1
            i += 1

#each time one of the 'if' branches are run, 1 is added to variable i. 

        if n % 2 == 0:
            n /= 2
            i += 1
         
    return i


def keep_em(names, keepers):
    
#creates two empty lists
    
    lx = -1
    goodstuff = []
    finlist = []
    
#iterates over keepers and saves the indexes of the 'Trues' in 'goodstuff'

    for x in keepers:
        lx += 1
        if x == True:
            goodstuff.append(lx)
    
#iterates over the indexes of the 'Trues' and saves the strings in names
#that have the same indexes to 'finlist'
    
    for x in goodstuff:
        finlist.append(names[x])
        
    return finlist


def more_mults(lst1_bottom, lst1_top, lst2_bottom, lst2_top, factor):
      
    x = lst1_bottom
    y = lst2_bottom
    inbetween1 = 0
    inbetween2 = 0
    
#counts the numbers in between the bottom and top of list1
    
    while x < lst1_top:
        x += 1
        inbetween1 += 1
        
#counts the numbers in between bottom and top of list2
        
    while y < lst2_top:
        y += 1
        inbetween2 += 1
    
    
    lst1_nums = 0
    lst2_nums = 0

#counts the number of factors in between bottom and top of list1,
#and sets the total number to list1_nums
    
    while lst1_bottom < lst1_top:
        
        if (factor + lst1_bottom) > lst1_top:
            pass
        else:
            lst1_nums += 1
        lst1_bottom += factor
        
#same thing but for list 2
    
    while lst2_bottom < lst2_top:
    
        if (factor + lst2_bottom) > lst2_top:
            pass
        else:
            lst2_nums += 1
        lst2_bottom += factor
        
#returns the list with more factors, or, if they are equal, checks
#the length of the list and will return the shorter list
#if both have same number of factors and length, it is a tie
        
    if lst1_nums > lst2_nums:
        return 'List 1'
    
    elif lst1_nums < lst2_nums:
        return 'List 2'
    
    elif lst1_nums == lst2_nums:
        if inbetween1 > inbetween2:
            return 'List 2'
        elif inbetween1 < inbetween2:
            return 'List 1'
        else:
            return 'Tie'
    

