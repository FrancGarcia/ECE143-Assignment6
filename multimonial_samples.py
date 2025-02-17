import random
def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                        
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert(isinstance(n, int) and n >= 0), "Number of trials must be an int of at least 0"
    assert(isinstance(k,int) and k >= 0), "Number of desired samples must be an int of at least 0"
    assert(round(sum(p),10) == 1.0), "The sum of the probabilities must be 1"
    for prob in p:
        assert(prob >= 0), "Each probability must be at least 0"
    res = [[0] * len(p) for _ in range(k)]
    for sample in range(k):
        for trial in range(n):
            chosen_index = random.choices(range(len(p)), p, k=1)[0]
            res[sample][chosen_index] += 1 
    return res