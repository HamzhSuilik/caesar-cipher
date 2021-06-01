from caesar_cipher.is_english_word import is_english_word
import re

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def encrypt(text: str,key : int):
    encrypted_text = ''
    for char in text :
        if re.sub(r'[^a-z]+','', char) :
            shifted = (char_dic[char] + key) % 26
            encrypted_text = encrypted_text + characters[shifted]
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text


def decrypt (text: str,key : int):
    return encrypt(text, - key)


def crack (encrypted_message : str):

    max_percentage = 0
    key = 0

    for i in range(26):
        percentage = is_english_word(encrypt(encrypted_message,i))
        if percentage > max_percentage :
            max_percentage = percentage
            key = i
    return encrypt(encrypted_message,key)


