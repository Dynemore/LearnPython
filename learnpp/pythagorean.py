# pythagorean.triple.py
from math import sqrt
# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
 for a in range(1, mx) for b in range(a, mx)]
print(triples)
# this will filter out all non pythagorean triples
triples = list(
 filter(lambda triple: triple[2].is_integer(), triples)) #cara filternya dengan milih yang isi element ke 3 / index ke 2 adalah integer
print(f"hasil:",triples) # prints: [(3, 4, 5.0), (6, 8, 10.0)]