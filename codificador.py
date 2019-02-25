from random import randint
from mtmHelper import MtmHelper

class Codificador:

    def __init__(self, nCoefsPolinomio, coefs = None):
        self.mtmHelper = MtmHelper()
        if not(coefs):
            self.coefs = [randint(1, 9) for i in range(nCoefsPolinomio)]
        else:
            self.coefs = coefs
        self.exp = list(range(nCoefsPolinomio))
        self.k = 1
        self.ultOp = "deriv"
    
    def f(self, x):
        y = 0
        for i in range(len(self.coefs)):
            y += (x ** self.exp[i])*self.coefs[i]
        return y

    def modificaPolinomio(self):
        def temZero(lista):
            return 0 in lista

        if (self.ultOp == "deriv" and sum(self.coefs) > (self.coefs[0] + self.coefs[1])) or not temZero(self.coefs):
            self.coefs = self.mtmHelper.derivaPol(self.coefs, self.exp)
            self.ultOp = "deriv"
        else:
            self.coefs = self.mtmHelper.integraPol(self.coefs, self.exp, self.k)
            self.k += 1
            self.ultOp = "integr"

    def tranfQuebradoEmTupla(self, inteiro, decimal):
        n = decimal
        while n - int(n) > 0:
            n *= 10
        return (int(inteiro), int(n))

    def codificaEmDecimal(self, valorUnicode):
        res = self.f(valorUnicode)
        self.modificaPolinomio()

        valorDecimail = res - int(res)
        if valorDecimail > 0:
            res = self.tranfQuebradoEmTupla(res, valorDecimail)
        
        return res

    def decodificaEmUnicode(self, valor):
        y = 0
        if type(valor) == tuple:
            parteDecimal = valor[1]
            while parteDecimal > 1:
                parteDecimal /= 10
            y = (valor[0] + parteDecimal)
        else:
            y = valor
        
        res = self.mtmHelper.raiz(lambda x: self.f(x) - y, 0, 300)

        intTeto = int(res) + 1
        intBase = int(res)
        if res - intBase < intTeto - res:
            res = intBase
        else:
            res = intTeto

        self.modificaPolinomio()
        return res
