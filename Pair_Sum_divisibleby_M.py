def solve(A, B):
    mod = (10**9)+7
    count = [0]*B
    for i in range(len(A)):
        idx = A[i]%B
        count[idx] = count[idx]+1
        
    ans = (count[0]*(count[0]-1))//2
    ans = ans%mod
    i = 1
    j = B-1
    while(i<=j):
        if i==j:
            ans = ans + (count[i]*(count[i]-1))//2
            ans = ans%mod
        else:
            ans = ans + (count[i]*count[j])
            ans = ans%mod
            
        i = i+1
        j = j-1
        
    return ans
#Main
A =[ 1, 2, 3, 4, 5 ]
B = 2
ans = solve(A,B)
print(ans)