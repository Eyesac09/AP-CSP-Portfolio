#Isaac Infante
#Pokemon

#init
import time
import random
x = 0
ember = 0
flamethrower = 0
scratch = 0
slash = 0
level = 0
train_count = 0
ember_level = 1
flamethrower_level = 1
scratch_level = 1
slash_level = 1
pokemon_form = "Charmander"
evolved = False
pokemon_name = "Charmander"
pokemon_level = 1
attack_levels = {'ember': 1,'flamethrower': 1,'scratch': 1,'slash': 1}
points = 0

#functions
def charmander():
    print((r"             _.--\"\"`-..\n"))
    print((r"           ,'          `.\n"))
    print((r"         ,'          __  `.\n"))
    print((r"        /|          \" __   \\\n"))
    print((r"       , |           / |.   .\n"))
    print((r"       |,'          !_.'|   |\n"))
    print((r"     ,'             '   |   |\n"))
    print((r"    /              |`--'|   |\n"))
    print((r"   |                `---'   |\n"))
    print((r"    .   ,                   |                       ,\".\n"))
    print((r"     ._     '           _'  |                    , ' \\ `\n"))
    print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n"))
    print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n"))
    print(("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n"))
    print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,\n"))
    print((r"   `.      '            '            /          '    |'. |/\n"))
    print((r"     `.   |              \\       _,-'           |       ''\n"))
    print((r"       `._'               \\   '\"\\                .      |\n"))
    print((r"          |                '     \\                `._  ,'\n"))
    print((r"          |                 '     \\                 .'|\n"))
    print((r"          |                 .      \\                | |\n"))
    print((r"          |                 |       L              ,' |\n"))
    print((r"          `                 |       |             /   '\n"))
    print((r"           \\                |       |           ,'   /\n"))
    print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'\n"))
    print((r"        /     .             .      `!             ,j'\n"))
    print((r"       /       `.          /        .           .'/\n"))
    print((r"      .          `.       /         |        _.'.'\n"))
    print((r"       `.          7`'---'          |------\"'_.'\n"))
    print((r"      _,.`,_     _'                ,''-----\"'\n"))
    print((r"  _,-_    '       `.     .'      ,\\\n"))
    print((r"  -\" /`.         _,'     | _  _  _.|\n"))
    print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /\n"))
    print((r"                           `\" \" -' mh\n"))
    print(("\n"))
    print(("\n"))
def charmeleon():
    print((r"                     ,-'`\\\n"))
    print((r"                 _,\"'    j\n"))
    print((r"          __....+       /               .\n"))
    print((r"      ,-'\"             /               ; `-._.'.\n"))
    print((r"     /                (              ,'       .'\n"))
    print((r"    |            _.    \\             \\   ---._ `-.\n"))
    print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n"))
    print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l\n"))
    print((r" .,-        `._  |  |    |              \\       _   l .\n"))
    print((r"/              `\"--'    /              .'       ``. |  )\n"))
    print((".\\    ,                 |                .        \\ `. '\n"))
    print(("`.                .     |                '._  __   ;. \\'\n"))
    print((r" `-..--------...'       \\                  `'  `-\"'.  \\\n"))
    print((r"     `......___          `._                        |  \\\n"))
    print((r"              /`            `..                     |   .\n"))
    print((r"             /|                `-.                  |    L\n"))
    print((r"            / |               \\   `._               .    |\n"))
    print((r"          ,'  |,-\"-.   .       .     `.            /     |\n"))
    print((r"        ,'    |     '   \\      |       `.         /      |\n"))
    print((r"      ,'     /|       \\  .     |         .       /       |\n"))
    print((r"    ,'      / |        \\  .    +          \\    ,'       .'\n"))
    print((r"   .       .  |         \\ |     \\          \\_,'        / j\n"))
    print((r"   |       |  L          `|      .          `        ,' '\n"))
    print((r"   |    _. |   \\          /      |           .     .' ,'\n"))
    print((r"   |   /  `|    \\        .       |  /        |   ,' .'\n"))
    print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'\n"))
    print((r"   `. |___,`    /  `.   /`.       '          |  .'\n"))
    print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'\n"))
    print((r"               |        .'  / _/_|          .\n"))
    print((r"               `,       `\"'/\"'    \\          `.\n"))
    print((r"                 `,       '.       `.         |\n"))
    print((r"            __,.-'         `.        \\'       |\n"))
    print((r"           /_,-'\\          ,'        |        _.\n"))
    print((r"            |___.---.   ,-'        .-':,-\"`\\,' .\n"))
    print((r"                 L,.--\"'           '-' |  ,' `-.\\\n"))
    print((r"                                       `.' mh\n"))
def charizard():
    print((r"                .\"-,.__\n"))
    print((r"                `.     `.  ,\n"))
    print((r"             .--'  .._,'\"-' `.\n"))
    print((r"            .    .'         `'\n"))
    print((r"            `.   /          ,'\n"))
    print((r"              `  '--.   ,-\"'\n"))
    print((r"               `\"`   |  \\\n"))
    print((r"                  -. \\, |\n"))
    print((r"                   `--Y.'      ___.\n"))
    print((r"                        \\     L._, \\\n"))
    print((r"              _.,        `.   <  <\\                _\n"))
    print((r"            ,' '           `, `.   | \\            ( `\n"))
    print((r"         ../, `.            `  |    .\\`.           \\ \\_\n"))
    print((r"        ,' ,..  .           _.,'    ||\\l            )  '\".\n"))
    print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n"))
    print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n"))
    print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n"))
    print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `.\n"))
    print((r"   | /           |L__           |    |          / /          `. `.\n"))
    print((r"  , /            .   .          |    |         / /             ` `\n"))
    print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n"))
    print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n"))
    print((".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n"))
    print(("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n"))
    print(("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n"))
    print(("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n"))
    print(("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n"))
    print(("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n"))
    print(("||/            _,-------7 '              . |  `-'    l         /    `||\n"))
    print((". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n"))
    print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'\n"))
    print((r"         /      ,'      |               |,'    \\-.._,.'/'\n"))
    print((r"         .     /        .               .       \\    .''\n"))
    print((r"       .`.    |         `.             /         :_,'.'\n"))
    print((r"         \\ `...\\   _     ,'-.        .'         /_.-'\n"))
    print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /\n"))
    print((r"               .'        /\"'          |  \"'   '_\n"))
    print((r"              /_|.-'\\ ,\".             '.'`__'-( \\\n"))
    print((r"                / ,\"'\"\\,'               `/  `-.|\" mh\n"))
def check_evolution():
    global attack_levels, pokemon_name, pokemon_form, evolved, pokemon_level
    max_attack = max(attack_levels.values())
    if not evolved and max_attack >= 10:
        print("Your Charmander has evolved into Charmeleon!")
        pokemon_name = "Charmeleon"
        pokemon_form = "Charmeleon"
        evolved = True
        pokemon_level = 10
    elif evolved and max_attack >= 20:
        print("Your Charmeleon has evolved into Charizard!")
        pokemon_name = "Charizard"
        pokemon_form = "Charizard"
        # Keep evolved True
        pokemon_level = 20
    elif max_attack < 20:
        pokemon_level = max_attack
def display_pokemon():
    print(pokemon_name)
    if pokemon_form == "Charmander":
        charmander()
    elif pokemon_form == "Charmeleon":
        charmeleon()
    elif pokemon_form == "Charizard":
        charizard()


def pokemon_game():
    print("Welcome to Pokemon CTF! To start, we have provided you with a starter pokemon, Charmander!")
    global ember, flamethrower, scratch, slash
    global x
    global level
    global train_count
    while True:
        print("Home Screen Menu")
        print("Day Counter")
        print("Train Pokemon")
        print("Info Screen")
        menu = input("Where would you like to head to?: ")
        if menu == "Day Counter":
            print(f"Days Played: {x}")
            train_count = 0
            day = input("Would you like to end for today?: ")
            if day == "Yes":
                x += 1
                end = input("Would you like to reset progress?: ")
                if end == "Yes":
                    break
                if end == "No":
                    print("back to main menu")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
            if day == "No":
                print("back to main menu")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")

        if menu == "Train Pokemon":

            if train_count >= 2:
                print("You have already trained twice today. End the day to train again.")
                continue
            view_stat = input("View stats for attacks?: ")
            if view_stat == "Yes":
                print("Ember: ", attack_levels['ember'])
                print("Flamethrower:", attack_levels['flamethrower'])
                print("Scratch:", attack_levels['scratch'])
                print("Slash:", attack_levels['slash'])

            pokemon = input(f"Which Pokemon would you like to train? (Options: {pokemon_name}): ").strip().lower()
            if pokemon == pokemon_name.lower():
                train_count += 1
                print("Attacks: Ember, Flamethrower, Scratch, or Slash")
                train = input("Which attack do you want to train (can only train two times a day)?: ")
                if train == "Ember":
                    print("Ember")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    power = ['+1', '+2', '+3', '+5']
                    random_power = random.choice(power)
                    increment = int(random_power)
                    attack_levels['ember'] += 1
                    check_evolution()
                    print(f"Ember level is now: {attack_levels['ember']}")
                    again = input("Train again?: ")
                    if again == "Yes":
                        if train_count >= 2:
                            print("You have already trained twice today. End the day to train again.")
                            continue
                        train_count += 1
                        print("Attacks: Ember, Flamethrower, Scratch, or Slash")
                        train_2 = input("Which attack do you want to train (can only train two times a day)?: ")
                        if train_2 == "Ember":
                            print("Ember")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['ember'] += 1
                            check_evolution()
                            print(f"Ember level is now: {attack_levels['ember']}")
                        if train_2 == "Flamethrower":
                            print("Flamethrower")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['flamethrower'] += 1
                            check_evolution()
                            print(f"Flamethrower level is now: {attack_levels['flamethrower']}")
                        if train_2 == "Scratch":
                            print("Scratch")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['scratch'] += 1
                            check_evolution()
                            print(f"Scratch level is now: {attack_levels['scratch']}")
                        if train_2 == "Slash":
                            print("Slash")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['slash'] += 1
                            check_evolution()
                            print(f"Slash level is now: {attack_levels['slash']}")

                if train == "Flamethrower":
                    print("Flamethrower")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    power = ['+1', '+2', '+3', '+5']
                    random_power = random.choice(power)
                    increment = int(random_power)
                    attack_levels['flamethrower'] += 1
                    check_evolution()
                    print(f"Flamethrower level is now: {attack_levels['flamethrower']}")
                    again = input("Would you like to train again?: ")

                    if again == "Yes":
                        if train_count >= 2:
                            print("You have already trained twice today. End the day to train again.")
                            continue
                        train_count += 1
                        print("Attacks: Ember, Flamethrower, Scratch, or Slash")
                        train_2 = input("Which attack do you want to train (can only train two times a day)?: ")
                        if train_2 == "Ember":
                            print("Ember")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['ember'] += 1
                            check_evolution()
                            print(f"Ember level is now: {attack_levels['ember']}")
                        if train_2 == "Flamethrower":
                            print("Flamethrower")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['flamethrower'] += 1
                            check_evolution()
                            print(f"Flamethrower level is now: {attack_levels['flamethrower']}")
                        if train_2 == "Scratch":
                            print("Scratch")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['scratch'] += 1
                            check_evolution()
                            print(f"Scratch level is now: {attack_levels['scratch']}")
                        if train_2 == "Slash":
                            print("Slash")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['slash'] += 1
                            check_evolution()
                            print(f"Slash level is now: {attack_levels['slash']}")

                if train == "Scratch":
                    print("Scratch")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    power = ['+1', '+2', '+3', '+5']
                    random_power = random.choice(power)
                    increment = int(random_power)
                    attack_levels['scratch'] += 1
                    check_evolution()
                    print(f"Scratch level is now: {attack_levels['scratch']}")
                    again = input("Would you like to train again?: ")

                    if again == "Yes":
                        if train_count >= 2:
                            print("You have already trained twice today. End the day to train again.")
                            continue
                        train_count += 1
                        print("Attacks: Ember, Flamethrower, Scratch, or Slash")
                        train_2 = input("Which attack do you want to train (can only train two times a day)?: ")
                        if train_2 == "Ember":
                            print("Ember")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['ember'] += 1
                            check_evolution()
                            print(f"Ember level is now: {attack_levels['ember']}")
                        if train_2 == "Flamethrower":
                            print("Flamethrower")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['flamethrower'] += 1
                            check_evolution()
                            print(f"Flamethrower level is now: {attack_levels['flamethrower']}")
                        if train_2 == "Scratch":
                            print("Scratch")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['scratch'] += 1
                            check_evolution()
                            print(f"Scratch level is now: {attack_levels['scratch']}")
                        if train_2 == "Slash":
                            print("Slash")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['slash'] += 1
                            check_evolution()
                            print(f"Slash level is now: {attack_levels['slash']}")

                if train == "Slash":
                    print("Slash")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    power = ['+1', '+2', '+3', '+5']
                    random_power = random.choice(power)
                    increment = int(random_power)
                    attack_levels['slash'] += 1
                    check_evolution()
                    print(f"Slash level is now: {attack_levels['slash']}")
                    again = input("Would you like to train again?: ")

                    if again == "Yes":
                        if train_count >= 2:
                            print("You have already trained twice today. End the day to train again.")
                            continue
                        train_count += 1
                        print("Attacks: Ember, Flamethrower, Scratch, or Slash")
                        train_2 = input("Which attack do you want to train (can only train two times a day)?: ")
                        if train_2 == "Ember":
                            print("Ember")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['ember'] += 1
                            check_evolution()
                            print(f"Ember level is now: {attack_levels['ember']}")
                        if train_2 == "Flamethrower":
                            print("Flamethrower")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['flamethrower'] += 1
                            check_evolution()
                            print(f"Flamethrower level is now: {attack_levels['flamethrower']}")
                        if train_2 == "Scratch":
                            print("Scratch")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['scratch'] += 1
                            check_evolution()
                            print(f"Scratch level is now: {attack_levels['scratch']}")
                        if train_2 == "Slash":
                            print("Slash")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            power = ['+1', '+2', '+3', '+5']
                            random_power = random.choice(power)
                            increment = int(random_power)
                            attack_levels['slash'] += 1
                            check_evolution()
                            print(f"Slash level is now: {attack_levels['slash']}")
                    if again == "No":
                        home = input("Going back to home screen")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                        time.sleep(1)

        if menu == "Info Screen":
            while True:
                print("View Pokemon")
                print("Exit")
                info_screen = input("Which would you like to access: ")

                if info_screen == "View Pokemon":
                    print("Charmander")
                    display_pokemon()
                    leave_1 = input("Go back or view pokemon level?: ")
                    if leave_1 == "Go back":
                        print("Back to Info Screen")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                    if leave_1 == "View pokemon level":
                        poke_type = input("Which Pokemon?: ")
                        if poke_type == "Charmander":
                            print(f"Level: {pokemon_level}")
                            leave_2 = input("Go Back?: ")
                            if leave_2 == "Yes":
                                print("Back to Info Screen")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print("..")
                                time.sleep(1)
                                print("...")
                            if leave_2 == "No":
                                print("Too bad")
                                print("Back to Info Screen")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print("..")
                                time.sleep(1)
                                print("...")




                if info_screen == "Exit":
                        print("back to main menu")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                        break




#main

pokemon_game()

