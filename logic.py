import random
import sys




featured_units = {
    "1" : ["SSR AGL The strength to let go of emotions, Jiren!",
        "SSR INT The Three Super Saiyans Assemble, Super Saiyan Son Goku & Super Saiyan Vegeta & Super Saiyan Trunks (teenage years)!",
        "SSR STR Super Powers Unite, Super Saiyan Son Goku!",
        "SSR TEQ The final stretch heats up, Jiren (full power)!",
        "SSR INT Immortal Justice, Toppo!",
        "SSR INT Hidden Determination, Android No. 16!",
        "SSR TEQ The determination to not give up, Android No. 18!",
        "SSR TEQ Unwavering Determination, Android No. 17!",
        "SSR PHY Light of Victory, Super Saiyan Son Goku",
        "SSR AGL Absolute confidence, Super Vegeta!"
            ],
    "2" : [
        "SSR TEQ Awakening That Causes Tumult Goku (Ultra Instinct -Sign-)",
        "SSR STR Pride Trooper's Blitz Captain, Dyspo!",
        "SSR Power Acquired Through Time-Traveling Goku Black (Super Saiyan Rosé)",
        "SSR Vow to Prove Victorious Super Saiyan 4 Goku",
        "SSR Proud Saiyan Lineage Super Saiyan God SS Vegeta & Super Saiyan Trunks (Future)",
        "SSR Power and Knowledge Obtained Majin Buu (Gotenks)",
        "SSR Warriors Brought Back to the Present World Goku & Vegeta (Angel)",
        "SSR Power Raised to the Maximum Super Saiyan God SS Goku (Kaioken)",
        "SSR Sons of a Great Father Gohan (Teen) & Goten (Kid)",
        "SSR Invincible Legend of Universe 11 Jiren"
            ],

    "3" : [
        "SSR TEQ Policeman of Universe 3 Catopesra!",
        "SSR PHY Intimidating Aura That Tolerates No Evil, Toppo!",
        "SSR INT Resonant Breathing, Androids #17 & #18!",
        "SSR TEQ Power Boosted Through Training, Super Saiyan Trunks (Teen)!",
        "SSR AGL Rampage of Sadness and Fury, Kale (Berserk)!",
        "SSR AGL Attack of a New Android, Gamma 2!",
        "SSR STR Birth of a New Android, Gamma 1!",
        "SSR STR Pride Trooper's Blitz Captain, Dyspo!",
        "SSR AGL Urgently Summoned Fighters, Krillin & Android #18!"

            ]
                 }

def stoneTracker(stoneCount, stoneUse):
    stoneCount = stoneCount - stoneUse
    return stoneCount

def stonesSpent(stoneUse):
    return stoneUse




def main():
    print("\nTo exit the program type \'exit\'")
    stoneCount = int(input("\nHow many stones do you have?: "))
    while stoneCount == 'exit':
        print("\nExiting the summon")
        sys.exit()
    stoneCount = validate_stone_count(stoneCount)
    if stoneCount is None:
        sys.exit()





    while stoneCount >= 5:
        # majd = "my knitta"  # ye
        # hamza = "shafted"  # teq ui goku keeps dodging
        # shaftedSummons = [hamza, majd]
        # print(shaftedSummons)
        # print("\n")
        print("\n")
        Multi = False
        Lr = False


        banner = input("\nSelect a banner: (1) AGL Jiren || (2) Teq UI Goku || (3) PHY Toppo: ")
        print("\n")
        while banner == "exit":
            print("Exiting the summon")
            sys.exit()
        banner = validate_banner(banner)
        if banner is None:
            sys.exit()



        rate = input("Enter SSR rate greater than 0: ")  # asks user for SSR rate
        print("\n")
        while rate == 'exit':
            print("\nExiting the summon")
            sys.exit()
        rate = validate_rate(rate)
        if rate is None:
            sys.exit()

        summonValue = input(
            "Single Summon (1) | Multi Summon (10) | Super Multi (77): ")
        # asks user if they want a single or multi summon
        print("\n")
        while summonValue == 'exit':
            print("\nExiting the summon")
            sys.exit()

        summonValue = validate_summon_value(summonValue)  # validates the input
        if summonValue is None:
            sys.exit()

        if summonValue == 10 and stoneCount >= 50:       
            stoneUse = stonesSpent(stoneUse = 50)
            Multi = True

        elif summonValue == 77 and stoneCount >= 300:
            stoneUse = stonesSpent(stoneUse = 300)
            Multi = True
        elif summonValue == 1 and stoneCount >= 5:
            stoneUse = stonesSpent(stoneUse = 5)
            Multi = False
        else:
            print("\nGet yo broke ahh out of here")
            continue

        stoneCount = stoneTracker(stoneCount, stoneUse)
        print(
            "                                                      You have " +
            str(stoneCount) + " stones left")

        summonShaft = RNG(summonValue, Multi, rate, Lr, banner)


        print(summonShaft)


        if stoneCount < 5:
            print("Get yo broke ahh out of here")
            break


def validate_banner(banner):
    while True:
        while True:
            if banner.lower() == 'exit':
                return None
            if banner in ["1", "2", "3"]:
                return banner
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
            banner = input("\nSelect a banner: (1) AGL Jiren || (2) TEQ UI Goku || (3) PHY Toppo: ")
            print('\n')


def validate_rate(rate):  # Function to validate the rate
    while True:
        if rate.lower() == 'exit':
            return None
        try:
            rate = int(rate)
            if rate > 0:
                return rate
            else:
                print("Invalid input. Please enter a number greater than 0")
        except ValueError:
            print("Invalid input. Please enter a number greater than 0")
        rate = input("Enter SSR rate greater than 0: ")
        print("\n")


def validate_summon_value(summonValue):  # Function to validate summonValue
    while True:
        if summonValue.lower() == 'exit':
            return None
        try:
            summonValue = int(summonValue)
            if summonValue in [1, 10, 77]:
                return summonValue
            else:
                print("Invalid input. Please enter 1, 10, or 77.")
        except ValueError:
            print("Invalid input. Please enter 1, 10, or 77.")
        summonValue = input(
            "Single Summon (1) | Multi Summon (10) | Super Multi (77) |\
        or (exit): ")
        print("\n")


def validate_stone_count(stoneCount):  # Function to validate the stone count
    while True:
        if stoneCount == 'exit':
            return None
        try:
            stoneCount = int(stoneCount)
            if stoneCount >= 0:
                return stoneCount
            else:
                print("Invalid input. Please enter a number greater than 0")
        except ValueError:
            print("Invalid input. Please enter a number greater than 0")
        stoneCount = input("How many stones do you have?: ")
        print("\n")




def RNG(summonValue, Multi, rate, Lr, banner):  # RNG for summons
    Lr = False
    result = ''



    if Multi:  # Handles Multi Summons



            print("Summon Results\n")
            for _ in range(summonValue - 1):  # Loops for the summon
                id = random.randint(1, 100)
                id2 = random.randint(1, 10)
                id3 = random.randint(1, len(featured_units[banner]))
                if id <= rate * 10:
                    if id2 <= 5:  # Featured unit
                        Lr = True
                        result += printFeaturedUnit(banner, id3)
                    else:
                        result += "SSR\n"
                elif id <= 70:
                    result += "SR\n"
                else:
                    result += "R\n"

            id4 = random.randint(1, 100)  # Handles GSSR
            id5 = random.randint(1, len(featured_units[banner]))
            if id4 <= 10:
                Lr = True
                result += printFeaturedUnit(banner, id5)

            else:
                result += "SSR\n"
            if Lr:
                return  result + "\nFeatured character is coming!"

    else:  # Handles Single Summons


            id = random.randint(1, 100)
            id2 = random.randint(1, 10)
            id3 = random.randint(1, len(featured_units[banner]))




            print("Summon Results\n")

            if id <= rate * 10:
                if id2 <= 5:
                    Lr = True
                    result += printFeaturedUnit(banner, id3)
                else:
                    result+= "SSR\n"
            elif id <= 70:
                result+="SR\n"
            else:
                result+="R\n"

    if Lr:
        return result + "\nFeatured character is coming!"
    else:
        return result + '\nYou got shafted!'


def printFeaturedUnit(banner, id):


    return featured_units[banner][id - 1] + "\n"


if __name__ == "__main__":
    main()

