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


def criptografar():

    mensagem = input("Mensagem(Apenas letras e sem acentos): ").strip()
    chave, deslocamento = input("Chave(0 a 25) e deslocamento(D - Direita e E - Esquerda): ").strip().upper().split()
    chave = int(chave)
    
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


def decodificar():

    cifra = input("Mensagem criptografada: ").strip()
    chave, deslocamento = input("Chave(0 a 25) e deslocamento(D - Direita e E - Esquerda): ").strip().upper().split()
    chave = int(chave)

    alfabetodeslocado = novoalfabeto(chave, deslocamento)
    mensagemDescriptografada = ""
    tamanho = len(cifra)

    for j in range(0, tamanho):
        for i in range(0, 26):
            if cifra[j].upper() == alfabetodeslocado[i]:
                if cifra[j].isupper():
                    mensagemDescriptografada+=alfabeto[i]
                else:
                    mensagemDescriptografada+=alfabeto[i].lower()
        if cifra[j] == ' ': mensagemDescriptografada+=cifra[j]

    return mensagemDescriptografada


def main():

    while True:
        print("Escolha uma das opções abaixo: ")
        print("[0] - Criptografar\n[1] - Decodificar\n[2] - Sair do programa")
        op = input("-> ")
        if op == '0':
            print(f"Mensagem criptografada: {criptografar()}")
        elif op == '1':
            print(f"Mensagem descriptografada: {decodificar()}")
        else: break

main()
