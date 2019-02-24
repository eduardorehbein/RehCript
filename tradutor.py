class Tradutor:
    
    def fraseParaNumeros(self, frase):
        palavras = frase.split()
        return [[ord(letra) for letra in palavra] for palavra in palavras]
    
    def numerosParaFrase(self, matrizNumerica):
        matrizTraduzida = list(map(lambda palavra: list(map(lambda valor: chr(valor), palavra)), matrizNumerica))
        matrizPalavras = list(map(lambda palavra: "".join(palavra), matrizTraduzida))
        frase = ""
        for i in range(len(matrizPalavras)):
            frase += matrizPalavras[i]
            if i < len(matrizPalavras) - 1:
                frase += " "
        return frase
