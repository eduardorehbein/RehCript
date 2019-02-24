class Conversor32:
    '''Converte valores dentre as bases Decimal, Binária e 32'''
    
    def transformaParaLetra32(self, array):
        '''Transforma um array de 5 bits em um valor da base 32'''
        if array == [0, 0, 0, 0, 0]:
            return 0
        elif array == [0, 0, 0, 0, 1]:
            return 1
        elif array == [0, 0, 0, 1, 0]:
            return 2
        elif array == [0, 0, 0, 1, 1]:
            return 3
        elif array == [0, 0, 1, 0, 0]:
            return 4
        elif array == [0, 0, 1, 0, 1]:
            return 5
        elif array == [0, 0, 1, 1, 0]:
            return 6
        elif array == [0, 0, 1, 1, 1]:
            return 7
        elif array == [0, 1, 0, 0, 0]:
            return 8
        elif array == [0, 1, 0, 0, 1]:
            return 9
        elif array == [0, 1, 0, 1, 0]:
            return "a"
        elif array == [0, 1, 0, 1, 1]:
            return "b"
        elif array == [0, 1, 1, 0, 0]:
            return "c"
        elif array == [0, 1, 1, 0, 1]:
            return "d"
        elif array == [0, 1, 1, 1, 0]:
            return "e"
        elif array == [0, 1, 1, 1, 1]:
            return "f"
        elif array == [1, 0, 0, 0, 0]:
            return "g"
        elif array == [1, 0, 0, 0, 1]:
            return "h"
        elif array == [1, 0, 0, 1, 0]:
            return "i"
        elif array == [1, 0, 0, 1, 1]:
            return "j"
        elif array == [1, 0, 1, 0, 0]:
            return "k"
        elif array == [1, 0, 1, 0, 1]:
            return "l"
        elif array == [1, 0, 1, 1, 0]:
            return "m"
        elif array == [1, 0, 1, 1, 1]:
            return "n"
        elif array == [1, 1, 0, 0, 0]:
            return "o"
        elif array == [1, 1, 0, 0, 1]:
            return "p"
        elif array == [1, 1, 0, 1, 0]:
            return "q"
        elif array == [1, 1, 0, 1, 1]:
            return "r"
        elif array == [1, 1, 1, 0, 0]:
            return "s"
        elif array == [1, 1, 1, 0, 1]:
            return "t"
        elif array == [1, 1, 1, 1, 0]:
            return "u"
        elif array == [1, 1, 1, 1, 1]:
            return "v"
        else:
            raise ValueError("O valor de entrada não é um array com 5 bits")

    def binParaBase32(self, arrayBin):
        '''Transforma um array que representa um valor da base binária em um array da base 32'''
        while len(arrayBin) % 5 != 0:
            arrayBin.insert(0, 0)

        res = list()
        grupo = list()
        contador = 0
        for i in range(len(arrayBin)):
            grupo.append(arrayBin[i]) 
            if contador == 4:
                res.append(self.transformaParaLetra32(grupo))
                grupo.clear()
                contador = 0
            else:
                contador += 1

        return res

    def decParaBin(self, valor):
        '''Transforma um número positivo em um array que representa um valor binário'''
        if valor < 0:
            raise ValueError("Esta função não trabalha com valores negativos")
        elif valor == 0:
            return [0]
        else:
            res = list()
            while valor > 0:
                res.append(valor % 2)
                valor = valor // 2
            res.reverse()
            
            return res
    
    def decParaBase32(self, valor):
        '''Recebe um valor decimal e retorna um array que representa esse valor na base 32'''
        return self.binParaBase32(self.decParaBin(valor))

    def base32ParaDec(self, valor):
        dicionario = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15, "g":16, "h":17, "i":18, "j":19, "k":20, "l":21, "m":22, "n":23, "o":24, "p":25, "q":26, "r":27, "s":28, "t":29, "u":30, "v":31}
        res = 0
        listValor = list(valor)
        listValor.reverse()
        for i in range(len(listValor)):
            res += dicionario[listValor[i]]*(32 ** i)
        return res
