# MaestasP5
# Programmer: Shawn Maestas
# Email: smaestas52@student.cnm.edu
# Purpose: provides user capability to play rock scissor paper
# Python version 3.14

# Setting up variables:
from random import choice
game_results = {}
player_score = 0
computer_score = 0
game_counter = 0
options = ('rock', 'paper', 'scissors')
game_value = len(game_results)
variables = ['Tie', 'User Wins', 'Computer wins']

# Initial prompt:
print('You will be playing rock, paper, scissors against our program!\n')

#Creating a function for user input:
def user_answer():
    while True:
        user_input = input('Please make a choice: rock, paper, or scissors: \n').lower()
        if user_input == 'rock' or user_input == 'paper' or user_input == 'scissors':
            return user_input
        else:
            print('\ninvalid input.')

user_input = user_answer()

#Create a function for the Rock Paper Scissors rules:
def rps_function():
    global game_counter
    global player_score
    global computer_score
    computer_input = choice(options) #The choice option seemed better for the situation as I already had the variables list.
    if computer_input == 'rock' and user_input == 'rock':
        outcome = variables[0] #0 = Tie
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked "{computer_input}". This round is a tie!')
        game_number = game_counter
        game_results['Game ' + str(game_number)] = outcome
        return game_results, game_counter, outcome

    elif computer_input == 'rock' and user_input == 'paper':
        outcome = variables[1] #1 = User wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked "{computer_input}". You won this round!')
        game_number = game_counter
        player_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Player score: ' + str(player_score)]
        return game_results, game_counter, outcome, player_score

    elif computer_input == 'rock' and user_input == 'scissors':
        outcome = variables[-1] #-1 = Computer wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked "{computer_input}". The computer won this round!')
        game_number = game_counter
        computer_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Computer score: ' + str(computer_score)]
        return game_results, game_counter, outcome, computer_score

    elif computer_input == 'paper' and user_input == 'rock':
        outcome = variables[-1] #-1 = Computer wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked "{computer_input}". The computer won this round!')
        game_number = game_counter
        computer_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Computer score: ' + str(computer_score)]
        return game_results, game_counter, outcome, computer_score

    elif computer_input == 'paper' and user_input == 'paper':
        outcome = variables[0] #0 = Tie
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked "{computer_input}". This round is a tie!')
        game_number = game_counter
        game_results['Game ' + str(game_number)] = outcome
        return game_results, game_counter, outcome

    elif computer_input == 'paper' and user_input == 'scissors':
        outcome = variables[1] #1 = User wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked {computer_input}. You won this round!')
        game_number = game_counter
        player_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Player score: ' + str(player_score)]
        return game_results, game_counter, outcome, player_score

    elif computer_input == 'scissors' and user_input == 'rock':
        outcome = variables[1] #1 = User wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked {computer_input}. You won this round!')
        game_number = game_counter
        player_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Player score: ' + str(player_score)]
        return game_results, game_counter, outcome

    elif computer_input == 'scissors' and user_input == 'paper':
        outcome = variables[-1] #-1 = Computer wins
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked {computer_input}. The computer won this round!')
        game_number = game_counter
        computer_score += 1
        game_results['Game ' + str(game_number)] = [outcome, 'Computer score: ' + str(computer_score)]
        return game_results, game_counter, outcome, computer_score

    elif computer_input == 'scissors' and user_input == 'scissors':
        outcome = variables[0] #0 = Tie
        game_counter += 1
        print(f'\nGame {game_counter}:')
        print('-'*20)
        print(f'\nYou picked "{user_input}" and the computer picked {computer_input}. This round is a tie!')
        game_number = game_counter
        game_results['Game ' + str(game_number)] = outcome
        return game_results, game_counter, outcome

#Calling the Rock Paper Scissors function for the initial game.
rps_function()

#Request for a new game and define the scores.
new_game = input('\nWould you like to play again? (yes or no): ').lower()
if new_game == 'yes':
    play_again = True
    while play_again:
        user_input = user_answer()
        rps_function()
        print(f'\ntotal games played: {len(game_results)}')
        print(f'\nyour score: \n{"-"*20}\nwins: {player_score}\nlosses: {computer_score}\nties: {list(game_results.values()).count("Tie")}')
        new_game = input('\nWould you like to play again? (yes or no): ').lower()
        if new_game == 'no':
            print(f'\nThanks for playing, below are your results!\n{"-"*46}')
            for game, results in game_results.items():
                print(f'\n{game}: {results}')
            break
elif new_game == 'no':
    print('Thanks for playing!')
    print(f'\ntotal games played: {len(game_results)}')
    print(f'\nyour score: \n{"-"*20}\nwins: {player_score}\nlosses: {computer_score}\nties: {list(game_results.values()).count("Tie")}')
    print(f'\nBelow are your results:\n{"-"*46}')
    for game, results in game_results.items():
        print(f'\n{game}: {results}')
else:
    print('Invalid input. Please enter yes or no.')