from tradutor import Tradutor
from codificador import Codificador
from conversorDeBases import ConversorDeBases
from random import randint

class RehCript:
    
    def __init__(self, codLvl = 5):
        if codLvl > 2:
            self.codLvl = codLvl
        else:
            self.codLvl = 3
        self.tradutor = Tradutor()

    def eNumero(self, a):
        if a == "0" or a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9":
            return True
        return False

    def codifica(self, msg):
        def geraChave(codificador):
            def addLetra(chave = ""):
                novaChave = chave
                novaChave += conversor.dicionarioDecBase[randint(10, conversor.base - 3)]
                return novaChave

            def addNumero(chave, codificador, contador):
                novaChave = chave
                novaChave += str(codificador.coefs[contador])
                return addLetra(novaChave)

            chave = addLetra()
            chave += str(len(codificador.coefs))
            contadorCoefs = 0
            letrasEmSeq = 0
            n = randint(1, 3)
            while contadorCoefs < len(codificador.coefs):
                if (n == 1 and not(self.eNumero(chave[-1]))) or letrasEmSeq > 3:
                    chave = addNumero(chave, coder, contadorCoefs)
                    contadorCoefs += 1
                    letrasEmSeq = 0
                else:
                    chave = addLetra(chave)
                    letrasEmSeq += 1
                n = randint(1, 3)
            chave = addLetra(chave)
            chave += str(conversor.base)

            return chave

        #Traduz a mensagem numa matriz onde cada caracter passa a ser representado pelo seu valor Unicode
        matriz = self.tradutor.fraseParaNumeros(str(msg))

        #Codifica os valores Unicode de acordo com a f(x) = a*x**n + b*x**(n-1) + ... + c*x**0
        coder = Codificador(self.codLvl)
        conversor = ConversorDeBases()

        #Gera a chave da criptografia
        chave = geraChave(coder)

        #Monta a matriz com os valores codificados
        matrizCod = list(map(lambda palavra: list(map(lambda valor: coder.codificaEmDecimal(valor), palavra)), matriz))
        
        #Converte os valores decimais codificados em valores da base X
        for iP in range(len(matrizCod)):
            for iV in range(len(matrizCod[iP])):
                if type(matrizCod[iP][iV]) == tuple:
                    matrizCod[iP][iV] = (conversor.decParaBaseX(matrizCod[iP][iV][0]), conversor.decParaBaseX(matrizCod[iP][iV][1]))
                else:
                    matrizCod[iP][iV] = conversor.decParaBaseX(matrizCod[iP][iV])
        
        #Condensa o valor final em uma string
        string = chave
        string += conversor.espaco
        for palavra in range(len(matrizCod)):
            for caracter in range(len(matrizCod[palavra])):
                if type(matrizCod[palavra][caracter]) == tuple:
                    string += (matrizCod[palavra][caracter][0] + conversor.virgula + matrizCod[palavra][caracter][1])
                else:
                    string += matrizCod[palavra][caracter]
                if caracter < len(matrizCod[palavra]) - 1:
                    string += conversor.separacao
            if palavra < len(matrizCod) - 1:
                string += conversor.espaco
        
        return string

    def decodifica(self, msg):
        def processaChave(msg):
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
            base = msg[contador] + msg[contador + 1]
            contador += 3 #Pula a base e o espaço

            return int(nCoefs), coefs, int(base), msg[contador:]

        #Cria o coder, o conversor e tira a chave da mensagem
        nCoefs, coefs, base, msgLimpa = processaChave(msg)
        coder = Codificador(nCoefs, coefs)
        conversor = ConversorDeBases(base)
        palavras = msgLimpa.split(conversor.espaco)

        #Monta uma matriz separando cada grupo que representa um valor decimal numa outra base
        matrizCod32 = list(map(lambda palavra: palavra.split(conversor.separacao), palavras))
    
        #Monta a matriz com os códigos na base decimal
        matrizCodDec = list()
        for palavra in matrizCod32:
            novaPalavra = list()
            for caracter in palavra:
                if conversor.virgula in caracter:
                    valorQuebrado = caracter.split(conversor.virgula)
                    novaPalavra.append((conversor.baseXParaDec(valorQuebrado[0]), conversor.baseXParaDec(valorQuebrado[1])))
                else:
                    novaPalavra.append(conversor.baseXParaDec(caracter))
            matrizCodDec.append(novaPalavra)

        #Decodifica os valores em valores da tabela Unicode
        matrizUnicode = list(map(lambda palavra: list(map(lambda valor: coder.decodificaEmUnicode(valor), palavra)), matrizCodDec))
        
        return self.tradutor.numerosParaFrase(matrizUnicode)
