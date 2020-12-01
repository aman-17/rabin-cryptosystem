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
    # Decryption
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('                                               <Rabin 512>                                            ','red','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')

    cprint('\n                                        <Rabin-512 Decryption>                                        ', 'red', 'on_grey')
    print('\n')
    
    ciphertext = int(delete_space(input('Ciphertext = ')), 32)    
    cprint('Private Keys :','red', 'on_grey')

    print('\n')
    p = int(delete_space(input('p = ')), 32)  
    q = int(delete_space(input('q = ')), 32)  
    plaintext = Rabin.decryption(ciphertext, p, q)
    print('Plaintext =', add_space(format(plaintext, 'x').zfill(226 // 4)))
    
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('                                               <Rabin 512>                                            ','red','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    cprint('******************************************************************************************************','green','on_grey')
    

