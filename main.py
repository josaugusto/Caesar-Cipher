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
        if mensagem[j] == ' ' or mensagem[j] == '\n': mensagemCriptografada+=mensagem[j]

    return mensagemCriptografada


def descriptografar(mensagemCifrada, chave, deslocamento):
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
        if mensagemCifrada[j] == ' ' or mensagemCifrada[j] == '\n': mensagemDescriptografada+=mensagemCifrada[j]

    return mensagemDescriptografada


def criptoanálise(mensagemCifrada):
    for k in range(0, 26):
        print(f"Chave: {k} e Deslocamento: {'D'}:\n{descriptografar(mensagemCifrada, k, 'D')}")
        print(f"Chave: {k} e Deslocamento: {'E'}:\n{descriptografar(mensagemCifrada, k, 'E')}")
