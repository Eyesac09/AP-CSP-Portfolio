#Isaac Infante
#Milk Bottles
#Create a Python program that generates and prints out the lyrics to the song "99 Bottles of Milk on the Wall." Follow the guidelines below:


#functions

def ninety_nine_bottles():
    for i in range(99, 0, -1):
        bottles_current = f"{i} bottle{'s' if i > 1 else ''}"
        bottles_next = f"{i-1} bottle{'s' if i-1 > 1 or i-1 == 0 else ''}"
        print(f"{bottles_current} of milk on the wall, {bottles_current} of milk.")
        if i > 1:
            print(f"Take one down and pass it around, {bottles_next} of milk on the wall.\n")
        else:
            print(f"Take one down and pass it around, no more bottles of milk on the wall.\n")
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more, 99 bottles of milk on the wall.")


#main
ninety_nine_bottles()
