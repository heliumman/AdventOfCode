import common
import day22A


def main():
    dat = common.readFile('day22.dat')
    
    player1, player2 = day22A.parse_data(dat)
    player1, player2 = play_game(player1,player2)

    winner = []

    if len(player1) > 0:
        winner = player1
    else:
        winner = player2
    
    total = 0
    for c in winner:
        total = total + (c * (winner.index(c) + 1))
    
    print(total)

def play_game(player1, player2):

    prev_rounds = []

    while len(player1) > 0 and len(player2) > 0:
        if [player1, player2] in prev_rounds:
            return (player1, [])
        else:
            prev_rounds.append([[], []])
            prev_rounds[-1][0].extend(player1)
            prev_rounds[-1][1].extend(player2)
        
        p1 = player1[-1]
        p2 = player2[-1]

        if p1 <= len(player1) - 1 and p2 <= len(player2) - 1:
            tmp1, tmp2 = play_game(player1[-1-p1:-1], player2[-1-p2:-1])
            if len(tmp1) > 0:
                player1, player2 = day22A.move_cards(player1, player2)
            else:
                player2, player1 = day22A.move_cards(player2, player1)
        else:
            if p1 > p2:
                player1, player2 = day22A.move_cards(player1, player2)
            else:
                player2, player1 = day22A.move_cards(player2, player1)

    return (player1, player2)

if __name__ == '__main__':
    main()