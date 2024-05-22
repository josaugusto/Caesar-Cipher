alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    
def novo_alfabeto(chave, deslocamento):
    if deslocamento == 'D':
        letras_deslocadas = alfabeto[-chave::1]
        alfabeto_deslocado = letras_deslocadas + alfabeto[0:26-chave]    
    else:
        letras_deslocadas = alfabeto[0:chave]
        alfabeto_deslocado = alfabeto[chave::] + letras_deslocadas
    return alfabeto_deslocado

def criptografar(mensagem, chave, deslocamento):
    alfabeto_deslocado = novo_alfabeto(chave, deslocamento)
    mensagem_criptografada = ""

    for j in range(0, len(mensagem)):
        for i in range(0, 26):
            if mensagem[j].upper() == alfabeto[i]:
                if mensagem[j].isupper():
                    mensagem_criptografada+=alfabeto_deslocado[i]
                else:
                    mensagem_criptografada+=alfabeto_deslocado[i].lower()
        if mensagem[j] == ' ' or mensagem[j] == '\n': mensagem_criptografada+=mensagem[j]
    return mensagem_criptografada

def descriptografar(mensagem_cifrada, chave, deslocamento):
    alfabeto_deslocado = novo_alfabeto(chave, deslocamento)
    mensagem_descriptografada = ""
    
    for j in range(0, len(mensagem_cifrada)):
        for i in range(0, 26):
            if mensagem_cifrada[j].upper() == alfabeto_deslocado[i]:
                if mensagem_cifrada[j].isupper():
                    mensagem_descriptografada+=alfabeto[i]
                else:
                    mensagem_descriptografada+=alfabeto[i].lower()
        if mensagem_cifrada[j] == ' ' or mensagem_cifrada[j] == '\n': mensagem_descriptografada+=mensagem_cifrada[j]
    return mensagem_descriptografada

def criptoanalise(mensagem_cifrada):
    for k in range(0, 26):
        print(f"Chave: {k} Esquerda:\n{descriptografar(mensagem_cifrada, k, 'E')}")
        print(f"Chave: {k} Direita:\n{descriptografar(mensagem_cifrada, k, 'D')}")
