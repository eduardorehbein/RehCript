from mtmHelper import MtmHelper

mh = MtmHelper()
coef = [2, 3, 4, 5]
exp = list(range(len(coef)))
k = 2

print("Coeficientes:", coef, ",expoentes:", exp)

for i in range(3):
    coef= mh.derivaPol(coef, exp)
    print("Coeficientes:", coef, ",expoentes:", exp)

for j in range(3):
    coef= mh.integraPol(coef, exp, k)
    print("Coeficientes:", coef, ",expoentes:", exp)
    k += 1
