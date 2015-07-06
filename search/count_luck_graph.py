# Enter your code here. Read input from STDIN. Print output to STDOUT

def dfs(graph):
    pass

cases = int(raw_input())
for case in xrange(cases):
    n, m = int(raw_input()), int(raw_input())
    graph = []
    for _ in xrange(n):
        row = raw_input().split()
        graph.append(row)
    k = int(raw_input())
    