import random
from functions import*
# Configuration: Items and their properties
items = {
    "medicine": {"disaster": "the plague", "base damage": 40, "Durability": 1},
    "Canned food": {"disaster": "Great Famine", "base damage": 30, "Durability": 1},
    "Reinforced Wood": {"disaster": "Hurricane", "base damage": 25, "Durability": 2},
    "Steel Shield": {"disaster": "Bandit Ambush", "base damage": 20, "Durability": 3}
}

def main():
    try:
        num=int(input("Enter number of players: "))
    except ValueError:
        num=2 # Default to 2 players if invalid input
    
    players={}
    take_names(players,num)
 # Game Loop: 5 Days
    for day in range(1,6):
        print(f"\nDay {day}:")
        # Randomly select an item for the day
        item_name=random.choice(list(items.keys()))
        print(f"Auction for: {item_name} (Protect against {items[item_name]['disaster']})")
        bids={}
        # bids={"Player1":50, "Player2":70}
        take_bids(players,bids)
        # Determine highest bidder
        if bids:
            winner=sorted(bids,key= lambda x: bids[x],reverse=True)[0]
            if bids[winner]>0:
                players[winner]["coins"]-=bids[winner]
                # Add item to inventory
                durability=items[item_name]["Durability"]
                players[winner]["inv"][item_name]=durability
            else:
                print("No valid bids placed.")

        system_game(players, items[item_name]["disaster"], items[item_name]["base damage"], day, item_name)
    print("\nGame Over! Final Player States:")
    for name, data in players.items():
        status="Alive" if data['health']>0 else "Dead"
        print(f"{name}: {status} | Health: {data['health']}")
        

if __name__ == "__main__":

    print("Game is ready to start ...")
    main()
    print("Game has ended.")