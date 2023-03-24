n = str(input())
str_arr = list(n)
str_arr.sort(reverse=True)
string = str_arr[0]
for i in range(len(n)-1):
    string += str_arr[i+1]
print(string)