class Plugboard():
    '''Plugboard is a part of the enigma machine which can cause a letter to be changed 0, 1 or 2 times.'''
    def __init__(self, dict_of_connections):
        self.dict_of_connections = {k.upper():v.upper() for k,v in dict_of_connections.items()}

    def plugboard_encrypt_the_letters(self, message):
        '''Takes as input a dictionary of letters to connect and swaps the connected letters with each other. 
        Letters without connections do not change. E.g. A connection between "w" and "h" is made, so if the 
        message "HELLOWORLD" passes though the plugboard, it will come out as "WELLOHORLD".'''
        cryptograph = []
        for letter in message.upper().replace(" ", ""):
            if letter in self.dict_of_connections.keys():
                cryptograph.append(self.dict_of_connections[letter])
            elif letter in self.dict_of_connections.values():
                cryptograph.append(list(self.dict_of_connections.keys())[(list(self.dict_of_connections.values()).index(letter))])
            else:
                cryptograph.append(letter)
        return "".join(cryptograph)
