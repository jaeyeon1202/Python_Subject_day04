start=int(input("시작:"))
end=int(input("끝:"))

s=1
if start < end:
    for i in range(start,end+1):
        s= s*i
if start > end:
    for i in range(end,start+1):
        s= s*i
if start == end:
    for i in range(start,start+1):
        s= s*i
print(s)