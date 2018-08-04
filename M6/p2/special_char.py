"""string"""
def main():
    """special"""
    str_input = input()
    st1 = ""
    for letter in str_input:
        if letter in '!' '@' '#' '$' '%' '^' '&' '*':
            st1 = st1 + " "
        else:
            st1 = st1+ letter
    print(st1)
if __name__ == "__main__":
    main()
