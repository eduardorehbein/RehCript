class MtmHelper:
    '''Responsável por fazer alguns cálculos matemáticos específicos que são utilizados na codificação dos valores decimais dentro do modelo de criptografia RehCript'''

    def media(self, a, b):
        '''Recebe 2 valores reais e retorna sua média aritmética'''
        return (a+b)/2

    def estaPerto(self, a, b, prec=0.001):
        '''Recebe 2 valores e compara sua proximidade baseado no parâmetro prec'''
        return abs(a - b) < prec

    def raiz(self, f, a, b, prec=0.001):
        '''Recebe uma f(x), 2 valores de x e a precisão desejada no cálculo. A partir dos valores de X é aplicado o método matemático da abscisão para retornar uma raíz de f entre eles'''
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
        '''Recebe uma lista/array dos coeficientes numéricos de um polinômio, ordenados de acordo com os seus expoentes, e retorna uma lista que corresponde à sua derivada'''
        novosCoeficientes = list(map(lambda coef, exp: coef*exp, coefOrdenados ,expOrdenados))
        return novosCoeficientes[1:] + [0]

    def integraPol(self, coefOrdenados, expOrdenados, k):
        '''Recebe uma lista/array dos coeficientes numéricos de um polinômio, ordenados de acordo com os seus expoentes, e retorna uma lista que corresponde à sua integral'''
        return [k] + list(map(lambda x, exp: x/exp, coefOrdenados[:-1], expOrdenados[1:]))
