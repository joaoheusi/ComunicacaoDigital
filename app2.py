""" 2) Desenvolva uma aplicação que implementa checksum para blocos de 4 palavras
com 12 bits cada. Simule, por meio de uma função, a inversão de um bit de
transmissão entre dois meios de comunicação. A partir dessa inversão, demonstre
a efetividade da técnica utilizando a soma de verificação que a inversão é detectada. """

import re 
import random
from app import flip_n_bit,split_bits

def slice_values(value):
    return re.findall('............', value)
            
def one_complement(value):
    a = format(value,'012b')
    a = a.replace('1','2')
    a = a.replace('0','1')
    a = a.replace('2','0')
    return a


def join_bits(value):
    word = ''
    for i in value:
        word+='{}'.format(value[i])
    return word

def generate_sum(value):
    return_sum = 0
    counter = 0
    for number in value:
        return_sum+= int(number,2)
        if return_sum > 4095:
            return_sum-= 4096
            counter+=1
    for i in range(counter):
        return_sum += 1
    return one_complement(return_sum)
    

def receive_values():
    print('Insira uma plavra decada vez (12 bits) ou as 4 palavras juntas(48bits)')
    return_value = []
    given_value = input()
    if len(given_value) > 12:
        return_value = slice_values(given_value)
    else:
        return_value.append(given_value)
        return_value.append(input())
        return_value.append(input())
        return_value.append(input())
    
    return return_value


def generate_error(value):
    rand1 = random.randint(0,3)
    rand2 = random.randint(1,12)
    value[rand1] =  join_bits(flip_n_bit( split_bits(value[rand1]),rand2))
    return value


def checksum_main():


    # Receber a mensagem


    msg_sent = receive_values()

    # Realizar Checksum da mensagem
    sent_checksum = generate_sum(msg_sent)
    

    # Gerar erro propositalmente

    msg_error = generate_error(msg_sent)

    # Fazer checksum da mensagem com erro

    erro_checksum = generate_sum(msg_error)


    # Comparar os dois Checksums

    print(sent_checksum)

    print(erro_checksum)


if __name__ == "__main__":
    checksum_main()