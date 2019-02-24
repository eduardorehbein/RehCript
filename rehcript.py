from tradutor import Tradutor
from codificador import Codificador
from conversor32 import Conversor32

class RehCript:
    
    def __init__(self, codLvl = 5):
        if codLvl > 2:
            self.codLvl = codLvl
        else:
            self.codLvl = 3
        self.tradutor = Tradutor()
        self.c32 = Conversor32()

    def codifica(self, msg):
        #Traduz a mensagem numa matriz onde cada caracter passa a ser representado pelo seu valor unicode
        matriz = self.tradutor.fraseParaNumeros(msg)

        #Codifica os valores unicode de acordo com a f(x) = a*x**n + b*x**(n-1) + ... + c*x**0
        coder = Codificador(self.codLvl)
        matrizCodDec = list(map(lambda palavra: list(map(lambda valor: coder.codificaEmDecimal(valor), palavra)), matriz))
        
        #Converte os valores decimais codificados em valores da base 32
        matrizCod32 = list(map(lambda palavra: list(map(lambda valor: self.c32.decParaBase32(valor), palavra)), matrizCodDec))

        #Gera a chave da criptografia
        chave = 0
        for i in range(len(coder.coefs)):
            chave += coder.coefs[-(i + 1)]*(10 ** i)
        
        #Condensa o valor final em uma string, w -> separa caracter, x -> separa palavra (talvez fazer isso variar no codificador futuraente)
        string = ""
        for valor32 in self.c32.decParaBase32(chave):
            string += str(valor32)
        string += "x"
        for palavra in range(len(matrizCod32)):
            for caracter in range(len(matrizCod32[palavra])):
                for valor in range(len(matrizCod32[palavra][caracter])):
                    string += str(matrizCod32[palavra][caracter][valor])
                if caracter < len(matrizCod32[palavra]) - 1:
                    string += "w"
            if palavra < len(matrizCod32) - 1:
                string += "x"
        
        return string

    def decodifica(self, msg):
        palavras = msg.split("x")

        chave = self.c32.base32ParaDec(palavras[0])
        coefs = [int(x) for x in str(chave)]
        coder = Codificador(len(coefs), coefs)

        palavras.remove(palavras[0])
        matrizCod32 = list(map(lambda palavra: palavra.split("w"), palavras))
        matrizCodDec = list(map(lambda palavra: list(map(lambda valor: self.c32.base32ParaDec(valor), palavra)), matrizCod32))
        matrizUnicode = list(map(lambda palavra: list(map(lambda valor: coder.decodificaEmUnicode(valor), palavra)), matrizCodDec))
        
        return self.tradutor.numerosParaFrase(matrizUnicode)
