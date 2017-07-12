"""
GAME OF CROWN AND ANCHOR:

The game is a betting game where users bet money on the slots on a spinning wheel. The wheel is spun and it
stops on one of the slots. Each player starts with $10. The game continues until one player is left!!!

Enjoy :)
"""
import numpy as np
import random
import time
import sys

def number_of_players(count):
    try:
        count = int(count)
    except:
        type(count) == str
        count = input("Value Error: Enter a number please: ")
        number_of_players(count)
    player_dict(count)

def player_dict(count):
    players_list = [] ###: initializing player_list to be an empty list
    for i in np.arange(1, count+1):
        player_list = [] ###: will be a dictionary for player and money amount
        player = {} ###: empty data structure
        player_name = str(input("GAME: What is Player " + str(i) + "'s name? "))
        player[player_name] = 10 ###: string key-value, init to be 10 (we start with $10)
        player_list.append(player) ###: appending to player list to the dictionary player
        players_list.append(player_list)
    input("GAME: Okay! Let's play! Press Enter")
    if len(players_list) > 0:
        print("GAME: Each of you have $10. You can bet in $1, $2, $5, or $10 increments. "
              "You may also place more than one bet per round. Players may also choose to skip a round."
              "Once you have entered your bet, you will be prompted to choose which symbols to bet on (eg. '$5 on hearts')")
    turns(players_list)

def turns(players_list):
    ###: extra check to see if
    possible_bets = (1, 2, 5, 10)
    player_names = []
    ###: extracting data we currently have and placing in empty list 'players = []'
    while True: ###: all(i >= 0 for i in players_cash):
        ###: symbolizing alternating turns
        for player in players_list:
            ###: Check if game is over
            players_cash = []
            ###: following for-loop not duplicated: we need to check if players have 0 cash
            for p in players_list:
                player_dict = p[0]
                for key, value in player_dict.items():
                    player_names.append(key)
                    players_cash.append(value)
            if all(i <= 0 for i in players_cash):
                print("GAME OVER! There are no more players with remaining cash")
                sys.exit() ###: Will sys.exit() will end the program
            ###: player end check:
            ###: Check if player should be skipped
            if list(player[0].values())[0] <= 0:
                print("GAME: ", list(player[0].keys())[0], "has no mo money boss! Next Player")
                continue ###: just means skip to the next player (if he doesn't have money)
            print("GAME: It is ", list(player[0].keys())[0], "'s turn.")
            print("Current player list " + str(players_list))
            number_of_bets = int(input("GAME: How many bets would you like to make this round? (Enter 0 if you want to skip this turn) "))
            betting_amounts(number_of_bets, possible_bets, player)
            next(player) ###: KEY TO CODE! will iterate over players
            ###: since player is a list of dictionary and bets, we're deleting old bets after used
            del player[1:]

def betting_amounts(number_of_bets, possible_bets, player):
    try:
        valid_bets = ['anchor','club','diamond','heart','spade','crown']
        bet = {}
        for i in range(number_of_bets):
            ###: We stay in this while loop until it breaks (i.e. wew entered a valid bet)
            while True:
                bet_amount = int(input("GAME: How much do you want to bet? "))
                if bet_amount not in possible_bets:
                    print("Sorry, please enter a valid bet amount. (1,2,5,or 10)")
                    continue
                else:
                    break
            ###: Same for this while loop (i.e. we entered valid suit)
            while True:
                ###:
                bet_string = str(input("GAME: Betting on? "))
                if bet_string not in valid_bets:
                    print("Sorry, please enter a valid suit. (anchor, club, diamond, heart, spade, or crown)")
                    continue
                else:
                    break
            bet[bet_string] = bet_amount ###: dict 'bet' = bet_amount
        player.append(bet)
    except ValueError:
        if str(user_bet.lower()) == 'skip':
            print('Turn skipped')

def wheel_spin():
    ###: Decided to replicate the wheel in the picture instead of select random suits
    wheel = [['anchor', 'anchor', 'anchor'], ['club', 'club', 'diamond'], ['heart,', 'heart', 'heart'],
             ['anchor', 'crown', 'crown'], ['club', 'club', 'club'], ['spade', 'heart', 'heart'],
             ['diamond', 'diamond', 'diamond'], ['anchor', 'anchor', 'crown'], ['spade', 'spade', 'spade'],
             ['club', 'diamond', 'diamond'], ['crown', 'crown', 'crown'], ['club', 'crown', 'heart'],
             ['spade', 'spade', 'heart'], ['spade', 'diamond', 'crown'], ['anchor', 'anchor', 'anchor'],
             ['club', 'club', 'diamond'], ['heart', 'heart', 'heart'], ['anchor', 'crown', 'crown'],
             ['club', 'club', 'club'], ['spade', 'heart', 'heart'], ['diamond', 'diamond', 'diamond'],
             ['anchor', 'anchor', 'crown'], ['spade', 'spade', 'spade'], ['club', 'diamond', 'diamond'],
             ['crown', 'crown', 'crown'], ['club', 'crown', 'heart'], ['spade', 'spade', 'heart'],
             ['spade', 'diamond', 'crown']]

    slot = random.randint(0,len(wheel)-1)
    spin = wheel[slot]
    return(spin)

def next(player):
    player_info = player[0]
    bets = player[1]
    player_name = ''
    for key, value in player_info.items() :
        player_name = key

    ###: if player didn't want to bet (SKIP) return back
    ###: when iterating through number of bets, if '0' entered, we return from function without every spinning
    if len(bets) == 0:
        print("Turn skipped")
        return

    ###: WHEEL
    print("GAME: Spinning...")
    time.sleep(3) ###: pause for 3s
    spin = wheel_spin() ### run the wheel_spin func
    print("GAME: You span: " + str(spin))
    spin = str(spin)
    for bet in bets:
        number_of_times_appeared = spin.count(bet)
        if bet == 'anchor':
            if number_of_times_appeared == 3:
                print("GAME: CISC121 - Winner on Anchors!")
                bets[bet] *= 3
                player_info[player_name] += bets[bet]
                print("GAME: Congratulations! ", bet, " appeared three times!!!")
                print("Your total cash is now: ", player_info[player_name])
        if number_of_times_appeared == 1:
            bets[bet] *= 1
            player_info[player_name] += bets[bet]
            print("GAME: Congratulations! ", bet, " appeared once!")
            print("GAME: Your total cash is now: ", player_info[player_name])
        elif number_of_times_appeared == 2:
            bets[bet] *= 2
            player_info[player_name] += bets[bet]
            print("GAME: Congratulations! ", bet, " appeared twice!!")
            print("GAME: Your total cash is now: ", player_info[player_name])
        elif number_of_times_appeared == 3:
            bets[bet] *= 3
            player_info[player_name] += bets[bet]
            print("GAME: Congratulations! ", bet, " appeared three times!!!")
            print("GAME: Your total cash is now: ", player_info[player_name])
        else:
            player_info[player_name] -= bets[bet]
            print("GAME: Sorry no luck! Your cash is", player_info[player_name])

###: main function to run program
def main():
    count = input("Welcome to Crown and Anchor! \nHow many players will be joining us this round?: ")
    count = int(count)
    number_of_players(count)

if __name__ == '__main__':
    main()