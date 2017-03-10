S=[[-1,0,0],[-1,0,1],[-1,1,0],[-1,1,1]]
W=[2.5,0,0]
d=[-1,-1,-1,1]
Miss=[]
def findMisclassify():
    for i in range(len(S)):
        result=0
        for j in range(len(S[i])):
            result += d[i]*S[i][j]*W[j]    
        if result <= 0:
                Miss.append(S[i]);
findMisclassify()
while (len(Miss)>0):
    Miss =[]
    for i in range(len(S)):
        result=0
        for j in range(len(S[i])):
            result += d[i]*S[i][j]*W[j]    
        if result <= 0:
            for j in range(len(S[i])):
                W[j]+= d[i]*S[i][j]
            Miss.append(S[i]);
print W