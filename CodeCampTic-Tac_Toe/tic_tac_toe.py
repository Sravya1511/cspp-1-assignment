# l_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(0, len(l_1), 3):
#     for j in range(3):
#         print(l_1[i+j], end = "\t")
#     print("\n")

# def get_game(pos):
#     print("enter o or x")
#     letter = input()
#     if letter != 'o' or letter != 'x':
#     dic = {0:"_", 1:"_", 2:"_", 3:"_", 4:"_", 5:"_", 6:"_", 7:"_", 8:"_"}
#     if pos in dic.keys():
#         l_1[pos] = letter
#     for i in range(0, len(l_1), 3):
#         for j in range(3):
#             print(l_1[i+j], end = "\t")
#         print("\n")
#     return l_1

# # def updated_pos:
# def winner(l_1):
#     for i in range(0, len(l_1), 3):
#         if l_1[i] == l_1[i+1] == l_1[i+2]:
#             return True
            
#     for i in range(3):
#         if l_1[i] == l_1[i+3] == l_1[i+3]:
#             return True
        
#     if l_1[0] == l_1[4] == l_1[8]:
#         return True
    
#     if l_1[2] == l_1[4] == l_1[6]:
#         return True


# while winner(l_1) != True:
#     print("play tic tac toe")
#     print("player1_human")
#     print("enter position between 0 to 8")
#     pos = int(input())
#     l_1 = get_game(pos)
#     if winner(l_1) == True:
#         print("player 1 won")
#         break
#     print("player2_comp")
#     import random
#     pos = random.randrange(0, 9)
#     l_1 = get_game(pos)
#     if winner(l_1) == True:
#         print("player 2 won")
#         break
game_list = []
l = input()
for i in range(3):
    # for j in range(3):
    li = list((map(str, l.split())))
    game_list.append(li)
print(game_list)







