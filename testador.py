from rehcript import RehCript
from chave import Chave

msg = input("\nDigite sua mensagem: ")
lvl = input("Qual o nível de complexidade que você deseja no codificador? ")

print("\n---------- Teste sem a chave pré definida ----------\n")

rc = RehCript(int(lvl))
msgCodificada = rc.codifica(msg)

print("Sua mensagem codificada:", msgCodificada)
print("\nTamanho da mensagem original:", len(msg), "caracteres")
print("Tamanho da mensagem codificada:", len(msgCodificada), "caracteres\n")

msgDecodificada = rc.decodifica(msgCodificada)

print("Mensagem decodificada:", msgDecodificada)

if msg == msgDecodificada:
    print("\nFunfa perfeitamente XDXD")
else:
    print("\nNão funfa")

print("\n---------- Teste com a chave pré definida ----------\n")

chave = Chave(list(range(int(lvl))), 59)

print("chave.gerastring() ->", chave.geraString())

rc = RehCript(chave.codLvl(), chave)
msgCodificada = rc.codifica(msg)

print("\nSua mensagem codificada:", msgCodificada)
print("\nTamanho da mensagem original:", len(msg), "caracteres")
print("Tamanho da mensagem codificada:", len(msgCodificada), "caracteres\n")

msgDecodificada = rc.decodifica(msgCodificada)

print("Mensagem decodificada:", msgDecodificada)

if msg == msgDecodificada:
    print("\nFunfa perfeitamente XDXD\n")
else:
    print("\nNão funfa\n")

# - Refatorar as classes e documentá-las melhor
# - Remover os exp ordenados da jogada
# - Fazer uma classe que converte arquivos com a criptografia
# - Fazer espaços, separações e vírgulas se transformarem em valores da base X
