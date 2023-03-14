from xmlrpc.client import ServerProxy
import msvcrt

s = ServerProxy('http://localhost:20064', allow_none = True)

while True:
    print ('')
    print ('Selecione a operação que deseja realizar')
    print ("'+' para operação de soma")
    print ("'-' para operação de subtração")
    print ("'*' para operação de multiplicação")
    print ("'/' para operação de divisão")

    operador = input ('Digite o Operador: ')

    if s.isValid(operador):
        a = int(input('Digite o valor a: '))
        b = int(input('Digite o valor b: '))

        print ('O resultado é: ', s.calc(a,b,operador))

    else:
        print ('operação não é válida')

    print('')
    print("pressione 'n' para sair...")
    print("pressione qualquer tecla para continuar...")

    key = msvcrt.getwch()
    if key == 'n':
        exit()
