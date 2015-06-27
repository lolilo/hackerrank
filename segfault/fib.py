max_n = 5000000
mod = 100000    
def fib(n):
    if n==1: return 0
    if n==2: return 1
    if memo[n]: return memo[n]  #if the number is already calculated, return from the table
    memo[n]=(fib(n-1)+fib(n-2))%mod #Calculate and Memorize
    return memo[n]

memo = [0 for i in range(0,max_n+2)]

for i in range(2, max_n+1): #generate all the numbers
   fib(i)

n=int(input())
print (memo[n])
