# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
    
# Read the array of n integers
arr = list(map(int, input().split()))
# Read sets A (liked) and B (disliked)
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    
print(happiness)
