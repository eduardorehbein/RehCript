class Tradutor:
    '''Faz a tradução entre valores decimais e caracteres baseado na tabela Unicode'''
    
    def paraNumero(self, letra):
        '''Recebe um caracter e retorna o valor decimal correspondente da tabela Unicode'''
        return ord(letra)

    def paraLetra(self, inteiro):
        '''Recebe um valor decimal e retorna o caracter correspondente da tabela Unicode'''
        return chr(inteiro)

    def fraseParaNumeros(self, frase):
        '''Recebe uma string e retorna uma matriz de caracteres em seus respectivos valores decimais baseados na Unicode'''
        palavras = frase.split()
        return [[self.paraNumero(letra) for letra in palavra] for palavra in palavras]
    
    def matrizParaFrase(self, matrizNumerica):
        '''Recebe uma matriz de caracteres em seus valores decimais tabelados na Unicode e retorna uma string que representa a frase completa'''
        matrizTraduzida = list(map(lambda palavra: list(map(lambda valor: self.paraLetra(valor), palavra)), matrizNumerica))
        matrizPalavras = list(map(lambda palavra: "".join(palavra), matrizTraduzida))
        frase = ""
        for i in range(len(matrizPalavras)):
            frase += matrizPalavras[i]
            if i < len(matrizPalavras) - 1:
                frase += " "
        return frase
