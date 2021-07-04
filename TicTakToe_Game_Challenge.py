import itertools
def win(current_game):
    def all_same(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False
    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is Horizontal winner")
            return True

    # vertical winner

    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the Vertical winner")
            return True
    # Diagonal Winner
    daig = []
    for ix in range(len(game)):
        daig.append(game[ix][ix])
    if all_same(daig):
        print(f"Player {daig[0]} is the Diagonal winner")
        return True

    daig = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        daig.append(game[idx][reverse_idx])
    if all_same(daig):
        print(f"Player {daig[0]} is the Diagonal winner")
        return True
    return False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column]!=0:
            print("This space is already occupied,try another")
            return False
        #print("   "+"  ".join([str[i] for i in range(len(game_map))]))
        print("   0  1  2")
        if not just_display:
            game_map[row][column]=player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map
    except IndexError :
        print("Did you attempt to play a row or column outside the range of 0,1 or 2?(IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False



play=True
players=[1,2]
while play:
    #game_size=input("what size of tic tak game you want?")
    #game=[[for i in range(i)] for i in range(3)]
    game=[[0,0,0],
          [0,0,0],
          [0,0,0]]
    game_won=False
    player_choice=itertools.cycle([1,2])
    game_board(game,just_display=True)
    while not game_won:
        current_player=next(player_choice)
        played=False
        while not played:
            print(f"Current_player :{current_player}")
            column_choice=int(input("what column do you want to play 0 1 2 :"))
            row_choice=int(input("what row do you want to play 0 1 2: "))
            played=game_board(game,player=current_player,row=row_choice,column=column_choice)
        if win(game):
            game_won=True
            again=input("do you want to play the game again (y/n")
            if again.lower()=='y':
                print("restarting")
            elif again.lower()=='n':
                print("Bye")
                play=False
            else:
                print("Not valid anser but , c ya")
                play=False


