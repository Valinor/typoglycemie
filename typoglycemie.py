import sys
import random

def randomize(word,change_number=50):
    word_array=list(word[1:-1])
    size=len(word_array)
    for _ in range(change_number):
        first_letter=random.randrange(0,size)
        second_letter=random.randrange(0,size)
        mem=word_array[first_letter]
        word_array[first_letter]=word_array[second_letter]
        word_array[second_letter]=mem
    return word[0]+"".join(word_array)+word[-1]

def typoglycemie(data):
    data=data.split(" ")
    result=[]
    for word in data:
        if len(word)<4:
            result.append(word)
        else:
            result.append(randomize(word))
    return " ".join(result)

if __name__ == '__main__':
    if len(sys.argv)>1:
        with open(sys.argv[1]) as f:
            result=f.readlines()
            for phrase in result:
                print typoglycemie(phrase)
