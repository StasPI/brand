from fuzzywuzzy import fuzz
from fuzzywuzzy import process


a = ['Абслют', 'Обсалют']
b = ['Абсолют', '"Абсолют”']
c = ['Alpen Gold', 'Alpen/Gold']
d = ['Айсберри', 'Айс берри']

def eva(x, y):
    a = fuzz.partial_ratio(x, y)
    print(a)
    b = fuzz.ratio(x, y)
    print(b)
    c = fuzz.WRatio(x, y)
    print(c)
    print(' ')
    
def eva2(x, y):
    a = fuzz.partial_ratio(x, y)
    print(a)
    b = fuzz.ratio(x, y)
    print(b)
    c = fuzz.WRatio(x, y)
    print(c)
    print('===================== ')
    
eva(a[0], a[1])
eva2(a[1], a[0])
eva(b[0], b[1])
eva2(b[1], b[0])
eva(c[0], c[1])
eva2(c[1], c[0])
eva(d[0], d[1])
eva2(d[1], d[0])



