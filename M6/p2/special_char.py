'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    str_input = input()
    for letter in str_input:
        if letter in '!' '@' '#' '$' '%' '^' '&' '*':
            print(" ")
        else:
            print(str(letter)
if __name__ == "__main__":
    main()
