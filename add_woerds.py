def concatenate(*arg):    
     s=''
     for i in range(len(arg)):
         s=s+arg[i]+'-'
    
     return s.strip('-')
   
print(concatenate("I", "love", "Python", "!"))
