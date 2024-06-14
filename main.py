alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 


def novo_alfabeto(chave, deslocamento):
    if deslocamento == 'D':
        chave = -chave
    return alfabeto[chave:] + alfabeto[:chave]

def aux_cripto_descripto(mensagem, alfabeto, alfabeto_deslocado):
    for j in range(0, len(mensagem)):
        for i in range(0, 26):
            if mensagem[j].upper() == alfabeto[i]:
                if mensagem[j].isupper():
                    mensagem_processada+=alfabeto_deslocado[i]
                else:
                    mensagem_processada+=alfabeto_deslocado[i].lower()
        if mensagem[j] == ' ' or mensagem[j] == '\n': mensagem_processada+=mensagem[j]
    return mensagem_processada

def criptografar(mensagem, chave, deslocamento):
    alfabeto_deslocado = novo_alfabeto(chave, deslocamento)

    return aux_cripto_descripto(mensagem, alfabeto, alfabeto_deslocado);

def descriptografar(mensagem_cifrada, chave, deslocamento):
    alfabeto_deslocado = novo_alfabeto(chave, deslocamento)
    
    return aux_cripto_descripto(mensagem_cifrada, alfabeto_deslocado, alfabeto)

def criptoanalise(mensagem_cifrada):
    for k in range(0, 26):
        print(f"Chave: {k} Esquerda:\n{descriptografar(mensagem_cifrada, k, 'E')}")
        print(f"Chave: {k} Direita:\n{descriptografar(mensagem_cifrada, k, 'D')}")
