import sys
input = sys.stdin.readline

height = []
eighth = 0
ninth = 0

for i in range(9):
    height.append(int(input()))

height_sum = sum(height)
for i in range(8):
    for j in range(i+1,9):
        if height_sum-(height[i]+height[j]) == 100:
            eighth = height[i]
            ninth = height[j]

height.remove(eighth)
height.remove(ninth)
height.sort()

for i in height:
    print(i)