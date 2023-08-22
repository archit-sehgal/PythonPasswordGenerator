import random
x=["1","2","3","4","5"]
y=["a","b","c","d","e","f"]
z=["!","@","$","%","&"]
num=int(input("how many numbers:"))
lett=int(input("how many letters:"))
symb=int(input("how many symbols:"))
pasw=[]
for n in range(0,num):
    pasw+=random.choice(x)
for l in range(0,lett):
    pasw+=random.choice(y)
for s in range(0,symb):
    pasw+=random.choice(z)
random.shuffle(pasw)
password=''.join(pasw)
print(password)