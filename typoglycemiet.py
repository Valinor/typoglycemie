import sys
import random

def main(data):
    data=data.split(" ")
    result=[]
    for mot in data:
        if len(mot)<4:
            result.append(mot)
        else:
            word_array=list(mot[1:-1])
            size=len(word_array)
            for _ in range(50):
                un=random.randrange(0,size-1)
                deux=random.randrange(0,size-1)
                mem1=word_array[un]
                word_array[un]=word_array[deux]
                word_array[deux]=mem1
            mot=mot[0]+"".join(word_array)+mot[-1]
            result.append(mot)
    return " ".join(result)

if __name__ == '__main__':
    print "test"+str(len(sys.argv))+sys.argv[0]
    if len(sys.argv)>1:
        with open(sys.argv[1]) as f:
            result=f.readlines()
            for phrase in result:
                print main(phrase)
