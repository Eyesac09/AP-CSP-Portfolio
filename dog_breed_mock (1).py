#Isaac Infante
#Mock Project
#Dog Breeds
#The purpose of this program is to help users find a dog that fits their needs

#init
import pandas as pd
import random
import time

#data
data = pd.read_csv("dog_breed.csv")
data.columns = ["ID","Breed","Group","Purpose","LifeMin","LifeMax","HeightMin","HeightMax","WeightMin","WeightMax","Temperament","ImageURL"]

#helping functions
def getDogSize(size):
    size = size.lower()
    if size == "tiny":
        low, high = 0, 10
    elif size == "small":
        low, high = 11, 25
    elif size == "medium":
        low, high = 26, 60
    elif size == "large":
        low, high = 61, float("inf")
    else:
        return "Invalid size"
    filtered = data[(data["WeightMin"] >= low) & (data["WeightMin"] <= high)]
    if filtered.empty:
        return "No breeds found"
    choice = random.choice(filtered["Breed"].tolist())
    return choice

def lookup(breed_group):
    breed_group = breed_group.lower()
    names = data["Breed"].tolist()
    groups = data["Group"].tolist()
    temps = data["Temperament"].tolist()
    images = data["ImageURL"].tolist()
    matches = []
    for i in range(len(groups)):
        if groups[i].lower() == breed_group:
            matches.append(i)
    if len(matches) == 0:
        print("Breed group not found")
        return
    choice = random.choice(matches)
    print("Name:", names[choice])
    print("Temperament:", temps[choice])
    print("Image:", images[choice])

def human_purpose(goal):
    goal = goal.lower()
    names = data["Breed"].tolist()
    groups = data["Group"].tolist()
    purpose = data["Purpose"].tolist()
    matches = []
    for i in range(len(purpose)):
        if purpose[i].lower() == goal:
            matches.append(i)
    if len(matches) == 0:
        print("Purpose not found")
        return
    choice = random.choice(matches)
    print("=====================================================")
    print("Name:", names[choice])
    print("")
    print("Breed:", groups[choice])
    print("")
    print("Purpose:", purpose[choice])
    print("=====================================================")

#main function with interface
def main():
    running = True
    while running:
        print("=====================================================")
        print("Welcome to Dog Finder! Discover your ideal dog breed!")
        print("-----------------------------------------------------")
        time.sleep(1)
        print("[1]. Dog Size Preference")
        print("[2]. Dog Breed Group Finder")
        print("[3]. Dog Purpose Preference")
        print("[4]. Quit")
        menu_selection = input("Please select an option: ")
        print("-----------------------------------------------------")

        if menu_selection == "1":
            size_preference = input("Do you like tiny, small, medium, or large dogs?: ").lower()
            result = getDogSize(size_preference)
            print("Your dog match:", result)

        elif menu_selection == "2":
            group_preference = input("What dog group do you like (Toy, Working, Hound, Terrier, etc.)?: ")
            lookup(group_preference)

        elif menu_selection == "3":
            purpose_preference = input("What purpose are you looking for (herding, guarding, hunting, etc.)?: ")
            human_purpose(purpose_preference)

        elif menu_selection == "4":
            print("Goodbye!")
            running = False

        else:
            print("Invalid choice. Try again.")


#main
main()

#Sources of Information

#Dog Data Set
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

