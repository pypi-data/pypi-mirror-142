#!/usr/bin/env python3

'''Encrypts and/or decrypts messages.
'''

import sys
from enigma_kostas import plugboard, rotors

def enigma_encrypt(message, rotor_order_str):
    '''Takes as inputs a message to encrypt/decrypt and the order of the 3 out of 5 pre built rotors. The connections of the plugboard are 
    already given and can be changed by modifying the "plug" dictionary.

    Parameters
    ----------
    message 
        The message to encrypt or decrypt.
    rotor_order_str
        A string of three numbers from 1-5, e.g. "243".

    Returns
    -------
    char
        The message encrypted or decrypted.
    '''
    plug = plugboard.Plugboard({"W": "H", "A": "B", "o": "e" })
    
    # Set up the enigma parts
    rotor1 = rotors.Rotor(1)
    rotor2 = rotors.Rotor(2)
    rotor3 = rotors.Rotor(3)
    rotor4 = rotors.Rotor(4)
    rotor5 = rotors.Rotor(5)
    ref = rotors.Reflector(1)

    total_rotors = {1: rotor1, 2: rotor2, 3: rotor3, 4: rotor4, 5: rotor5}
    rotor_order_list = [total_rotors[int(index)] for index in rotor_order_str]

    message = message.upper().replace(" ", "")

    # Encrypt a message
    encrypt = []
    for letter in message:
        plug_in = plug.plugboard_encrypt_the_letters(letter)
        out1 = rotor_order_list[0].rottor_encrypt_the_letter(plug_in)
        out2 = rotor_order_list[1].rottor_encrypt_the_letter(out1)
        out3 = rotor_order_list[2].rottor_encrypt_the_letter(out2)
        out_ref = ref.reflector_change_the_letter(out3)
        out4 = rotor_order_list[2].rottor_decrypt_the_letter(out_ref)
        out5 = rotor_order_list[1].rottor_decrypt_the_letter(out4)
        out6 = rotor_order_list[0].rottor_decrypt_the_letter(out5)
        plug_out = plug.plugboard_encrypt_the_letters(out6)
        encrypt.append(plug_out)
        
    return "".join(encrypt)


if __name__ == "__main__": 
    message = str(sys.argv[1])
    rotor_order_str = str(sys.argv[2])
    print(enigma_encrypt(message, rotor_order_str))
    
