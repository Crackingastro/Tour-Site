x = "hh"
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

final = ""
for i in range (0,len(x)):
    if i == 0:
        pos = letters.index(x[i])
        x = letters[:pos+1]
        for k in x:
            final = k
            print(final,end="\n") 
    else:
        pos = letters.index(x[i])
        print("here")
        print(x[i])
        
        print(pos)
        x = letters[:pos+1]
        print(x)
        for k in x:
            man = final+str(k)
            
            print(man,end="\n")
        
            
