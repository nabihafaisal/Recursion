def pwr(a,b):
    if(b==0):
        return(1)
    else:
        return(a*pwr(a,b-1))



print(pwr(3,4))
    
    
