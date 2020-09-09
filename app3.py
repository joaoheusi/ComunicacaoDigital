""" Desenvolva uma aplicação que permite realizar o cálculo de CRC para uma palavra
de 8 bits usando o polinômio x3 + x2 + x. Deverá ser implementado o detector de
erro. Dica: utilize operadores de bitwise para implementar o cálculo. """



POLYNOM = ['1110']

def send_message():
    return input('Digite a palavra de 8 bits a ser calculada:\n')

def receive_check():
    return input('Digite a mensagem que foi recebida para verificar se ela possui erro:\n')


def to_vector(given):
    return [i for i in given]


def zeroes(size):
    return [ '0' for i in range(size)]


def xor(a, b):

    result = []

    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def binary_division(divisor, divident):
    pick = len(divisor) 
   
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
   
            tmp = xor(divisor, tmp) + divident[pick] 
   
        else:   
  
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        pick += 1
   
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 


def crc_main():
    

    key = '1110'
    sent_message = send_message()

    sent_with_crc = sent_message + binary_division(key, sent_message)
    
    print('A mensagem enviada foi:{}'.format(sent_with_crc))

    received_division = binary_division(key, sent_with_crc)

    print('Resultado da divisão de: {} pela chave {} ----> {}'.format(sent_with_crc,key,received_division))   

    b = input('Simule uma mensagem errada recebida:\n')
    
    print('Resultado da divisão da mensagem:{}'.format(binary_division(b,key)))


    
#10011010

if __name__ == "__main__":
    crc_main()