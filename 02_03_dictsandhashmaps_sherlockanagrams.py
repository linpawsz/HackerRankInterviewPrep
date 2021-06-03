from itertools import combinations
from collections import Counter


def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]          # What does this line do?
        print(a)
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j in b]))   # What does this line do?
        print(count)
    return sum(count)


x = "cdcd"
print(sherlockAndAnagrams(x))