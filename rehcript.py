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
        #Traduz a mensagem numa matriz onde cada caracter passa a ser representado pelo seu valor Unicode
        matriz = self.tradutor.fraseParaNumeros(str(msg))

        #Codifica os valores Unicode de acordo com a f(x) = a*x**n + b*x**(n-1) + ... + c*x**0
        coder = Codificador(self.codLvl)

        #Gera a chave da criptografia
        chave = 0
        for i in range(len(coder.coefs)):
            chave += coder.coefs[-(i + 1)]*(10 ** i)

        #Monta a matriz com os valores codificados
        matrizCod = list(map(lambda palavra: list(map(lambda valor: coder.codificaEmDecimal(valor), palavra)), matriz))
        
        #Converte os valores decimais codificados em valores da base 32
        for iP in range(len(matrizCod)):
            for iV in range(len(matrizCod[iP])):
                if type(matrizCod[iP][iV]) == tuple:
                    matrizCod[iP][iV] = (self.c32.decParaBase32(matrizCod[iP][iV][0]), self.c32.decParaBase32(matrizCod[iP][iV][1]))
                else:
                    matrizCod[iP][iV] = self.c32.decParaBase32(matrizCod[iP][iV])
        
        #Condensa o valor final em uma string, w -> separa caracter, x -> separa palavra, y -> separa a parte inteira da decimal (talvez fazer isso variar no codificador futuraente)
        string = ""
        for valor32 in self.c32.decParaBase32(chave):
            string += str(valor32)
        string += "x"
        for palavra in range(len(matrizCod)):
            for caracter in range(len(matrizCod[palavra])):
                if type(matrizCod[palavra][caracter]) == tuple:
                    string += (matrizCod[palavra][caracter][0] + "y" + matrizCod[palavra][caracter][1])
                else:
                    string += matrizCod[palavra][caracter]
                if caracter < len(matrizCod[palavra]) - 1:
                    string += "w"
            if palavra < len(matrizCod) - 1:
                string += "x"
        
        return string

    def decodifica(self, msg):
        #Separa a mensagem em palavras
        palavras = msg.split("x")

        #Cria o coder usando a chave
        chave = self.c32.base32ParaDec(palavras[0])
        coefs = [int(x) for x in str(chave)]
        coder = Codificador(len(coefs), coefs)

        #Monta uma matriz separando cada grupo que representa um valor decimal numa outra base
        palavras.remove(palavras[0])
        matrizCod32 = list(map(lambda palavra: palavra.split("w"), palavras))
    
        #Monta a matriz com os códigos na base decimal
        matrizCodDec = list()
        for palavra in matrizCod32:
            novaPalavra = list()
            for caracter in palavra:
                if "y" in caracter:
                    valorQuebrado = caracter.split("y")
                    novaPalavra.append((self.c32.base32ParaDec(valorQuebrado[0]), self.c32.base32ParaDec(valorQuebrado[1])))
                else:
                    novaPalavra.append(self.c32.base32ParaDec(caracter))
            matrizCodDec.append(novaPalavra)

        #Decodifica os valores em valores da tabela Unicode
        matrizUnicode = list(map(lambda palavra: list(map(lambda valor: coder.decodificaEmUnicode(valor), palavra)), matrizCodDec))
        
        return self.tradutor.numerosParaFrase(matrizUnicode)
