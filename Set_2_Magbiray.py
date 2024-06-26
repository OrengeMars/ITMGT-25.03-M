#!/usr/bin/env python
# coding: utf-8

# In[54]:


def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter == " ":
        return " "
    
    letter = letter.upper()
    
    index = alphabet.find(letter)
    
    sindex = (index + shift) % len(alphabet)
    
    return alphabet[sindex]

shift_letter("A", 1)


# In[24]:


def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""

    for char in message:
        if char == " ":
            cipher += " "
        else:
            char = char.upper()
            index = alphabet.find(char)
            sindex = (index + shift) % len(alphabet)
            cipher += alphabet[sindex]

    return cipher

caesar_cipher("gex", 12)


# In[5]:


def shift_by_letter(letter, letter_shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter == " ":
        return " "
    
    letter = letter.upper()
    
    index = alphabet.find(letter)
    shiftedletter = alphabet.find(letter_shift)
    
    sindex = (index+shiftedletter) % len(alphabet)
    
    return alphabet[sindex]
    
shift_by_letter("A","C" )    


# In[22]:


def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    key_length = len(key)
    encrypted_message = ""

    extended_key = (key * (len(message) // key_length + 1))[:len(message)]

    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encrypted_message += " "
        else:

            key_index = alphabet.index(extended_key[i])

            message_index = alphabet.index(char.upper())

            shifted_index = (message_index + key_index) % 26

            encrypted_message += alphabet[shifted_index]

    return encrypted_message

vigenere_cipher("Hello", "KEY")


# In[29]:


def scytale_cipher(message, shift):

    while len(message) % shift != 0:
        message += "_"
    
    encoded = [""] * len(message)
    message_len = len(message)
    
    for i in range(message_len):
        new_index = (i // shift) + (message_len // shift) * (i % shift)
        encoded[i] = message[new_index]
    
    result = ""
    for char in encoded:
        result += char
        
    return result

scytale_cipher("INFORMATION_AGE", 3)


# In[30]:


def scytale_decipher(message, shift):

    deciphered = [""] * len(message)
    message_len = len(message)
    
    for i in range(message_len):

        original = (i // shift) + (message_len // shift) * (i % shift)

        deciphered[original] = message[i]
    
    result = ""
    for char in deciphered:
        result += char
    
    return result

scytale_decipher("IMNNA_FTAOIGROE", 3)


# In[ ]:




