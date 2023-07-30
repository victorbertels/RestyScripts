
    try:
        open("token.txt" ,"r")
    
    except:
        open("tokennietgelukt.txt" , "w")



f = open('token.txt', 'w')
file_contents = f.read()
print(file_contents)


"""

with open('token.txt', 'w') as f:
    print("did i create?")
    
    print(f)
    print("Paste your token")
    token = str(input())
    f.write(token)
    print(token)
    """