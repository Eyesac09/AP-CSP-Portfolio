#Isaac Infante
#Nickname
#Reccomends a nickname based on user input

#functions
def nickname():
    superhero = input("Welcome to Superhero generator! Find out which superhero aligns to your personality. Do you prefer a PACIFIT or AGGRESIVE solution? (answer in ALL CAPS): ")
    if superhero == "PACIFIST":
        peace = input("Are you FAST AND QUICK? Or are you AGILE AND ACROBATIC: ")
        if peace == "FAST AND QUICK":
            quick = input("Do you rely on your own SPEED, or TRANSPORT?: ")
            if quick == "SPEED":
                print("Your superhero identity is The Flash!")
            if quick == "TRANSPORT":
                print("Your superhero identity is Silver Surfer!")
        elif peace == "AGILE AND ACROBATIC":
            supersuit = input("Do you prefer a TRADITIONAL or TECH supersuit?: ")
            if supersuit == "TRADITIONAL":
                print("Your superhero identity is Wonder Woman!")
            elif supersuit == "TECH":
                print("Your superhero identity is MCU Spiderman!")
    if superhero == "AGGRESIVE":
        aggresive = input("Would you prefer the ability to FLY? Or NO SUPERPOWERS?: ")
        if aggresive == "FLY":
            fighting = input("Is your main source of fighting your HUMAN BODY? Or through a WEAPON?: ")
            if fighting == "HUMAN BODY":
                print("Your superhero identity is Super Man!")
            elif fighting == "WEAPON":
                print("Your superhero identity is Thor!")
        elif aggresive == "NO SUPERPOWERS":
            attack = input("Do you rely on ADVANCED FIGHTING, or TECH CENTERED WEAPONS?: ")
            if attack == "ADVANCED FIGHTING":
                print("Your superhero identity is Black Widow!")
            elif attack == "TECH CENTERED WEAPONS":
                print("Your superhero identity is Iron Man!")


#main
nickname()
