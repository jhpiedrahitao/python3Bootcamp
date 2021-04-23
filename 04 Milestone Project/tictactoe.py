from IPython.display import clear_output
#variables
game_state=True
game=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
keyboard=[['7','8','9'],['4','5','6'],['1','2','3']]
key={7:[0,0],8:[0,1],9:[0,2],4:[1,0],5:[1,1],6:[1,2],1:[2,0],2:[2,1],3:[2,2]}
player1=None
player2=None
player=1
win=False

def askForPlayer():
    player1=None
    player2=None
    player_input=None
    while ( player_input not in ['X', 'O']):
        clear_output() 
        print('Bienvenido a triky')
        player_input=input('jugador uno sera X o O: ').upper()
    clear_output()    
    if player_input=='X':
        player1='X'
        player2='O'
    elif player_input=='O': 
        player1='O'
        player2='X'
    return(player1,player2)

def showBoard():
    global game
    global player1
    global player2
    i=0;
    print(f'El jugador 1 es {player1} y el jugador 2 es {player2} \n\n\n')
    for line in range(0,len(game)):
        print (' '+game[line][0]+' ║ '+game[line][1]+' ║ '+game[line][2]+'        '+' '+keyboard[line][0]+' ║ '+keyboard[line][1]+' ║ '+keyboard[line][2]+' ')
        if i<2:
            print ('═══╬═══╬═══       ═══╬═══╬═══')
            
        i+=1
    print('\n')
    
def playAgain():
    state= None
    player_input=None
    while ( player_input not in ['S', 'N']):
        player_input=input('Deseas jugar nuevamente S o N: ').upper()
        clear_output()    
    if player_input=='S':
        return True
    elif player_input=='N': 
        return False


def move():
    global player
    player_input=None
    value=10
    while (value not in range(1,10)):
        clear_output()
        showBoard()
        player_input=input(f'Jugador {player} ingresa tu siguiente jugada (0 a 9): ')
        if player_input.isdigit():
            player_input=int(player_input)
            if player_input in range(1,10):
                if game[key[player_input][0]][key[player_input][1]]== ' ':
                    value=player_input
    return value

def updateBoard(pos):
    global player
    if player==1:
        game[key[pos][0]][key[pos][1]]=player1
        player=2
    elif player==2:
        game[key[pos][0]][key[pos][1]]=player2
        player=1
        
def won():
    if ' ' not in game[0]+game[1]+game[2]:
        clear_output()
        showBoard()
        print('Empate')
        return 'TIE'
    elif game[0] in [['X','X','X'],['O','O','O']] or game[1] in [['X','X','X'],['O','O','O']] or game[0] in [['X','X','X'],['O','O','O']] or game[0][0]==game[1][0]==game[2][0]!=' ' or game[0][1]==game[1][1]==game[2][1]!=' ' or game[0][2]==game[1][2]==game[2][2]!=' ' or game[0][0]==game[1][1]==game[2][2]!=' ' or game[0][2]==game[1][1]==game[2][0]!=' ':
        if  player==2:
            clear_output()
            showBoard()
            print('Gana el jugador 1')
            return player1
        elif player==1:
            clear_output()
            showBoard()
            print('Gana el jugador 2')
            return player2

def clearGame():
    global game
    game=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
clear_output()
# verify if want to play
while(game_state):
    clearGame();
    # ask for player
    player1,player2=askForPlayer();
    # show board
    while(game_state):
        showBoard()
        # ask for imput 
        pos=move()
        # update board
        updateBoard(pos)
        # verify if win
        win=won()
        # ask for play again
        if win in ['X','O','TIE']:
            game_state=playAgain()
            break
    print('Gracias por jugar')
game_state=True