def securePasswordGenerator(lengthOfPassword):

    """    This is a Python based strong password generator.
    This program generates an n(user prompt) character strong password that includes atleast but not limited to one uppercase letter,
    one lowercase letter, one digit and one special character.
    Try to keep the length of the password atleast above 7 characters.
    Go ahead and enjoy the program
    May the strength be with you :p
    Cheers!!!"""
    
    if lengthOfPassword > 7:
        import random
        passwordList = []
        numbers = list(range(10))
        characters = list("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
        upperAlphabets = [chr(tempVariable) for tempVariable in range(65, 91)]
        lowerAlphabets = [chr(tempVariable) for tempVariable in range(97, 123)]

        lsno = []
        mydict = {"nono": len(numbers), "chno": len(characters), "ucno": len(upperAlphabets), "lcno": len(lowerAlphabets)}
        for a in range(len(numbers)):
            for b in range(len(characters)):
                for c in range(len(upperAlphabets)):
                    for d in range(len(lowerAlphabets)):
                        if a >= 1 and b >= 1 and c >= 1 and d >= 1:
                            if a + b + c + d == lengthOfPassword:
                                lsno.append([a, b, c, d])
        req = random.choice(lsno)
        random.shuffle(req)

        for i in range(req[0]):
            passwordList.append(random.choice(numbers))
        for i in range(req[1]):
            passwordList.append(random.choice(upperAlphabets))
        for i in range(req[2]):
            passwordList.append(random.choice(lowerAlphabets))
        for i in range(req[3]):
            passwordList.append(random.choice(characters))

        random.shuffle(passwordList)
        yourPassword = ""
        yourPassword = "".join(str(tempVariable) for tempVariable in passwordList)
        print(yourPassword)

    else:
        print("Your specified length is small to create a unique strong password.")


print(securePasswordGenerator.__doc__)
n = int(input("Enter the required length of your password: "))
securePasswordGenerator(n)

