def group_skills(candidate_skills_list):
    newlist =[]
    listoflists=[]
#Creates two empty lists, one will be used to temporarily store the samller
#list of each candidate, the other will hold all candidate's lists
    
    a=0
    i=0

    while i < len(candidate_skills_list):
        while a < 4:
            newlist.append(candidate_skills_list[i])
            a+=1
            i+=1
            
#iterates through four list entries at a time, before adding them all
#to the final list
            
        listoflists.append(newlist)
        newlist=[]
        a=0
        
#a is reset to 0 so cadidate_skills_list can be iterated through again, but
#1 retians it's value so as to ensure there are no repeats
        
    return listoflists
    
        
            


def evaluate_candidates(candidate_names, candidate_scores, threshold):
    a=0
    i=0
    total_scores = 0 

#iterates through the candidate's 3 scores
    while a < len(candidate_scores):
        for x in candidate_scores:
                total_scores += (x[1] + x[2] + x[3])
#checks if the total scores meet the threshold, and if it does, adds the
#candidate to the list if they are not already in there
                if (total_scores >= threshold) and x[0] not in candidate_names:
                        cadidate_names.append[0]
#if the scores are below the threshold and the cadidate is
#in the list, removes them                            
                if (total_scores < threshold) and x[0] in candidate_names:
                            candidate_names.remove(x[0])
                            
                total_scores = 0
                a+=1
                    
    return candidate_names


def rank_candidates(candidate_skills, skills_rank):
#sets up a counter and some blank lists to use later
    rank = 0
    skillz =[]
    cool_can = []
    final_list = []
    
#iterates through the lists in candidate_skills, and appends their skills only
#to the list 'skillz'
    
    for x in candidate_skills:
            
        skillz.append(x[1])
        skillz.append(x[2])
        skillz.append(x[3])
       
#iterates through the skills to see if they have ranks, and if so, adds the rank
#number in the dictionary that corresponds to the rank to the counter 'rank' 
        for y in skillz:
            if y in skills_rank:
                rank += skills_rank[y]
                
#creates a temporarly list, cool_can, that contains the candidate name
#and their total rank, before appending that list to the 'final_list'
                
        cool_can.append(x[0])
        cool_can.append(rank)
        final_list.append(cool_can)
        
#resets the temporary lists and rank to be used for the next candidate
#in the loop
        
        cool_can = []
        skillz =[]
        rank = 0
                
    return final_list
        

def group_rankings(candidate_rankings):

#creates two lists, one temporary, and two variables for iteration

    temp_list =[]
    final_list = []
    a=0
    b=0

#iterates through the lists in candidate_rankings, and creates a new
#list where the number comes first

    for x in candidate_rankings:
         
        temp_list.append(x[1])
        temp_list.append(x[0])

#if this is not the cycle of loops and the number of temp_list matches one
#in a list in final_list, it adds the second value (the name) of temp_list
#to that list. Also adds 1 to b to signify that the if statement ran 
        

        if a != 0:
            for y in final_list:
                if temp_list[0] in y:
                    y.append(temp_list[1])
                    b +=1
                    break
                
#adds 1 to b just to ensure it is not the same value of the original,
#so it will not run accidentally
                
        b+=1
        
#if this is not the first cycle and the previous statement did
#NOT run, then append temp_list to final_list and reset b to 0
        
        if a!=0 and b==1:
            final_list.append(temp_list)
            b=0
            
#resets b in case the above statement didn't run
            
        b=0    

#if this is the first loop (a = 0), append temp_list to final_list, and set a
#to a different value to signify this statement has run
        if a == 0:
            final_list.append(temp_list)
            a = 9999

            
        temp_list =[]
                   
    return final_list
                

def move_forward(candidate_rankings, candidate_scores):
    
#sets up two variables and three lists, one of which is formatted
#like the lists in 'final_list' will be, to use as a comparison
    
    tempscore = 0
    temprank = 0
    temp_list = []
    final_list = []
    mover=['alden',0,0]

#iterates over the candidate_rankings and scores, adding a candidate's
#name, rank, and score respectivley to 'temp_list' before appending that
#list into 'final_list'

    for x in candidate_rankings:
        for y in candidate_scores:
            if y[0] == x[0]:
                temprank = x[1]
                tempscore = y[1] + y[2] + y[3]
                temp_list.append(x[0])
                temp_list.append(temprank)
                temp_list.append(tempscore)
                final_list.append(temp_list)
                temp_list = []
                
#iterates over the lists in final_list, and if a candidate's rank is higher
#than the one in 'mover', it replaces the mover list with the candidate's list

#if the candidate's rank is the same as the one in 'mover', it compares the
#total scores of the two candidates and the one with the higher one
#is set as 'mover'
    
    for a in final_list:
        if a[1] > mover[1]:
            mover = a
        elif a[1] == mover[1]:
            if a[2] > mover[2]:
                mover = a

#the name of the candidate in 'mover' is returned
                
    return mover[0]


                
            

def database_info(hired):
    pass
