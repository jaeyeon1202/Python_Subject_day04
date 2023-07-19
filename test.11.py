music="beautiful my life"

print(len(music))

print(music[:7])
print(music[3:])
print(music[2:5])

for i in range(7):
    print(music[i],end="")
print("")
for i in range(3,len(music)):
    print(music[i],end="")
print("")
for i in range(2,5):
    print(music[i],end="")
print("")