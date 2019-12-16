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

    def encrypt(self, alph: str, pang: str, sep: str) -> str:
        newSep = []
        sepr = sep[::-1]
        for char in sepr:
            newSep.append(pang[alph.index(char)])
        separ = ''.join(newSep)
        encryptedText = self.text[::-1] # Encrpytion code goes here...
        newText = []
        for char in encryptedText:
            newText.append(pang[alph.index(char)] + separ)
        encryptedText = ''.join(newText)
        return encryptedText, pang

class decFile(encFile):
    def decrypt(self, alph: str, pang: str, sep:str) -> str:
        newSep = []
        for char in sep:
            newSep.append(alph[pang.index(char)])
        separ = ''.join(newSep)[::-1]
        newText = []
        for char in encryptedText.split(separ):
            newText.append(alph[pang.index(char)])
        decryptedText = ''.join(newText)
        decryptedText = decryptedText[::-1]
        return decryptedText

class keyFile():
    def __init__(self, typeArg: str, level: int) -> None:
        self.type = typeArg
        self.level = level

    def initFile(self, encFile: encFile) -> None:
        pass

if (False):
    pangram = [y for y in chars]
    alphabet = pangram.copy()
    random.shuffle(pangram)
    file = encFile(input("Input text to encrypt: "))
    seperatorWord = input("Please input seperator word (longer word gives higher accuracy but slower performace): ")
    text, key = file.encrypt(alphabet, pangram, seperatorWord)
    print("Text:", text)
    print("Key:", key)
else:
    alphabet = [y for y in chars]
    file = decFile(input("Input text to decrypt: "))
    seperatorWord = input("Please input seperator word: ")
    pangram = input("Please input key: ")[1:-1].replace('\'','').split(', ')
    print(pangram)
    text = file.decrypt(alphabet, pangram, seperatorWord)
    print("Text:", text)
