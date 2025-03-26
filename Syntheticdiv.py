dop = int(input("dop: "))
c = []
answer = []
ez1=[]
ez2=""
e = dop -1
for i in range(dop,-1,-1):
    a = int(input(f'coefficent for x^{i}'))
    c.append(a)
dividedby = int(input("what will this be divided by"))
q=0
for i in c:
    if q==0:
        w = i
        answer.append(i)
    if q == 1:
        p = (w * dividedby)
        w = i + p
        answer.append(w)
    q = 1
for i in answer:
    dop = dop -1
    if dop == e:
        ez1.append(f'{i}x^{dop} ')
        ez2 = "".join(ez1)
        continue
    if dop == -1:
        ez1.append(f' R: {i}')
        ez2 = "".join(ez1)
        break
    if dop == 1:
        ez1.append(f'+ {i}x ')
        ez2 = ''.join(ez1)
        continue
    if dop ==0:
        ez1.append(f'+ {i} ')
        ez2 = ''.join(ez1)
        continue
    ez1.append(f'+ {i}x^{dop} ')
    ez2 = ''.join(ez1)
print(ez2)
