# -*- coding: UTF-8 -*-

import getpass
import os
import time

#print('╝╠║═╣╗╔╚') MAPA de CARACTERES DO WINDOWS


def menu():
    print('╔════════════════════════╗')
    print('║          MENU          ║')
    print('╠════════════════════════╣')
    print('║',' '*22,'║')
    print('║ 1 - Login              ║')
    print('║ 2 - Cadastro           ║')
    print('║ 0 - Sair               ║')
    print('║',' '*22,'║')
    print('╚════════════════════════╝')

def cadastro():
    nome = str(input("Digite Seu Nome: "))# pylint: disable=unused-variable
    idade = int(input("Digite Sua Idade: "))
    print(f"Você tem {idade} anos!")
    email = input("Digite um e-mail válido: ")
    with open('dados.txt') as f_obj:
        contents = f_obj.read()

    items = contents.split()

    if email in items:
        # VERIFICA e FAZ VOLTAR PARA O MENU
        os.system('cls')
        for i in range(5,0,-1):
            print('E-mail já cadastrado, por favor faça o login!')
            print("Voltando para o MENU em : ", i)
            time.sleep(1)     # Lib import time ( Serve para Dar um Tempo no Console antes de limpar a tela ) 
            os.system("cls")  # Lib import os   ( Serve para limpar o DOS // CMD )
        login_or_register()   # Chama a FUNÇAO principal
        
    else:
        print()
        confirmar = input("Seu e-mail " + email + " está correto? ")
        if confirmar == "não":
                email = input("Digite novamente seu e-mail: ")
        senha = getpass.getpass("Digite sua senha: ")

        banco = open("dados.txt", "a")
        banco.write(email + "\n")
        banco.write(senha + "\n")
        banco.close()

#LOGIN
def login():
    email = str(input("Informe seu e-mail: "))
    senha = getpass.getpass("Informe sua senha: ")

    with open('dados.txt') as f_obj:
        contents = f_obj.read()

    items = contents.split()

    if email and senha in items:
        print('E-mail já cadastrado')
    else:
        print("Algo está errado, verifique e tente novamente.")
        login()

#print('╝╠║═╣╗╔╚')

def login_or_register():
    os.system('cls')
    menu()
    print()
    info_menu = str.upper(input(' Opção: '))
    if info_menu == "LOGIN" or info_menu == "1":
        os.system('cls')
        login()
    elif info_menu == "CADASTRO" or info_menu == "2":
        os.system('cls')
        cadastro()
    elif info_menu == "SAIR" or info_menu == "0":
        os.system('cls')
        exit # Funçao Nativa do Python para ( Força o Fechamento do Programa )
    elif info_menu == "":
        os.system('cls')
        for i in range(5,0,-1):
            print("Informaçao errada!")
            print("Voltando para o MENU em : ", i)
            time.sleep(1)     #Lib import time ( Serve para Dar um Tempo no Console antes de limpar a tela ) 
            os.system("cls")  #Lib import os   ( Serve para limpar o DOS // CMD )
        print()
        login_or_register()   # Chama a FUNÇAO principal


login_or_register()