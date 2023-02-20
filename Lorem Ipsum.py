from random import randint, choice
from config import *

chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if numbers:

    for num in nums:

        chars.append(num)

if symbols:

    for symbol in ListSymbols:

        chars.append(symbol)

para = ""

for _ in range(paras):

    word = ""
    wordCount = randint(wordsPerPara[0],wordsPerPara[1])

    for _ in range(wordCount):

        for _ in range(randint(length[0],length[1])):

                word += choice(chars)

        para += word + " "

    print(para)
    para = ""
    print()