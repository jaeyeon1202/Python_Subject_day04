#랜덤함수
import random
a=["red","blue","green","purple"]

print(random.choice(a))
print(random.randint(1,3))
print(random.randrange(1,3))
random.shuffle(a)
print(a)
print(random.random()) #0.0001~0.9999