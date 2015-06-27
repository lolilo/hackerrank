import sys
sys.setrecursionlimit(100000)
coin = [1,5,10,20,50]
max_n=10000

# index is the coin_array index, current_value is what we have calculated so far
# N is the target value

def coinChange(index,current_value): 
   # print index
   if(current_value==N):return 1 # base case -- if current_value = N, return 1, meaning we have found a collection of coins that add up to it
   if(current_value>N):return 0 # this collection doesn't work
   if index==len(coin): return 0 # desired index is out of range of available coins, collection also doesn't work
   if memo[index]!=-1: return memo[index][current_value] # we have already calculated how many ways to reach index value; return this precalculated value


   # otherwise, we need to do work
   ans=coinChange(index,current_value + coin[index])+coinChange(index+1,current_value)
   ans=ans%10000000
   memo[index][current_value]=ans
   return ans # how many ways can we combine change to reach the target value?

memo = [[-1 for j in range(6)] for k in range(max_n)]
# t=int(input())
l = [5]
for i in xrange(len(l)):
   N=int(l[i])   
   print (coinChange(0,0))
   # memo=[[-1 for k in range(max_n)] for j in range(6)]
   memo = [[-1 for j in range(6)] for k in range(max_n)]

