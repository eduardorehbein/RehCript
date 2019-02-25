from tradutor import Tradutor
from codificador import Codificador
from conversorDeBases import ConversorDeBases
from chave import Chave
from random import randint

class RehCript:
    
    def __init__(self, codLvl = 5, chave = None):
        if codLvl > 2:
            self.codLvl = codLvl
        else:
            self.codLvl = 3
        self.chave = chave
        self.tradutor = Tradutor()

    def caracteresEspeciais(self, conversor):
        return conversor.dicionarioDecBase[conversor.base], conversor.dicionarioDecBase[conversor.base + 1], conversor.dicionarioDecBase[conversor.base + 2]

    def codifica(self, msg):
        def condensaEmString(matriz, separacao, espaco, virgula):
            string = ""

            #iP = indice palavra, iC = indice caracter
            for iP in range(len(matriz)):
                for iC in range(len(matriz[iP])):
                    if type(matriz[iP][iC]) == tuple:
                        string += (matriz[iP][iC][0] + virgula + matriz[iP][iC][1])
                    else:
                        string += matriz[iP][iC]
                    if iC < len(matriz[iP]) - 1:
                        string += separacao
                if iP < len(matriz) - 1:
                    string += espaco
            
            return string
        
        #Traduz a mensagem numa matriz onde cada caracter passa a ser representado pelo seu valor Unicode
        matriz = self.tradutor.fraseParaNumeros(str(msg))

        if not self.chave:
            #Codifica os valores Unicode de acordo com a f(x) da classe e suas variações
            coder = Codificador(self.codLvl)

            #Cria o conversor e define caracteres de separação entre letras/espaçamento entre palavras/vírgula dos números reais de acordo com a base do conversor
            conversor = ConversorDeBases()
        else:
            coder = Codificador(self.chave.codLvl(), self.chave.coefs)
            conversor = ConversorDeBases(self.chave.base)

        separacao, espaco, virgula = self.caracteresEspeciais(conversor)
        res = ""

        if not self.chave:
            #Gera a chave da criptografia se ela não tiver sido pré definida pelo usuário e a coloca na mensagems
            chave = Chave(coder.coefs, conversor.base)
            res += chave.geraString() + espaco

        #Monta a matriz com os valores codificados
        matrizCod = list(map(lambda palavra: list(map(lambda valor: coder.codifica(valor), palavra)), matriz))
        
        #Converte os valores decimais codificados em valores da base X (iP = indice palavra, iV = indice valor)
        for iP in range(len(matrizCod)):
            for iV in range(len(matrizCod[iP])):
                if type(matrizCod[iP][iV]) == tuple: #[0] - parte inteira, [1] - parte decimal
                    matrizCod[iP][iV] = (conversor.decParaBaseX(matrizCod[iP][iV][0]), conversor.decParaBaseX(matrizCod[iP][iV][1])) 
                else:
                    matrizCod[iP][iV] = conversor.decParaBaseX(matrizCod[iP][iV])
        
        return res + condensaEmString(matrizCod, separacao, espaco, virgula)

    def decodifica(self, msg):
        #Cria o coder, o conversor e extrai a mensagem limpa baseados na chave
        chave = self.chave
        msgLimpa = msg

        if not chave:
            chave = Chave()
            msgLimpa = chave.extraiDados(msg)
        
        coder = Codificador(chave.codLvl(), chave.coefs)
        conversor = ConversorDeBases(chave.base)

        #Separa a mensagem em palavras codificadas
        separacao, espaco, virgula = self.caracteresEspeciais(conversor)
        palavras = msgLimpa.split(espaco)

        #Separa as palavras em caracteres codificados
        matrizCod = list(map(lambda palavra: palavra.split(separacao), palavras))
    
        #Coloca os valores da matriz na base decimal (iP = indice palavra, iC = indice caracter)
        for iP in range(len(matrizCod)):
            for iC in range(len(matrizCod[iP])):
                if virgula in matrizCod[iP][iC]:
                    valorQuebrado = matrizCod[iP][iC].split(virgula) #valorQuebrado[0] - parte inteira, valorQuebrado[1] - parte decimal
                    matrizCod[iP][iC] = (conversor.baseXParaDec(valorQuebrado[0]), conversor.baseXParaDec(valorQuebrado[1])) 
                else:
                    matrizCod[iP][iC] = conversor.baseXParaDec(matrizCod[iP][iC])

        #Decodifica os valores em valores da tabela Unicode
        matrizUnicode = list(map(lambda palavra: list(map(lambda valor: coder.decodifica(valor), palavra)), matrizCod))
        
        return self.tradutor.matrizParaFrase(matrizUnicode)
