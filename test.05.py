b=["g","o","o","d","","l","u","c","k"] 
c=("g","o","o","d","","l","u","c","k")
a="good luck"

# 각 자료형의 l글자를 출력하자. (인덱싱)
print(b[5])
print(c[5])
print(a[5])

#각 자료형의 luck를 출력해보자(슬라이싱)
print(b[5:])
print(c[5:])
print(a[5:])

#각 자료형의 good를 출력해보자.(반복문)
for i in range(4):
    print(b[i],end="")
print("")
for i in range(4):
    print(c[i],end="")
print("")
for i in range(4):
    print(a[i],end="")
print("")