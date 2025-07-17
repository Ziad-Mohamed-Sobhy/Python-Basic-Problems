# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
m = int(input())                      
a = set(map(int, input().split())) 
n = int(input())              
b = set(map(int, input().split()))  
sym_diff = sorted(a ^ b)
for num in sym_diff:
    print(num)
