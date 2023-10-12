import sys
import random
import codecs


def randomize(word, change_number=50):
    word_array = list(word[1:-1])
    size = len(word_array)
    for _ in range(change_number):
        first_letter = random.randrange(0, size)
        second_letter = random.randrange(0, size)
        mem = word_array[first_letter]
        word_array[first_letter] = word_array[second_letter]
        word_array[second_letter] = mem
    return word[0] + "".join(word_array) + word[-1]


def typoglycemie(data):
    result = [word if len(word) < 4 else randomize(word) for word in data.split(" ")]
    return " ".join(result)


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
