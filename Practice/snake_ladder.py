import random
position1 = 0
position2 = 0
temp1 = 0
temp2 = 0
global position
position = 0
def dice():

    # return random.randrange(1, 7, 1)
    n = int(input())
    return n
def position(n, position):
    ladder = {1:13, 15:34, 19:48, 27:54, 37:98, 53:65, 76:91, 9:26, 45:67}
    snakes = {99:45, 85:67, 67:46, 45:17, 36:17, 56:12, 16:1}
    # n = dice()
    position = position+n
    if position in ladder:
        print("ladder!")
        position = ladder[position]
    elif position in snakes:
        print("snakes:(")
        position = snakes[position]
    return position
# def play_game:
while temp1<100 or temp2<100:
    # temp1 = 0
    # temp2 = 0
    print("enter dice value for player 1")
    n = dice()
    print("player 1 got", n)
    position1 = position(n, position1)
    print("player 1 position is", position1)
    print("enter dice value for player 2")
    n = dice()
    print("player 2 got", n)
    position2 = position(n, position2)
    print("player 2 position is", position2)




