alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 26 letras


def novoalfabeto(key, displacement):

    letrasdeslocadas = [] 
    alfabetodeslocado = []
    if displacement == 'D':
        for i in range(-key, 0, 1):
            letrasdeslocadas.append(alfabeto[i])
        alfabetodeslocado = letrasdeslocadas + alfabeto[0:26-key]    
    else:
        for i in range(key-key, key):
            letrasdeslocadas.append(alfabeto[i])
        alfabetodeslocado = alfabeto[key::] + letrasdeslocadas
        
    return alfabetodeslocado


def criptografar(mensagem, chave, deslocamento):
    alfabetodeslocado = novoalfabeto(chave, deslocamento)
    mensagemCriptografada = ""
    tamanho = len(mensagem)

    for j in range(0, tamanho):
        for i in range(0, 26):
            if mensagem[j].upper() == alfabeto[i]:
                if mensagem[j].isupper():
                    mensagemCriptografada+=alfabetodeslocado[i]
                else:
                    mensagemCriptografada+=alfabetodeslocado[i].lower()
        if mensagem[j] == ' ': mensagemCriptografada+=mensagem[j]

    return mensagemCriptografada


def decodificar(mensagemCifrada, chave, deslocamento):
    alfabetodeslocado = novoalfabeto(chave, deslocamento)
    mensagemDescriptografada = ""
    tamanho = len(mensagemCifrada)

    for j in range(0, tamanho):
        for i in range(0, 26):
            if mensagemCifrada[j].upper() == alfabetodeslocado[i]:
                if mensagemCifrada[j].isupper():
                    mensagemDescriptografada+=alfabeto[i]
                else:
                    mensagemDescriptografada+=alfabeto[i].lower()
        if mensagemCifrada[j] == ' ': mensagemDescriptografada+=mensagemCifrada[j]

    return mensagemDescriptografada


def criptoanalise(mensagemCifrada):
    for k in range(0, 26):
        print(f"Chave: {k} e Deslocamento: {'D'} = {decodificar(mensagemCifrada, k, 'D')}", end=' | ')
        print(f"Chave: {k} e Deslocamento: {'E'} = {decodificar(mensagemCifrada, k, 'E')}")


def main():

    while True:
        print("Escolha uma das opções abaixo: ")
        print("[0] - Criptografar\n[1] - Decodificar\n[2] - Criptoanálise\n[3] - Sair do programa")
        op = input("-> ")
        if op == '0':
            mensagem = input("Mensagem(Apenas letras e sem acentos): ").strip()
            chave, deslocamento = input("Chave(0 a 25) e deslocamento(D - Direita e E - Esquerda): ").strip().upper().split()
            chave = int(chave)
            print(f"Mensagem criptografada: {criptografar(mensagem, chave, deslocamento)}")
        elif op == '1':
            mensagemCifrada = input("Mensagem criptografada: ").strip()
            chave, deslocamento = input("Chave(0 a 25) e deslocamento(D - Direita e E - Esquerda): ").strip().upper().split()
            chave = int(chave)
            print(f"Mensagem descriptografada: {decodificar(mensagemCifrada, chave, deslocamento)}")
        elif op == '2':
            mensagemCifrada = input("Mensagem criptografada: ").strip()
            criptoanalise(mensagemCifrada)
        elif op == '3': 
            break
main()

