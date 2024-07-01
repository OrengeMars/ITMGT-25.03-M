#!/usr/bin/env python
# coding: utf-8

# set 4

# In[1]:


def bin_to_dec(binary_string):

    decimal = 0
    length = len(binary_string)
    
    for bin in range(length):
        decimal += int(binary_string[length - 1 - bin]) * (2 ** bin)
    
    return decimal

bin_to_dec("1011")


# In[14]:


def dec_to_bin(number):
    binary = ""
    num = number
    
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    
    return binary

dec_to_bin(5)
    


# In[4]:


def telephone_cipher(message):

    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    result = ""
    prev = ""

    for letter in message:
        
        if letter in encoder_dict:
            
            sequence = encoder_dict[letter]
            
            if sequence[0] == prev:
                
                result += "_"
            result += sequence
            prev = sequence[0]

    return result
            
telephone_cipher("ABC")


# In[10]:


def telephone_decipher(telephone_string):

    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    
    message = ""
    seq = ""
    
    for char in telephone_string:
        if char == "_":
            if seq in decipher_dict:
                message += decipher_dict[seq]
            seq = ""
        else:
            seq += char
            if seq not in decipher_dict:
                if seq[:-1] in decipher_dict:
                    message += decipher_dict[seq[:-1]]
                seq = char
    
    if seq in decipher_dict:
        message += decipher_dict[seq]
    
    return message

telephone_decipher("4466690366609996668803666")


# In[ ]:




