"""Assume s is a string of lower case characters"""
def main():
    '''longest'''
    str_ = input()
    tstr_ = ""
    for i, item in enumerate(str_):
        flag_ = 0
        tstr2_ = ""
        tt_ = item
        ji_ = i
        while flag_ != 1 and ji_ != len(str_):
            if ord(tt_) <= ord(str_[ji_]):
                tt_ = str_[ji_]
                tstr2_ += str_[ji_]
            else:
                flag_ = 1
            ji_ += 1

        if len(tstr2_) > len(tstr_):
            tstr_ = tstr2_
    print(tstr_)
if __name__ == "__main__":
    main()
