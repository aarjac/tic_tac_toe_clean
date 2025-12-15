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

def print_board(game_board):

    row_index=0
    
    for row in game_board.values():
        
        column_index=0
        
        for column in row:
            
            if column_index<(len(row)-1):
                
                print(column,' | ',end='')
          
            else:
              
                print(column)
           
            column_index+=1
    
        row_index+=1

        if row_index<(len(row)):

            print('-------------')
        
        else:
            
            print('\n')
        


def main():
   
    player1_mark=''
    player2_mark=''
    game_board={'row1':[' ',' ',' '],'row2':[' ',' ',' '],'row3':[' ',' ',' ']}
    
    print('Welcome to the Tic-Tac-Toe Game\n')
    player1_mark,player2_mark=get_player_marks(player1_mark, player2_mark)
    print('\n')
    
    print_board(game_board)
    

if __name__=="__main__":
    main()