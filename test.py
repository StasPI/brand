a = 'у поликарпа два карася три Карпа'
b = 'карпа'

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
print(fuzz.partial_ratio(a,b))


import jellyfish
print(jellyfish.damerau_levenshtein_distance(a,b))
print(jellyfish.hamming_distance(a,b))
print(jellyfish.jaro_winkler_similarity(a,b))


print(a.split())
if b.lower() in a.lower().split():
    print('111111111111111111111111111111')
    
c = [1,2,3,4,5]
if 2 in c:
    print('11111111111111111111111111111')