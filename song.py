import sys

def two_fer_test(name):
    """
        Two-fer or 2-fer is short for two for one. One for you and one for me.
        Given a name, return a string with the message:
            Alice	One for Alice, one for me.
            Bob	One for Bob, one for me.
            One for you, one for me.
            Zaphod	One for Zaphod, one for me.
            python3 song.py redi
        Inputs and output : python3 song.py Redi, one for redi, one for me, 
            python3 song.py, one for you, one for me
            python3 song.py 227599, Exception: 227599 is not name of a person. Please Enter a name
    """
    if name.isalpha():
        Two_fer = f"one for {name}, one for me"
        print(Two_fer)
    else:
        raise Exception(f'{name} is not name of a person. Please Enter a name')



if __name__=="__main__":
    params = sys.argv[1:]
    if len(params) == 0:
        two_fer_test("you")
    else:
        two_fer_test(params[0])
