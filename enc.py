import prime
import Rabin
import sys
from termcolor import colored, cprint


def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


# main()
if __name__ == '__main__':
    
    ###########################################################
    # 256-bit prime number generation
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('                                               <Rabin 512>                                            ','red','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    #print(add_space(format(prime.generate_a_prime_number(256), 'x')))

    ###########################################################
    # Encryption
    cprint('\n                                        <Rabin-512 Encryption>                                        ', 'red', 'on_grey')

    print('\n')
    # p and q has 128 bits
    p = int(delete_space(input('p = ')), 32)   # p = daaefe652cad1614f17e87f2cd80973f
    print('\n')
    q = int(delete_space(input('q = ')), 32)   # q = f99988626723eef2a54ed484dfa735c7
    n = p*q
    print("\n\n")
    #print('n = pq =', add_space(format(n, 'x')))

    
   
    plaintext = int(delete_space(input('Plaintext = ')), 32)   # plaintext = be000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed
    ciphertext = Rabin.encryption(plaintext, n)
    print("\n\n")
    print('Ciphertext =', add_space(format(ciphertext, 'x')))
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('                                               <Rabin 512>                                            ','red','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    
