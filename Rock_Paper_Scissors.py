from random import choice

# Created a list 'l' with items R for Rocks, P for Paper and S for Scissors
l=['R','P','S']

# Declared counters to check conditions
player_score=0
computer_score=0
round_=0

# Declared condition for trying the game all over again
is_running=True

print('Welcome! Let us play ROCK, PAPER SCISSORS!')

# Begin a loop to start the game
while is_running:

    # Begin another loop to cater for the three rounds of the game
    while round_<=2:
        CPU=choice(l)
        player=input(('enter an option from list')).upper()

        # Created loop to ensure user (player) input is correct
        while player not in l:
            print('Invalid input. Try again')
            player=input(('enter an option from list')).upper()

        # Display player input and computer choice to compare
        # and determine winner of the round
        print('Player:',player,'Computer:',CPU)

        # Test conditions to determine round's winner
        if player==CPU:
            print('it is a tie. Take an extra round')
        elif (player=='R' and CPU=='S') or (player=='P' and CPU=='R') or (player=='S' and CPU=='P'):
            print('Player wins this round')
            player_score+=1
            round_+=1
        elif (player=='S' and CPU=='R') or (player=='R' and CPU=='P') or (player=='P' and CPU=='S'):
            print('Computer wins this round')
            computer_score+=1
            round_+=1

        # Test conditions to wrap up the game
        if player_score>=2 and round_==3:
            print('Game over. Player wins!')
        elif computer_score>=2 and round_==3:
            print('Game over. Computer wins!')

    # Confirm if user would like to play the game again
    another_try=(input('Another try? Enter Y for yes and N for no')).upper()
    if another_try=='Y':
        round_=0
        pass
    elif another_try=='N':
        is_running=False
        print('Goodbye')
    else:
        print('Wrong input. Enter Y or N')
