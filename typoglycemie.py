import sys
import random
import codecs
import re

pattern = r'\s+|\w+|[^\w\s]'

def randomize(word, change_number=50):
    word_array = list(word)
    size = len(word_array)
    for _ in range(change_number):
        first_letter = random.randrange(1, size-1)
        second_letter = random.randrange(1, size-1)
        word_array[first_letter], word_array[second_letter]= word_array[second_letter],word_array[first_letter]
    return "".join(word_array)


def typoglycemie(data):
    result = [word if len(word) < 4 else randomize(word) for word in re.findall(pattern, data)]
    return "".join(result)


def main(argv):
    try:
        with codecs.open(argv[1], encoding="utf-8") as reading_file:
            for phrase in reading_file.readlines():
                print(typoglycemie(phrase[:-1]))
    except IndexError:
        print("Should use arg (python typoglycemie.py mysample.data")
    except Exception:
        print(sys.exc_info()[0])


if __name__ == '__main__':
    main(sys.argv)
