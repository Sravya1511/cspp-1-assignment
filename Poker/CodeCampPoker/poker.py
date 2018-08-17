'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def is_straight(hand):
    """straight"""
    # results = ["1", "2", "3"]
    # hand = [int(i) for i in hand]
    # print(hand)
    name_cards = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    hand_new = []

    for i in hand:
        if i[0] in name_cards.keys():
            temp = name_cards[i[0]]
        else:
            temp = int(i[0])
        hand_new.append(temp)
    # for i in range(len(hand_new)):
    #     l = []
    #     l.append(int(hand[i][0]))
    #     print(l)
    # length = len(l)
    # print(length)
    c_1 = 0
    for i in hand_new:
        temp = i
        if temp+1 in hand_new:
            c_1 = c_1+1
        if temp-1 in hand_new:
            c_1 = c_1+1
    # print("lent",l)
    if c_1 == (2*(len(hand_new))-2):
        return True
    return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # for i in range(len(hand)):
    #     l = []
    #     l.append(hand[i][1])
    #     # print(l)
    for i in range(len(hand)-1):
        if hand[i][1] != hand[i+1][1]:
            return False
    return True
def four_of_a_kind(hand):
    """four of kind"""
    len_1 = len(hand)
    
    for i in range(len_1):
        four = 0
        for j in range(len_1):
            if i!=j:
                if hand[i][0] == hand[j][0]:
                    four = four+1
        if four == 3:
            return True
    return False
def three_of_a_kind(hand):
    """three of a kind"""
    len_1 = len(hand)
    for i in range(len_1):
        three = 0
        for j in range(len_1):
            if i!=j:
                if hand[i][0] == hand[j][0]:
                    three = three+1
            # print(three)
        if three == 2:
            return True
    return False
def one_pair(hand):
    """onepair"""
    one_p = 0
    len_1 = len(hand)
    for i in range(len_1):
        for j in hand:
            if hand[i][0] == j[0]:
                one_p = one_p+1
            # print(two)
    if one_p == 7:
        return True
    return False
def two_pair(hand):
    """two pair"""
    two_p = 0
    len_1 = len(hand)
    for i in range(len_1):
        for j in hand:
            if hand[i][0] == j[0]:
                two_p = two_p+1
            # print(two)
    if two_p == 9:
        return True
    return False
def full_house(hand):
    """fullHouse"""
    full_h = 0
    len_1 = len(hand)
    for i in range(len_1):
        for j in hand:
            if hand[i][0] == j[0]:
                full_h = full_h+1
    if full_h == 13:
        return True
    return False
def high_card(hand):
    """fullHouse"""
    high = 0
    len_1 = len(hand)
    for i in range(len_1):
        for j in hand:
            if hand[i][0] == j[0]:
                high = high+1
    if high == 5:
        return True
    return False
# def comparision_high_card(hand):
#     for i in hand:
#         if i[0] == 'A':
#             return True
    # return False
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 9
    if four_of_a_kind(hand):
        return 8
    if full_house(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if three_of_a_kind(hand):
        return 4
    if two_pair(hand):
        return 3
    if one_pair(hand):
        return 2
    if high_card(hand):
        # if comparision_high_card(hand):
        #     return 1.2
        # return 1.1
        return 1
    return 0

def poker(hands):
    # print(is_flush(hands))
    # print(is_straight(hands))
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    # return max(hands, key=hand_rank)


    lst = list(map(hand_rank,hands))
    # print(lst)
    maxTemp = max(lst)
    countMAx = lst.count(maxTemp)
    if countMAx == 1 :  
        return hands[lst.index(maxTemp)]
    # else :
    #     # temp_hands =[]
    #     # for i in lst:
    #     #     if i == maxTemp:
    #     #         temp_hands.append(hands[lst.index(i)])
    #     # # T=map(sortedList,temp_hands,)
    #     # Temp_hands2=hands.copy()
    #     # Temp_Ranks
    #     # k=0
    #     # for i in temp_hands:
    #     #     Temp_hands2[k] = sorted(i, reverse = True)
    #     #     k+=1
    #     # TempMax = max(Temp_hands2)
    #     # Max_index=Temp_hands2.index(TempMax)
    #     # print(Temp_hands2[i])
    #     hands_temp = hands.copy()
    #     hands_temp.sort()
    else: 
        l_m = []
        for i in range(len(hands)):
            l1 = hands[i]
            l1.sort()
            l1.reverse()
        l_m.append(l1)

# l_m.reverse()
# print(l_m)
# print(l_m[0][4][0])
    for i in range(0, 5):
        if l_m[0][i][0] > l_m[1][i][0]:
            return l_m[0]


if __name__ == "__main__":
    # read the nmber of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
