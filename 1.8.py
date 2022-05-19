#1.8.7
X = int(input())
print(X // 60)
print(X % 60)

#1.8.8
X_in = int(input())
H = int(input())
M = int(input())
X=(X_in+H*60+M)%(24*60)
print(X // 60)
print(X % 60)