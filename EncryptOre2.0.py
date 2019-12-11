import random
import sys
from getpass import getpass






def main():

    password = getpass("Enter password: ")
    if password != ("lol"):
        sys.exit()
    

    alphabet = ["a","b","c","d","e","f","g","h", "i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ", ",", ".", "!", ":",";","?", "'", "1","2","3","4","5","6","7","8","9","0"]
    pangram = ["s","p","h","i","n","x","o","f","b","l","a","c","k","q","u","a","r","t","z","j","u","d","g","e","m","y","v","o","w", " ", ",", ".", "!",":",";","?", "'","1","2","3","4","5","6","7","8","9","0"]
    hourList = []
    for x in range(1,25):
        hourList.append(str(x))
    eOrD = input("Encrypt or decrypt? Enter 'e' or 'd': ")

    while eOrD != "e" and eOrD != "d":
        eOrD = input("Encrypt or decrypt? Enter 'e' or 'd': ")
    
    if eOrD == "e":                                             # ENCODER CODE
    
    
        rOrM = input("Random or manual time? Enter 'r' or 'm': ")
        
        while rOrM != "r" and rOrM != "m":
            rOrM = input("Random or manual time? Enter 'r' or 'm': ")
        
        if rOrM == "m":
            day = int(input("Day: "))
            hour = int(input("Hour: "))
        elif rOrM == "r":
            day = random.randint(1,4)
            hour = random.randint(1,24)
        
        seperatorWord = input("Seperator Word: ")
        
        Input = str(input("Input: "))
        output = []

        inputList = []
        for x in Input:
            inputList.append(x)

        def encode1():
            for i in inputList:
                if alphabet.index(i) >= (len(alphabet) - hour):
                    char = alphabet[hour - (len(alphabet) - alphabet.index(i))]
                else:
                    char = alphabet[alphabet.index(i) + hour]
                output.append(char)

        def encode2():
            for i in inputList:
                char = alphabet[-(alphabet.index(i)) - 1]
                output.append(char)

        def encode3():
            for i in inputList:
                char = str(((alphabet.index(i)+1) * hour) + 37)
                output.append(char + seperatorWord)
            
        def encode4():
            for i in inputList:
                if pangram.index(i) >= (len(pangram) - hour):
                    char = pangram[hour - (len(pangram) - pangram.index(i))]
                else:
                    char = pangram[pangram.index(i) + hour]
                output.append(char)

        if day == 1:
            encode1()
            output.append(day)
            output.append("~")
            output.append(hour)
        if day == 2 and (hour == 42 or hour == 7):
            encode2()
            output.append(day)
            output.append("~")
            output.append(hour)
        elif day == 2:
            encode1()
        if day == 3:
            encode3()
            output.append(alphabet[day])
            output.append("~")
            output.append(alphabet[hour])
        if day == 4:
            encode4()
            output.append(day)
            output.append("~")
            output.append(hour)

        for a in output:
            print(a, end = "")
            
    elif eOrD == "d":                                   # DECRYPTOR CODE
    
        day = input("Day: ")
        if day != 1 and day != 2 and day != 3 and day != 4:
            day = alphabet.index(day)
        else:
            day = int(day)

        hour = input("Hour: ")
        if hourList.count(hour) == 0:
            hour = alphabet.index(hour)
        else:
            hour = int(hour)

        seperatorWord = input("Seperator Word(if there is none, this doesn't matter): ")
        

        Input = str(input("Input: "))
        output = []

        inputList = []
        for x in Input:
            inputList.append(x)

        
        def decode1():
            for i in inputList:
                if alphabet.index(i) <= (hour - 1):
                     char = alphabet[-hour + alphabet.index(i)]
                else:
                    char = alphabet[alphabet.index(i) - hour]
                output.append(char)

        def decode2():
            for i in inputList:
                char = alphabet[-(alphabet.index(i)) - 1]
                output.append(char)

        def decode3():
            for i in inputList:
                if i not in seperatorWord:
                    for x in range(alphabet.index(i), alphabet.index(i) + 3):
                        if str(x) not in seperatorWord:
                            char = alphabet[((int(i) - 37)/hour)-1]
                            output.append(char)
                    
        def decode4():
            for i in inputList:
                if pangram.index(i) <= (hour - 1):
                    char = pangram[-hour + pangram.index(i)]
                else:
                    char = pangram[pangram.index(i) + hour]
                output.append(char)
        
        



        if day == 1:
            decode1()
            
        if day == 2 and (hour == 42 or hour == 7):
            decode2()
            
        elif day == 2:
            decode1()

        if day == 3:
            decode3()
            
        if day == 4:
            decode4()
            

        for a in output:
            print(a, end = "")

            
if __name__ == "__main__":
    main()
    
        
