import random


def shuffle_list(l: list) -> list:
    random.shuffle(l)
    return l


string = (
    'Some random text without punctuation and words from one and '
    'two characters I am'
)

string = [w[0] + ''.join(shuffle_list(list(w[1:-1]))) + w[-1]
          if len(w) > 2 else w for w in string.split()]
print(string)
