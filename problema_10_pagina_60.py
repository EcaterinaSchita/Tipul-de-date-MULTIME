import itertools
multimea={1,2,3,4}
for i in range(len(multimea)):
    submultimile=itertools.combinations(m, i+1)
    print(set(submultimile))