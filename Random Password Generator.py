import random
passlen = int(input('enter the length of password'))
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()?'
P =''.join(random.sample(s,passlen))
print(P)          