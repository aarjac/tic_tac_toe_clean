def get_player_marks(player1_mark, player2_mark):
    
    player1_mark='WRONG'
    acceptable_choices=['X','O']
    
    while player1_mark=='WRONG':

        player1_mark=input('Player 1 enter your marker (X or O): ')
        player1_mark=player1_mark.upper()

        if player1_mark not in acceptable_choices:
            
            player1_mark='WRONG'
            print('You did not enter X or O. Try again...')
       
        else:

            acceptable_choices.remove(player1_mark)
            player2_mark=acceptable_choices[0]

    return player1_mark, player2_mark

def rules(rules_board):

    seperator='-'*(len(rules_board[0])*6-3)

    print('''Rules:\n
          1. Each player will choose their mark
          2. Players will take turns placing their marks
          3. To win you must get 3 of your marks in a row\n
          Here are how the numbers selected correspond to each move\n''')
    
    for index,row in enumerate(rules_board):
       
        print(' | '.join(f'{cell:^3}' for cell in row))
       
        if index<(len(rules_board)-1):  
           
            print(seperator) 
   
    print('\n')


def print_board(game_board):
     
    seperator='-'*(len(game_board[0])*6-3)

    for index,row in enumerate(game_board):
       
        print(' | '.join(f'{cell:^3}' for cell in row))
       
        if index<(len(game_board)-1):  
           
            print(seperator) 
   
    print('\n')

def get_player_move(player, moves_used):

    player_move=0
    acceptable_choices=[num for num in range(1,10)]

    while player_move not in acceptable_choices:

        player_move=int(input(f'{player} please enter your move (1,2,3,4,5,6,7,8, or 9): '))

        if player_move not in acceptable_choices:
            
            player_move=0
            print('You did not enter a valid move. The moves, starting from the top left corner are 1,2,3,4,5,6,7,8, or 9. Try again...')

        elif player_move in moves_used:

            player_move=0
            print('That move has already been played. Try again...')

        else:
            
            return player_move
   
        
def mark_board(player_move, player_mark, game_board):

    for row_index,row in enumerate(game_board):
        
        for column_index in range(len(row)):
            
            player_move-=1

            if player_move==0:

                game_board[row_index][column_index]=player_mark

            else:
                
                pass
    
    return game_board

def check_winner(player1_mark, player2_mark, game_board):

    x_marks=['X','X','X']
    o_marks=['O','O','O']
    winning_mark=''
    column1=[]
    column2=[]
    column3=[]
    diagonal1=[]
    diagonal2=[]
    

    for row_index,row in enumerate(game_board):

        column1+=row[0]
        column2+=row[1]
        column3+=row[2]
        

        for column_index,column in enumerate(row):

            if row_index==column_index:

                diagonal1.append(game_board[row_index][column_index])

            else:
                
                pass

            if (row_index+column_index)==2:

                diagonal2.append(game_board[row_index][column_index])

            else:

                pass

        if x_marks==column1 or x_marks==column2 or x_marks==column3 or x_marks==row or x_marks==diagonal1 or x_marks==diagonal2:

            winning_mark='X'

        elif o_marks==column1 or o_marks==column2 or o_marks==column3 or o_marks==row or o_marks==diagonal1 or o_marks==diagonal2:
        
            winning_mark='O'
        
        else:

            pass

        if winning_mark==player1_mark:

            return 'Player 1'

        elif winning_mark==player2_mark:

            return 'Player 2'
    
    return 'NO WINNER'

def check_play():

    acceptable_choices=['Y','N']
    play=''

    while play not in acceptable_choices:

        play=input('Would you like to play again (Y or N)? ')
        play=play.upper()
        
        if play in acceptable_choices:

            return play
        
        else: 

            pass    

def main():
   
    player1_mark=''
    player2_mark=''
    rules_board=[['1','2','3'],['4','5','6'],['7','8','9']]
    game_board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    moves_used=[]
    number_of_moves=9
    player1_move=0
    play='Y'
    winner='NO WINNER'

    print('Welcome to the Tic-Tac-Toe Game\n')
    rules(rules_board)
    player1_mark,player2_mark=get_player_marks(player1_mark, player2_mark)

    while play=='Y':

        while winner=='NO WINNER':
    
            print('\n')
            print_board(game_board)
            
            player1_move=get_player_move('Player 1', moves_used)
            moves_used.append(player1_move)
            game_board=mark_board(player1_move, player1_mark, game_board)
            print('\n')
            print_board(game_board)

            winner=check_winner(player1_mark, player2_mark, game_board)

            if winner!='NO WINNER':
                break
            else:
                pass

            if len(moves_used)==number_of_moves:
            
                winner="DRAW"
                break

            else:

                pass

            player2_move=get_player_move('Player 2', moves_used)
            game_board=mark_board(player2_move, player2_mark, game_board)
            moves_used.append(player2_move)
            print('\n')
            print_board(game_board)

            winner=check_winner(player1_mark, player2_mark, game_board)

        if winner=='DRAW':

            print("There is no winner. It's a draw...")
            play=check_play()

        elif winner=='Player 1' or winner=='Player 2':

            print(f'Congradulations {winner}! YOU WON!\n')
            play=check_play()

        if play=='Y':

            winner='NO WINNER'
            game_board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            moves_used=[]

        else:

            break

if __name__=="__main__":
    main()