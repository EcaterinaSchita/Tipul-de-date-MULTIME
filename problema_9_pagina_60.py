A = set(eval(input("Introduceti multimea A: ")))
B = set(eval(input("Introduceti o alta multimea B: ")))
print(A)
print(B)
print("Intersectia multimilor este : ", A.intersection(B))
print("Reuniunea multimilor: ", A.union(B))
print("Diferenta multimilor este: ", A.difference(B))