nr=eval(input('Introduceti un numar:'))
suma=0
while nr%2==0 or (nr%2!=0 and nr%3!=0):
    if nr%2==0:
        suma+=nr
    
    nr=eval(input('Introduceti un numar:'))

print('Suma numerelor pare introduse:',suma)
