import random

_letters = "enitrlsauodychgmpbkvwfzxqj"
_speeds = [93, 66, 63, 56, 57, 48, 45, 81, 78, 65, 50, 55, 38, 83, 51, 40, 40, 42, 35, 46, 40, 34, 41, 47, 35, 25]

_letters = [i for i in _letters]
_w = [(max(_speeds)-i+1) for i in _speeds]


def gen(letters, number_of_words, max_lenght, weights=None, caps=0):
  _res = []
  for j in range(number_of_words):
    k = random.randint(1, max_lenght)
    _res.append(''.join(random.choices(letters, k=k, weights=weights)))
    if random.randint(1,100) < caps:
        _res[-1] = _res[-1].capitalize()
    
  return _res

' '.join(gen(_letters, 1000, 6, _w, 20))
