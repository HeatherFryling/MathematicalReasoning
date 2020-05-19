# Heather Fryling
# Introduction to Graph Theory
# Coursera
# 5/19/2020
# Completed an implementation of the Gale-Shapley algorithm

def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0] 
        
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]         
        
        # Write your code here
        
        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        # She accepts if unmarried or if he is at a lower index in her list
        if currentHusband == None or herPreferences.index(he) < herPreferences.index(currentHusband):
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
            if currentHusband != None:
                unmarriedMen.append(currentHusband)
        nextManChoice[he] = nextManChoice[he] + 1
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
            
    # Note that if you don't update the unmarriedMen list, 
    # then this algorithm will run forever. 
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse
    
# You might want to test your implementation on the following two tests:
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])

print(stableMatching(3, [[0, 1, 2], [1, 2, 0], [2, 1, 0]], [[1, 2, 0],[0, 1, 2], [2, 1, 0]]))