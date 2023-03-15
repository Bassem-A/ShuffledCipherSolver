# Shuffle auto solver

x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc" #Pre Shuffle (Same Length as flag needed, just change length as needed, make sure every character is unique)
y = "BDFHJLNPRTVXZbAEIMQUYcGOWCSKa" #Post Shuffle (We got this after the shuffle happened)
solution = ""
dex = []
#ignore = []
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if(x[i]==y[j] and j not in dex):
            print(j)
            
            dex.append(j)
            
            
z = "lgcnyurVr34d0Df{__3_R}43na501" #Shuffled Flag (hard coded in the app)

for i in dex:
    solution += z[int(i)]
    
#print(dex)    
print(solution)
