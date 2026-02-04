def take_names(players,num_of_players):
    """
    Takes player names and initializes their states.
    Inventory is initialized as an empty dictionary
    """
    for i in range(num_of_players):
        name=input(f"Enter name for Player {i+1}: ")
        # using Dict for Inventory for o(1) access
        players[name]={"Health":100,"coins":100,"inv":{}}


def take_bids(players):
    """
    Takes bids from players for the current itme.
    validates that the player has enough coins.
    """
    for name , data in players.items():
        # Only alive players can bid
        if data["health"]>0:
            while True:
                try: 
                    bid_input=input(f"Player {name} ({data['coins']} coins), enter your bid: ")
                    bid=int(bid_input)

                    if bid <= data["coins"]:
                        data["bid"]=bid
                        break
                    else:
                        print(f"Not enough cions! You only have {data['coins']} coins.")
                except ValueError:
                    print("Please enter a valid number.")



