from conversorDeBases import ConversorDeBases
from random import randint

class Chave:
    def __init__(self, coefs = None, base = None):
        self.coefs = coefs
        self.base = base

    def codLvl(self):
        return len(self.coefs)

    def eNumero(self, a):
        if a == "0" or a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9":
            return True
        return False

    def geraString(self):
        if self.coefs == None or self.base == None:
            print("A chave não foi construida corretamente")
            return None

        conversor = ConversorDeBases(self.base)

        def addLetra(string = ""):
            novaString = string
            novaString += conversor.dicionarioDecBase[randint(10, conversor.base - 3)]
            return novaString

        def addNumero(string, contador):
            novaString = string
            novaString += str(self.coefs[contador])
            return addLetra(novaString)

        string = addLetra()
        string += str(len(self.coefs))
        contadorCoefs = 0
        letrasEmSeq = 0
        n = randint(1, 3)
        while contadorCoefs < len(self.coefs):
            if (n == 1 and not(self.eNumero(string[-1]))) or letrasEmSeq > 3:
                string = addNumero(string, contadorCoefs)
                contadorCoefs += 1
                letrasEmSeq = 0
            else:
                string = addLetra(string)
                letrasEmSeq += 1
            n = randint(1, 3)
        string = addLetra(string)
        string += str(conversor.base)

        return string

    def extraiDados(self, msg):
        def pulaLetras(msg, contador):
            novoContador = contador
            while not self.eNumero(msg[novoContador]):
                novoContador += 1
            return novoContador

        nCoefs = ""
        coefs = []
        contador = 0

        contador = pulaLetras(msg, contador)
        while self.eNumero(msg[contador]):
            nCoefs += msg[contador]
            contador += 1
        while len(coefs) < int(nCoefs):
            if self.eNumero(msg[contador]):
                novoCoef = ""
                while self.eNumero(msg[contador]):
                    novoCoef += msg[contador]
                    contador += 1
                coefs.append(int(novoCoef))
            else:
                contador = pulaLetras(msg, contador)

        contador = pulaLetras(msg, contador)
        base = msg[contador] + msg[contador + 1] #Porque a base é entre 20 e 59
        contador += 3 #Pula a base e o espaço

        self.base = int(base)
        self.coefs = coefs

        return msg[contador:]
