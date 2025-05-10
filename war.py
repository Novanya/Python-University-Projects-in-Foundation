#Initialize modules
import random
import sys
import os
from datetime import datetime

#Card functions
def create_card(value, suit=None): #to create a card
    return {'value': value, 'suit': suit}

def card_to_string(card): #convert card set to a string
    if card['suit']:
        return f"{card['value']}{card['suit']}"
    return f"{card['value']}"

#function to compare cards
def compare_cards(card1, card2):
    values_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'Joker']
    idx1 = values_order.index(card1['value'])
    idx2 = values_order.index(card2['value'])
    if idx1 > idx2:
        return 1
    elif idx1 < idx2:
        return -1
    else:
        return 0

# Deck functions
def build_deck():
    suits = ['♥', '♦', '♣', '♠'] #hearts, diamonds, clubs, spades
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = []
    
    for suit in suits: #create 52 cards
        for value in values:
            cards.append(create_card(value, suit))
    
    # Add 2 Joker cards
    cards.append(create_card('Joker'))
    cards.append(create_card('Joker'))
    return cards

#shuffling all 54 cards together
def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck):
    if len(deck) > 0: #check if the deck has cards
        return deck.pop() #ensure cards not reused
    return None

# Player functions
def create_player(name): #create a player with empty deck and a pile called won cards
    return {
        'name': name,
        'deck': [],
        'won_cards': []
    }

def add_card_to_player(player, card): #add cards to a player's deck
    player['deck'].append(card)

def shuffle_player_deck(player): #shuffle a plyer's deck
    random.shuffle(player['deck'])

def play_card_from_player(player): #remove a card from player's deck function
    if len(player['deck']) > 0:
        return player['deck'].pop(0)
    return None #no cards left

def win_cards_for_player(player, cards): #add won cards to a player's pile
    player['won_cards'].extend(cards)

def total_player_cards(player): #count total cards one player has
    return len(player['deck']) + len(player['won_cards'])

#functions in game
def initialize_game(rounds):
    human = create_player("Human")
    pc = create_player("PC")
    war_count = 0 #war round counter
    game_history = [] #storing history of round
    full_history = [] #to store history of entire game
    
    #Build and shuffle deck
    deck = build_deck()
    shuffle_deck(deck)
    
    #Distribute cards evenly
    while len(deck) > 0:
        add_card_to_player(human, deal_card(deck))
        add_card_to_player(pc, deal_card(deck))

    #shuffling individual decks
    shuffle_player_deck(human)
    shuffle_player_deck(pc)
    
    return {
        'rounds': rounds,
        'human': human,
        'pc': pc,
        'war_count': war_count,
        'game_history': game_history,
        'full_history': full_history
    }

#function to play one round
def play_round(game): 
    human_card = play_card_from_player(game['human'])
    pc_card = play_card_from_player(game['pc'])
    
    if human_card is None or pc_card is None:
        return False  #game over
    
    result = f"{card_to_string(human_card)} vs {card_to_string(pc_card)} - "
    comparison = compare_cards(human_card, pc_card)
    
    if comparison > 0:
        win_cards_for_player(game['human'], [human_card, pc_card])
        result += "H" #player win
    elif comparison < 0:
        win_cards_for_player(game['pc'], [human_card, pc_card])
        result += "P" #pc win
    else:
        #war!
        war_cards = [human_card, pc_card]
        result += "WAR"
        game['war_count'] += 1
        war_winner = resolve_war(game, war_cards)
        if war_winner:
            win_cards_for_player(war_winner, war_cards)
    
    game['game_history'].append(result)
    return True

#resolve the war
def resolve_war(game, war_cards):
    human = game['human']
    pc = game['pc']
    
    for _ in range(3): #drawing 3 additional cards
        h_card = play_card_from_player(human)
        p_card = play_card_from_player(pc)
        
        if h_card is None or p_card is None:
            return None #no cards to continue war then
        
        war_cards.extend([h_card, p_card])
    
    #compare the 4th card
    h_fourth = play_card_from_player(human)
    p_fourth = play_card_from_player(pc)
    
    if h_fourth is None or p_fourth is None:
        return None
    
    war_cards.extend([h_fourth, p_fourth])
    comparison = compare_cards(h_fourth, p_fourth)
    
    if comparison > 0:
        return human #player win the war
    elif comparison < 0:
        return pc #pc win the war
    else:
        #another war!!! (if tie)
        return resolve_war(game, war_cards)

def play_game(game):
    now = datetime.now() #get current date and time
    print(f"Date: {now.strftime('%Y-%m-%d')}")
    print(f"Time: {now.strftime('%H:%M')}")
    print(f"\nTotal Rounds: {game['rounds']}\n")
    
    for round_num in range(1, game['rounds'] + 1):
        print(f"\nRound {round_num} results")
        print("-------------")
        print("No : Hum vs PC - Winner")

        #continue playing rounds till one player's deck is empty
        while game['human']['deck'] and game['pc']['deck']:
            if not play_round(game):
                break
        
        #display result of a round
        for i, result in enumerate(game['game_history'], 1):
            print(f"{i}: {result}")
        
        #store full history with round number
        game['full_history'].append((round_num, game['game_history'].copy()))
        
        #reset for next round if want
        if round_num < game['rounds']:
            #combineing won cards again to deck
            game['human']['deck'].extend(game['human']['won_cards'])
            game['pc']['deck'].extend(game['pc']['won_cards'])
            game['human']['won_cards'] = []
            game['pc']['won_cards'] = []
            shuffle_player_deck(game['human'])
            shuffle_player_deck(game['pc'])
            game['game_history'] = []
            game['war_count'] = 0

#determining winner by comparing all the cards of both players.
def determine_winner(game):
    human_total = total_player_cards(game['human']) #get total cards from player
    pc_total = total_player_cards(game['pc']) #get total cards for pc

    #display final result counts
    print(f"\nPC card count {pc_total}")
    print(f"Human card count {human_total}")
    print(f"War count {game['war_count']}")

    #determine winner and display
    if human_total > pc_total:
        print("\nHuman won the game!")
        return "Human"
    elif pc_total > human_total:
        print("\nPC won the game!")
        return "PC"
    else:
        print("\nThe game is a tie!")
        return "Tie"
#save result to txt file
def save_to_file(game):
    now = datetime.now()
    random_num = random.randint(1000, 9999)
    filename = f"{now.strftime('%Y%m%d_%H-%M')}_{random_num}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        #writing date,time, total round amount
        f.write(f"Date: {now.strftime('%Y-%m-%d')}\n")
        f.write(f"Time: {now.strftime('%H:%M')}\n\n")
        f.write(f"Total Rounds: {game['rounds']}\n\n")

        #write result for every round
        for round_num, round_history in game['full_history']:
            f.write(f"Round {round_num} results\n")
            f.write("-------------\n")
            f.write("No : Hum vs PC - Winner\n")
            for i, result in enumerate(round_history, 1):
                f.write(f"{i}: {result}\n")
            f.write("\n")
    
        human_total = total_player_cards(game['human'])
        pc_total = total_player_cards(game['pc'])
    
#write results
        f.write(f"PC card count {pc_total}\n")
        f.write(f"Human card count {human_total}\n")
        f.write(f"War count {game['war_count']}\n\n")

    #declare winner
        if human_total > pc_total:
            f.write("Human won the game!\n")
        elif pc_total > human_total:
            f.write("PC won the game!\n")
        else:
            f.write("The game is a tie!\n")
    
        #now generate HTML version
        html_file = save_to_html(game, filename)
        return filename, html_file

#saving result in html page
def save_to_html(game, txt_filename):
    """Generate an HTML version of the game results"""
    html_filename = os.path.splitext(txt_filename)[0] + ".html"
    
    with open(html_filename, 'w', encoding='utf-8') as f: #html structure basic one
        f.write(f"""<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Results</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .round {{ margin-top: 20px; }}
        .round-header {{ font-weight: bold; }}
        .results {{ margin-left: 20px; }}
    </style>
</head>
<body>
    <p>Date: {datetime.now().strftime('%Y-%m-%d')}</p>
    <p>Time: {datetime.now().strftime('%H:%M')}</p>
    <p><br><br>Total Rounds: {game['rounds']}<br><br></p>
""")
        
        #add round results
        for round_num, round_history in game['full_history']:
            f.write(f"""
    <div class="round">
        <p class="round-header">Round {round_num} Results</p>
        <pre class="results">
""")
            for i, result in enumerate(round_history, 1):
                f.write(f"{i}: {result}\n")
            f.write("""
        </pre>
    </div>
""")
        
        #add summary
        human_total = total_player_cards(game['human'])
        pc_total = total_player_cards(game['pc'])
        
        f.write(f"""
    <pre>
PC card count: {pc_total}
Human card count: {human_total}
War count: {game['war_count']}
""")
        
        #add winner 
        if human_total > pc_total:
            f.write("\nHuman won the game!\n")
        elif pc_total > human_total:
            f.write("\nPC won the game!\n")
        else:
            f.write("\nThe game is a tie!\n")
        
        f.write("""</pre>
</body>
</html>
""")
        
    return html_filename

def main():
    #command line arguments
    rounds = 1  #default 1
    if len(sys.argv) > 1:
        try:
            rounds = int(sys.argv[1])
            if rounds < 1 or rounds > 5:
                print("Invalid number of rounds. Must be between 1 and 5. Using default (1 round).")
                rounds = 1
        except ValueError:
            print("Invalid argument. Using default (1 round).")

    #functions instialization
    game = initialize_game(rounds)
    play_game(game)
    winner = determine_winner(game)
    save_to_file(game)

if __name__ == "__main__":
    main()
