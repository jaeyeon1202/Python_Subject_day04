a="파이썬은완전재미있어요"
a=["파","이","썬","은","완","전","재","미","있","어","요"]
for i in range(len(a)):
    if i % 2 == 1:
        a[i]="#"
print(a)

a="파이썬은완전재미있어요"
print(a[0])
for i in range(len(a)):
    if i % 2 ==1:
        print("#",end="")
    if i % 2 ==0:
        print(a[i],end="")