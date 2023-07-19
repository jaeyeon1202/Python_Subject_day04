s=input("문자열 입력:")


for i in range(len(s)):
    if s[i] != "o" :
        print(s[i],end="")
    else:
        print("*",end="")
print("")

print(s.replace("o","*"))