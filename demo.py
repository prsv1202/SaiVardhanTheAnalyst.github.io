sweets=[1,0,0,1,0,1,0,0]
N=7
K=2
def solve(s,n,k):
    c=0
    i=1
    if s[0]==0 and s[1]==0:
        c+=1
    while (i<n-1):
        if s[i-1]==0 and s[i]==0 and s[i+1]==0:
            c+=1
        i+=1
    if s[-1]==0 and s[-2]==0:
        c+=1
    if c>=1:
        return 1
    else:
        return 0

