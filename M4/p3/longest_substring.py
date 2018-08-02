'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    str_ = input()
    a_ = len(str_)
    max_ = ""
    temp_ = 0
    co_ = 0
    I = 0
    str1 = ""
    for x in range(0, a_-1):
        if str_[x] < str_[x+1]:
            co_ = co_+1
            str1 = str1 + str_[x]
        else:
            if co_ > temp_:
                temp_ = co_
                co_ = 0
                max_ = str1
                max_ = str1 + str_[x]
    print(max_)
if __name__ == "__main__":
    main()
