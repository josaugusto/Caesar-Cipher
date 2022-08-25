import PySimpleGUI as sg
from GUI import *

sg.theme('DarkBlue2')


layoutMenu = [ 
    [sg.Text('Bem-vindo ao programa de criptografia de Cifra de César\nPor favor selecione uma das duas opções a baixo')],
    [sg.Button('Criptografar', size=(15, 2), expand_x=True)],
    [sg.Button('Descriptografar', size=(15, 2), expand_x=True)]
]

layoutCriptografar = [
    [sg.Text('Informe a mensagem a ser Criptografada:')],
    [sg.Input(key='mensagem', size=(100, 100), expand_y=True)],
    [sg.Text('Informe a chave(0 a 25)'), sg.Input(key='chave', size=(2, 0)), sg.Checkbox('Direita'), sg.Checkbox('Esquerda')],
    [sg.Button('Codificar')],
    [sg.Text('Mensagem Descriptografada')],
    [sg.Input(size=(100, 100), expand_y=True)],
    [sg.Button('Voltar')]
]

layoutDescriptografar = []

def cria_interface():
    print()
