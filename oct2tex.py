'''
usage:
cat about.txt | python soinput.py
'''


import sys


def read_in():
    lines = sys.stdin.read()

    return lines


def tokenize(input):
    tokens = []
    temp=""
    for i in input:
        if(i=="\n" or i==" " or i==","):
            if(temp!=""):
                tokens.append(numberize(temp))
                temp = ""

        elif(i=="["):
            tokens.append(temp)
            tokens.append(i)
            temp=""

        elif(i==";" or i=="=" or i=="]" or i=="*" or i=="/" or i=="+"):
            tokens.append(numberize(temp))
            tokens.append(i)
            temp=""

        else:
            temp += i

    return tokens

def numberize(s):
    return "%"+str(s)


def interp(tokens):

    prev = 0
    for ind in range(len(tokens)):
        t = tokens[ind]

        if(t=="["):
            prev = t
            tokens[ind] = "\n\\begin{bmatrix}\n"
        elif(t=="]"):
            prev = t
            tokens[ind] = "\n\\end{bmatrix}\n"
        elif(t==";"):
            prev = t
            tokens[ind] = "\\\\\n"
        else:
            prev = t

        if(t!='' and t[0]=='%'):
            tokens[ind] = " & " + str(t)

    return tokens


def main():
    out = interp(tokenize(read_in()))

    for s in out:
        print(s, end='', flush=True)



if __name__ == '__main__':
    main()