import sys

n = int(sys.stdin.readline())
s_list = [sys.stdin.readline().strip() for i in range(n)]

def vps(s):
    temp = []
    for i in s:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) >= 1 and temp[-1] == '(':
                temp.pop()
            else:
                return False
    
    if len(temp) == 0:
        return True
    else:
        return False
   
for i in range(n):
    if vps(s_list[i]) == True:
        print("YES")
    else:
        print("NO")