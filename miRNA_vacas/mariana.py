
import csv
import sys
from pprint import pprint

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = list()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = list()
                    longest = c
                    lcs_set.append(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.append(S[i-c+1:i+1])

    return lcs_set[0]

file_name = sys.argv[1]
with open(file_name) as f:
    l = f.readlines()
    l = [x.strip() for x in l]

result = None

for line in l:

        if not result:
                result = line
                continue
        result = lcs(line, str(result))

print(str(result))

