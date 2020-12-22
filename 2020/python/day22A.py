import common


def main():
    dat = common.readFile('day22.dat')
    
    player1, player2 = parse_data(dat)
    player1, player2 = play_rounds(player1,player2)

    winner = []

    if len(player1) > 0:
        winner = player1
    else:
        winner = player2
    
    total = 0
    for c in winner:
        total = total + (c * (winner.index(c) + 1))
    
    print(total)

def parse_data(dat):
    player1 = []
    player2 = []

    i = 0
    
    for d in dat:
        if d.startswith('Player'):
            i = i + 1
        elif d == '':
            pass
        else:
            if i == 1:
                player1.insert(0, int(d))
            else:
                player2.insert(0, int(d))


    return (player1, player2)

def play_rounds(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        p1 = player1[-1]
        p2 = player2[-1]

        if p1 > p2:
            player1, player2 = move_cards(player1, player2)
        else:
            player2, player1 = move_cards(player2, player1)
    
    return (player1, player2)

def move_cards(winner, loser):
    winner_card = winner[-1]
    losers_card = loser[-1]

    winner.remove(winner_card)
    loser.remove(losers_card)

    winner.insert(0, winner_card)
    winner.insert(0, losers_card)

    return (winner, loser)

if __name__ == '__main__':
    main()