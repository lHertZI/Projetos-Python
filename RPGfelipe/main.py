from personagem import Personagem
import cadastro
import os
def menu():
    print('╔════════════════════════╗')
    print('║          MENU          ║')
    print('╠════════════════════════╣')
    print('║',' '*22,'║')
    print('║ 1 - Warrior            ║')
    print('║ 2 - Archer             ║')
    print('║ 3 - Wizard             ║')
    print('║ 0 - Sair               ║')
    print('║',' '*22,'║')
    print('╚════════════════════════╝')
menu()
character = input("Qual Classe Você Deseja? ")
personagem = Personagem()
if character == "1":
   os.system('cls')
   personagem.warrior()
   print("Caracteristicas Warrior: ")
   print("Vida:", personagem.health)
   print("Ataque:", personagem.attack)
   print("Mobilidade:", personagem.mobility)
   print("Dinheiro:", personagem.coin)
   

elif character == "2":
   os.system('cls')
   personagem.archer()
   print("Caracteristicas Archer: ")
   print("Vida:", personagem.health)
   print("Ataque:", personagem.attack)
   print("Mobilidade:", personagem.mobility)
   print("Dinheiro:", personagem.coin)
    
elif character == "3":
   os.system('cls')
   personagem.wizard()
   print("Caracteristicas Wizard: ")
   print("Vida:", personagem.health)
   print("Ataque:", personagem.attack)
   print("Mobilidade:", personagem.mobility)
   print("Dinheiro:", personagem.coin)

elif character == "0":
    print("Tchau!")
    exit