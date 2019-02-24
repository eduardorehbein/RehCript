from random import randint

class Codificador:

    def __init__(self, nCoefsPolinomio, coefs = None):
        if not(coefs):
            self.coefs = [randint(0, 9) for i in range(nCoefsPolinomio)]
            if self.coefs[len(self.coefs) - 1] == 0:
                self.coefs[len(self.coefs) - 1] += 1
        else:
            self.coefs = coefs
        self.k = 1 #o k sera usado na integração
    
    def f(self, x):
        y = 0
        for i in range(len(self.coefs)):
            y += (x ** i)*self.coefs[i]
        return y

    def codificaEmDecimal(self, valorASCII):
        return self.f(valorASCII)

    def decodificaEmASCII(self, decimal):
        def media(a, b):
            return (a+b)/2

        def estaPerto(a, b, prec=0.001):
            return abs(a - b) < prec

        def busca(f, a, b, prec=0.001):
            x = media(a, b)
            fx = f(x)
            if estaPerto(a,b,prec):
                return x
            if fx>0:
                return busca(f,a,x,prec)
            if fx<0:
                return busca(f,x,b,prec)
            return x

        def metodoDoIntervaloMedio(f, a, b, prec=0.001): #abssição
            fA = f(a)
            fB = f(b)
            if (fA<0<fB):
                return busca(f, a, b, prec)
            elif (fB<0<fA):
                return busca(f, b, a, prec)
            elif fA==0:
                return a
            elif fB==0:
                return b
            else:
                print('Os valores não têm sinais opostos:')
                print('\tf({:.2f})={:.2f}'.format(a, fA))
                print('\tf({:.2f})={:.2f}'.format(b, fB))
                return

        def g(x):
            return self.f(x) - decimal
        
        res = metodoDoIntervaloMedio(g, 0, 300)

        intTeto = int(res) + 1
        intBase = int(res)
        if res - intBase < intTeto - res:
            res = intBase
        else:
            res = intTeto
        
        return res
