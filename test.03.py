#컬렉션 자료형: 저장공간1개, 여러개를 저장
a="good luck"      #문자열
print(a[0])
print(a[-1])
print(a[1:4])
print(a[:4])
print(a[5:])


b=["g","o","o","d"]  #리스트
print(b[0])
print(b[-1])

c=("g","o","o","d")
print(c[0])
print(c[-1])


d=[78, 85, 97]

s=d[0]+d[1]+d[2]
s=0
for i in range(3):
    s=s+d[i]
 
