import sys
sys.setrecursionlimit(100000)
coin = [1,5,10,20,50]
max_n=10000

def coinChange(index,current_value): 
   print 'current index is', index
   print 'current value is', current_value
   print ''
   if(current_value==N):return 1 # base case -- if current_value = N, return 1, meaning we have found a collection of coins that add up to it
   if(current_value>N):return 0 # this collection doesn't work
   if index==len(coin): return 0 # desired index is out of range of available coins, collection also doesn't work
   if memo[index][current_value]!=-1: return memo[index][current_value] # we have already calculated how many ways to reach index value; return this precalculated value


   ans=coinChange(index,current_value + coin[index])+coinChange(index+1,current_value)
   print 'ans is', ans, 'for memo at {index}, {value}'.format(index=index, value=current_value)
   ans=ans%10000000
   memo[index][current_value]=ans
   return ans

memo=[[-1 for k in range(max_n)] for j in range(6)]
# t=int(input())
l = [5]
for i in xrange(len(l)):
   N=int(l[i])   
   print (coinChange(0,0))
   # memo=[[-1 for k in range(max_n)] for j in range(6)]
   memo = [[-1 for j in range(6)] for k in range(max_n)]
