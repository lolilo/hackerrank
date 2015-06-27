import sys
sys.setrecursionlimit(100000)
coin = [1,5,10,20,50]
max_n=10000

def coinChange(index,current_value): 
   # print index, current_value
   if(current_value==N):return 1 
   if(current_value>N):return 0
   if index==len(coin): return 0
   if memo[current_value][index]!=-1: return memo[current_value][index]
   ans=coinChange(index,current_value + coin[index])+coinChange(index+1,current_value)
   ans=ans%10000000
   memo[current_value][index]=ans
   return ans

# memo=[[-1 for k in range(max_n)] for j in range(6)]
memo = [[-1 for j in range(6)] for k in range(max_n)] 

# t=int(input())
l = [5, 10, 15]
for i in xrange(len(l)):
   N=int(l[i])   
   print (coinChange(0,0))
   # memo=[[-1 for k in range(max_n)] for j in range(6)]
   memo = [[-1 for j in range(6)] for k in range(max_n)]
