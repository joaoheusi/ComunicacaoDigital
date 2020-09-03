""" Desenvolver uma aplicação que permite realizar Código Hamming para asseguintes
configurações Hamming(7,4), Hamming(12,8) e Hamming(15,11) usando as
palavras de dados quaisquer e que possuam os tamanhos indicados. Além disso, o
código deverá permitir escolher qual versão utilizar. Deverá ser implementando o
detector e corretor de erro. """

def split_bits(value):
    return [int(letter) for letter in value]

def to_bool(value):
    return [bool(letter) for letter in value]

def to_ones_and_zeros(value):
    num_vector = []
    num = ''
    for position in value:
        if position:
            num+='1'
            num_vector.append(1)         
        else:
            num+='0'
            num_vector.append(0)

    return num,num_vector

def flip_n_bit(value,position):
    if(value[position-1] == 1):
        value[position-1] = 0
    else:
        value[position-1] = 1
    return value

def hammingFour(data):

        result_vector = []
        result_vector.append(data[0] ^ data[1] ^ data[3])
        result_vector.append(data[0] ^ data[2] ^ data[3])
        result_vector.append(data[0])
        result_vector.append(data[1] ^ data[2] ^ data[3])
        result_vector.append(data[1])
        result_vector.append(data[2])
        result_vector.append(data[3])

        a,b = to_ones_and_zeros(result_vector)
        print(a)
        return result_vector

def checkHammingFour(checker):
    k_vector = []
    value = to_bool(split_bits(checker))
    k2 = value[3] ^ value[4]  ^ value[5] ^ value[6]
    k1 = value[1] ^ value[2]  ^ value[5] ^ value[6]
    k0 = value[0] ^ value[2]  ^ value[4] ^ value[6]

    k_vector.append(k2)
    k_vector.append(k1)
    k_vector.append(k0)

    num, num_vector = to_ones_and_zeros(k_vector)
    error_position = int(num,2)

    if error_position == 0:
        print('A mensagem foi transmitida corretamente.')
    else:
        print('Foi encontrado um erro na posição {}, a mensagem corrigida é:{}'.format(error_position,flip_n_bit(split_bits(checker),error_position)))
        
    #print(error_position)
    #print(num_vector)


def hammingEight(data):

        result_vector = []

        result_vector.append(data[0] ^ data[1] ^ data[3] ^ data[4] ^ data[6])
        result_vector.append(data[0] ^ data[2] ^ data[3] ^ data[5] ^ data[6])
        result_vector.append(data[0])
        result_vector.append(data[1] ^ data[2] ^ data[3] ^ data[7])
        result_vector.append(data[1])
        result_vector.append(data[2])
        result_vector.append(data[3])
        result_vector.append(data[4] ^ data[5] ^ data[6] ^ data[7])
        result_vector.append(data[4])
        result_vector.append(data[5])
        result_vector.append(data[6])
        result_vector.append(data[7])

        a,b = to_ones_and_zeros(result_vector)
        print(a)
        return result_vector

def checkHammingEight(checker):
    k_vector = []
    value = to_bool(split_bits(checker))
    k3 = value[7] ^ value[8] ^ value[9] ^ value[10] ^ value[11] 
    k2 = value[3] ^ value[4] ^ value[5] ^ value[6] ^ value[11]
    k1 = value[1] ^ value[2] ^ value[5] ^ value[6] ^ value[9] ^ value[10]
    k0 = value[0] ^ value[2] ^ value[4] ^ value[6] ^ value[8] ^ value[10] 

    k_vector.append(k3)
    k_vector.append(k2)
    k_vector.append(k1)
    k_vector.append(k0)

    num, num_vector = to_ones_and_zeros(k_vector)
    error_position = int(num,2)

    if error_position == 0:
        print('A mensagem foi transmitida corretamente.')
    else:
        print('Foi encontrado um erro na posição {}, a mensagem corrigida é:{}'.format(error_position,flip_n_bit(split_bits(checker),error_position)))
        
    #print(error_position)
    #print(num_vector)


def hammingEleven(data):

        result_vector = []

        result_vector.append(data[0] ^ data[1] ^ data[3] ^ data[4] ^ data[6] ^ data[8] ^ data[10])
        result_vector.append(data[0] ^ data[2] ^ data[3] ^ data[5] ^ data[6] ^ data[9] ^ data[10])
        result_vector.append(data[0])
        result_vector.append(data[1] ^ data[2] ^ data[3] ^ data[7] ^ data[8] ^ data[9] ^ data[10])
        result_vector.append(data[1])
        result_vector.append(data[2])
        result_vector.append(data[3])
        result_vector.append(data[4] ^ data[5] ^ data[6] ^ data[7] ^ data[8] ^ data[9] ^ data[10])
        result_vector.append(data[4])
        result_vector.append(data[5])
        result_vector.append(data[6])
        result_vector.append(data[7])
        result_vector.append(data[8])
        result_vector.append(data[9])
        result_vector.append(data[10])

        a,b = to_ones_and_zeros(result_vector)
        print(a)
        return result_vector

def checkHammingEleven(checker):
    k_vector = []
    value = to_bool(split_bits(checker))
    k3 = value[7] ^ value[8] ^ value[9] ^ value[10] ^ value[11] ^ value[12] ^ value[13] ^ value[14]
    k2 = value[3] ^ value[4] ^ value[5] ^ value[6] ^ value[11] ^ value[12] ^ value[13] ^ value[14]
    k1 = value[1] ^ value[2] ^ value[5] ^ value[6] ^ value[9] ^ value[10] ^ value[13] ^ value[14]
    k0 = value[0] ^ value[2] ^ value[4] ^ value[6] ^ value[8] ^ value[10] ^ value[12] ^ value[14]

    k_vector.append(k3)
    k_vector.append(k2)
    k_vector.append(k1)
    k_vector.append(k0)

    num, num_vector = to_ones_and_zeros(k_vector)
    error_position = int(num,2)

    if error_position == 0:
        print('A mensagem foi transmitida corretamente.')
    else:
        print('Foi encontrado um erro na posição {}, a mensagem corrigida é:{}'.format(error_position,flip_n_bit(split_bits(checker),error_position)))
        
    #print(error_position)
    #print(num_vector)


def CheckHammingSize(value):
    if len(value) == 7:
        checkHammingFour(value)
    elif len(value) == 12:
        checkHammingEight(value)
    elif len(value) == 15:
        checkHammingEleven(value)
    else:
        return False



def HammingSize(value):
    size = 0
    data = to_bool(split_bits(value))
    if len(value) == 4:
        hammingFour(data)
    elif len(value) == 8:
        hammingEight(data)
    elif len(value) == 11:
        hammingEleven(data)
    else:
        return False


def Hamming_main():
    print('Digite o valor da mensagem que deseja convertar utilizando Hamming:')
    HammingSize(input())
    print('Digite um valor de mensagem para verificar se existe erro:')
    CheckHammingSize(input())   

 
if __name__ == "__main__":
    Hamming_main()