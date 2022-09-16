import sys 

def GetContentByTokenFromHeaderFile(Data, Token):
    f = open(Data, "rb")
    try:
        TokenList = f.readlines()
    finally:
        f.close()
    
    for i in TokenList:
        if (i.upper().find("#DEFINE")==0):
            if (i[8:].split("	")[0].strip().upper() == Token.upper()):
                return i.split("	")[-1].strip()
    return "N/A"

def GetContentByTokenFromMAK(Data, Token):
    f = open(Data, "rb")
    try:
        TokenList = f.readlines()
    finally:
        f.close()
    Start = -1
    End = -2
    for index in range(0,len(TokenList)):
        if (TokenList[index].split("=")[0].strip().upper() == Token.upper()):
            Start = index
            End = index
            for end_index in range(index+1,len(TokenList)):
                if (TokenList[end_index].upper().find("=") > -1):
                    End = end_index
                    break
            break

    if Start > -1:
        if (End - Start) < 2:
            return "".join(TokenList[Start].split("=")[-1].strip())
        else:
            return "".join(TokenList[Start:End])
    else:
        return "N/A"

def main(args = None):
    import textwrap
    USAGE=textwrap.dedent("""\
        Usage:
            (1) <Token.mak> <Token.h> CheckToken
                # Check BIOS token from file token.mak and token.h
        """)
    if args is None:
        args = sys.argv[1:]       
    else:
        sys.exit(-1)
    
    if (not (GetContentByTokenFromHeaderFile(args[1], args[2]) == "N/A")):
        print (GetContentByTokenFromHeaderFile(args[1], args[2]))
    else:
        if (not (GetContentByTokenFromMAK(args[0], args[2]) == "N/A")):
            print (GetContentByTokenFromMAK(args[0], args[2]))
        else:
            print("N/A")
    
if __name__ == '__main__':
    main()