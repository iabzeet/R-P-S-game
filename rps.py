"""
    Rock, Paper, Scissors program
    made on 12-04-2020
    by @iabzeet
    inspired from @Davidoff7776 for practice purposes
"""



from random import choice                       #importing choice from random for easy access

def show_statistics(scores):                    #shows the scores at the start of the execution on the prompt
    return f'WIN: {scores["WIN"]}\nLOSE: {scores["LOSE"]}\nDRAW: {scores["DRAW"]}'


def player_choice():                            #executes right after and gives a player a choice to chose      PLAYER'S CHOICE(human)
    while True:                                 #between rock, paper, scisssors
        print('Rock, paper or scissors?')
        choice = input('>').capitalize()                #takes input from the prompt
        if choice in ('Rock', 'Paper', 'Scissors'):     #if choice is between those then executes further or teminates if not
            return choice


def computer_choice():                              #executes after the player's choice and runs in the background  COMPUTER'S CHOICE(ai)
    return choice(('Rock', 'Paper', 'Scissors'))    #and choses between these items randomly


def game_outcome(player, computer):                 #compares the player's and computer's choices and take their choices as it's arguements
    POSSIBLE_OUTCOMES = {                           #possible outcomes to compare and rules
        ('Paper', 'Rock'): 'covers',                #(player, computer): 'rule/line'  if player is winning compares like this
        ('Rock', 'Scissors'): 'crushes',            # or (computer, player): 'rule/line' if computer is winning compares like this
        ('Scissors', 'Paper'): 'cuts'
    }
    if player == computer:                          #returns DRAW if player's and computer's choices are the same
        print("DRAW. Nobody wins or losses.")
        return 'DRAW'
    elif (player, computer) in POSSIBLE_OUTCOMES:   #returns WIN if player has won
        print(f'{player} {POSSIBLE_OUTCOMES[player, computer]} {computer}. You won!')           #{POSSIBLE_OUTCOMES[player, computer]}      comparing each choices from each with the elements of POSSIBELE_OUTCOMES set for the right combination, then returns the value of key of the correct combinaton, applies for wiining of the computer as well
        return 'WIN'
    else:                                           #returns LOSE if player has lose
        print(f'{computer} {POSSIBLE_OUTCOMES[computer, player]} {player}. You lost!')
        return 'LOSE'




def rock_paper_scissors(scores):
    print(show_statistics(scores))                  #execution 1
    player = player_choice()                        #execution 2
    computer = computer_choice()                    #execution 3
    outcome = game_outcome(player, computer)        #execution 4
    scores[outcome] += 1                            #inceases value of DRAW, WIN, LOSE accordingly based on the game_outcome(player, computer) result by 1 in the scores
    return scores                                   #returns the increased score and keep adding if the player chose to play further, and update the value of scores in the MAIN FUNCTION


def play_again():                                   #executes right after the player has won, draw or lose
    while True:
        print('\nDo you want to play again?')       #asks if the player wants to play further
        print('(Y)es')
        print('(N)o')
        ans = input('> ').lower()
        if ans == 'y':                              #returns True if the player wishes to play again
            return True
        elif ans == 'n':
            return False                            #or False otherwise and terminates


def main():                                         #main functon
    scores = {                                      #keeps the track of original scores
        'WIN': 0,
        'LOSE': 0,
        'DRAW': 0
    }
    still_playing = True
    while still_playing:
        scores = rock_paper_scissors(scores)        #main function 2
        still_playing = play_again()                #keeps the loop running if the value is True or terminates othewise if the value is False

if __name__ == '__main__':
    main()