# KeyCrypt
# A basic keyfile encryption plugin for EncryptOre.
# Author: Dallin Guisti
# Python version 3.6.5
# Copyright (c) 2019 EncryptOre TM. All rights reserved.
# Note: EncryptOre TM is a registered project by D-Multi inc (c). All associated icons and code belongs to them.

from string import printable as chars
import random

class encFile():
    def __init__(self, text: str) -> None:
        self.text = text

    def encrypt(self, alph: str, pang: str) -> str:
        encryptedText = self.text[::-1] # Encrpytion code goes here...
        newText = []
        for char in encryptedText:
            newText.append(pang[alph.index(char)])
        encryptedText = ''.join(newText)
        encryptedText = ''.join(format(ord(i), 'b') for i in encryptedText)
        return encryptedText, pang

class keyFile():
    def __init__(self, typeArg: str, level: int) -> None:
        self.type = typeArg
        self.level = level

    def initFile(self, encFile: encFile) -> None:
        pass


pangram = [y for y in chars]
alphabet = pangram.copy()
random.shuffle(pangram)
file = encFile(input("Input text to encrypt: "))
text, key = file.encrypt(alphabet, pangram)
print(text)