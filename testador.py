from rehcript import RehCript

msg = input("Digite sua mensagem: ")
lvl = input("Qual o nível de complexidade que você deseja no codificador? ")

rc = RehCript(int(lvl))
msgCodificada = rc.codifica(msg)

print(msgCodificada, "\n")
print("Tamanho da mensagem original:", len(msg), "caracteres")
print("Tamanho da mensagem codificada:", len(msgCodificada), "caracteres", "\n")

msgDecodificada = rc.decodifica(msgCodificada)

print("Mensagem decodificada:", msgDecodificada)

# - Adicionar derivação e integração
# - Mascarar os coeficientes da chave usando valores aleatórios 0-31 juntamente com o 
# dicionário da base 32, tudo isso para que espaços entre letras e palavras possam ser usados como valores 
# Unicode, sendo eles 0 e 1
