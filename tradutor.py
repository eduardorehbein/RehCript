class Tradutor:
    
    def paraNumero(self, letra):
        return ord(letra)

    def paraLetra(self, inteiro):
        return chr(inteiro)

    def fraseParaNumeros(self, frase):
        palavras = frase.split()
        return [[self.paraNumero(letra) for letra in palavra] for palavra in palavras]
    
    def numerosParaFrase(self, matrizNumerica):
        matrizTraduzida = list(map(lambda palavra: list(map(lambda valor: self.paraLetra(valor), palavra)), matrizNumerica))
        matrizPalavras = list(map(lambda palavra: "".join(palavra), matrizTraduzida))
        frase = ""
        for i in range(len(matrizPalavras)):
            frase += matrizPalavras[i]
            if i < len(matrizPalavras) - 1:
                frase += " "
        return frase
