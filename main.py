class main:
    def __init__(self,nombre):
        self.nombre=nombre
    def cuenta_info(self):
        print('informacion de la cuenta: ')
        print('Nombre: ', nombre[10], end="\n")
        print('Numero de cuenta: ', info[nombre][0], end="\n")
    def pin_change(self):
        i=3
        while(i>0):
            p=int(input('ingresa el PIN: '))
            if p==info[nombre][2]:
                x=input(' ingresa el PIN bien')
                info[nombre][2]=x
                break
            else:
                i=i-1
                print('PIN incorrect, {} tries left'.format(i))
        if i==0:
            del info[nombre]
            print('cuenta Bloqueada')
    def cuenta_balance(self):
        print('cuenta Balance: ',info[nombre][3])
    def retirar(self):
        print('cuenta Balance: ',info[nombre][3])
        main=float(input('ingrese la cantidad que desea retirar: '))
        if main<=info[nombre][3]:
            info[nombre][3]=info[nombre][3]-main
            print('su nuevo sald es : ', info[nombre][3])
        else:
            print('fono insuficiente')

info={"David":[1235,1000]}
k=info.keys()
while (1):
    nombre=str(input('Enter nombre: '))
    if nombre in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==info[nombre][2]:
                a=main(nombre)
                while(1):
                    print('Presina 1 para ver tu saldo')
                    print('Presiona 2 para retirar')
                    print('Presiona 3 para depositar')
                    s=int(input('Select Operation: '))
                    if  s==1:
                        a.cuenta_balance()
                    elif s==2:
                        a.retirar()
                    elif s==3:
                        a.deposito()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit, press any other key to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Gracias!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print(' PIN Incorrecto , {} 3 intentos restantes'.format(i))
        if i==0:
            del info[nombre]
            print('Cuenta bloqueada!')
        break