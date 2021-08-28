'''
Pair Sum divisible by M

Problem Description:
Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.
Since the answer may be large, return the answer modulo (109 + 7).

Problem Constraints:
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106

Input Format:
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format:
Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 2
 
Input 2:
 A = [5, 17, 100, 11]
 B = 28

Example Output
Output 1:
 4
 
Output 2:
 1

Example Explanation
Explanation 1:
All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5).  So total 4 pairs.
'''

'''
Brute force : Traverse over the whole array and find each pairs that is divisible by B
Time Complexity : O(n^2)
SPace Complexity : O(1)
'''

#Optimized Approach:
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

#TIme Complexity : O(n) + O(B)
#Space Complexity : O(B)
