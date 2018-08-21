# def main():
#     hand = {'a':1, 'x':2, 'l':3, 'e':1}
#     word = "lxla"
#     for i in word:
#         if i in hand.keys():
#             hand[i] = hand[i] - 1
#     print(hand)
# if __name__ == "__main__":
#     main()


# def main():
#     hand = {'a':1, 'x':2, 'l':3, 'e':1}
#     l=0
#     for i in hand:
#         l = l+hand[i]
#     print(l)
# if __name__ == "__main__":
#     main()

x = int(input())
lis = []
for i in range(x):
    n = int(input())
    lis.append(n)
lis.sort()
print(lis[n-1])
