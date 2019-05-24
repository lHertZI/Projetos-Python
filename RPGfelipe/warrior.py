import IA
from main import personagem
import jsonpickle
from random import randint

go = True
lojafechada = False
punhalequipado = False
espadaequipada = False
couroequipado = False

SAVEGAME_FILENAME = 'FelipinasGame.json'

game_state = dict()

def load_game():
    """Load game state from a predefined savegame location and return the
    game state contained in that savegame.
    """
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state

def save_game():
    """Save the current game state to a savegame in a predefined location.
    """
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))

def initialize_game():
    """If no savegame exists, initialize the game state with some
    default values.
    """
    global game_state
    player = personagem
    enemy = IA

    state = dict()
    state['players'] = [player]
    state['npcs'] = [enemy]
    return state

def menu():
    global game_state

    while True:
        print('╔════════════════════════╗')
        print('║          MENU          ║')
        print('╠════════════════════════╣')
        print('║',' '*22,'║')
        print('║ 1 - Loja               ║')
        print('║ 2 - Estatísticas       ║')
        print('║ 3 - Iniciar Aventura!  ║')
        print('║',' '*22,'║')
        print('║ Créditos:              ║')
        print('║          FelipinasMano ║')
        print('║',' '*22,'║')
        print('╚════════════════════════╝')
        try:
            seleção = input("Escolha uma opção: ")
        except ValueError:
            print()
            print("Você pode usar somente os números 1, 2, ou 3.")
            print()
            menu()
        if seleção == "1":
                print("Loja De Armas")
                print("1 - Punhal De Bronze: $50\n2- Espada De Bronze: $100")
                armseleção = int(input("Escolha um item: "))

        if armseleção == "1":
            if personagem.coin() <= 50:
                personagem.coin() - 50
                print("Sua Força Aumentou em +11")
                personagem.attack() + 11
                print(game_state)

        elif seleção == "2":
                    player = game_state['players'][0]            
                    print()
                    print("Status Player:\nHealth: {}\nStrength: {}\nGold: {}".format(player.health, player.strength, player.gold))
                    if punhalequipado == True:
                        print("Você está com um punhal equipado.")
                    elif espadaequipada == True:
                        print ("Você está equipando uma espada.")
                    elif couroequipado == True:
                        print("Você está vestindo um couro.")
menu()
def Loja():
    print()