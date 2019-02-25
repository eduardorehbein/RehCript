class MtmHelper:

    def media(self, a, b):
        return (a+b)/2

    def estaPerto(self, a, b, prec=0.001):
        return abs(a - b) < prec

    def raiz(self, f, a, b, prec=0.001): #abssição
        def busca(f, a, b, prec=0.001):
            x = self.media(a, b)
            fx = f(x)
            if self.estaPerto(a,b,prec):
                return x
            if fx>0:
                return busca(f,a,x,prec)
            if fx<0:
                return busca(f,x,b,prec)
            return x
        
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
    
    def derivaPol(self, coefOrdenados, expOrdenados):
        novosCoeficientes = list(map(lambda coef, exp: coef*exp, coefOrdenados ,expOrdenados))
        return novosCoeficientes[1:] + [0]

    def integraPol(self, coefOrdenados, expOrdenados, k):
        return [k] + list(map(lambda x, exp: x/exp, coefOrdenados[:-1], expOrdenados[1:]))
