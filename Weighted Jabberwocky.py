import random

_letters = "enitrlsauodychgmpbkvwfzxqj"
_speeds = [79, 62, 57, 56, 60, 45, 49, 86, 57, 49, 47, 54, 39, 98, 42, 43, 33, 33, 37, 46, 41, 31, 57, 41, 31, 25]


_letters = [i for i in _letters]
_w = [(max(_speeds)-i+1) for i in _speeds]


def gen(letters, number_of_words, max_lenght, weights=None):
  _res = []
  for j in range(number_of_words):
    k = random.randint(1, max_lenght)
    _res.append(''.join(random.choices(letters, k=k, weights=weights)))
  return _res

' '.join(gen(_letters, 1000, 6, _w))
