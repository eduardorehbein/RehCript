from rehcript import RehCript

msg = input("\nDigite sua mensagem: ")
lvl = input("Qual o nível de complexidade que você deseja no codificador? ")

rc = RehCript(int(lvl))
msgCodificada = rc.codifica(msg)

print("\nSua mensagem codificada:", msgCodificada)
print("\nTamanho da mensagem original:", len(msg), "caracteres")
print("Tamanho da mensagem codificada:", len(msgCodificada), "caracteres", "\n")

msgDecodificada = rc.decodifica(msgCodificada)

print("Mensagem decodificada:", msgDecodificada)

if msg == msgDecodificada:
    print("\nFunfa perfeitamente XDXD\n")
else:
    print("\nNão funfa\n")

# - Refatorar as classes e documentá-las melhor
# - Extrair os espaços/palavras/virgulas de dentro da classe ConversorDeBases
# - Mudar a parte que "Converte os valores decimais codificados em valores da base X" para ficar igual ao que acontece na func debaixo
# - Criar a classe chave pra representar a chave
# - Fazer espaços, separações e vírgulas se transformarem em valores da base X
