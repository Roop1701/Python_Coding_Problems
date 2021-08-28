#Code Chef LT99 August Question 2
'''
You are given an integer N. Consider the sequence containing the integers 1,2,…,N in increasing order (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.

Input Format
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output Format
For each test case, print a single line containing one integer --- the maximum length of a contiguous subsequence with even sum.

Constraints
1≤T≤104
2≤N≤104
Subtasks
Subtask #1 (100 points): original constraints

Sample Input 1 
3
3
4
5

Sample Output 1 
3
4
4

Explanation
Example case 1: The optimal choice is to choose the entire sequence, since the sum of all its elements is 1+2+3=6, which is even.
Example case 3: One of the optimal choices is to choose the subsequence [1,2,3,4], which has an even sum.
'''
def solve(n):
    if n<=1:
        return 0
    if n == 2:
        return 1
    ans = (n*(n+1))//2
    if ans%2 == 0:
        return n
    else:
        return n-1
T = int(input())
i = 1
while i<=T:
    n = int(input())
    ans = solve(n)
    print(ans)
    i = i+1