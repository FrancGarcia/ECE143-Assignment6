def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                        
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert(isinstance(n, int) and n >= 0), "Number of trials must be an int of at least 0"
    assert(isinstance(k,int) and k >= 0), "Number of desired samples must be an int of at least 0"
    assert(isinstance(sum(p) == 1)), "The sum of the probabilities must be 1"
    for prob in p:
        assert(isinstance(prob, float) and prob >= 0), "Each probability must be a valid float of at least 0"
    