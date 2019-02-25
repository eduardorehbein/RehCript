class Conversor32:
    '''Converte valores dentre as bases Decimal, Binária e 32'''
    
    def __init__(self):
        self.dicionarioBaseDec = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15, "g":16, "h":17, "i":18, "j":19, "k":20, "l":21, "m":22, "n":23, "o":24, "p":25, "q":26, "r":27, "s":28, "t":29, "u":30, "v":31}
        self.dicionarioDecBase = dict((v,c) for c, v in self.dicionarioBaseDec.items())

    def decParaBase32(self, valor):
        '''Transforma um número de base decimal positivo em um valor da base 32'''
        if valor < 0:
            raise ValueError("Esta função não trabalha com valores negativos")
        elif valor == 0:
            return [0]
        else:
            res = list()
            while valor > 0:
                res.append(self.dicionarioDecBase[valor % 32])
                valor = valor // 32
            res.reverse()
            
            return "".join(res)

    def base32ParaDec(self, valor):
        res = 0
        listValor = list(valor)
        listValor.reverse()
        for i in range(len(listValor)):
            res += self.dicionarioBaseDec[listValor[i]]*(32 ** i)
        return res
