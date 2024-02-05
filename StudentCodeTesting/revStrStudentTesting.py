def reverse(string):
    
    string= str(string)
    sep = ''
    
    for i in reversed(string):
        sep += i
    return(sep)
