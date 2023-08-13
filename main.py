alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 


def novoalfabeto(chave, deslocamento):
    letrasdeslocadas = [] 
    alfabetodeslocado = []
    
    if deslocamento == 'D':
        for i in range(-chave, 0, 1):
            letrasdeslocadas.append(alfabeto[i])
        alfabetodeslocado = letrasdeslocadas + alfabeto[0:26-chave]    
    else:
        for i in range(0, chave):
            letrasdeslocadas.append(alfabeto[i])
        alfabetodeslocado = alfabeto[chave::] + letrasdeslocadas
        
    return alfabetodeslocado


def criptografar(mensagem, chave, deslocamento):
    alfabetodeslocado = novoalfabeto(chave, deslocamento)
    mensagemCriptografada = ""

    for j in range(0, len(mensagem)):
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

    for j in range(0, len(mensagemCifrada)):
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
        print(f"Chave: {k} Esquerda:\n{descriptografar(mensagemCifrada, k, 'E')}")
        print(f"Chave: {k} Direita:\n{descriptografar(mensagemCifrada, k, 'D')}")
